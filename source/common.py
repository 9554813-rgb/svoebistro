# -*- coding: utf-8 -*-
"""Общее для всех 6 дизайнов: данные бистро, фото, движок (корзина, раскрытие разделов, оформление)."""
import json, zipfile, base64

ZIP = '/mnt/user-data/uploads/Клод Своё бистро/svoe-bistro-photos.zip'

def photos():
    z = zipfile.ZipFile(ZIP)
    return {n[:-4]: 'data:image/jpeg;base64,' + base64.b64encode(z.read(n)).decode()
            for n in z.namelist() if n.endswith('.jpg')}

CFG = {
    'address': 'бульвар Белых Ночей, 3, Новоселье',
    'phone': '+7 (921) 957-47-03', 'phoneHref': 'tel:+79219574703',
    'coords': [59.807682, 30.082894],
    'yandex': 'https://yandex.ru/maps/org/svoye_bistro/97745822539/',
    'vk': 'https://vk.ru/svoe_bistro',
    'rating': '4,8', 'ratingCount': '81 оценка',
    'hours': {0: [9, 21], 1: [8, 21], 2: [8, 21], 3: [8, 21], 4: [8, 21], 5: [8, 22], 6: [9, 22]},
    'delivery': {'fee': 150, 'freeFrom': 1500, 'minOrder': 700, 'time': '45–60 минут'},
    'privacy': 'privacy.html',
    'consent': 'soglasie.html',
    # Сведения о продавце (обязательны при продаже через сайт). ИНН взят из рекламной метки
    # карточки на Яндекс Картах — СВЕРИТЬ с владельцами; остальное заполнить.
    'seller': {'name': 'ООО «СВОЕ ДЕЛО»', 'inn': '4707063482', 'ogrn': '[ОГРН]',
               'address': '[юридический адрес]', 'email': '[e-mail]'},
}

GROUPS = [
    {'id': 'bakery',    'name': 'Пекарня',        'cover': 'croissant',  'emoji': '🥐', 'note': 'Своя выпечка каждый день'},
    {'id': 'breakfast', 'name': 'Завтраки',       'cover': 'croque',     'emoji': '🍳', 'note': 'С 8:00 в будни, с 9:00 в выходные'},
    {'id': 'starters',  'name': 'Закуски',        'cover': 'tartarFries','emoji': '🥩', 'note': 'Тартары, паштеты, антипасти'},
    {'id': 'salads',    'name': 'Салаты и супы',  'cover': 'greenSalad', 'emoji': '🥗', 'note': 'Лёгкое и тёплое'},
    {'id': 'mains',     'name': 'Горячее и паста','cover': 'duck',       'emoji': '🍝', 'note': 'Паста, бургер, утка, стейк'},
    {'id': 'drinks',    'name': 'Кофе и напитки', 'cover': 'coffee',     'emoji': '☕', 'note': 'Кофе, чай, лимонады'},
]

# id, группа, название, описание, цена, фото, эмодзи, метка (hit / love / new / '')
P = [
 ('k1','bakery','Круассан классический','Слоёный, хрустящий, сливочный',180,'croissant','🥐','hit'),
 ('k3','bakery','Синнабон вишня / шоколад','С вишней, сливочным кремом и шоколадом',360,'cinnabon','🍒','love'),
 ('k5','bakery','Даниш с инжиром','Слоёное тесто, крем и свежий инжир',360,'danish','🍑','new'),
 ('k6','bakery','Аман с пеканом','Карамелизованная выпечка с пеканом',250,'aman','🌰',''),
 ('k2','bakery','Круассан миндальный','С миндальным кремом и лепестками',290,'','🥐',''),
 ('k4','bakery','Шведская булочка','Скрученная, ароматная, к кофе',180,'','🥨',''),
 ('k7','bakery','Аман классика','Хрустящая карамельная корочка',150,'','🧁',''),
 ('z1','breakfast','Крок мадам','Горячий сэндвич с сыром и яйцом',590,'croque','🍳','hit'),
 ('z2','breakfast','Сырники','С кремом из сгущёнки и сезонными фруктами',580,'syrniki','🥞','love'),
 ('z3','breakfast','Каша из зелёной гречи с пашотом','Сытно и легко',390,'grecha','🥣',''),
 ('s11','starters','Тартар с картошкой фри','Говяжий тартар и хрустящий фри',450,'tartarFries','🍟','hit'),
 ('s10','starters','Тартар с круассаном','Говяжий тартар и тёплый круассан',450,'tartarCroissant','🥩','love'),
 ('s13','starters','Креветки пиль-пиль','Аргентинские креветки с чесноком и зеленью',790,'shrimp','🦐',''),
 ('s1','starters','Хлеб и взбитое масло','Хлеб собственной выпечки',240,'','🍞',''),
 ('s3','starters','Хумус','',350,'','🥙',''),
 ('s4','starters','Взбитая брынза с томатами','',550,'','🍅',''),
 ('s5','starters','Паштет с мандаринами','',450,'','🍊',''),
 ('s6','starters','Тарамасалата из лосося','С икрой трески',600,'','🐟',''),
 ('s7','starters','Баккала мантекато','',550,'','🐟',''),
 ('s8','starters','Брезаола','',550,'','🥩',''),
 ('s9','starters','Хамон из утки мулард','',660,'','🦆',''),
 ('s12','starters','Антипасти','',750,'','🧀',''),
 ('s2','starters','Домашние оливки','',490,'','🫒',''),
 ('c2','salads','Зелёный салат','',590,'greenSalad','🥬',''),
 ('c1','salads','Израильский салат','',390,'','🥗',''),
 ('c3','salads','Салат с бедром цыплёнка','',430,'','🥗',''),
 ('u1','salads','Куриный бульон','',350,'','🍲',''),
 ('u2','salads','Луковый суп','',600,'','🧅',''),
 ('m1','mains','Смэш-бургер','',630,'burger','🍔','hit'),
 ('m3','mains','Утиная нога','С соусом из чёрной смородины',860,'duck','🦆',''),
 ('m2','mains','Куриное бедро с пюре','',720,'chicken','🍗',''),
 ('p2','mains','Каламарата с говядиной','',720,'','🍝','love'),
 ('p1','mains','Казаречче качо-э-пепе','С мортаделлой',750,'','🍝',''),
 ('p3','mains','Орзо с лангустинами','',790,'','🦐',''),
 ('m4','mains','Говяжьи щёки','С шато из овощей',820,'','🥘',''),
 ('m5','mains','Палтус с томатами и оливками','',1290,'','🐟','love'),
 ('t1','mains','Стейк с салатом из трав','Рибай, стриплойн или чак ролл',1330,'','🥩',''),
 ('f4','drinks','Капучино','',240,'coffee','☕','love'),
 ('f1','drinks','Эспрессо','',180,'','☕',''),
 ('f2','drinks','Американо','',190,'','☕',''),
 ('f3','drinks','Фильтр-кофе','',200,'','☕',''),
 ('f6','drinks','Латте','',270,'','🥛',''),
 ('f7','drinks','Флэт уайт','',270,'','☕',''),
 ('h1','drinks','Чай Эрл Грей, 600 мл','',350,'','🫖',''),
 ('h3','drinks','Травяной чай со смородиной','600 мл',350,'','🫖',''),
 ('d1','drinks','Лимонад «Lapochka»','330 мл',300,'','🍋',''),
 ('d3','drinks','Сок «Rich»','200 мл',230,'','🧃',''),
]
PRODUCTS = [dict(id=a, group=b, name=c, desc=d, price=e, photo=f, emoji=g, tag=h) for a,b,c,d,e,f,g,h in P]

REVIEWS = [
 {'name':'Татьяна Д.','date':'19 сентября','text':'Выпечка на высоком уровне собственного изготовления, чего в Новоселье нам не хватало. Очень вкусный, воздушный, хрустящий, сливочный круассан.'},
 {'name':'Кристина К.','date':'2 октября','text':'Таких вкусных крок мадам и синнабона я давно не ела. Теперь хочется приезжать сюда из города на завтраки.'},
 {'name':'Арина Ч.','date':'28 сентября','text':'Пожалуй, самый красивый интерьер в Новоселье, внимательная команда и вкусная еда. Крок мадам, бургер и тартар особенно понравились.'},
 {'name':'Кристина Л.','date':'31 октября','text':'Вкуснейший хлеб, выпечка, кофе и горячие блюда! Если собрались в бистро с ребёнком — смело идите, вам тут будут рады.'},
 {'name':'VARVARA V.','date':'25 сентября','text':'Хочется отметить ремесленный труд пекарей. Мои фавориты: шу баноффи, синнабон с вишней и шоколадный чизкейк.'},
 {'name':'Настасья Х.','date':'6 октября','text':'Друзья привезли выпечку из бистро — так вкусно, что не могли не написать отзыв. Отдельное удовольствие от красивой упаковки.'},
]

# ---------- Общие стили: корзина, форма, плавающие кнопки, базовые кнопки ----------
CSS = r'''
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:80px}
html,body{overflow-x:clip}
body{margin:0;-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}
a{color:inherit}
button{font-family:inherit}
:focus-visible{outline:3px solid var(--ui-acc);outline-offset:3px}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
body.lock{overflow:hidden}
.demo{font:500 12.5px/1.4 system-ui,sans-serif;text-align:center;padding:7px 16px;background:#111;color:#eee}
.demo b{color:#fff}
.wrap{max-width:1180px;margin:0 auto;padding:0 16px}
.emo{display:grid;place-items:center;width:100%;height:100%;font-size:40px;background:var(--ui-emo-bg,#eee)}
/* Кнопки «В корзину» и счётчик */
.add{width:100%;min-height:44px;border:var(--ui-bd);border-radius:var(--ui-btn-r);background:var(--ui-add-bg,var(--ui-acc));color:var(--ui-add-ink,var(--ui-acc-ink));font-weight:700;font-size:14px;cursor:pointer;transition:transform .15s,filter .15s}
.add:hover{filter:brightness(.95)}
.stp{display:flex;align-items:center;min-height:44px;border-radius:var(--ui-btn-r);background:var(--ui-stp-bg,var(--ui-acc));color:var(--ui-stp-ink,var(--ui-acc-ink));padding:3px;border:var(--ui-bd)}
.stp button{width:38px;height:38px;flex:none;border:0;border-radius:calc(var(--ui-btn-r) - 3px);background:rgba(255,255,255,.22);color:inherit;font:700 20px/1 system-ui;cursor:pointer}
.stp span{flex:1;text-align:center;font-weight:800}
.bump{animation:bump .45s cubic-bezier(.3,1.6,.5,1)}
@keyframes bump{30%{transform:scale(.92)}65%{transform:scale(1.06)}}
.cnt{position:absolute;top:-5px;right:-5px;min-width:21px;height:21px;padding:0 5px;border-radius:11px;background:var(--ui-cnt-bg,var(--ui-acc));color:var(--ui-cnt-ink,var(--ui-acc-ink));font:800 11px/21px system-ui;text-align:center}
.cnt.pop{animation:pop .4s}@keyframes pop{40%{transform:scale(1.4)}}
/* Корзина */
.dr-ov{position:fixed;inset:0;background:rgba(0,0,0,.45);opacity:0;pointer-events:none;transition:opacity .25s;z-index:200}
.dr-ov.open{opacity:1;pointer-events:auto}
.dr{position:fixed;top:0;right:0;height:100%;height:100dvh;width:min(440px,100%);background:var(--ui-bg);color:var(--ui-ink);z-index:210;transform:translateX(100%);transition:transform .3s cubic-bezier(.2,.8,.2,1);display:flex;flex-direction:column;box-shadow:-20px 0 40px -20px rgba(0,0,0,.4);font-family:var(--ui-font)}
.dr.open{transform:none}
.dr-h{display:flex;align-items:center;gap:10px;padding:14px 16px;border-bottom:1px solid var(--ui-line)}
.dr-h h2{margin:0;flex:1;font:var(--ui-font-h)}
.dr-x{width:42px;height:42px;border-radius:var(--ui-btn-r);border:1px solid var(--ui-line);background:var(--ui-paper);color:var(--ui-ink);font-size:22px;cursor:pointer}
.dr-b{flex:1;overflow-y:auto;padding:16px}
.dr-f{padding:14px 16px calc(14px + env(safe-area-inset-bottom));border-top:1px solid var(--ui-line);background:var(--ui-paper)}
.dr-f:empty{display:none}
.dr-row{display:grid;grid-template-columns:58px 1fr;gap:12px;padding:10px;margin-bottom:10px;background:var(--ui-paper);border-radius:var(--ui-r);border:1px solid var(--ui-line)}
.dr-th{width:58px;height:58px;border-radius:calc(var(--ui-r) - 4px);overflow:hidden}
.dr-th img{width:100%;height:100%;object-fit:cover}.dr-th .emo{font-size:26px}
.dr-n{font-weight:700;font-size:14px;line-height:1.25;display:flex;gap:8px}
.dr-n span{flex:1}.dr-n small{display:block;font-weight:500;color:var(--ui-ink2);font-size:12px;margin-top:2px}
.dr-rm{border:0;background:none;color:var(--ui-ink2);font-size:20px;cursor:pointer;line-height:1;padding:0 2px}
.dr-bot{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:8px}
.dr-bot .stp{min-height:38px}.dr-bot .stp button{width:32px;height:32px;font-size:17px}.dr-bot .stp span{min-width:26px}
.dr-sum{font-weight:800;white-space:nowrap}
.hint{background:var(--ui-soft);border-radius:var(--ui-r);padding:10px 12px;font-size:14px;margin-bottom:12px}
.prog{height:8px;background:var(--ui-paper);border-radius:8px;overflow:hidden;margin-top:8px}.prog i{display:block;height:100%;background:var(--ui-acc)}
.tot{display:flex;justify-content:space-between;font-weight:800;font-size:19px;margin:6px 0 12px}
.line{display:flex;justify-content:space-between;color:var(--ui-ink2);font-size:14px;margin-bottom:4px}
.warn{color:#B3261E;font-size:13.5px;font-weight:600;margin:0 0 10px}
.go{width:100%;min-height:52px;border:var(--ui-bd);border-radius:var(--ui-btn-r);background:var(--ui-acc);color:var(--ui-acc-ink);font-weight:800;font-size:16px;cursor:pointer}
.go:disabled{opacity:.6}
.empty{text-align:center;padding:40px 10px;color:var(--ui-ink2)}.empty b{display:block;font-size:56px;margin-bottom:8px}
.back{border:0;background:none;color:var(--ui-ink2);font-weight:600;cursor:pointer;padding:0 0 12px;font-size:14px}
.fld{margin-bottom:13px}.fld>label,.fld>.lb{display:block;font-weight:700;font-size:13px;margin-bottom:5px}
.fld input[type=text],.fld input[type=tel],.fld input[type=date],.fld select,.fld textarea{width:100%;min-height:48px;border:1.5px solid var(--ui-line);border-radius:var(--ui-btn-r);background:var(--ui-paper);color:var(--ui-ink);padding:11px 13px;font:16px var(--ui-font)}
.fld textarea{min-height:76px;resize:vertical}
.fld input:focus,.fld select:focus,.fld textarea:focus{outline:none;border-color:var(--ui-acc)}
.fld .bad{border-color:#B3261E!important}
.er{color:#B3261E;font-size:12.5px;font-weight:600;margin-top:3px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.seg{display:grid;grid-template-columns:1fr 1fr;gap:5px;background:var(--ui-soft);padding:4px;border-radius:calc(var(--ui-btn-r) + 4px)}
.seg input{position:absolute;opacity:0;pointer-events:none}
.seg label{min-height:44px;display:flex;align-items:center;justify-content:center;border-radius:var(--ui-btn-r);font-weight:700;font-size:14px;cursor:pointer}
.seg input:checked+label{background:var(--ui-paper);box-shadow:0 3px 10px -4px rgba(0,0,0,.25)}
.seg input:focus-visible+label{outline:3px solid var(--ui-acc)}
.chk{display:flex;gap:10px;align-items:flex-start;font-size:13px}.chk input{width:21px;height:21px;flex:none;accent-color:var(--ui-acc)}
.done{text-align:center;padding:26px 4px}.done b{display:block;font-size:60px}
.ono{display:inline-block;font-weight:800;font-size:21px;background:var(--ui-soft);padding:10px 16px;border-radius:var(--ui-r);margin:8px 0 14px}
/* Плашка корзины на телефоне */
.cbar{position:fixed;left:12px;right:12px;bottom:calc(12px + env(safe-area-inset-bottom));z-index:120;display:none;align-items:center;justify-content:space-between;gap:10px;min-height:56px;padding:0 20px;border:var(--ui-bd);border-radius:var(--ui-btn-r);background:var(--ui-acc);color:var(--ui-acc-ink);font:700 15px var(--ui-font);cursor:pointer;box-shadow:0 12px 28px -10px rgba(0,0,0,.5)}
.cbar.show{display:flex}
@media (min-width:960px){.cbar{display:none!important}}
/* Плавающие кнопки «наверх / вниз» */
.fnav{position:fixed;left:10px;bottom:calc(80px + env(safe-area-inset-bottom));z-index:110;display:flex;flex-direction:column;gap:8px;opacity:0;pointer-events:none;transform:translateY(8px);transition:opacity .25s,transform .25s}
.fnav.show{opacity:1;pointer-events:auto;transform:none}
.fnav button{width:46px;height:46px;border-radius:var(--ui-fn-r,50%);border:var(--ui-bd);background:var(--ui-paper);color:var(--ui-ink);display:grid;place-items:center;cursor:pointer;box-shadow:0 8px 20px -8px rgba(0,0,0,.45)}
.fnav button:first-child{background:var(--ui-acc);color:var(--ui-acc-ink)}
.fnav button[hidden]{display:none}
@media (min-width:960px){.fnav{bottom:24px;left:auto;right:18px}}
@media (max-width:959px){.fnav button{width:42px;height:42px;opacity:.92}}
.seller{font-size:11.5px;line-height:1.5;opacity:.72;padding:12px 0 0}.seller a{color:inherit}
.reveal{opacity:0;transform:translateY(18px);transition:opacity .6s ease,transform .6s ease}
.reveal.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation:none!important;transition:none!important}.reveal{opacity:1;transform:none}}
'''

# ---------- Общий движок ----------
JS = r'''
(function(){
const D = window.DATA, PH = window.PH, TPL = window.TPL;
const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
const byId = Object.fromEntries(D.products.map(p => [p.id, p]));
const fmt = n => n.toLocaleString('ru-RU') + ' ₽';
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const photo = k => (k && PH[k]) ? PH[k] : '';
const KEY = 'svoe-bistro-' + (document.body.dataset.v || 'x');
const DAYS = ['Воскресенье','Понедельник','Вторник','Среда','Четверг','Пятница','Суббота'];
const SHORT = ['Вс','Пн','Вт','Ср','Чт','Пт','Сб'];
let cart = (() => { try { const r = JSON.parse(localStorage.getItem(KEY) || '{}'), c = {}; for (const k in r) if (byId[k] && r[k] > 0) c[k] = Math.min(99, r[k] | 0); return c; } catch(e){ return {}; } })();
const save = () => { try { localStorage.setItem(KEY, JSON.stringify(cart)); } catch(e){} };

function action(id){
  const q = cart[id] || 0, n = esc(byId[id].name);
  return q ? `<div class="stp" role="group" aria-label="Количество: ${n}"><button data-dec="${id}" aria-label="Убрать одну">−</button><span>${q}</span><button data-inc="${id}" aria-label="Добавить ещё">+</button></div>`
           : `<button class="add" data-add="${id}" aria-label="В корзину: ${n}">${window.ADD_LABEL || '+ В корзину'}</button>`;
}
const slot = id => `<div class="act" data-act="${id}">${action(id)}</div>`;
const thumb = (p, alt) => p.photo ? `<img src="${photo(p.photo)}" alt="${esc(alt || p.name)}" loading="lazy" decoding="async">` : `<span class="emo" role="img" aria-label="${esc(p.name)}">${p.emoji}</span>`;
const TAGS = { hit:'Хит', love:'Хвалят гости', new:'Новинка' };
window.UI = { fmt, esc, photo, slot, thumb, TAGS, byId };

/* ---------- Заполнение страницы ---------- */
function fill(){
  $$('img[data-photo]').forEach(i => { i.src = photo(i.dataset.photo); });
  $$('[data-bg]').forEach(e => { e.style.backgroundImage = `url(${photo(e.dataset.bg)})`; });
  $$('[data-cfg]').forEach(e => { e.textContent = D.cfg[e.dataset.cfg]; });
  $$('a[data-tel]').forEach(a => a.href = D.cfg.phoneHref);
  $$('a[data-route]').forEach(a => { a.href = `https://yandex.ru/maps/?rtext=~${D.cfg.coords[0]},${D.cfg.coords[1]}&rtt=auto`; a.target = '_blank'; a.rel = 'noopener'; });
  $$('a[data-reviews-link]').forEach(a => { a.href = D.cfg.yandex + 'reviews/'; a.target = '_blank'; a.rel = 'noopener'; });
  $$('a[data-vk]').forEach(a => { a.href = D.cfg.vk; a.target = '_blank'; a.rel = 'noopener'; });
  $$('iframe[data-map]').forEach(f => { const [la, lo] = D.cfg.coords; f.src = `https://yandex.ru/map-widget/v1/?ll=${lo}%2C${la}&z=16&pt=${lo},${la},pm2rdm&lang=ru_RU`; });
  $$('a[data-privacy]').forEach(a => a.href = D.cfg.privacy);
  $$('[data-year]').forEach(e => e.textContent = new Date().getFullYear());
  // группы: число позиций и «от … ₽»
  D.groups.forEach(g => {
    const items = D.products.filter(p => p.group === g.id);
    $$(`[data-gcount="${g.id}"]`).forEach(e => e.textContent = items.length + ' ' + plural(items.length, 'позиция', 'позиции', 'позиций'));
    $$(`[data-gfrom="${g.id}"]`).forEach(e => e.textContent = 'от ' + fmt(Math.min(...items.map(p => p.price))));
  });
  $$('[data-group-items]').forEach(el => {
    const g = el.dataset.groupItems;
    el.innerHTML = D.products.filter(p => p.group === g).map(p => TPL.item(p)).join('');
  });
  $$('[data-reviews]').forEach(el => { el.innerHTML = D.reviews.slice(0, +el.dataset.reviews || 3).map((r, i) => TPL.review(r, i)).join(''); });
  // часы и статус
  const now = new Date(), d = now.getDay(), [o, c] = D.cfg.hours[d], h = now.getHours() + now.getMinutes() / 60, open = h >= o && h < c;
  const nextOpen = D.cfg.hours[h >= c ? (d + 1) % 7 : d][0];
  $$('[data-status]').forEach(e => { e.textContent = open ? `Открыто до ${c}:00` : `Закрыто · откроемся в ${nextOpen}:00`; e.classList.toggle('closed', !open); });
  $$('[data-hours]').forEach(el => {
    el.innerHTML = [1,2,3,4,5,6,0].map(i => `<li class="${i === d ? 'today' : ''}"><span>${el.dataset.hours === 'short' ? SHORT[i] : DAYS[i]}</span><b>${D.cfg.hours[i][0]}:00–${D.cfg.hours[i][1]}:00</b></li>`).join('');
  });
  $$('[data-open]').forEach(t => { const el = document.getElementById(t.dataset.open); const on = !!el && el.classList.contains('is-open'); t.setAttribute('aria-expanded', on); t.classList.toggle('is-active', on); if (el) t.setAttribute('aria-controls', el.id); });
}
const plural = (n, a, b, c) => { const m10 = n % 10, m100 = n % 100; return m10 === 1 && m100 !== 11 ? a : (m10 >= 2 && m10 <= 4 && (m100 < 10 || m100 >= 20) ? b : c); };

/* ---------- Раскрытие разделов ---------- */
function setOpen(el, on){
  el.classList.toggle('is-open', on);
  $$(`[data-open="${el.id}"]`).forEach(o => { o.setAttribute('aria-expanded', on); o.classList.toggle('is-active', on); });
  if (el.classList.contains('modal')) document.body.classList.toggle('lock', on || !!$('.modal.is-open') || drawerOpen);
}
function toggle(t){
  const el = document.getElementById(t.dataset.open); if (!el) return;
  const was = el.classList.contains('is-open');
  if (was && t.hasAttribute('data-keep')) return;
  if (t.dataset.scope) $$(`[data-open][data-scope="${t.dataset.scope}"]`).forEach(o => { if (o.dataset.open !== el.id){ const x = document.getElementById(o.dataset.open); if (x && x.classList.contains('is-open')) setOpen(x, false); } });
  setOpen(el, !was);
  if (!was && t.hasAttribute('data-scroll')) setTimeout(() => {
    const r = el.getBoundingClientRect(), off = +t.dataset.scroll || 90;
    if (r.top < off || r.top > innerHeight * .55) window.scrollTo({ top: scrollY + r.top - off, behavior: 'smooth' });
  }, 80);
}

/* ---------- Корзина ---------- */
let drawerOpen = false, view = 'cart', lastFocus = null, last = 0;
const form = { method: 'delivery' };
const count = () => Object.values(cart).reduce((a, b) => a + b, 0);
const sub = () => Object.entries(cart).reduce((s, [id, q]) => s + byId[id].price * q, 0);
const delCost = (s, m) => m !== 'delivery' ? 0 : (s >= D.cfg.delivery.freeFrom ? 0 : D.cfg.delivery.fee);
function setQty(id, q){ q = Math.max(0, Math.min(99, q)); if (q) cart[id] = q; else delete cart[id]; save(); refresh(); }
function refresh(){
  const n = count();
  $$('[data-cart-count]').forEach(c => { c.textContent = n; if (n !== last){ c.classList.remove('pop'); void c.offsetWidth; c.classList.add('pop'); } });
  last = n;
  $$('[data-act]').forEach(e => e.innerHTML = action(e.dataset.act));
  $('#cbar').classList.toggle('show', n > 0 && !drawerOpen);
  $('#cbarT').textContent = `Корзина · ${n} шт · ${fmt(sub())}`;
  if (drawerOpen && view === 'cart') renderCart();
  if (drawerOpen && view === 'form') sumBox();
}
function openDrawer(){ lastFocus = document.activeElement; drawerOpen = true; view = 'cart'; $('#dr').classList.add('open'); $('#drOv').classList.add('open'); $('#dr').setAttribute('aria-hidden','false'); document.body.classList.add('lock'); $('#cbar').classList.remove('show'); renderCart(); setTimeout(() => $('#drX').focus(), 50); }
function closeDrawer(){ drawerOpen = false; $('#dr').classList.remove('open'); $('#drOv').classList.remove('open'); $('#dr').setAttribute('aria-hidden','true'); if (!$('.modal.is-open')) document.body.classList.remove('lock'); view = 'cart'; refresh(); if (lastFocus) lastFocus.focus(); }
function renderCart(){
  $('#drT').textContent = 'Корзина';
  const ids = Object.keys(cart), b = $('#drB'), f = $('#drF');
  if (!ids.length){ b.innerHTML = `<div class="empty"><b aria-hidden="true">🥐</b>Пока пусто. Начните с круассана — с него всё начинается.</div>`; f.innerHTML = ''; return; }
  const s = sub(), dl = D.cfg.delivery;
  const hint = s < dl.freeFrom ? `<div class="hint">Ещё <b>${fmt(dl.freeFrom - s)}</b> до бесплатной доставки<div class="prog"><i style="width:${Math.min(100, s / dl.freeFrom * 100)}%"></i></div></div>` : `<div class="hint">🎉 Доставка будет бесплатной</div>`;
  b.innerHTML = hint + ids.map(id => { const p = byId[id], q = cart[id]; return `<div class="dr-row"><div class="dr-th">${thumb(p)}</div><div>
    <div class="dr-n"><span>${esc(p.name)}<small>${fmt(p.price)}</small></span><button class="dr-rm" data-rm="${id}" aria-label="Удалить ${esc(p.name)}">×</button></div>
    <div class="dr-bot"><div class="stp"><button data-dec="${id}" aria-label="Убрать одну">−</button><span>${q}</span><button data-inc="${id}" aria-label="Добавить ещё">+</button></div><span class="dr-sum">${fmt(p.price * q)}</span></div></div></div>`; }).join('');
  const minW = s < dl.minOrder ? `<p class="warn">Минимум на доставку — ${fmt(dl.minOrder)}. Самовывоз — без минимума.</p>` : '';
  f.innerHTML = `${minW}<div class="tot"><span>Итого</span><span>${fmt(s)}</span></div><button class="go" data-checkout>Оформить заказ →</button>`;
}
const todayISO = () => { const d = new Date(); d.setMinutes(d.getMinutes() - d.getTimezoneOffset()); return d.toISOString().slice(0, 10); };
function times(ds){
  const day = new Date(ds + 'T12:00').getDay(), [o, c] = D.cfg.hours[day], today = ds === todayISO(), nh = new Date().getHours();
  let r = today && nh >= o && nh < c - 1 ? '<option>Как можно скорее</option>' : '';
  for (let h = o; h < c; h++){ if (today && h <= nh) continue; r += `<option>${String(h).padStart(2,'0')}:00–${String(h + 1).padStart(2,'0')}:00</option>`; }
  return r || '<option value="">Сегодня уже не успеем — выберите завтра</option>';
}
function renderForm(){
  view = 'form'; $('#drT').textContent = 'Оформление';
  $('#drB').innerHTML = `<button class="back" data-back>← Назад в корзину</button><form id="of" novalidate>
   <div class="fld"><span class="lb">Как получить</span><div class="seg"><input type="radio" name="m" id="m1" value="delivery" ${form.method === 'delivery' ? 'checked' : ''}><label for="m1">🛵 Доставка</label><input type="radio" name="m" id="m2" value="pickup" ${form.method === 'pickup' ? 'checked' : ''}><label for="m2">🏃 Самовывоз</label></div></div>
   <div class="fld"><label for="fn">Имя</label><input type="text" id="fn" autocomplete="given-name" placeholder="Как к вам обращаться"><div class="er" id="en"></div></div>
   <div class="fld"><label for="fp">Телефон</label><input type="tel" id="fp" inputmode="tel" autocomplete="tel" placeholder="+7 (___) ___-__-__"><div class="er" id="ep"></div></div>
   <div class="fld" id="fa" ${form.method === 'pickup' ? 'hidden' : ''}><label for="fad">Адрес в Новоселье</label><input type="text" id="fad" autocomplete="street-address" placeholder="Улица, дом, подъезд, квартира"><div class="er" id="ea"></div></div>
   <div class="two"><div class="fld"><label for="fd">Дата</label><input type="date" id="fd" min="${todayISO()}" value="${todayISO()}"></div><div class="fld"><label for="ft">Время</label><select id="ft">${times(todayISO())}</select></div></div>
   <div class="fld"><label for="fc">Комментарий</label><textarea id="fc" placeholder="Домофон, приборы, прожарка…"></textarea></div>
   <input type="text" id="fw" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px">
   <div class="fld"><label class="chk"><input type="checkbox" id="fk"><span>Даю <a href="${D.cfg.consent}" target="_blank" rel="noopener">согласие на обработку персональных данных</a></span></label><p style="margin:6px 0 0;font-size:12px;color:var(--ui-ink2)">Порядок обработки — в <a href="${D.cfg.privacy}" target="_blank" rel="noopener">политике обработки персональных данных</a>.</p><div class="er" id="ek"></div></div>
  </form>`;
  $('#drF').innerHTML = `<div id="sb"></div><p class="warn" id="se" hidden></p><button class="go" type="submit" form="of" id="sbtn">Отправить заказ</button>`;
  sumBox();
  const f = $('#of');
  f.addEventListener('change', e => {
    if (e.target.name === 'm'){ form.method = e.target.value; $('#fa').hidden = form.method !== 'delivery'; sumBox(); }
    if (e.target.id === 'fd') $('#ft').innerHTML = times(e.target.value || todayISO());
  });
  $('#fp').addEventListener('focus', e => { if (!e.target.value) e.target.value = '+7 '; });
  $('#fp').addEventListener('input', e => { let d = e.target.value.replace(/\D/g, ''); if (d[0] === '7' || d[0] === '8') d = d.slice(1); if (d.length > 10 && (d[0] === '7' || d[0] === '8')) d = d.slice(1); d = d.slice(0, 10); let r = '+7'; if (d.length) r += ' (' + d.slice(0, 3); if (d.length >= 3) r += ') ' + d.slice(3, 6); if (d.length >= 6) r += '-' + d.slice(6, 8); if (d.length >= 8) r += '-' + d.slice(8, 10); e.target.value = r; });
  f.addEventListener('submit', submit);
  $('#drB').scrollTop = 0;
}
function sumBox(){ const b = $('#sb'); if (!b) return; const s = sub(), dc = delCost(s, form.method);
  b.innerHTML = `<div class="line"><span>Блюда (${count()} шт)</span><span>${fmt(s)}</span></div>${form.method === 'delivery' ? `<div class="line"><span>Доставка</span><span>${dc ? fmt(dc) : 'бесплатно'}</span></div>` : ''}<div class="tot"><span>К оплате</span><span>${fmt(s + dc)}</span></div>`; }
async function submit(e){
  e.preventDefault();
  const v = { name: $('#fn').value.trim(), phone: $('#fp').value, addr: $('#fad').value.trim(), date: $('#fd').value, time: $('#ft').value };
  const er = {}; if (v.name.length < 2) er.n = 'Напишите имя'; if (v.phone.replace(/\D/g, '').length !== 11) er.p = 'Проверьте телефон';
  if (form.method === 'delivery' && v.addr.length < 5) er.a = 'Укажите адрес'; if (!$('#fk').checked) er.k = 'Нужно согласие';
  [['n','#fn'],['p','#fp'],['a','#fad'],['k','#fk']].forEach(([k, s]) => { $('#e' + k).textContent = er[k] || ''; $(s).classList.toggle('bad', !!er[k]); $(s).setAttribute('aria-invalid', !!er[k]); });
  const s = sub(), se = $('#se');
  if (form.method === 'delivery' && s < D.cfg.delivery.minOrder){ se.hidden = false; se.textContent = `Минимум на доставку — ${fmt(D.cfg.delivery.minOrder)}. Добавьте ещё ${fmt(D.cfg.delivery.minOrder - s)} или выберите самовывоз.`; return; }
  const first = Object.keys(er)[0]; if (first){ $({ n:'#fn', p:'#fp', a:'#fad', k:'#fk' }[first]).focus(); return; }
  const btn = $('#sbtn'); btn.disabled = true; btn.textContent = 'Отправляем…'; se.hidden = true;
  let no;
  if (window.API_URL){
    // Отправка заказа на сервер (Google Apps Script). Цены сервер пересчитает сам.
    try {
      const r = await fetch(window.API_URL, { method: 'POST', headers: { 'Content-Type': 'text/plain;charset=utf-8' },
        body: JSON.stringify({ type: 'order', method: form.method, name: v.name, phone: v.phone, address: v.addr, date: v.date, time: v.time,
          comment: $('#fc').value.trim(), website: $('#fw') ? $('#fw').value : '', items: Object.entries(cart).map(([id, q]) => ({ id, q })) }) });
      const j = await r.json();
      if (!j.ok) throw new Error(j.error || 'Ошибка сервера');
      no = j.number;
    } catch(err){
      se.hidden = false; se.textContent = `Не получилось отправить заказ (${err.message}). Попробуйте ещё раз или позвоните: ${D.cfg.phone}`;
      btn.disabled = false; btn.textContent = 'Отправить заказ'; return;
    }
  } else {
    await new Promise(r => setTimeout(r, 600));          // ДЕМО: адрес сервера не указан
    no = `${String(new Date().getDate()).padStart(2,'0')}${String(new Date().getMonth() + 1).padStart(2,'0')}-${Math.floor(1000 + Math.random() * 9000)}`;
  }
  cart = {}; save(); view = 'done'; $('#drT').textContent = 'Готово!';
  $('#drB').innerHTML = `<div class="done" role="status"><b aria-hidden="true">🥐</b><h3>Спасибо, заказ принят!</h3><div class="ono">№ ${no}</div><p>${form.method === 'delivery' ? 'Привезём' : 'Будет готов к самовывозу'}: ${v.date.split('-').reverse().join('.')}, ${esc(v.time)}.</p><p>Мы перезвоним, чтобы подтвердить заказ.</p>${window.API_URL ? '' : '<p style="font-size:12.5px;opacity:.7">Демо-режим: заказ никуда не отправлен.</p>'}<button class="go" data-close-dr>Вернуться к меню</button></div>`;
  $('#drF').innerHTML = ''; refresh();
}

/* ---------- Каркас: корзина, плашка, кнопки наверх/вниз ---------- */
document.body.insertAdjacentHTML('beforeend', `
<div class="dr-ov" id="drOv"></div>
<aside class="dr" id="dr" role="dialog" aria-modal="true" aria-labelledby="drT" aria-hidden="true">
  <div class="dr-h"><h2 id="drT">Корзина</h2><button class="dr-x" id="drX" aria-label="Закрыть корзину">×</button></div>
  <div class="dr-b" id="drB"></div><div class="dr-f" id="drF"></div>
</aside>
<div class="fnav" id="fnav">
  <button id="fUp" aria-label="Наверх"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg></button>
  <button id="fDown" aria-label="Вниз, к контактам"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M19 12l-7 7-7-7"/></svg></button>
</div>
<button class="cbar" id="cbar"><span id="cbarT"></span><span>Оформить →</span></button>`);

document.addEventListener('click', e => {
  const t = e.target.closest('button, a, [data-open]'); if (!t) return;
  if (t.dataset.open !== undefined && t.dataset.open){ e.preventDefault(); toggle(t); return; }
  if (t.hasAttribute('data-close')){ const m = t.closest('.is-open'); if (m) setOpen(m, false); return; }
  if (t.dataset.add){ setQty(t.dataset.add, (cart[t.dataset.add] || 0) + 1); $$(`[data-act="${t.dataset.add}"] .stp`).forEach(x => x.classList.add('bump')); return; }
  if (t.dataset.inc){ setQty(t.dataset.inc, (cart[t.dataset.inc] || 0) + 1); return; }
  if (t.dataset.dec){ setQty(t.dataset.dec, (cart[t.dataset.dec] || 0) - 1); return; }
  if (t.dataset.rm){ setQty(t.dataset.rm, 0); return; }
  if (t.hasAttribute('data-open-cart') || t.id === 'cbar'){ e.preventDefault(); openDrawer(); return; }
  if (t.hasAttribute('data-checkout')){ renderForm(); return; }
  if (t.hasAttribute('data-back')){ view = 'cart'; renderCart(); return; }
  if (t.hasAttribute('data-close-dr') || t.id === 'drX'){ closeDrawer(); return; }
});
$('#drOv').addEventListener('click', closeDrawer);
$$('.modal').forEach(m => m.addEventListener('click', e => { if (e.target === m) setOpen(m, false); }));
document.addEventListener('keydown', e => { if (e.key !== 'Escape') return; if (drawerOpen) return closeDrawer(); $$('.modal.is-open').forEach(m => setOpen(m, false)); });
document.addEventListener('animationend', e => e.target.classList.remove('bump'));
function fnav(){ const y = scrollY, h = document.documentElement.scrollHeight - innerHeight; $('#fnav').classList.toggle('show', y > 450); $('#fDown').hidden = y > h - 250; }
$('#fUp').addEventListener('click', () => scrollTo({ top: 0, behavior: 'smooth' }));
$('#fDown').addEventListener('click', () => scrollTo({ top: document.documentElement.scrollHeight, behavior: 'smooth' }));
addEventListener('scroll', fnav, { passive: true });
// появление блоков при прокрутке
const io = 'IntersectionObserver' in window ? new IntersectionObserver(es => es.forEach(x => { if (x.isIntersecting){ x.target.classList.add('in'); io.unobserve(x.target); } }), { threshold: .1 }) : null;
$$('.reveal').forEach(el => io ? io.observe(el) : el.classList.add('in'));

if (window.API_URL) $$('.demo').forEach(d => d.remove());
{ const S = D.cfg.seller, f = $('footer');
  if (S && f) f.insertAdjacentHTML('beforeend', `<div class="seller"><div class="wrap">Продавец: ${esc(S.name)} · ИНН ${esc(S.inn)} · ОГРН ${esc(S.ogrn)} · ${esc(S.address)} · ${esc(D.cfg.phone)} · ${esc(S.email)} · <a href="${D.cfg.privacy}">Политика обработки персональных данных</a> · <a href="${D.cfg.consent}">Согласие на обработку ПДн</a></div></div>`); }
fill(); refresh(); fnav();
if (window.AFTER) window.AFTER();
})();
'''

DEMO = '<div class="demo"><b>Демо-концепт</b> сайта с доставкой для «Своего бистро» · заказы не отправляются, условия доставки — пример</div>'

def page(v, title, fonts, css, body, tpl, add_label='+ В корзину', after=''):
    """Собирает один самодостаточный HTML-файл."""
    data = {'products': PRODUCTS, 'groups': GROUPS, 'reviews': REVIEWS, 'cfg': CFG}
    return ('<!doctype html><html lang="ru"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            f'<title>{title}</title>'
            '<meta name="description" content="Бистро с пекарней в Новоселье: выпечка, завтраки и любимые блюда. Доставка и самовывоз.">'
            '<script>/* ===== АДРЕС СЕРВЕРА ЗАКАЗОВ =====\n   Вставьте между кавычками ссылку веб-приложения Google Apps Script (…/exec).\n   Пусто — сайт работает в демо-режиме, заказы никуда не уходят. */\nwindow.API_URL = \'\';</script>'
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            f'<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">'
            f'<style>{CSS}\n{css}</style></head><body data-v="{v}">{DEMO}{body}'
            f'<script>window.PH={json.dumps(photos())};window.DATA={json.dumps(data, ensure_ascii=False)};'
            f'window.ADD_LABEL={json.dumps(add_label, ensure_ascii=False)};window.TPL={tpl};{after}</script>'
            f'<script>{JS}</script></body></html>')
