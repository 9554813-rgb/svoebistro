/**
 * «Своё бистро» — сервер заказов и броней на Google Apps Script
 * ----------------------------------------------------------------
 * Что делает:
 *   1) принимает с сайта заказы на доставку/самовывоз и заявки на бронь стола;
 *   2) сам пересчитывает цены по своему прайсу (подделать сумму с сайта нельзя);
 *   3) записывает в эту Google Таблицу: листы «Заказы» и «Брони»;
 *   4) отправляет уведомление в Telegram;
 *   5) отдаёт список заказов админ-панели и меняет статусы (по секретному ключу).
 *
 * Настройка — один раз (подробно в админ-панели, кнопка «Как подключить»):
 *   Файл → Настройки проекта → Свойства скрипта, добавить:
 *     TG_TOKEN    — токен бота от @BotFather
 *     TG_CHAT_ID  — id чата для уведомлений (можно несколько через запятую)
 *     ADMIN_KEY   — придуманный пароль для админ-панели (длинный!)
 *     ADMIN_URL   — (необязательно) адрес админ-панели, если она выложена в интернет
 *     TG_FULL     — (необязательно) yes = присылать в Telegram имя, телефон и адрес.
 *                   По умолчанию НЕ присылаются: Telegram — иностранный сервис, а это
 *                   трансграничная передача персональных данных (152-ФЗ). Решение — за юристом кафе.
 *   Затем: выполнить функцию setup → «Начать развёртывание» → «Веб-приложение»,
 *   «Выполнять от имени: я», «У кого есть доступ: все» → скопировать ссылку.
 */

const TZ = 'Europe/Moscow';
const SHEET_ORDERS = 'Заказы';
const SHEET_BOOKINGS = 'Брони';

const ORDER_STATUSES = ['Новый', 'Принят', 'Готовится', 'В доставке', 'Готов к выдаче', 'Выполнен', 'Отменён'];
const BOOKING_STATUSES = ['Новая', 'Подтверждена', 'Гости пришли', 'Отменена'];

// Прайс: id блюда → [название, цена ₽]. Меняете цены на сайте — поменяйте и здесь.
const PRICES = {
 "k1": [
  "Круассан классический",
  180
 ],
 "k3": [
  "Синнабон вишня / шоколад",
  360
 ],
 "k5": [
  "Даниш с инжиром",
  360
 ],
 "k6": [
  "Аман с пеканом",
  250
 ],
 "k2": [
  "Круассан миндальный",
  290
 ],
 "k4": [
  "Шведская булочка",
  180
 ],
 "k7": [
  "Аман классика",
  150
 ],
 "z1": [
  "Крок мадам",
  590
 ],
 "z2": [
  "Сырники",
  580
 ],
 "z3": [
  "Каша из зелёной гречи с пашотом",
  390
 ],
 "s11": [
  "Тартар с картошкой фри",
  450
 ],
 "s10": [
  "Тартар с круассаном",
  450
 ],
 "s13": [
  "Креветки пиль-пиль",
  790
 ],
 "s1": [
  "Хлеб и взбитое масло",
  240
 ],
 "s3": [
  "Хумус",
  350
 ],
 "s4": [
  "Взбитая брынза с томатами",
  550
 ],
 "s5": [
  "Паштет с мандаринами",
  450
 ],
 "s6": [
  "Тарамасалата из лосося",
  600
 ],
 "s7": [
  "Баккала мантекато",
  550
 ],
 "s8": [
  "Брезаола",
  550
 ],
 "s9": [
  "Хамон из утки мулард",
  660
 ],
 "s12": [
  "Антипасти",
  750
 ],
 "s2": [
  "Домашние оливки",
  490
 ],
 "c2": [
  "Зелёный салат",
  590
 ],
 "c1": [
  "Израильский салат",
  390
 ],
 "c3": [
  "Салат с бедром цыплёнка",
  430
 ],
 "u1": [
  "Куриный бульон",
  350
 ],
 "u2": [
  "Луковый суп",
  600
 ],
 "m1": [
  "Смэш-бургер",
  630
 ],
 "m3": [
  "Утиная нога",
  860
 ],
 "m2": [
  "Куриное бедро с пюре",
  720
 ],
 "p2": [
  "Каламарата с говядиной",
  720
 ],
 "p1": [
  "Казаречче качо-э-пепе",
  750
 ],
 "p3": [
  "Орзо с лангустинами",
  790
 ],
 "m4": [
  "Говяжьи щёки",
  820
 ],
 "m5": [
  "Палтус с томатами и оливками",
  1290
 ],
 "t1": [
  "Стейк с салатом из трав",
  1330
 ],
 "f4": [
  "Капучино",
  240
 ],
 "f1": [
  "Эспрессо",
  180
 ],
 "f2": [
  "Американо",
  190
 ],
 "f3": [
  "Фильтр-кофе",
  200
 ],
 "f6": [
  "Латте",
  270
 ],
 "f7": [
  "Флэт уайт",
  270
 ],
 "h1": [
  "Чай Эрл Грей, 600 мл",
  350
 ],
 "h3": [
  "Травяной чай со смородиной",
  350
 ],
 "d1": [
  "Лимонад «Lapochka»",
  300
 ],
 "d3": [
  "Сок «Rich»",
  230
 ]
};

// Условия доставки — те же, что на сайте
const DELIVERY = { fee: 150, freeFrom: 1500, minOrder: 700 };

const ORDER_COLS = [
  ['number', 'Номер'], ['created', 'Создан'], ['status', 'Статус'], ['method', 'Получение'],
  ['name', 'Имя'], ['phone', 'Телефон'], ['address', 'Адрес'], ['date', 'Дата'], ['time', 'Время'],
  ['items', 'Состав'], ['subtotal', 'Блюда, ₽'], ['delivery', 'Доставка, ₽'], ['total', 'Итого, ₽'],
  ['comment', 'Комментарий'], ['updated', 'Изменён']
];
const BOOKING_COLS = [
  ['number', 'Номер'], ['created', 'Создана'], ['status', 'Статус'], ['date', 'Дата'], ['time', 'Время'],
  ['guests', 'Гостей'], ['name', 'Имя'], ['phone', 'Телефон'], ['comment', 'Комментарий'], ['updated', 'Изменена']
];

/* ======================= Настройка таблицы ======================= */
function setup() {
  const ss = SpreadsheetApp.getActive();
  [[SHEET_ORDERS, ORDER_COLS, ORDER_STATUSES], [SHEET_BOOKINGS, BOOKING_COLS, BOOKING_STATUSES]].forEach(([name, cols, statuses]) => {
    let sh = ss.getSheetByName(name);
    if (!sh) sh = ss.insertSheet(name);
    sh.getRange(1, 1, sh.getMaxRows(), cols.length).setNumberFormat('@');   // всё как текст: даты и телефоны не «портятся»
    sh.getRange(1, 1, 1, cols.length).setValues([cols.map(c => c[1])]).setFontWeight('bold').setBackground('#FDEEE3');
    sh.setFrozenRows(1);
    // выпадающий список статусов прямо в таблице
    const rule = SpreadsheetApp.newDataValidation().requireValueInList(statuses, true).build();
    sh.getRange(2, 3, sh.getMaxRows() - 1, 1).setDataValidation(rule);
    sh.setColumnWidth(10, 320);
  });
  const props = PropertiesService.getScriptProperties();
  if (!props.getProperty('SEQ_ORDER')) props.setProperty('SEQ_ORDER', '1000');
  if (!props.getProperty('SEQ_BOOKING')) props.setProperty('SEQ_BOOKING', '100');
  if (!props.getProperty('ADMIN_KEY')) props.setProperty('ADMIN_KEY', Utilities.getUuid().replace(/-/g, '').slice(0, 20));
  Logger.log('Готово. Ключ админ-панели (ADMIN_KEY): ' + props.getProperty('ADMIN_KEY'));
}

/* ======================= Вход ======================= */
function doGet(e) {
  const p = (e && e.parameter) || {};
  if (p.action === 'list') {
    if (!checkKey(p.key)) return json({ ok: false, error: 'auth' });
    return json({
      ok: true, now: stamp(new Date()),
      orders: readRows(SHEET_ORDERS, ORDER_COLS),
      bookings: readRows(SHEET_BOOKINGS, BOOKING_COLS),
      statuses: { orders: ORDER_STATUSES, bookings: BOOKING_STATUSES }
    });
  }
  return json({ ok: true, service: 'svoe-bistro', version: 1 });
}

function doPost(e) {
  let data;
  try { data = JSON.parse(e.postData.contents); } catch (err) { return json({ ok: false, error: 'Неверный формат запроса' }); }
  if (data.website) return json({ ok: true, number: '—' });          // ловушка для ботов: поле скрыто от людей
  const lock = LockService.getScriptLock();
  try {
    lock.waitLock(15000);
    if (data.action === 'status') return json(setStatus(data));
    if (data.type === 'order') return json(createOrder(data));
    if (data.type === 'booking') return json(createBooking(data));
    return json({ ok: false, error: 'Неизвестный тип запроса' });
  } catch (err) {
    return json({ ok: false, error: String(err.message || err) });
  } finally {
    try { lock.releaseLock(); } catch (e2) {}
  }
}

/* ======================= Заказ ======================= */
function createOrder(d) {
  const name = clean(d.name, 60), phone = cleanPhone(d.phone), method = d.method === 'pickup' ? 'pickup' : 'delivery';
  const address = clean(d.address, 200), comment = clean(d.comment, 500);
  const date = /^\d{4}-\d{2}-\d{2}$/.test(d.date || '') ? d.date : Utilities.formatDate(new Date(), TZ, 'yyyy-MM-dd');
  const time = clean(d.time, 40) || 'Как можно скорее';
  if (name.length < 2) throw new Error('Укажите имя');
  if (!phone) throw new Error('Проверьте телефон');
  if (method === 'delivery' && address.length < 5) throw new Error('Укажите адрес доставки');
  if (!Array.isArray(d.items) || !d.items.length) throw new Error('Корзина пуста');
  let subtotal = 0; const lines = [];
  d.items.slice(0, 60).forEach(it => {
    const p = PRICES[it.id], q = Math.max(0, Math.min(99, parseInt(it.q, 10) || 0));
    if (!p || !q) return;
    subtotal += p[1] * q; lines.push(`${p[0]} × ${q} = ${money(p[1] * q)}`);
  });
  if (!lines.length) throw new Error('Корзина пуста');
  if (method === 'delivery' && subtotal < DELIVERY.minOrder) throw new Error('Минимальный заказ на доставку — ' + money(DELIVERY.minOrder));
  const delivery = method === 'delivery' && subtotal < DELIVERY.freeFrom ? DELIVERY.fee : 0;
  const number = String(nextSeq('SEQ_ORDER'));
  const now = stamp(new Date());
  appendRow(SHEET_ORDERS, ORDER_COLS, {
    number, created: now, status: ORDER_STATUSES[0], method: method === 'delivery' ? 'Доставка' : 'Самовывоз',
    name, phone, address: method === 'delivery' ? address : '', date, time, items: lines.join('\n'),
    subtotal, delivery, total: subtotal + delivery, comment, updated: now
  });
  if (prop('TG_FULL') !== 'yes') {
    // Без имени, телефона, адреса и комментария: Telegram — иностранный сервис (см. 152-ФЗ).
    notify([
      `🧾 <b>Новый заказ № ${number}</b>`,
      `${method === 'delivery' ? '🛵 Доставка' : '🏃 Самовывоз'} · ${fmtDate(date)}, ${esc(time)}`,
      '', ...lines.map(l => '— ' + esc(l)), '',
      `<b>Итого: ${money(subtotal + delivery)}</b>`,
      'Телефон и адрес — в админ-панели.'
    ]);
    return { ok: true, number, total: subtotal + delivery };
  }
  notify([
    `🧾 <b>Новый заказ № ${number}</b>`,
    `${method === 'delivery' ? '🛵 Доставка' : '🏃 Самовывоз'} · ${fmtDate(date)}, ${esc(time)}`,
    `👤 ${esc(name)} · ${esc(phone)}`,
    method === 'delivery' ? `📍 ${esc(address)}` : '',
    '', ...lines.map(l => '— ' + esc(l)), '',
    `Блюда: ${money(subtotal)}${method === 'delivery' ? ` · Доставка: ${delivery ? money(delivery) : 'бесплатно'}` : ''}`,
    `<b>Итого: ${money(subtotal + delivery)}</b>`,
    comment ? `💬 ${esc(comment)}` : ''
  ]);
  return { ok: true, number, total: subtotal + delivery };
}

/* ======================= Бронь ======================= */
function createBooking(d) {
  const name = clean(d.name, 60), phone = cleanPhone(d.phone), date = clean(d.date, 10), time = clean(d.time, 10);
  const guests = clean(d.guests, 20), comment = clean(d.comment, 300);
  if (!phone) throw new Error('Проверьте телефон');
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date) || !time) throw new Error('Выберите дату и время');
  const number = 'Б-' + nextSeq('SEQ_BOOKING');
  const now = stamp(new Date());
  appendRow(SHEET_BOOKINGS, BOOKING_COLS, { number, created: now, status: BOOKING_STATUSES[0], date, time, guests, name, phone, comment, updated: now });
  if (prop('TG_FULL') !== 'yes') {
    notify([`📅 <b>Бронь стола ${number}</b>`, `${fmtDate(date)} в ${esc(time)} · ${esc(guests)}`, '', 'Телефон гостя — в админ-панели. Перезвоните, чтобы подтвердить.']);
    return { ok: true, number };
  }
  notify([
    `📅 <b>Бронь стола ${number}</b>`,
    `${fmtDate(date)} в ${esc(time)} · ${esc(guests)}`,
    `👤 ${esc(name || 'без имени')} · ${esc(phone)}`,
    comment ? `💬 ${esc(comment)}` : '',
    '', 'Перезвоните гостю, чтобы подтвердить бронь.'
  ]);
  return { ok: true, number };
}

/* ======================= Статус (из админ-панели) ======================= */
function setStatus(d) {
  if (!checkKey(d.key)) return { ok: false, error: 'auth' };
  const isOrder = d.kind !== 'booking';
  const list = isOrder ? ORDER_STATUSES : BOOKING_STATUSES;
  if (list.indexOf(d.status) < 0) return { ok: false, error: 'Неизвестный статус' };
  const sh = sheet(isOrder ? SHEET_ORDERS : SHEET_BOOKINGS, isOrder ? ORDER_COLS : BOOKING_COLS);
  const last = sh.getLastRow();
  if (last < 2) return { ok: false, error: 'Запись не найдена' };
  const nums = sh.getRange(2, 1, last - 1, 1).getValues().map(r => String(r[0]));
  const i = nums.indexOf(String(d.number));
  if (i < 0) return { ok: false, error: 'Запись не найдена' };
  const row = i + 2, cols = isOrder ? ORDER_COLS : BOOKING_COLS, now = stamp(new Date());
  sh.getRange(row, 3).setValue(d.status);
  sh.getRange(row, cols.length).setValue(now);
  if (prop('NOTIFY_STATUS') === 'yes') notify([`${isOrder ? '🧾 Заказ №' : '📅 Бронь'} ${esc(d.number)}: <b>${esc(d.status)}</b>`]);
  return { ok: true, number: d.number, status: d.status, updated: now };
}

/* ======================= Telegram ======================= */
function notify(lines) {
  const token = prop('TG_TOKEN'), chats = prop('TG_CHAT_ID');
  if (!token || !chats) return;
  const text = lines.join('\n').replace(/\n{3,}/g, '\n\n').trim();
  const adminUrl = prop('ADMIN_URL');
  chats.split(',').map(s => s.trim()).filter(Boolean).forEach(chat => {
    const body = { chat_id: chat, text, parse_mode: 'HTML', disable_web_page_preview: true };
    if (/^https:\/\//.test(adminUrl)) body.reply_markup = { inline_keyboard: [[{ text: 'Открыть админ-панель', url: adminUrl }]] };
    try {
      UrlFetchApp.fetch(`https://api.telegram.org/bot${token}/sendMessage`, { method: 'post', contentType: 'application/json', payload: JSON.stringify(body), muteHttpExceptions: true });
    } catch (err) { console.error('Telegram: ' + err); }  // заказ всё равно сохранён в таблице
  });
}

/** Запустите после того, как написали боту /start (или добавили его в группу) — в журнале появится id чата. */
function findChatId() {
  const r = UrlFetchApp.fetch(`https://api.telegram.org/bot${prop('TG_TOKEN')}/getUpdates`, { muteHttpExceptions: true });
  const upd = (JSON.parse(r.getContentText()).result || []);
  const seen = {};
  upd.forEach(u => { const c = (u.message || u.my_chat_member || u.channel_post || {}).chat; if (c && !seen[c.id]) { seen[c.id] = 1; Logger.log(`id: ${c.id}   ${c.title || ((c.first_name || '') + ' ' + (c.last_name || ''))}`); } });
  if (!upd.length) Logger.log('Пусто. Напишите боту любое сообщение (или /start в группе) и запустите снова.');
}

/** Проверка: отправит тестовое сообщение в Telegram. */
function testTelegram() { notify(['✅ <b>Своё бистро</b>: уведомления работают!']); }

/* ======================= Вспомогательное ======================= */
function sheet(name, cols) {
  const ss = SpreadsheetApp.getActive();
  let sh = ss.getSheetByName(name);
  if (!sh) { setup(); sh = ss.getSheetByName(name); }
  return sh;
}
function appendRow(name, cols, obj) {
  const sh = sheet(name, cols);
  const row = sh.getLastRow() + 1;
  sh.getRange(row, 1, 1, cols.length).setNumberFormat('@').setValues([cols.map(c => obj[c[0]] === undefined ? '' : String(obj[c[0]]))]);
}
function readRows(name, cols) {
  const sh = sheet(name, cols);
  const last = sh.getLastRow();
  if (last < 2) return [];
  const from = Math.max(2, last - 499);                                  // последние 500 записей
  return sh.getRange(from, 1, last - from + 1, cols.length).getValues()
    .filter(r => r[0] !== '')
    .map(r => { const o = {}; cols.forEach((c, i) => o[c[0]] = r[i] instanceof Date ? stamp(r[i]) : r[i]); return o; })
    .reverse();
}
function nextSeq(key) {
  const props = PropertiesService.getScriptProperties();
  const n = (parseInt(props.getProperty(key), 10) || (key === 'SEQ_ORDER' ? 1000 : 100)) + 1;
  props.setProperty(key, String(n));
  return n;
}
function checkKey(k) { const real = prop('ADMIN_KEY'); return !!real && String(k || '') === real; }
function prop(k) { return PropertiesService.getScriptProperties().getProperty(k) || ''; }
function json(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
function stamp(d) { return Utilities.formatDate(d, TZ, 'dd.MM.yyyy HH:mm'); }
function money(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + ' ₽'; }
function fmtDate(s) { const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s || ''); return m ? `${m[3]}.${m[2]}` : esc(s || ''); }
function clean(v, max) { return String(v == null ? '' : v).replace(/[\u0000-\u001f]+/g, ' ').trim().slice(0, max).replace(/^[=+\-@]/, "'$&"); }
function cleanPhone(v) { const d = String(v || '').replace(/\D/g, ''); const n = d.length === 11 && /^[78]/.test(d) ? d.slice(1) : (d.length === 10 ? d : ''); return n ? `+7 (${n.slice(0, 3)}) ${n.slice(3, 6)}-${n.slice(6, 8)}-${n.slice(8)}` : ''; }
function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
