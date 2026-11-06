// Тестовый стенд: запускает настоящий Code.gs с имитацией Google Таблицы, Telegram и т.д.
const fs = require('fs'), http = require('http'), vm = require('vm'), path = require('path');
const ROOT = process.argv[2], PORT = +process.argv[3] || 8765;
const tg = [];                                   // «отправленные» в Telegram сообщения
const sheets = {};
function makeSheet(name){
  const cells = {}; // key r,c
  const sh = {
    name, getMaxRows: () => 1000,
    getLastRow(){ let m = 0; for (const k in cells){ const r = +k.split(',')[0]; if (cells[k] !== '' && r > m) m = r; } return m; },
    setFrozenRows(){}, setColumnWidth(){},
    getRange(r, c, nr = 1, nc = 1){
      const rg = {
        setNumberFormat(){ return rg; }, setFontWeight(){ return rg; }, setBackground(){ return rg; }, setDataValidation(){ return rg; },
        setValues(v){ v.forEach((row, i) => row.forEach((x, j) => cells[(r + i) + ',' + (c + j)] = x)); return rg; },
        setValue(x){ cells[r + ',' + c] = x; return rg; },
        getValues(){ const out = []; for (let i = 0; i < nr; i++){ const row = []; for (let j = 0; j < nc; j++) row.push(cells[(r + i) + ',' + (c + j)] ?? ''); out.push(row); } return out; }
      };
      return rg;
    }
  };
  return sh;
}
const props = {};
const ctx = {
  SpreadsheetApp: {
    getActive: () => ({ getSheetByName: n => sheets[n] || null, insertSheet: n => (sheets[n] = makeSheet(n)) }),
    newDataValidation: () => ({ requireValueInList(){ return this; }, build(){ return {}; } })
  },
  PropertiesService: { getScriptProperties: () => ({ getProperty: k => props[k] ?? null, setProperty: (k, v) => { props[k] = String(v); } }) },
  LockService: { getScriptLock: () => ({ waitLock(){}, releaseLock(){} }) },
  UrlFetchApp: { fetch: (url, o) => { tg.push({ url, body: o && o.payload ? JSON.parse(o.payload) : null }); return { getContentText: () => '{"ok":true,"result":[]}' }; } },
  ContentService: { MimeType: { JSON: 'json' }, createTextOutput: s => ({ s, setMimeType(){ return this; } }) },
  Utilities: {
    getUuid: () => 'aaaa-bbbb-cccc-dddd-eeee-ffff',
    formatDate: (d, tz, f) => { const p = n => String(n).padStart(2, '0'); return f === 'yyyy-MM-dd' ? `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}` : `${p(d.getDate())}.${p(d.getMonth() + 1)}.${d.getFullYear()} ${p(d.getHours())}:${p(d.getMinutes())}`; }
  },
  Logger: { log: (...a) => console.log('[Logger]', ...a) }, console, JSON, Date, Math, String, parseInt, Array, Object, RegExp, Error
};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(__dirname, '..', 'Code.gs'), 'utf8'), ctx);
props.TG_TOKEN = 'TEST'; props.TG_CHAT_ID = '-100500'; props.ADMIN_KEY = 'secret-key';
ctx.setup();
const types = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript' };
http.createServer((req, res) => {
  const u = new URL(req.url, 'http://x');
  const cors = { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json; charset=utf-8' };
  if (u.pathname === '/exec'){
    if (req.method === 'GET'){ const out = ctx.doGet({ parameter: Object.fromEntries(u.searchParams) }); res.writeHead(200, cors); return res.end(out.s); }
    if (req.method === 'POST'){ let b = ''; req.on('data', c => b += c); req.on('end', () => { const out = ctx.doPost({ postData: { contents: b } }); res.writeHead(200, cors); res.end(out.s); }); return; }
    res.writeHead(204, cors); return res.end();
  }
  if (u.pathname === '/_tg'){ res.writeHead(200, cors); return res.end(JSON.stringify(tg)); }
  if (u.pathname === '/_sheets'){ res.writeHead(200, cors); const o = {}; for (const n in sheets){ const sh = sheets[n]; o[n] = sh.getRange(1, 1, sh.getLastRow(), 15).getValues(); } return res.end(JSON.stringify(o)); }
  const f = path.join(ROOT, decodeURIComponent(u.pathname));
  if (fs.existsSync(f) && fs.statSync(f).isFile()){ res.writeHead(200, { 'Content-Type': types[path.extname(f)] || 'application/octet-stream' }); return fs.createReadStream(f).pipe(res); }
  res.writeHead(404); res.end('nf');
}).listen(PORT, () => console.log('mock on', PORT));
