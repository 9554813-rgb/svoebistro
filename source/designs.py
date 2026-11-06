# -*- coding: utf-8 -*-
from common import GROUPS, page
import random

PIN = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
CLOCK = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'
PHONE = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>'
BAG = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 8h12l-1 12H7L6 8Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>'
ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CLOSE = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>'
ICONS = {  # линейные иконки «почему мы»
 'bread':'<path d="M5 11a4 4 0 0 1 3-6h8a4 4 0 0 1 3 6v8H5z"/><path d="M9 11v8M15 11v8"/>',
 'cup':'<path d="M4 9h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"/><path d="M17 11h1.5a2.5 2.5 0 0 1 0 5H17"/><path d="M8 3c0 2 2 2 2 4M12 3c0 2 2 2 2 4"/>',
 'sun':'<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 'bike':'<circle cx="6" cy="17" r="3"/><circle cx="18" cy="17" r="3"/><path d="M6 17l4-8h5l3 8M10 9 8 5H5M15 9l1-3h3"/>',
}
def icon(k, size=30): return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[k]}</svg>'

FEATS = [('bread','Своя выпечка','Круассаны, синнабоны и хлеб на закваске каждое утро'),
         ('sun','Завтраки с 8:00','Крок мадам, сырники, каша из зелёной гречи'),
         ('cup','Хороший кофе','Капучино, фильтр, флэт уайт — и чай в больших чайниках'),
         ('bike','Доставка и самовывоз','Привезём по Новоселью или соберём к вашему приходу')]

TAG_JS = "${p.tag?`<span class=\"tag t-${p.tag}\">${UI.TAGS[p.tag]}</span>`:''}"

D = []

# =====================================================================
# 1. ШАЛФЕЙ — по референсу «КофеЛавка»: органика, круглые фото, шалфей
# =====================================================================
def d1():
    groups = ''.join(f'''<button class="g" data-open="g-{g["id"]}" data-scope="grp" data-keep data-scroll="150">
      <span class="g-ph"><img data-photo="{g["cover"]}" alt=""></span><b>{g["name"]}</b><small data-gcount="{g["id"]}"></small><em data-gfrom="{g["id"]}"></em></button>''' for g in GROUPS)
    panels = ''.join(f'''<div class="panel{' is-open' if i == 0 else ''}" id="g-{g["id"]}" role="region" aria-label="{g["name"]}">
      <div class="panel-h"><h3>{g["name"]}</h3><p>{g["note"]}</p></div><div class="items" data-group-items="{g["id"]}"></div></div>''' for i, g in enumerate(GROUPS))
    feats = ''.join(f'<div class="f"><span class="f-i">{icon(k)}</span><b>{t}</b><p>{s}</p></div>' for k, t, s in FEATS)
    body = f'''
<header class="hd"><div class="wrap hd-in">
  <a class="logo" href="#top"><img data-photo="logo" alt="Логотип «Своё бистро»"><span><b>своё бистро</b><small>пекарня · Новоселье</small></span></a>
  <nav class="nav" aria-label="Разделы"><a href="#menu">Меню</a><a href="#why">О нас</a><a href="#reviews">Отзывы</a><a href="#contacts">Контакты</a></nav>
  <a class="ib" data-tel aria-label="Позвонить">{PHONE}</a>
  <button class="ib cart" data-open-cart aria-label="Корзина">{BAG}<span class="cnt" data-cart-count>0</span></button>
</div></header>
<main id="top">
<section class="hero wrap">
  <div class="hero-t reveal">
    <h1>Своя выпечка и&nbsp;любимые блюда — к&nbsp;вам домой</h1>
    <p>Бистро с пекарней в самом сердце Новоселья. Завтраки с 8:00, горячее и кофе — с доставкой и самовывозом.</p>
    <a href="#menu" class="btn">Посмотреть меню {ARROW}</a>
    <div class="rate"><span class="av"><img data-photo="croissant" alt=""><img data-photo="cinnabon" alt=""><img data-photo="croque" alt=""></span>
      <span><b><span data-cfg="rating"></span> ★</b> · <span data-cfg="ratingCount"></span><br>на Яндекс Картах</span></div>
  </div>
  <div class="hero-i reveal">
    <div class="blob"><img data-photo="syrniki" alt="Сырники с кремом и клубникой"></div>
    <div class="loc">{PIN}<span><span data-cfg="address"></span><br><small data-status></small></span></div>
    <svg class="leaf" width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" aria-hidden="true"><path d="M5 19C5 10 11 5 20 4c-1 9-6 15-15 15z"/><path d="M5 19 14 10"/></svg>
  </div>
</section>
<section id="menu" class="wrap sec">
  <div class="sec-h reveal"><h2>Что у нас есть</h2><p>Нажмите на группу — ниже откроется меню</p></div>
  <div class="groups">{groups}</div>
  <div class="panels">{panels}</div>
</section>
<section id="why" class="wrap"><div class="why reveal"><h2>Почему гости выбирают нас</h2><div class="feats">{feats}</div></div></section>
<section id="reviews" class="wrap sec">
  <div class="sec-h reveal"><h2>Отзывы гостей</h2><a data-reviews-link class="lnk">Все отзывы на Яндекс Картах →</a></div>
  <div class="revs" data-reviews="3"></div>
</section>
<section id="contacts" class="wrap sec">
  <div class="cont reveal">
    <div class="cont-t"><h2>Приходите в гости!</h2><p>Или закажите домой — привезём тёплым.</p>
      <ul class="info"><li>{PIN}<span data-cfg="address"></span></li><li>{CLOCK}<span data-status></span></li><li>{PHONE}<a data-tel data-cfg="phone"></a></li></ul>
      <ul class="hours" data-hours="short"></ul>
      <a class="btn" data-route>Построить маршрут {ARROW}</a></div>
    <div class="map"><iframe data-map title="Своё бистро на карте" loading="lazy"></iframe></div>
  </div>
</section>
</main>
<footer class="ft"><div class="wrap ft-in"><span class="ft-logo">своё бистро</span><span>Выпечка · Завтраки · Любимые блюда</span><a data-vk>ВКонтакте</a><a data-privacy>Политика конфиденциальности</a><small>© <span data-year></span> · демо-концепт</small></div></footer>'''
    css = r'''
:root{--bg:#F7F1E8;--paper:#FFFCF7;--sage:#D4DCC8;--sage2:#E6EBDD;--sage-d:#7E9468;--ink:#2B2A26;--ink2:#6B675E;--or:#E8742F;--or-d:#D2621F;--line:#E8DFD2;
--ui-bg:var(--bg);--ui-paper:var(--paper);--ui-ink:var(--ink);--ui-ink2:var(--ink2);--ui-line:var(--line);--ui-acc:var(--or);--ui-acc-ink:#fff;--ui-soft:var(--sage2);--ui-r:22px;--ui-btn-r:999px;--ui-bd:0;--ui-font:'Nunito',sans-serif;--ui-font-h:700 22px 'Comfortaa',sans-serif;--ui-emo-bg:var(--sage2);--ui-add-bg:var(--sage2);--ui-add-ink:var(--ink)}
body{background:var(--bg);color:var(--ink);font:16px/1.55 'Nunito',sans-serif}
h1,h2,h3{font-family:'Comfortaa',sans-serif;font-weight:700;line-height:1.15;margin:0 0 .45em;letter-spacing:-.01em}
.btn{display:inline-flex;align-items:center;gap:10px;min-height:52px;padding:0 26px;border-radius:999px;background:var(--or);color:#fff;font-weight:800;text-decoration:none;box-shadow:0 10px 22px -10px rgba(232,116,47,.8);transition:transform .15s,background .15s}
.btn:hover{background:var(--or-d);transform:translateY(-2px)}
.hd{position:sticky;top:0;z-index:50;background:rgba(247,241,232,.93);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.hd-in{display:flex;align-items:center;gap:10px;height:68px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;margin-right:auto}
.logo img{width:44px;height:44px;border-radius:50%}
.logo b{display:block;font:700 19px 'Comfortaa',sans-serif;color:var(--ink)}.logo small{color:var(--ink2);font-size:12px}
.nav{display:none;gap:4px;margin-right:10px}.nav a{text-decoration:none;font-weight:700;padding:8px 14px;border-radius:999px}.nav a:hover{background:var(--sage2)}
@media(min-width:900px){.nav{display:flex}}
.ib{position:relative;width:46px;height:46px;border-radius:50%;border:0;background:var(--paper);color:var(--ink);display:grid;place-items:center;cursor:pointer;text-decoration:none}
.ib.cart{background:var(--or);color:#fff}
.hero{display:grid;gap:26px;padding-top:16px;padding-bottom:30px;align-items:center}
@media(min-width:900px){.hero{grid-template-columns:1fr 1.05fr;gap:40px;padding-top:30px}}
.hero h1{font-size:clamp(32px,7.5vw,54px)}
.hero p{color:var(--ink2);font-size:17px;max-width:470px;margin:0 0 24px}
.rate{display:flex;align-items:center;gap:12px;margin-top:24px;font-size:14px;color:var(--ink2)}
.rate .av{display:flex}.rate .av img{width:38px;height:38px;border-radius:50%;object-fit:cover;border:3px solid var(--bg);margin-left:-10px}.rate .av img:first-child{margin-left:0}
.rate b{color:var(--ink)}
.hero-i{position:relative}
.blob{aspect-ratio:1/1;max-width:560px;margin:0 auto;border-radius:58% 42% 50% 50%/48% 56% 44% 52%;overflow:hidden;box-shadow:0 30px 60px -30px rgba(80,60,30,.5);background:var(--sage)}
.blob img{width:100%;height:100%;object-fit:cover}
.loc{position:absolute;right:4%;bottom:6%;display:flex;gap:10px;align-items:flex-start;background:rgba(255,252,247,.94);border-radius:18px;padding:12px 14px;font-size:13px;max-width:230px;box-shadow:0 14px 30px -14px rgba(0,0,0,.35)}
.loc svg{color:var(--sage-d);flex:none}.loc small{color:var(--sage-d);font-weight:700}
.leaf{position:absolute;left:2%;top:4%;color:var(--sage-d);opacity:.8}
.sec{padding:40px 16px}
.sec-h{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:6px 20px;margin-bottom:20px}
.sec-h h2{font-size:clamp(26px,5.5vw,38px);margin:0}.sec-h p{margin:0;color:var(--ink2)}
.sec-h h2::after{content:"";display:block;width:70px;height:6px;border-radius:6px;background:var(--sage);margin-top:10px}
.lnk{color:var(--sage-d);font-weight:800}
.groups{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
@media(min-width:640px){.groups{grid-template-columns:repeat(3,1fr)}}
@media(min-width:1050px){.groups{grid-template-columns:repeat(6,1fr)}}
.g{display:flex;flex-direction:column;align-items:center;text-align:center;gap:2px;padding:14px 10px 16px;border:2px solid transparent;border-radius:26px;background:var(--paper);cursor:pointer;color:var(--ink);font:inherit;transition:transform .2s,border-color .2s,background .2s;box-shadow:0 12px 26px -20px rgba(80,60,30,.6)}
.g:hover{transform:translateY(-3px)}
.g.is-active{border-color:var(--sage-d);background:var(--sage2)}
.g-ph{width:96px;height:96px;border-radius:50%;overflow:hidden;margin-bottom:8px;box-shadow:0 10px 20px -10px rgba(0,0,0,.4)}
.g-ph img{width:100%;height:100%;object-fit:cover}
.g b{font:700 15px 'Comfortaa',sans-serif}.g small{color:var(--ink2);font-size:12.5px}.g em{font-style:normal;font-weight:800;color:var(--or);font-size:14px}
.panels{margin-top:16px}
.panel{display:none;background:var(--paper);border-radius:30px;padding:20px 16px;box-shadow:0 20px 40px -30px rgba(80,60,30,.6)}
.panel.is-open{display:block;animation:fade .35s ease}
@keyframes fade{from{opacity:0;transform:translateY(10px)}}
.panel-h{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 14px;margin-bottom:14px}.panel-h h3{font-size:24px;margin:0}.panel-h p{margin:0;color:var(--ink2);font-size:14px}
.items{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
@media(min-width:700px){.items{grid-template-columns:repeat(3,1fr)}}@media(min-width:1050px){.items{grid-template-columns:repeat(4,1fr)}}
.it{display:flex;flex-direction:column;align-items:center;text-align:center;background:var(--bg);border-radius:24px;padding:14px 12px;position:relative}
.it-ph{width:min(130px,100%);aspect-ratio:1;border-radius:50%;overflow:hidden;margin-bottom:10px;box-shadow:0 12px 22px -12px rgba(0,0,0,.45)}
.it-ph img{width:100%;height:100%;object-fit:cover}.it-ph .emo{font-size:46px}
.it h4{margin:0 0 3px;font-size:14.5px;line-height:1.3}.it p{margin:0 0 6px;color:var(--ink2);font-size:12.5px;line-height:1.35}
.it .pr{margin-top:auto;font-weight:800;color:var(--or);font-size:17px;margin-bottom:8px}.it .act{width:100%}
.tag{position:absolute;top:10px;left:10px;font-size:10.5px;font-weight:800;padding:4px 9px;border-radius:999px;background:var(--paper);color:var(--sage-d)}
.t-hit{background:var(--or);color:#fff}
.why{background:var(--sage);border-radius:36px;padding:28px 20px;display:grid;gap:20px}
@media(min-width:900px){.why{grid-template-columns:240px 1fr;align-items:center;padding:36px}}
.why h2{font-size:clamp(24px,5vw,32px);margin:0}
.feats{display:grid;grid-template-columns:repeat(2,1fr);gap:18px 14px}@media(min-width:900px){.feats{grid-template-columns:repeat(4,1fr)}}
.f{text-align:center}.f-i{width:62px;height:62px;border-radius:50%;background:var(--sage2);display:grid;place-items:center;margin:0 auto 8px;color:var(--ink)}
.f b{display:block;font-size:14.5px}.f p{margin:4px 0 0;font-size:13px;color:#4F5447}
.revs{display:grid;gap:14px}@media(min-width:800px){.revs{grid-template-columns:repeat(3,1fr)}}
.rv{background:var(--paper);border-radius:26px;padding:20px;position:relative}
.rv::before{content:"“";position:absolute;right:18px;top:-2px;font:700 70px 'Comfortaa';color:var(--sage)}
.rv .st{color:var(--or);letter-spacing:2px}.rv p{margin:8px 0 12px;font-size:15px}.rv b{font-size:14px}.rv small{color:var(--ink2)}
.cont{display:grid;gap:18px;background:var(--sage2);border-radius:36px;padding:22px}
@media(min-width:900px){.cont{grid-template-columns:1fr 1.2fr;padding:30px}}
.cont h2{font-size:clamp(24px,5vw,34px)}.cont p{color:var(--ink2);margin-top:0}
.info{list-style:none;padding:0;margin:0 0 14px;display:grid;gap:10px}.info li{display:flex;gap:10px;align-items:center;font-weight:700}.info svg{color:var(--sage-d);flex:none}
.closed{color:#B3261E}
.hours{list-style:none;padding:0;margin:0 0 18px;display:grid;grid-template-columns:repeat(2,1fr);gap:4px 18px;font-size:14px}
.hours li{display:flex;justify-content:space-between;border-bottom:1px dashed #C6CDB8;padding:4px 0}.hours li.today{color:var(--or);font-weight:800}
.map{border-radius:26px;overflow:hidden;min-height:300px;background:var(--sage)}.map iframe{width:100%;height:100%;min-height:300px;border:0;display:block}
.ft{padding:26px 0 96px;color:var(--ink2);font-size:14px}@media(min-width:960px){.ft{padding-bottom:30px}}
.ft-in{display:flex;flex-wrap:wrap;gap:8px 20px;align-items:center;border-top:1px solid var(--line);padding-top:20px}.ft-logo{font:700 20px 'Comfortaa';color:var(--ink)}
'''
    tpl = '{item:p=>`<article class="it">' + TAG_JS + '<div class="it-ph">${UI.thumb(p)}</div><h4>${UI.esc(p.name)}</h4>${p.desc?`<p>${UI.esc(p.desc)}</p>`:""}<div class="pr">${UI.fmt(p.price)}</div>${UI.slot(p.id)}</article>`,' \
          'review:r=>`<article class="rv reveal in"><div class="st">★★★★★</div><p>${UI.esc(r.text)}</p><b>${UI.esc(r.name)}</b> <small>· ${r.date}, Яндекс Карты</small></article>`}'
    return dict(file='1-shalfey.html', v='d1', title='Своё бистро — Шалfей'.replace('f','ф'),
                fonts='family=Comfortaa:wght@500;700&family=Nunito:wght@400;600;700;800', css=css, body=body, tpl=tpl)
D.append(d1)

# =====================================================================
# 2. РВАНАЯ БУМАГА — по референсу «Sweet Moments»: мокко, пастель, антиква
# =====================================================================
def torn(seed, h=16, step=2.5):
    random.seed(seed); pts = []
    x = 0.0
    while x <= 100.001:
        pts.append(f'{x:.1f}% calc(100% - {random.uniform(0, h):.0f}px)'); x += step
    return 'polygon(0 0,100% 0,' + ','.join(reversed(pts)) + ')'
def torn_top(seed, h=16, step=2.5):
    random.seed(seed); pts = []
    x = 0.0
    while x <= 100.001:
        pts.append(f'{x:.1f}% {random.uniform(0, h):.0f}px'); x += step
    return 'polygon(' + ','.join(pts) + ',100% 100%,0 100%)'

def d2():
    pastel = ['#F1CFCB', '#F4DCC7', '#DCC8D9', '#D7DEC9', '#F3E2B8', '#E8CFC0']
    cards = ''.join(f'''<button class="pc reveal" style="--c:{pastel[i]}" data-open="sh-{g["id"]}">
      <span class="pc-t">{g["name"]}</span><span class="pc-ph"><img data-photo="{g["cover"]}" alt=""></span>
      <span class="pc-b"><small data-gcount="{g["id"]}"></small><em>Открыть ↗</em></span></button>''' for i, g in enumerate(GROUPS))
    sheets = ''.join(f'''<div class="modal sheet" id="sh-{g["id"]}" role="dialog" aria-modal="true" aria-label="{g["name"]}">
      <div class="sheet-in" style="--c:{pastel[i]}"><div class="sheet-h"><div><h3>{g["name"]}</h3><p>{g["note"]}</p></div><button class="sx" data-close aria-label="Закрыть">{CLOSE}</button></div>
      <div class="list" data-group-items="{g["id"]}"></div></div></div>''' for i, g in enumerate(GROUPS))
    body = f'''
<header class="hd"><div class="wrap hd-in">
  <a class="logo" href="#top"><img data-photo="logo" alt="Логотип «Своё бистро»"><span>Своё бистро</span></a>
  <nav class="nav" aria-label="Разделы"><a href="#menu">Меню</a><a href="#about">О нас</a><a href="#contacts">Контакты</a></nav>
  <button class="ib" data-open-cart aria-label="Корзина">{BAG}<span class="cnt" data-cart-count>0</span></button>
</div></header>
<main id="top">
<section class="hero"><div class="wrap hero-in">
  <div class="hero-t reveal"><p class="kick">пекарня · бистро · Новоселье</p>
    <h1>Тёплые моменты начинаются здесь.</h1>
    <p>Свежая выпечка, завтраки и любимые блюда — в зале на бульваре Белых Ночей или у вас дома.</p>
    <a href="#menu" class="btn">Смотреть меню</a></div>
  <div class="hero-i reveal"><div class="plate"><img data-photo="cinnabon" alt="Синнабоны с вишней на витрине"></div></div>
</div></section>
<section class="strip wrap">
  <div class="s"><span class="s-i">{CLOCK}</span><div><b data-status></b><small>сегодня</small></div></div>
  <div class="s"><span class="s-i">{PIN}</span><div><b data-cfg="address"></b><small>самовывоз без очереди</small></div></div>
  <div class="s"><span class="s-i">★</span><div><b><span data-cfg="rating"></span> на Яндекс Картах</b><small data-cfg="ratingCount"></small></div></div>
</section>
<section id="menu" class="wrap sec"><h2 class="ttl reveal">Наше меню</h2><p class="sub reveal">Выберите группу — откроется список с ценами</p>
  <div class="pcs">{cards}</div></section>
{sheets}
<section id="about" class="wrap sec about">
  <div class="cup reveal"><img data-photo="coffee" alt="Капучино и выпечка"></div>
  <div class="reveal"><h2 class="ttl">Своё бистро</h2>
    <p>Бистро с собственной пекарней в самом сердце Новоселья. С утра — круассаны и синнабоны, днём и вечером — паста, горячее и стейки. Простые блюда в неожиданном исполнении.</p>
    <div class="qs" data-reviews="2"></div>
    <a class="btn ghost" data-reviews-link>Все отзывы на Яндекс Картах</a></div>
</section>
</main>
<footer class="ft" id="contacts"><div class="wrap ft-in">
  <div><div class="ft-logo">Своё бистро</div><p>Выпечка · Завтраки · Любимые блюда</p><a class="btn light" data-route>Построить маршрут</a></div>
  <div><h4>Адрес</h4><p data-cfg="address"></p><h4>Телефон</h4><p><a data-tel data-cfg="phone"></a></p></div>
  <div><h4>Часы работы</h4><ul class="hours" data-hours="short"></ul></div>
  <small class="cp">© <span data-year></span> · <a data-vk>ВКонтакте</a> · <a data-privacy>Политика конфиденциальности</a> · демо-концепт</small>
</div></footer>'''
    css = r'''
:root{--mo:#A27E7A;--mo-d:#6E4A48;--cr:#F6EEE4;--paper:#FFFAF4;--ink:#4A2E2E;--ink2:#7D6461;--line:#E8DACD;
--ui-bg:var(--cr);--ui-paper:var(--paper);--ui-ink:var(--ink);--ui-ink2:var(--ink2);--ui-line:var(--line);--ui-acc:var(--mo-d);--ui-acc-ink:#fff;--ui-soft:#F1E3DB;--ui-r:18px;--ui-btn-r:999px;--ui-bd:0;--ui-font:'Raleway',sans-serif;--ui-font-h:600 24px 'Playfair Display',serif;--ui-emo-bg:#F3E6DC}
body{background:var(--cr);color:var(--ink);font:16px/1.6 'Raleway',sans-serif}
h1,h2,h3,h4{font-family:'Playfair Display',serif;font-weight:600;line-height:1.1;margin:0 0 .4em}
.btn{display:inline-flex;align-items:center;min-height:50px;padding:0 28px;border-radius:999px;background:var(--mo-d);color:#fff;text-decoration:none;font-weight:700;letter-spacing:.03em;border:2px solid var(--mo-d)}
.btn:hover{background:#5A3B39}.btn.ghost{background:transparent;color:var(--mo-d)}.btn.ghost:hover{background:var(--mo-d);color:#fff}
.btn.light{background:var(--cr);color:var(--mo-d);border-color:var(--cr)}
.hd{position:sticky;top:0;z-index:50;background:rgba(246,238,228,.94);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.hd-in{display:flex;align-items:center;gap:14px;height:64px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;margin-right:auto}.logo img{width:40px;height:40px;border-radius:10px}.logo span{font:600 22px 'Playfair Display',serif}
.nav{display:none;gap:22px}.nav a{text-decoration:none;font-weight:600}.nav a:hover{color:var(--mo)}@media(min-width:800px){.nav{display:flex}}
.ib{position:relative;width:44px;height:44px;border-radius:50%;border:1.5px solid var(--ink);background:transparent;color:var(--ink);display:grid;place-items:center;cursor:pointer}
.hero{background:var(--mo);color:#FFF6EE;padding:40px 0 70px;clip-path:TORN_B;position:relative}
.hero::before{content:"";position:absolute;inset:0;opacity:.18;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");mix-blend-mode:overlay;pointer-events:none}
.hero-in{display:grid;gap:30px;align-items:center;position:relative}
@media(min-width:860px){.hero-in{grid-template-columns:1.1fr 1fr}}
.kick{text-transform:uppercase;letter-spacing:.2em;font-size:12px;font-weight:700;opacity:.85;margin:0 0 12px}
.hero h1{font-size:clamp(38px,8.5vw,68px);font-weight:500}
.hero-t>p:not(.kick){max-width:440px;opacity:.92;margin:0 0 26px}
.hero .btn{background:transparent;border-color:#FFF6EE;color:#FFF6EE}.hero .btn:hover{background:#FFF6EE;color:var(--mo-d)}
.plate{width:min(400px,86%);aspect-ratio:1;margin:0 auto;border-radius:50%;padding:16px;background:#FFF6EE;box-shadow:0 30px 50px -20px rgba(60,30,30,.6),inset 0 -10px 20px rgba(0,0,0,.08)}
.plate img{width:100%;height:100%;border-radius:50%;object-fit:cover}
.strip{display:grid;gap:14px;padding-top:6px;padding-bottom:10px}
@media(min-width:760px){.strip{grid-template-columns:repeat(3,1fr)}}
.s{display:flex;gap:12px;align-items:center}.s-i{width:48px;height:48px;border-radius:50%;background:#F1DCD6;display:grid;place-items:center;color:var(--mo-d);flex:none;font-size:20px}
.s b{display:block;font-family:'Playfair Display',serif;font-size:16px}.s small{color:var(--ink2);font-size:13px}.closed{color:#B3261E}
.sec{padding:44px 16px}
.ttl{font-size:clamp(30px,6.5vw,46px);text-align:center}.sub{text-align:center;color:var(--ink2);margin:-4px 0 24px}
.pcs{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}@media(min-width:860px){.pcs{grid-template-columns:repeat(3,1fr);gap:22px}}
.pc{display:flex;flex-direction:column;align-items:center;gap:10px;background:var(--c);border:0;border-radius:24px;padding:18px 12px 14px;cursor:pointer;color:var(--ink);font:inherit;transition:transform .25s,box-shadow .25s}
.pc:hover{transform:translateY(-5px) rotate(-.6deg);box-shadow:0 22px 34px -20px rgba(80,40,40,.55)}
.pc-t{font:600 clamp(18px,4.2vw,26px)/1.1 'Playfair Display',serif;text-align:center;min-height:2.2em;display:flex;align-items:center}
.pc-ph{width:82%;aspect-ratio:1;border-radius:50%;overflow:hidden;box-shadow:0 16px 26px -14px rgba(60,30,30,.55)}.pc-ph img{width:100%;height:100%;object-fit:cover}
.pc-b{display:flex;justify-content:space-between;align-items:center;width:100%;font-size:12.5px;color:var(--ink2);gap:6px}.pc-b em{font-style:italic;font-family:'Playfair Display';font-size:15px;color:var(--mo-d)}
.sheet{position:fixed;inset:0;z-index:150;background:rgba(74,46,46,.45);display:flex;align-items:flex-end;justify-content:center;opacity:0;pointer-events:none;transition:opacity .25s}
.sheet.is-open{opacity:1;pointer-events:auto}
.sheet-in{width:min(760px,100%);max-height:88vh;max-height:88dvh;overflow:auto;background:var(--cr);border-radius:28px 28px 0 0;padding:0 16px 22px;transform:translateY(40px);transition:transform .3s cubic-bezier(.2,.8,.2,1);border-top:12px solid var(--c)}
.sheet.is-open .sheet-in{transform:none}
@media(min-width:760px){.sheet{align-items:center}.sheet-in{border-radius:28px;max-height:84vh}}
.sheet-h{position:sticky;top:0;background:var(--cr);display:flex;justify-content:space-between;gap:10px;padding:16px 0 12px;z-index:2}
.sheet-h h3{font-size:30px;margin:0}.sheet-h p{margin:0;color:var(--ink2);font-size:14px}
.sx{width:44px;height:44px;border-radius:50%;border:1.5px solid var(--ink);background:transparent;color:var(--ink);display:grid;place-items:center;cursor:pointer;flex:none}
.list{display:grid;gap:10px}@media(min-width:760px){.list{grid-template-columns:1fr 1fr}}
.li{display:grid;grid-template-columns:70px 1fr;gap:12px;align-items:center;background:var(--paper);border-radius:18px;padding:10px}
.li-ph{width:70px;height:70px;border-radius:50%;overflow:hidden}.li-ph img{width:100%;height:100%;object-fit:cover}.li-ph .emo{font-size:30px}
.li h4{font-size:17px;margin:0 0 2px}.li p{margin:0;font-size:12.5px;color:var(--ink2);line-height:1.35}
.li-b{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-top:6px}.li-b .pr{font-weight:800}
.li .act{width:132px}.li .add,.li .stp{min-height:38px;font-size:13px}.li .stp button{width:30px;height:30px;font-size:16px}
.tag{display:inline-block;font:italic 13px 'Playfair Display';color:var(--mo);margin-left:6px}
.about{display:grid;gap:26px;align-items:center}@media(min-width:860px){.about{grid-template-columns:.9fr 1.1fr}}
.about .ttl{text-align:left}
.cup{width:min(380px,90%);aspect-ratio:1;margin:0 auto;border-radius:50%;overflow:hidden;border:14px solid #EBD8CF;box-shadow:0 26px 40px -24px rgba(60,30,30,.5)}.cup img{width:100%;height:100%;object-fit:cover}
.qs{display:grid;gap:12px;margin:18px 0 22px}
.q{background:#F1E3DB;border-radius:18px;padding:14px 16px}.q p{margin:0 0 6px;font:italic 17px/1.4 'Playfair Display',serif}.q small{color:var(--ink2)}
.ft{background:var(--mo-d);color:#F6EAE2;padding:46px 0 100px;clip-path:TORN_T;margin-top:20px}
@media(min-width:960px){.ft{padding-bottom:36px}}
.ft-in{display:grid;gap:22px}@media(min-width:800px){.ft-in{grid-template-columns:1.3fr 1fr 1fr}}
.ft-logo{font:500 34px 'Playfair Display',serif}.ft h4{font-size:15px;margin:0 0 4px;opacity:.8}.ft p{margin:0 0 12px}.ft a{color:#fff}
.hours{list-style:none;padding:0;margin:0;font-size:14px}.hours li{display:flex;justify-content:space-between;gap:12px;padding:3px 0;border-bottom:1px dashed rgba(255,255,255,.2)}.hours li.today{font-weight:800}
.cp{grid-column:1/-1;opacity:.75;font-size:12.5px}
'''.replace('TORN_B', torn(7)).replace('TORN_T', torn_top(11))
    tpl = '{item:p=>`<article class="li"><div class="li-ph">${UI.thumb(p)}</div><div><h4>${UI.esc(p.name)}' + TAG_JS.replace('class=\\"tag t-${p.tag}\\"','class=\\"tag\\"') + '</h4>${p.desc?`<p>${UI.esc(p.desc)}</p>`:""}<div class="li-b"><span class="pr">${UI.fmt(p.price)}</span>${UI.slot(p.id)}</div></div></article>`,' \
          'review:r=>`<div class="q"><p>«${UI.esc(r.text)}»</p><small>— ${UI.esc(r.name)}, Яндекс Карты</small></div>`}'
    return dict(file='2-rvanaya-bumaga.html', v='d2', title='Своё бистро — Рваная бумага',
                fonts='family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Raleway:wght@400;500;600;700;800', css=css, body=body, tpl=tpl)
D.append(d2)

# =====================================================================
# 3. ЛИСТВА — по референсу «Листва»: фото на весь экран, антиква с точкой, стеклянные панели
# =====================================================================
def d3():
    tabs = ''.join(f'<button class="tab" data-open="t-{g["id"]}" data-scope="tabs" data-keep>{g["name"]}</button>' for g in GROUPS)
    panels = ''.join(f'''<div class="tp{' is-open' if i == 0 else ''}" id="t-{g["id"]}" role="region" aria-label="{g["name"]}"><p class="tp-n">{g["note"]}</p><div class="tl" data-group-items="{g["id"]}"></div></div>''' for i, g in enumerate(GROUPS))
    body = f'''
<header class="hd"><div class="wrap hd-in">
  <a class="logo" href="#top"><img data-photo="logo" alt="Логотип «Своё бистро»"><span>Своё бистро<small>пекарня и бистро</small></span></a>
  <nav class="nav" aria-label="Разделы"><a href="#menu">Меню</a><a href="#more">О нас</a><a href="#visit">Контакты</a></nav>
  <button class="ib" data-open-cart aria-label="Корзина">{BAG}<span class="cnt" data-cart-count>0</span></button>
</div></header>
<main id="top">
<section class="hero" data-bg="hall">
  <div class="wrap hero-t reveal">
    <h1>Своё место в&nbsp;Новоселье<i>.</i></h1>
    <p>Свежая выпечка, завтраки и любимые блюда. Приходите в гости — или мы привезём всё к вам.</p>
    <div class="cta"><a href="#menu" class="btn">Открыть меню {ARROW}</a><a class="btn ghost" data-route>Маршрут</a></div>
  </div>
</section>
<section class="wrap visit" id="visit">
  <div class="glass reveal">
    <div class="map"><iframe data-map title="Своё бистро на карте" loading="lazy"></iframe></div>
    <ul class="info">
      <li><span class="ic">{PIN}</span><div><small>Адрес</small><b data-cfg="address"></b></div></li>
      <li><span class="ic">{CLOCK}</span><div><small>Сегодня</small><b data-status></b></div></li>
      <li><span class="ic">{PHONE}</span><div><small>Телефон</small><b><a data-tel data-cfg="phone"></a></b></div></li>
      <li class="r"><a class="btn wide" data-route>Построить маршрут {ARROW}</a></li>
    </ul>
  </div>
</section>
<section id="menu" class="wrap sec">
  <h2 class="ttl reveal">Меню<i>.</i></h2>
  <div class="tabs" role="tablist" aria-label="Группы меню">{tabs}</div>
  <div class="glass tps">{panels}</div>
</section>
<section id="more" class="wrap sec trio">
  <div class="glass box reveal"><small class="kick">Пекарня и бистро</small><h3>Больше чем просто кофе<i>.</i></h3>
    <p>Своя пекарня, хлеб на закваске, завтраки с 8:00 и горячие блюда до вечера. Простые блюда в неожиданном исполнении.</p>
    <ul class="hours" data-hours="short"></ul></div>
  <div class="photo reveal"><img data-photo="vitrine" alt="Витрина с данишами" loading="lazy"><span>своя выпечка<br>каждое утро</span></div>
  <div class="glass box reveal"><h3>Гости о нас<i>.</i></h3><div class="qs" data-reviews="2"></div><a class="lnk" data-reviews-link>Все отзывы ({''}<span data-cfg="rating"></span> ★) →</a></div>
</section>
</main>
<footer class="ft"><div class="wrap ft-in"><span class="ft-l">Своё бистро</span><span data-cfg="address"></span><a data-tel data-cfg="phone"></a><a data-vk>ВКонтакте</a><a data-privacy>Политика конфиденциальности</a><small>© <span data-year></span> · демо-концепт</small></div></footer>'''
    css = r'''
:root{--cr:#F6ECDF;--paper:#FFFBF5;--ink:#1F2A20;--ink2:#5D5A50;--or:#E2582F;--or-d:#C9471F;--line:#E6D7C4;--glass:rgba(255,250,243,.8);
--ui-bg:var(--cr);--ui-paper:var(--paper);--ui-ink:var(--ink);--ui-ink2:var(--ink2);--ui-line:var(--line);--ui-acc:var(--or);--ui-acc-ink:#fff;--ui-soft:#EFE2D1;--ui-r:18px;--ui-btn-r:999px;--ui-bd:0;--ui-font:'Manrope',sans-serif;--ui-font-h:400 26px 'Prata',serif;--ui-emo-bg:#F1E5D5}
body{background:var(--cr) radial-gradient(1200px 600px at 100% 0,#F9E3C8,transparent 60%);color:var(--ink);font:16px/1.6 'Manrope',sans-serif}
h1,h2,h3{font-family:'Prata',serif;font-weight:400;line-height:1.05;margin:0 0 .4em;letter-spacing:-.01em}
h1 i,h2 i,h3 i{font-style:normal;color:var(--or)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:0 26px;border-radius:999px;background:var(--or);color:#fff;font-weight:700;text-decoration:none;transition:background .15s,transform .15s}
.btn:hover{background:var(--or-d);transform:translateY(-1px)}.btn.ghost{background:rgba(255,251,245,.6);color:var(--ink);border:1.5px solid var(--ink)}.btn.wide{width:100%}
.hd{position:absolute;left:0;right:0;z-index:50}
.hd-in{display:flex;align-items:center;gap:14px;height:76px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;margin-right:auto}.logo img{width:46px;height:46px;border-radius:50%}
.logo span{font:400 22px 'Prata',serif;line-height:1}.logo small{display:block;font:600 10px 'Manrope';letter-spacing:.2em;text-transform:uppercase;color:var(--ink2);margin-top:4px}
.nav{display:none;gap:24px;background:var(--glass);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);padding:10px 20px;border-radius:999px}.nav a{text-decoration:none;font-weight:600}
@media(min-width:800px){.nav{display:flex}}
.ib{position:relative;width:48px;height:48px;border-radius:50%;border:0;background:var(--or);color:#fff;display:grid;place-items:center;cursor:pointer}
.hero{min-height:min(88vh,760px);background-size:cover;background-position:center 40%;position:relative;display:flex;align-items:flex-end;padding:110px 0 120px}
.hero::before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(246,236,223,.97) 0%,rgba(246,236,223,.85) 38%,rgba(246,236,223,.15) 75%),linear-gradient(0deg,var(--cr) 0%,transparent 30%)}
@media(max-width:760px){.hero::before{background:linear-gradient(0deg,var(--cr) 8%,rgba(246,236,223,.88) 48%,rgba(246,236,223,.35) 100%)}}
.hero-t{position:relative;width:100%}
.hero h1{font-size:clamp(44px,10vw,96px);max-width:680px}
.hero p{font-size:clamp(16px,2.6vw,20px);color:var(--ink2);max-width:440px;margin:0 0 26px}
.cta{display:flex;flex-wrap:wrap;gap:10px}
.visit{margin-top:-80px;position:relative;z-index:2}
.glass{background:var(--glass);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,.7);border-radius:28px;box-shadow:0 30px 60px -40px rgba(60,40,20,.5)}
.visit .glass{display:grid;gap:16px;padding:14px}@media(min-width:860px){.visit .glass{grid-template-columns:1.1fr 1fr;padding:16px}}
.map{border-radius:20px;overflow:hidden;min-height:260px;background:#E9DDCB}.map iframe{width:100%;height:100%;min-height:260px;border:0;display:block}
.info{list-style:none;padding:6px 6px 4px;margin:0;display:grid;align-content:center}
.info li{display:flex;gap:14px;align-items:center;padding:12px 0;border-bottom:1px solid var(--line)}.info li.r{border:0;padding-top:16px}
.ic{width:46px;height:46px;border-radius:50%;background:#F1E4D2;display:grid;place-items:center;flex:none}
.info small{display:block;color:var(--ink2);font-size:13px}.info b{font-weight:600;font-size:16px}.info a{text-decoration:none}.closed{color:#B3261E}
.sec{padding:50px 16px}
.ttl{font-size:clamp(44px,9vw,76px)}
.tabs{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 16px}
.tab{min-height:44px;padding:0 18px;border-radius:999px;border:1.5px solid var(--ink);background:transparent;color:var(--ink);font:600 15px 'Manrope';cursor:pointer;transition:background .15s,color .15s}
.tab:hover{background:rgba(255,255,255,.6)}.tab.is-active{background:var(--ink);color:var(--cr)}
.tps{padding:18px 14px}
.tp{display:none}.tp.is-open{display:block;animation:fade .35s}@keyframes fade{from{opacity:0}}
.tp-n{margin:0 0 12px;color:var(--ink2);font-size:14px}
.tl{display:grid;gap:10px}@media(min-width:800px){.tl{grid-template-columns:1fr 1fr;gap:12px}}
.row{display:grid;grid-template-columns:84px 1fr;gap:14px;align-items:center;padding:10px;border-radius:20px;background:rgba(255,255,255,.75)}
.row-ph{width:84px;height:84px;border-radius:16px;overflow:hidden}.row-ph img{width:100%;height:100%;object-fit:cover}.row-ph .emo{font-size:34px}
.row h4{font:400 18px/1.15 'Prata',serif;margin:0 0 3px}.row p{margin:0;color:var(--ink2);font-size:13px;line-height:1.35}
.row-b{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-top:6px}.row-b .pr{font-weight:800}
.row .act{width:130px}.row .add,.row .stp{min-height:38px;font-size:13px}.row .stp button{width:30px;height:30px;font-size:16px}
.tag{font-size:10.5px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--or);margin-left:6px;vertical-align:2px}
.trio{display:grid;gap:16px}@media(min-width:900px){.trio{grid-template-columns:1fr 1fr 1fr}}
.box{padding:22px}.box h3{font-size:30px}.box p{color:var(--ink2);margin-top:0}
.kick{display:block;color:var(--ink2);font-size:13px;margin-bottom:8px}
.hours{list-style:none;padding:0;margin:12px 0 0;display:grid;grid-template-columns:1fr 1fr;gap:2px 16px;font-size:14px}.hours li{display:flex;justify-content:space-between}.hours li.today{color:var(--or);font-weight:800}
.photo{position:relative;border-radius:28px;overflow:hidden;min-height:300px}.photo img{width:100%;height:100%;object-fit:cover;position:absolute;inset:0}
.photo span{position:absolute;left:16px;bottom:16px;background:var(--glass);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border-radius:16px;padding:10px 14px;font:400 18px/1.2 'Prata',serif}
.qs{display:grid;gap:10px;margin-bottom:12px}.q p{margin:0 0 4px;font-size:14.5px}.q small{color:var(--ink2)}
.lnk{color:var(--or);font-weight:700}
.ft{padding:24px 0 96px;font-size:14px;color:var(--ink2)}@media(min-width:960px){.ft{padding-bottom:28px}}
.ft-in{display:flex;flex-wrap:wrap;gap:8px 22px;align-items:center;border-top:1px solid var(--line);padding-top:18px}.ft-l{font:400 22px 'Prata';color:var(--ink)}
'''
    tpl = '{item:p=>`<article class="row"><div class="row-ph">${UI.thumb(p)}</div><div><h4>${UI.esc(p.name)}' + TAG_JS + '</h4>${p.desc?`<p>${UI.esc(p.desc)}</p>`:""}<div class="row-b"><span class="pr">${UI.fmt(p.price)}</span>${UI.slot(p.id)}</div></div></article>`,' \
          'review:r=>`<div class="q"><p>«${UI.esc(r.text)}»</p><small>${UI.esc(r.name)} · ${r.date}</small></div>`}'
    return dict(file='3-listva.html', v='d3', title='Своё бистро — Листва',
                fonts='family=Prata&family=Manrope:wght@400;500;600;700;800', css=css, body=body, tpl=tpl)
D.append(d3)

# =====================================================================
# 4. ЯРКИЙ ПОП — аккордеон из «стикеров»
# =====================================================================
def d4():
    acc = ''.join(f'''<div class="ac reveal" id="a-{g["id"]}">
      <button class="ac-h" data-open="a-{g["id"]}" data-scope="acc" data-scroll="80"><span class="ac-ph"><img data-photo="{g["cover"]}" alt=""></span>
        <span class="ac-t"><b>{g["name"].lower()}</b><small><span data-gcount="{g["id"]}"></span> · <span data-gfrom="{g["id"]}"></span></small></span><span class="ac-x" aria-hidden="true">+</span></button>
      <div class="ac-b"><div class="ac-in"><div class="cards" data-group-items="{g["id"]}"></div></div></div></div>''' for g in GROUPS)
    body = f'''
<header class="hd"><div class="wrap hd-in">
  <a class="logo" href="#top"><img data-photo="logo" alt="Логотип «Своё бистро»"><span>своё бистро</span></a>
  <nav class="nav" aria-label="Разделы"><a href="#menu">меню</a><a href="#reviews">отзывы</a><a href="#contacts">контакты</a></nav>
  <a class="ib" data-tel aria-label="Позвонить">{PHONE}</a>
  <button class="ib cart" data-open-cart aria-label="Корзина">{BAG}<span class="cnt" data-cart-count>0</span></button>
</div></header>
<main id="top">
<section class="hero"><div class="wrap hero-in">
  <div class="reveal"><span class="chip">★ <span data-cfg="rating"></span> · <span data-cfg="ratingCount"></span></span>
    <h1>хрустит, тает, <mark>едет к тебе</mark></h1>
    <p>Бистро с пекарней в Новоселье. Выпечка, завтраки и любимые блюда — доставка и самовывоз без очереди.</p>
    <a href="#menu" class="btn">выбрать вкусное →</a></div>
  <div class="stack reveal" aria-hidden="true">
    <div class="sp s1"><img data-photo="croissant" alt=""></div><div class="sp s2"><img data-photo="burger" alt=""></div><div class="sp s3"><img data-photo="cinnabon" alt=""></div>
    <span class="st st1">хит<br>гостей</span><span class="st st2">своя<br>выпечка</span>
  </div>
</div></section>
<div class="tick" aria-hidden="true"><div>круассаны ✺ синнабоны ✺ крок мадам ✺ смэш-бургер ✺ хлеб на закваске ✺ тартар ✺ кофе ✺ круассаны ✺ синнабоны ✺ крок мадам ✺ смэш-бургер ✺ хлеб на закваске ✺ тартар ✺ кофе ✺</div></div>
<section id="menu" class="wrap sec"><h2 class="ttl reveal">меню</h2><p class="sub">Жми на группу — она раскроется</p><div class="accs">{acc}</div></section>
<section id="reviews" class="rev"><div class="wrap sec"><h2 class="ttl light reveal">нас хвалят</h2><div class="revs" data-reviews="3"></div><a class="lnk" data-reviews-link>все отзывы на Яндекс Картах →</a></div></section>
<section id="contacts" class="wrap sec">
  <div class="cont reveal"><div><h2 class="ttl">заходи</h2>
    <p class="big" data-cfg="address"></p><p><b data-status></b></p><p><a data-tel data-cfg="phone"></a></p>
    <div class="btns"><a class="btn" data-route>маршрут →</a><a class="btn alt" data-vk>ВКонтакте</a></div></div>
    <ul class="hours" data-hours></ul></div>
</section>
</main>
<footer class="ft"><div class="wrap">своё бистро · © <span data-year></span> · <a data-privacy>политика конфиденциальности</a> · демо-концепт</div></footer>'''
    css = r'''
:root{--t:#D85F44;--l:#C9EA6B;--k:#1B1512;--c:#FFF1E4;
--ui-bg:var(--c);--ui-paper:#fff;--ui-ink:var(--k);--ui-ink2:#5E4A40;--ui-line:var(--k);--ui-acc:var(--k);--ui-acc-ink:var(--l);--ui-soft:var(--l);--ui-r:18px;--ui-btn-r:999px;--ui-bd:2.5px solid var(--k);--ui-font:'Manrope',sans-serif;--ui-font-h:800 22px 'Unbounded',sans-serif;--ui-emo-bg:var(--c);--ui-stp-bg:var(--l);--ui-stp-ink:var(--k);--ui-cnt-bg:var(--l);--ui-cnt-ink:var(--k)}
body{background:var(--c);color:var(--k);font:16px/1.55 'Manrope',sans-serif}
h1,h2,h3{font-family:'Unbounded',sans-serif;font-weight:800;line-height:1;margin:0 0 .4em;letter-spacing:-.02em}
.btn{display:inline-flex;align-items:center;min-height:52px;padding:0 24px;border:2.5px solid var(--k);border-radius:999px;background:var(--l);color:var(--k);font:800 15px 'Manrope';text-decoration:none;box-shadow:4px 4px 0 var(--k);transition:transform .12s,box-shadow .12s}
.btn:hover{transform:translate(-2px,-2px);box-shadow:6px 6px 0 var(--k)}.btn.alt{background:#fff}
.hd{position:sticky;top:0;z-index:50;background:var(--t);border-bottom:2.5px solid var(--k)}
.hd-in{display:flex;align-items:center;gap:8px;height:66px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;margin-right:auto}.logo img{width:42px;height:42px;border-radius:10px;border:2px solid var(--k)}.logo span{font:800 16px 'Unbounded';color:var(--c)}
.nav{display:none;gap:4px;margin-right:6px}.nav a{color:var(--c);text-decoration:none;font-weight:800;padding:8px 12px;border-radius:999px}.nav a:hover{background:rgba(0,0,0,.15)}@media(min-width:860px){.nav{display:flex}}
.ib{position:relative;width:46px;height:46px;border-radius:50%;border:2.5px solid var(--k);background:var(--c);color:var(--k);display:grid;place-items:center;cursor:pointer;text-decoration:none}.ib.cart{background:var(--k);color:var(--l)}
.hero{background:var(--t);padding:26px 0 40px;border-bottom:2.5px solid var(--k)}
.hero-in{display:grid;gap:30px;align-items:center}@media(min-width:880px){.hero-in{grid-template-columns:1.1fr 1fr}}
.chip{display:inline-block;background:var(--k);color:var(--c);border-radius:999px;padding:7px 14px;font-weight:700;font-size:13.5px;margin-bottom:14px}
.hero h1{font-size:clamp(36px,9.5vw,70px);color:var(--c)}
mark{background:var(--l);color:var(--k);padding:0 .12em;border-radius:.16em;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.hero p{color:#FFE7D6;max-width:470px;margin:0 0 22px}
.stack{position:relative;height:340px;max-width:440px;width:100%;justify-self:center}
.sp{position:absolute;width:62%;aspect-ratio:1;border:3px solid var(--k);border-radius:26px;overflow:hidden;box-shadow:6px 6px 0 var(--k);background:var(--k)}.sp img{width:100%;height:100%;object-fit:cover}
.s1{left:0;top:10px;transform:rotate(-7deg)}.s2{right:0;top:0;transform:rotate(5deg);z-index:2}.s3{left:20%;bottom:0;width:52%;transform:rotate(-2deg);z-index:3}
.st{position:absolute;z-index:4;display:grid;place-items:center;text-align:center;width:84px;height:84px;border-radius:50%;border:2.5px solid var(--k);font:800 11px/1.1 'Unbounded';box-shadow:3px 3px 0 var(--k)}
.st1{background:var(--l);right:2%;bottom:24%;transform:rotate(12deg)}.st2{background:var(--c);left:2%;bottom:6%;transform:rotate(-10deg)}
.tick{background:var(--k);color:var(--l);overflow:hidden;white-space:nowrap;padding:11px 0;font:800 14px 'Unbounded'}.tick div{display:inline-block;animation:tk 30s linear infinite}@keyframes tk{to{transform:translateX(-50%)}}
.sec{padding:44px 16px}
.ttl{font-size:clamp(32px,8vw,56px)}.ttl::after{content:"";display:block;width:80px;height:12px;border:2.5px solid var(--k);border-radius:999px;background:var(--l);margin-top:10px}
.ttl.light{color:var(--c)}.sub{font-weight:600;margin:0 0 18px}
.accs{display:grid;gap:14px}
.ac{border:3px solid var(--k);border-radius:24px;background:#fff;box-shadow:5px 5px 0 var(--k);overflow:hidden}
.ac-h{display:flex;align-items:center;gap:14px;width:100%;padding:12px 16px 12px 12px;border:0;background:transparent;cursor:pointer;color:var(--k);text-align:left}
.ac-ph{width:64px;height:64px;border-radius:50%;overflow:hidden;border:2.5px solid var(--k);flex:none}.ac-ph img{width:100%;height:100%;object-fit:cover}
.ac-t{flex:1}.ac-t b{display:block;font:800 clamp(17px,4.5vw,24px) 'Unbounded'}.ac-t small{font-weight:700;color:#5E4A40}
.ac-x{width:44px;height:44px;border-radius:50%;border:2.5px solid var(--k);background:var(--l);display:grid;place-items:center;font:800 26px/1 'Manrope';flex:none;transition:transform .25s}
.ac.is-open .ac-x{transform:rotate(45deg);background:var(--t);color:#fff}
.ac.is-open{background:var(--c)}
.ac-b{display:grid;grid-template-rows:0fr;transition:grid-template-rows .35s ease}.ac.is-open .ac-b{grid-template-rows:1fr}
.ac-in{overflow:hidden}.ac.is-open .ac-in{border-top:2.5px dashed var(--k)}
.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;padding:16px}@media(min-width:700px){.cards{grid-template-columns:repeat(3,1fr)}}@media(min-width:1050px){.cards{grid-template-columns:repeat(4,1fr)}}
.cd{background:#fff;border:2.5px solid var(--k);border-radius:18px;overflow:hidden;display:flex;flex-direction:column;position:relative}
.cd-ph{aspect-ratio:1;border-bottom:2.5px solid var(--k)}.cd-ph img{width:100%;height:100%;object-fit:cover}.cd-ph .emo{font-size:48px;background:var(--t)}
.cd-b{padding:10px 10px 12px;display:flex;flex-direction:column;flex:1}.cd h4{font-size:14px;margin:0 0 4px;line-height:1.25}.cd .pr{font-weight:800;margin-top:auto;margin-bottom:8px}
.tag{position:absolute;top:8px;left:8px;font:800 10px 'Manrope';text-transform:uppercase;padding:5px 9px;border-radius:999px;border:2px solid var(--k);background:var(--l)}.t-hit{background:var(--t);color:#fff}.t-new{background:var(--k);color:var(--l)}
.rev{background:var(--t);border-top:2.5px solid var(--k);border-bottom:2.5px solid var(--k)}
.revs{display:grid;gap:16px;margin-bottom:16px}@media(min-width:800px){.revs{grid-template-columns:repeat(3,1fr)}}
.rv{background:var(--c);border:3px solid var(--k);border-radius:22px;padding:18px;box-shadow:5px 5px 0 var(--k)}.rv:nth-child(2){transform:rotate(1.2deg)}.rv:nth-child(odd){transform:rotate(-1deg)}
.rv .stars{color:var(--t);letter-spacing:2px}.rv p{margin:8px 0 10px}.rv b{display:inline-block;background:var(--l);border:2px solid var(--k);border-radius:999px;padding:2px 10px;font-size:13px}
.lnk{color:var(--c);font-weight:800}
.cont{display:grid;gap:20px;background:var(--k);color:var(--c);border-radius:28px;padding:24px;box-shadow:6px 6px 0 var(--t)}@media(min-width:860px){.cont{grid-template-columns:1.2fr 1fr;padding:34px}}
.cont .ttl{color:var(--l)}.cont .big{font:800 20px/1.3 'Unbounded';margin:0 0 8px}.cont a{color:var(--c)}.cont p{margin:0 0 8px}
.btns{display:flex;flex-wrap:wrap;gap:12px;margin-top:16px}.btns .btn{box-shadow:4px 4px 0 var(--t)}
.closed{color:#FF9C8A}
.hours{list-style:none;padding:0;margin:0;align-self:center}.hours li{display:flex;justify-content:space-between;padding:7px 0;border-bottom:1.5px dashed rgba(255,241,228,.25)}.hours li.today{color:var(--l);font-weight:800}
.ft{padding:20px 0 96px;font-size:13px;font-weight:600}@media(min-width:960px){.ft{padding-bottom:26px}}
'''
    tpl = '{item:p=>`<article class="cd">' + TAG_JS + '<div class="cd-ph">${UI.thumb(p)}</div><div class="cd-b"><h4>${UI.esc(p.name)}</h4><div class="pr">${UI.fmt(p.price)}</div>${UI.slot(p.id)}</div></article>`,' \
          'review:r=>`<article class="rv"><div class="stars">★★★★★</div><p>${UI.esc(r.text)}</p><b>${UI.esc(r.name)}</b></article>`}'
    return dict(file='4-yarkiy-pop.html', v='d4', title='Своё бистро — Яркий поп',
                fonts='family=Unbounded:wght@600;800&family=Manrope:wght@500;600;700;800', css=css, body=body, tpl=tpl, add_label='+ в корзину')
D.append(d4)

# =====================================================================
# 5. ГРИФЕЛЬНАЯ ДОСКА — меню, написанное мелом
# =====================================================================
def d5():
    boards = ''.join(f'''<section class="bd reveal" id="b-{g["id"]}"><h3><span>{g["name"]}</span></h3><p class="bn">{g["note"]}</p>
      <div class="lns" data-group-items="{g["id"]}"></div>
      <button class="more" data-open="b-{g["id"]}"><span class="m1">Показать всё (<span data-gcount="{g["id"]}"></span>)</span><span class="m2">Свернуть ↑</span></button></section>''' for g in GROUPS)
    body = f'''
<div class="frame">
<header class="hd"><div class="wrap hd-in">
  <a class="logo" href="#top"><img data-photo="logo" alt="Логотип «Своё бистро»"><span>своё бистро</span></a>
  <nav class="nav" aria-label="Разделы"><a href="#menu">меню</a><a href="#reviews">отзывы</a><a href="#contacts">контакты</a></nav>
  <button class="ib" data-open-cart aria-label="Корзина">{BAG}<span class="cnt" data-cart-count>0</span></button>
</div></header>
<main id="top">
<section class="wrap hero">
  <div class="reveal"><p class="sm">пекарня · завтраки · любимые блюда</p><h1>Сегодня на доске</h1>
    <ul class="today">
      <li><span>Круассан классический</span><i></i><b>180</b></li>
      <li><span>Крок мадам</span><i></i><b>590</b></li>
      <li><span>Синнабон вишня / шоколад</span><i></i><b>360</b></li>
      <li><span>Смэш-бургер</span><i></i><b>630</b></li>
    </ul>
    <a href="#menu" class="btn">Всё меню ↓</a></div>
  <div class="pol reveal"><img data-photo="croissant" alt="Круассаны на витрине"><span>тёплые с утра!</span></div>
</section>
<section id="menu" class="wrap sec"><h2 class="ttl">Меню</h2><p class="hint2">Мелом — то, что любят гости. Нажмите «Показать всё», чтобы открыть раздел целиком.</p>
  <div class="boards">{boards}</div></section>
<section id="reviews" class="wrap sec"><h2 class="ttl">Пишут гости</h2><div class="revs" data-reviews="3"></div><a class="lnk" data-reviews-link>все отзывы — на Яндекс Картах →</a></section>
<section id="contacts" class="wrap sec">
  <div class="kraft reveal"><span class="tape" aria-hidden="true"></span>
    <h2>Заходите в гости</h2>
    <p><b data-cfg="address"></b><br><span data-status></span> · <a data-tel data-cfg="phone"></a></p>
    <ul class="hours" data-hours></ul>
    <div class="btns"><a class="btn dark" data-route>Построить маршрут</a><a class="btn line" data-vk>ВКонтакте</a></div></div>
</section>
</main>
<footer class="ft"><div class="wrap">своё бистро · © <span data-year></span> · <a data-privacy>политика конфиденциальности</a> · демо-концепт</div></footer>
</div>'''
    css = r'''
:root{--bd:#24302B;--bd2:#2C3A34;--ch:#F1EFE8;--ch2:#BAC3BC;--ye:#F3D677;--pk:#F2A7A0;--wood:#7A5236;--kr:#D9BD8F;--kr-ink:#3A2A1A;
--ui-bg:#F4F1EA;--ui-paper:#fff;--ui-ink:#24302B;--ui-ink2:#5B655F;--ui-line:#DCD6C9;--ui-acc:#24302B;--ui-acc-ink:var(--ye);--ui-soft:#ECE6D8;--ui-r:12px;--ui-btn-r:10px;--ui-bd:0;--ui-font:'Rubik',sans-serif;--ui-font-h:700 32px 'Amatic SC',cursive;--ui-emo-bg:#ECE6D8}
body{background:#3B2A1E;color:var(--ch);font:16px/1.5 'Rubik',sans-serif}
.frame{background:var(--bd);background-image:radial-gradient(circle at 30% 20%,rgba(255,255,255,.06),transparent 50%),url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.65' numOctaves='3'/%3E%3CfeColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 .07 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");min-height:100vh}
@media(min-width:960px){.frame{margin:14px;border:14px solid var(--wood);border-radius:10px;box-shadow:inset 0 0 40px rgba(0,0,0,.6),0 10px 30px rgba(0,0,0,.5)}}
h1,h2,h3{font-family:'Amatic SC',cursive;font-weight:700;line-height:1;margin:0 0 .3em;letter-spacing:.02em}
.btn{display:inline-flex;align-items:center;min-height:50px;padding:0 22px;border:2px solid var(--ch);border-radius:10px;color:var(--ch);text-decoration:none;font:700 15px 'Rubik';background:transparent;transition:background .15s,color .15s}
.btn:hover{background:var(--ch);color:var(--bd)}.btn.dark{background:var(--kr-ink);border-color:var(--kr-ink);color:var(--kr)}.btn.line{border-color:var(--kr-ink);color:var(--kr-ink)}
.hd{position:sticky;top:0;z-index:50;background:rgba(36,48,43,.95);border-bottom:2px dashed rgba(241,239,232,.25)}
.hd-in{display:flex;align-items:center;gap:12px;height:66px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;margin-right:auto}.logo img{width:42px;height:42px;border-radius:50%;filter:grayscale(.2)}.logo span{font:700 32px 'Amatic SC';color:var(--ch)}
.nav{display:none;gap:18px}.nav a{font:700 26px 'Amatic SC';text-decoration:none;color:var(--ch2)}.nav a:hover{color:var(--ye)}@media(min-width:760px){.nav{display:flex}}
.ib{position:relative;width:46px;height:46px;border-radius:10px;border:2px solid var(--ch);background:transparent;color:var(--ch);display:grid;place-items:center;cursor:pointer}
.hero{display:grid;gap:26px;padding-top:24px;padding-bottom:26px;align-items:center}@media(min-width:860px){.hero{grid-template-columns:1.2fr .8fr}}
.sm{font:600 22px 'Caveat',cursive;color:var(--ch2);margin:0}
.hero h1{font-size:clamp(56px,14vw,104px);color:var(--ye);text-shadow:0 0 1px rgba(255,255,255,.3)}
.today{list-style:none;padding:0;margin:4px 0 24px;font:600 clamp(22px,5.4vw,28px)/1.25 'Caveat',cursive;max-width:520px}
.today li{display:flex;align-items:baseline;gap:8px;padding:2px 0}.today i{flex:1;border-bottom:2px dotted rgba(241,239,232,.45);transform:translateY(-6px)}.today b{color:var(--pk)}
.pol{justify-self:center;background:#FBF8F1;padding:12px 12px 46px;width:min(330px,90%);transform:rotate(3deg);box-shadow:0 18px 30px rgba(0,0,0,.45);position:relative}
.pol::before{content:"";position:absolute;width:110px;height:28px;background:rgba(243,214,119,.75);top:-12px;left:50%;transform:translateX(-50%) rotate(-4deg)}
.pol img{aspect-ratio:1;object-fit:cover;width:100%}.pol span{position:absolute;left:0;right:0;bottom:8px;text-align:center;font:700 26px 'Caveat';color:#333}
.sec{padding:36px 16px}
.ttl{font-size:clamp(48px,11vw,80px);color:var(--ch)}.ttl::after{content:"";display:block;width:150px;height:10px;margin-top:4px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='150' height='10'%3E%3Cpath d='M2 6 C30 1 50 9 75 5 S120 2 148 6' stroke='%23F3D677' stroke-width='3' fill='none' stroke-linecap='round'/%3E%3C/svg%3E")}
.hint2{color:var(--ch2);font:600 21px 'Caveat';margin:0 0 18px}
.boards{display:grid;gap:22px}@media(min-width:900px){.boards{grid-template-columns:1fr 1fr;gap:26px 40px}}
.bd{border:2px dashed rgba(241,239,232,.22);border-radius:14px;padding:18px 16px}
.bd h3{font-size:44px;color:var(--ye);margin:0}.bn{color:var(--ch2);font:600 19px 'Caveat';margin:0 0 8px}
.ln{display:grid;grid-template-columns:auto 1fr auto auto;align-items:center;gap:10px;padding:7px 0;border-bottom:1px solid rgba(241,239,232,.08)}
.bd:not(.is-open) .ln:nth-child(n+5){display:none}
.ln-ph{width:44px;height:44px;border-radius:50%;overflow:hidden;border:2px solid rgba(241,239,232,.6)}.ln-ph img{width:100%;height:100%;object-fit:cover}.ln-ph .emo{font-size:20px;background:var(--bd2)}
.ln-n{font:600 22px/1.1 'Caveat',cursive;min-width:0}.ln-n small{display:block;font:400 12.5px 'Rubik';color:var(--ch2);margin-top:2px}
.ln-n em{font:700 12px 'Rubik';color:var(--pk);margin-left:6px;font-style:normal;text-transform:lowercase}
.ln-p{font:700 23px 'Caveat';color:var(--pk);white-space:nowrap}
.ln .act{width:88px}
@media(max-width:560px){.ln{grid-template-columns:44px 1fr auto;grid-template-areas:"ph nm nm" "ph pr ac";row-gap:4px}.ln>:first-child{grid-area:ph;align-self:start}.ln-n{grid-area:nm}.ln-p{grid-area:pr}.ln .act{grid-area:ac}}
.ln .add{min-height:38px;background:transparent;border:2px solid var(--ch);color:var(--ch);font-size:13px;border-radius:9px}.ln .add:hover{background:var(--ye);color:var(--bd);border-color:var(--ye)}
.ln .stp{min-height:38px;background:var(--ye);color:var(--bd);padding:2px}.ln .stp button{width:26px;height:30px;font-size:16px}.ln .stp span{font-size:14px}
.more{margin-top:10px;background:none;border:0;color:var(--ye);font:700 26px 'Amatic SC';cursor:pointer;padding:4px 0}.more .m2{display:none}.bd.is-open .m1{display:none}.bd.is-open .m2{display:inline}
.bd:has(.ln:nth-child(4):last-child) .more,.bd:has(.ln:nth-child(3):last-child) .more{display:none}
.revs{display:grid;gap:18px;margin-bottom:12px}@media(min-width:860px){.revs{grid-template-columns:repeat(3,1fr)}}
.rv p{font:600 23px/1.2 'Caveat',cursive;margin:0 0 6px}.rv b{color:var(--ye);font:700 24px 'Amatic SC'}
.lnk{color:var(--ye);font-weight:600}
.kraft{background:var(--kr);color:var(--kr-ink);border-radius:6px;padding:30px 22px;position:relative;box-shadow:0 20px 30px rgba(0,0,0,.4);transform:rotate(-.6deg);max-width:760px;margin:0 auto}
.tape{position:absolute;top:-14px;left:50%;width:130px;height:30px;background:rgba(255,255,255,.45);transform:translateX(-50%) rotate(3deg)}
.kraft h2{font-size:56px}.kraft a{color:var(--kr-ink)}.closed{color:#8C2A1C}
.hours{list-style:none;padding:0;margin:14px 0 20px;display:grid;gap:2px 30px}@media(min-width:600px){.hours{grid-template-columns:1fr 1fr}}
.hours li{display:flex;justify-content:space-between;border-bottom:1.5px dashed rgba(58,42,26,.3);padding:4px 0}.hours li.today{font-weight:800;color:#8C2A1C}
.btns{display:flex;flex-wrap:wrap;gap:10px}
.ft{padding:20px 0 96px;color:var(--ch2);font-size:13px}.ft a{color:var(--ch2)}@media(min-width:960px){.ft{padding-bottom:26px}}
'''
    tpl = '{item:p=>`<div class="ln">${p.photo?`<div class="ln-ph">${UI.thumb(p)}</div>`:`<span class="ln-ph"><span class="emo" aria-hidden="true">${p.emoji}</span></span>`}<div class="ln-n">${UI.esc(p.name)}${p.tag?`<em>${UI.TAGS[p.tag]}</em>`:""}${p.desc?`<small>${UI.esc(p.desc)}</small>`:""}</div><span class="ln-p">${p.price} ₽</span>${UI.slot(p.id)}</div>`,' \
          'review:r=>`<div class="rv reveal in"><p>«${UI.esc(r.text)}»</p><b>— ${UI.esc(r.name)}</b></div>`}'
    return dict(file='5-grifelnaya-doska.html', v='d5', title='Своё бистро — Грифельная доска',
                fonts='family=Amatic+SC:wght@700&family=Caveat:wght@600;700&family=Rubik:wght@400;500;700', css=css, body=body, tpl=tpl, add_label='+ взять')
D.append(d5)

# =====================================================================
# 6. БЕНТО — вся страница как сетка плиток; группа раскрывается прямо в сетке
# =====================================================================
def d6():
    cats = ''.join(f'''<article class="t cat" id="c-{g["id"]}">
      <button class="cat-h" data-open="c-{g["id"]}" data-scope="cats" data-scroll="80"><img data-photo="{g["cover"]}" alt="" loading="lazy">
        <span class="cat-t"><b>{g["name"]}</b><small><span data-gcount="{g["id"]}"></span> · <span data-gfrom="{g["id"]}"></span></small></span><span class="cat-x" aria-hidden="true">↗</span></button>
      <div class="cat-b"><div class="cat-top"><h3>{g["name"]}</h3><p>{g["note"]}</p><button class="cat-c" data-open="c-{g["id"]}" data-scope="cats">Свернуть ✕</button></div><div class="grid" data-group-items="{g["id"]}"></div></div>
    </article>''' for g in GROUPS)
    body = f'''
<header class="hd"><div class="wrap hd-in">
  <a class="logo" href="#top"><img data-photo="logo" alt="Логотип «Своё бистро»"><span>своё бистро</span></a>
  <nav class="nav" aria-label="Разделы"><a href="#menu">Меню</a><a href="#info">Доставка</a><a href="#contacts">Контакты</a></nav>
  <button class="ib" data-open-cart aria-label="Корзина">{BAG}<span class="cnt" data-cart-count>0</span></button>
</div></header>
<main id="top" class="wrap bento">
  <section class="t hero" data-bg="hall"><div class="hero-t"><span class="pill">Новоселье · бульвар Белых Ночей, 3</span><h1>Пекарня и&nbsp;бистро у&nbsp;дома</h1><a href="#menu" class="btn">Заказать {ARROW}</a></div></section>
  <a class="t rate" data-reviews-link><span class="big" data-cfg="rating"></span><span><span class="stars">★★★★★</span><small><span data-cfg="ratingCount"></span> · Яндекс Карты</small></span></a>
  <section class="t now"><span class="lbl">Сейчас</span><b data-status></b><button class="mini" data-open="hrs">Часы работы ▾</button><ul class="hours" id="hrs" data-hours="short"></ul></section>
  <h2 class="t ttl" id="menu">Меню <small>нажмите на плитку — она раскроется</small></h2>
  {cats}
  <section class="t deliv" id="info"><span class="lbl">Доставка</span><ul>
    <li><b>45–60 мин</b><small>по Новоселью</small></li><li><b>150 ₽</b><small>бесплатно от 1 500 ₽</small></li><li><b>от 700 ₽</b><small>минимальный заказ</small></li><li><b>0 ₽</b><small>самовывоз без очереди</small></li></ul></section>
  <section class="t revt"><span class="lbl">Гости пишут</span><div class="qs" data-reviews="2"></div></section>
  <section class="t map" id="contacts"><iframe data-map title="Своё бистро на карте" loading="lazy"></iframe></section>
  <section class="t contact"><span class="lbl">Контакты</span><p class="addr" data-cfg="address"></p><p><a data-tel data-cfg="phone"></a></p><a class="btn" data-route>Маршрут {ARROW}</a><a class="lnk" data-vk>ВКонтакте ↗</a></section>
</main>
<footer class="ft"><div class="wrap">© <span data-year></span> Своё бистро · <a data-privacy>Политика конфиденциальности</a> · демо-концепт</div></footer>'''
    css = r'''
:root{--bg:#F3F1EC;--p:#fff;--k:#141414;--k2:#6B6B6B;--ln:#E3E0DA;--t:#D85F44;--t2:#FBE3DB;
--ui-bg:var(--bg);--ui-paper:var(--p);--ui-ink:var(--k);--ui-ink2:var(--k2);--ui-line:var(--ln);--ui-acc:var(--k);--ui-acc-ink:#fff;--ui-soft:var(--t2);--ui-r:16px;--ui-btn-r:12px;--ui-bd:0;--ui-font:'Onest',sans-serif;--ui-font-h:700 22px 'Onest',sans-serif;--ui-emo-bg:var(--t2);--ui-add-bg:var(--bg);--ui-add-ink:var(--k);--ui-cnt-bg:var(--t);--ui-cnt-ink:#fff;--ui-fn-r:14px}
body{background:var(--bg);color:var(--k);font:15px/1.5 'Onest',sans-serif}
h1,h2,h3{font-weight:800;letter-spacing:-.03em;line-height:1;margin:0}
.btn{display:inline-flex;align-items:center;gap:8px;min-height:48px;padding:0 20px;border-radius:12px;background:var(--k);color:#fff;text-decoration:none;font-weight:700;transition:background .15s}.btn:hover{background:var(--t)}
.hd{position:sticky;top:0;z-index:50;background:rgba(243,241,236,.92);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.hd-in{display:flex;align-items:center;gap:12px;height:62px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;margin-right:auto}.logo img{width:38px;height:38px;border-radius:10px}.logo span{font-weight:800;font-size:18px;letter-spacing:-.02em}
.nav{display:none;gap:4px}.nav a{text-decoration:none;font-weight:600;padding:8px 12px;border-radius:10px}.nav a:hover{background:var(--p)}@media(min-width:760px){.nav{display:flex}}
.ib{position:relative;width:44px;height:44px;border-radius:12px;border:0;background:var(--k);color:#fff;display:grid;place-items:center;cursor:pointer}
.bento{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;padding-top:6px;padding-bottom:20px}
@media(min-width:900px){.bento{grid-template-columns:repeat(12,1fr);gap:14px}}
.t{background:var(--p);border-radius:22px;padding:18px;position:relative;overflow:hidden;min-width:0}
.lbl{display:block;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--k2);margin-bottom:8px}
.hero{grid-column:1/-1;min-height:380px;background-size:cover;background-position:center;display:flex;align-items:flex-end;padding:0;color:#fff}
.hero::before{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(0,0,0,.72),rgba(0,0,0,.05) 60%)}
.hero-t{position:relative;padding:22px}.hero h1{font-size:clamp(34px,7.5vw,64px);margin:12px 0 18px;max-width:640px}
.pill{display:inline-block;background:rgba(255,255,255,.18);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);border-radius:999px;padding:6px 12px;font-size:13px;font-weight:600}
.hero .btn{background:#fff;color:var(--k)}.hero .btn:hover{background:var(--t);color:#fff}
@media(min-width:900px){.hero{grid-column:span 8;grid-row:span 2;min-height:440px}}
.rate{display:flex;flex-direction:column;align-items:flex-start;gap:4px;text-decoration:none;background:var(--t);color:#fff}@media(min-width:420px){.rate{flex-direction:row;align-items:center;gap:14px}}
.rate .big{font-size:clamp(44px,12vw,56px);font-weight:800;letter-spacing:-.04em}.rate .stars{display:block;letter-spacing:2px}.rate small{opacity:.9}
@media(min-width:900px){.rate{grid-column:span 4}}
.now b{display:block;font-size:22px;letter-spacing:-.02em}.closed{color:#B3261E}
.mini{margin-top:10px;border:1px solid var(--ln);background:var(--bg);border-radius:10px;padding:8px 12px;font:600 13px 'Onest';cursor:pointer;color:var(--k)}
.hours{list-style:none;padding:0;margin:0;display:none;font-size:13.5px}.hours.is-open{display:grid;grid-template-columns:1fr 1fr;gap:2px 16px;margin-top:10px}
.hours li{display:flex;justify-content:space-between}.hours li.today{color:var(--t);font-weight:800}
@media(min-width:900px){.now{grid-column:span 4}}
.ttl{grid-column:1/-1;background:none;padding:20px 4px 4px;font-size:clamp(34px,7vw,56px)}.ttl small{display:block;font-size:14px;font-weight:500;color:var(--k2);letter-spacing:0;margin-top:8px}
.cat{padding:0;grid-column:span 1;transition:background .2s}
@media(min-width:900px){.cat{grid-column:span 4}}
.cat-h{display:block;width:100%;padding:0;border:0;background:none;cursor:pointer;text-align:left;color:var(--k);position:relative}
.cat-h img{width:100%;aspect-ratio:4/3;object-fit:cover;transition:transform .5s}
.cat-h:hover img{transform:scale(1.04)}
.cat-t{display:block;padding:12px 14px 14px}.cat-t b{display:block;font-size:17px;letter-spacing:-.02em}.cat-t small{color:var(--k2);font-size:12.5px}
.cat-x{position:absolute;top:10px;right:10px;width:38px;height:38px;border-radius:12px;background:#fff;display:grid;place-items:center;font-weight:800}
.cat-b{display:none;padding:18px}
.cat.is-open{grid-column:1/-1;background:var(--p)}
.cat.is-open .cat-h{display:none}.cat.is-open .cat-b{display:block;animation:fade .3s}@keyframes fade{from{opacity:0;transform:scale(.99)}}
.cat-top{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 14px;margin-bottom:14px}.cat-top h3{font-size:32px}.cat-top p{margin:0;color:var(--k2);flex:1}
.cat-c{border:0;background:var(--bg);border-radius:10px;padding:9px 14px;font:700 13px 'Onest';cursor:pointer;color:var(--k)}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}@media(min-width:700px){.grid{grid-template-columns:repeat(3,1fr)}}@media(min-width:1050px){.grid{grid-template-columns:repeat(5,1fr)}}
.it{border:1px solid var(--ln);border-radius:16px;overflow:hidden;display:flex;flex-direction:column;position:relative}
.it-ph{aspect-ratio:1}.it-ph img{width:100%;height:100%;object-fit:cover}.it-ph .emo{font-size:44px}
.it-b{padding:10px;display:flex;flex-direction:column;flex:1}.it h4{font-size:14px;margin:0 0 4px;font-weight:700;letter-spacing:-.01em;line-height:1.25}.it .pr{font-weight:800;margin-top:auto;margin-bottom:8px}
.tag{position:absolute;top:8px;left:8px;background:#fff;border-radius:8px;font-size:10.5px;font-weight:700;padding:4px 8px}.t-hit{background:var(--t);color:#fff}
.deliv{grid-column:1/-1}.deliv ul{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.deliv b{display:block;font-size:24px;letter-spacing:-.03em}.deliv small{color:var(--k2)}
@media(min-width:900px){.deliv{grid-column:span 6}.deliv ul{grid-template-columns:repeat(4,1fr)}}
.revt{grid-column:1/-1;background:var(--k);color:#fff}.revt .lbl{color:#aaa}
.qs{display:grid;gap:12px}.q p{margin:0 0 4px;font-size:14.5px}.q small{color:#aaa}
@media(min-width:900px){.revt{grid-column:span 6}.qs{grid-template-columns:1fr 1fr}}
.map{grid-column:1/-1;padding:0;min-height:280px;background:#E6E2DA}.map iframe{width:100%;height:100%;min-height:280px;border:0;display:block}
@media(min-width:900px){.map{grid-column:span 8}}
.contact{grid-column:1/-1;display:flex;flex-direction:column;gap:8px;align-items:flex-start}.contact p{margin:0}.contact .addr{font-size:20px;font-weight:800;letter-spacing:-.02em}.contact a{color:var(--k)}.contact .btn{color:#fff;margin-top:6px}
.lnk{font-weight:600}
@media(min-width:900px){.contact{grid-column:span 4}}
.ft{padding:6px 0 96px;color:var(--k2);font-size:13px}@media(min-width:960px){.ft{padding-bottom:26px}}
'''
    tpl = '{item:p=>`<article class="it">' + TAG_JS + '<div class="it-ph">${UI.thumb(p)}</div><div class="it-b"><h4>${UI.esc(p.name)}</h4><div class="pr">${UI.fmt(p.price)}</div>${UI.slot(p.id)}</div></article>`,' \
          'review:r=>`<div class="q"><p>«${UI.esc(r.text)}»</p><small>${UI.esc(r.name)} · ${r.date}</small></div>`}'
    return dict(file='6-bento.html', v='d6', title='Своё бистро — Бенто',
                fonts='family=Onest:wght@400;500;600;700;800', css=css, body=body, tpl=tpl, add_label='В корзину')
D.append(d6)

# =====================================================================
# 7. БЕЛАЯ СКАТЕРТЬ — по референсу «Flavoria»: белый, оранжевый, тёмно-зелёный,
#    антиква + рукописное слово, тарелка в круге, вкладки с подчёркиванием
# =====================================================================
def d7():
    tabs = ''.join(f'<button class="tb" data-open="w-{g["id"]}" data-scope="wt" data-keep>{g["name"]}</button>' for g in GROUPS)
    panels = ''.join(f'<div class="wp{" is-open" if i == 0 else ""}" id="w-{g["id"]}" role="region" aria-label="{g["name"]}"><div class="dishes" data-group-items="{g["id"]}"></div></div>' for i, g in enumerate(GROUPS))
    flinks = ''.join(f'<li><a href="#menu" data-open="w-{g["id"]}" data-scope="wt" data-keep data-scroll="90">{g["name"]}</a></li>' for g in GROUPS)
    LEAF = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 19C5 10 11 5 20 4c-1 9-6 15-15 15z"/><path d="M5 19 14 10"/></svg>'
    HEART = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" aria-hidden="true"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>'
    CHEF = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 14a4 4 0 1 1 1.5-7.7A4 4 0 0 1 16 6.3 4 4 0 1 1 17 14v5H7z"/><path d="M7 16h10"/></svg>'
    body = f'''
<div class="util"><div class="wrap util-in">
  <span class="u-a">{PIN}<span data-cfg="address"></span></span>
  <span>{CLOCK}<span data-status></span></span>
  <a data-tel>{PHONE}<span data-cfg="phone"></span></a>
</div></div>
<header class="hd"><div class="wrap hd-in">
  <a class="logo" href="#top"><img data-photo="logo" alt="Логотип «Своё бистро»"><span><b>Своё бистро</b><small>— пекарня —</small></span></a>
  <nav class="nav" aria-label="Разделы"><a href="#top" class="on">Главная</a><a href="#about">О нас</a><a href="#menu">Меню</a><a href="#reviews">Отзывы</a><a href="#foot">Контакты</a></nav>
  <button class="cta" data-open-cart>{BAG}<span class="cta-t">Корзина</span><span class="cnt" data-cart-count>0</span></button>
</div></header>
<main id="top">
<section class="hero wrap">
  <div class="reveal"><p class="kick">своя выпечка · любимые блюда</p>
    <h1>Вкусно на любое <span class="scr">настроение</span></h1>
    <p class="lead">Бистро с пекарней в самом сердце Новоселья. Завтраки с утра, горячее до вечера — в зале или с доставкой домой.</p>
    <div class="cta2"><a href="#menu" class="btn">Смотреть меню</a><a class="btn out" data-route>{PIN} Маршрут</a></div>
    <div class="feat3"><span><i>{LEAF}</i>Своя<br>пекарня</span><span><i>{CHEF}</i>Своя<br>кухня</span><span><i>{HEART}</i>Готовим<br>с любовью</span></div></div>
  <div class="plate reveal"><div class="pl"><img data-photo="shrimp" alt="Креветки пиль-пиль"></div><span class="badge"><b>45+</b>позиций<br>в меню</span></div>
</section>
<section id="about" class="about"><div class="wrap ab-in">
  <div class="ab-ph reveal"><img data-photo="hall2" alt="Зал и витрина «Своего бистро»" loading="lazy"><span class="ab-b"><b data-cfg="rating"></b>★ на Яндекс<br>Картах</span></div>
  <div class="reveal"><p class="kick">добро пожаловать</p><h2>Своё место, <span class="scr">своя</span> выпечка</h2>
    <p>Мы печём сами: круассаны, синнабоны, даниши и хлеб на закваске — каждое утро. А на кухне готовим простые блюда в неожиданном исполнении: от крок мадам до утиной ноги.</p>
    <p class="sign">Своё бистро ♡</p><a class="btn dk" data-route>Как добраться →</a></div>
  <ul class="ab-f reveal"><li><i>{LEAF}</i>Хорошие продукты</li><li><i>{CHEF}</i>Своя пекарня</li><li><i>{HEART}</i>Уютный зал</li></ul>
</div></section>
<section id="menu" class="wrap sec">
  <p class="kick c">выбор гостей</p><h2 class="orn">Наше меню</h2>
  <div class="tabs" role="tablist" aria-label="Группы меню">{tabs}</div>
  {panels}
</section>
<section class="wrap promo">
  <div class="pr-g reveal"><p class="kick">удобно</p><h3>Самовывоз без очереди</h3><p>Закажите заранее — соберём к нужному времени.</p><button class="btn wh" data-open-cart>Заказать →</button></div>
  <div class="pr-ph reveal"><img data-photo="burger" alt="Смэш-бургер" loading="lazy"></div>
  <div class="pr-ph reveal"><img data-photo="takeaway" alt="Фирменная упаковка" loading="lazy"></div>
  <div class="pr-c reveal"><h3>Доставка</h3><ul><li><span>По Новоселью</span><b>45–60 мин</b></li><li><span>Стоимость</span><b>150 ₽</b></li><li><span>Бесплатно</span><b>от 1 500 ₽</b></li><li><span>Минимальный заказ</span><b>700 ₽</b></li></ul><button class="btn" data-open-cart>Оформить заказ</button></div>
</section>
<section class="wrap perks">
  <div><i>{icon('bike', 28)}</i><b>Доставка</b><small>по Новоселью</small></div>
  <div><i>{icon('bread', 28)}</i><b>Выпечка</b><small>каждое утро</small></div>
  <div><i>{icon('sun', 28)}</i><b>Завтраки</b><small>с 8:00 в будни</small></div>
  <div><i>{PHONE}</i><b>Предзаказ</b><small><a data-tel data-cfg="phone"></a></small></div>
</section>
<section id="reviews" class="wrap sec"><p class="kick c">отзывы</p><h2 class="orn">Гости о нас</h2><div class="revs" data-reviews="3"></div><p class="c"><a class="lnk" data-reviews-link>Все отзывы на Яндекс Картах →</a></p></section>
</main>
<footer class="ft" id="foot"><div class="wrap ft-in">
  <div><a class="logo" href="#top"><img data-photo="logo" alt=""><span><b>Своё бистро</b><small>— пекарня —</small></span></a><p>Выпечка, завтраки и любимые блюда в Новоселье.</p><a data-vk>ВКонтакте ↗</a></div>
  <div><h4>Меню</h4><ul>{flinks}</ul></div>
  <div><h4>Контакты</h4><ul class="ci"><li>{PIN}<span data-cfg="address"></span></li><li>{PHONE}<a data-tel data-cfg="phone"></a></li><li><a data-route>Построить маршрут →</a></li></ul></div>
  <div><h4>Часы работы</h4><ul class="hours" data-hours="short"></ul></div>
  <small class="cp">© <span data-year></span> Своё бистро · <a data-privacy>Политика конфиденциальности</a> · демо-концепт</small>
</div></footer>'''
    css = r'''
:root{--w:#fff;--sf:#FBF7F2;--k:#1F1F1F;--k2:#62605B;--o:#E8641B;--o-d:#CF5410;--g:#2F4A22;--ln:#EEE7DD;
--ui-bg:var(--sf);--ui-paper:#fff;--ui-ink:var(--k);--ui-ink2:var(--k2);--ui-line:var(--ln);--ui-acc:var(--o);--ui-acc-ink:#fff;--ui-soft:#FCEBDD;--ui-r:14px;--ui-btn-r:8px;--ui-bd:0;--ui-font:'Montserrat',sans-serif;--ui-font-h:700 24px 'PT Serif',serif;--ui-emo-bg:#FBF1E6;--ui-stp-bg:var(--g);--ui-stp-ink:#fff}
body{background:var(--w);color:var(--k);font:15px/1.6 'Montserrat',sans-serif}
h1,h2,h3,h4{font-family:'PT Serif',serif;font-weight:700;line-height:1.1;margin:0 0 .4em}
.scr{font-family:'Marck Script',cursive;font-weight:400;color:var(--o);font-size:1.12em}
.kick{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--o);margin:0 0 10px}.c{text-align:center}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:50px;padding:0 24px;border-radius:8px;background:var(--o);color:#fff;font:700 13.5px 'Montserrat';letter-spacing:.06em;text-transform:uppercase;text-decoration:none;border:1.5px solid var(--o);cursor:pointer;transition:background .15s}
.btn:hover{background:var(--o-d)}.btn.out{background:#fff;color:var(--k);border-color:#F2C3A5}.btn.out:hover{border-color:var(--o)}.btn.dk{background:var(--g);border-color:var(--g)}.btn.wh{background:#fff;color:var(--g);border-color:#fff}
.util{border-bottom:1px solid var(--ln);font-size:12.5px;color:var(--k2)}
.util-in{display:flex;flex-wrap:wrap;justify-content:space-between;gap:4px 16px;padding-top:8px;padding-bottom:8px}.util-in>*{display:inline-flex;align-items:center;gap:6px;text-decoration:none}.util svg{color:var(--o);width:15px;height:15px}
@media(max-width:620px){.u-a{display:none!important}}
.closed{color:#B3261E}
.hd{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.96);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border-bottom:1px solid var(--ln)}
.hd-in{display:flex;align-items:center;gap:16px;height:70px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;margin-right:auto}.logo img{width:46px;height:46px;border-radius:50%}
.logo b{display:block;font:italic 700 22px 'PT Serif';line-height:1}.logo small{display:block;color:var(--o);font-size:10px;letter-spacing:.2em;text-transform:uppercase;margin-top:3px}
.nav{display:none;gap:22px}.nav a{text-decoration:none;font-weight:600;font-size:13px;text-transform:uppercase;letter-spacing:.06em;padding:6px 0;border-bottom:2px solid transparent}.nav a:hover,.nav a.on{color:var(--o);border-color:var(--o)}
@media(min-width:980px){.nav{display:flex}}
.cta{position:relative;display:inline-flex;align-items:center;gap:8px;min-height:46px;padding:0 18px;border-radius:999px;border:0;background:var(--o);color:#fff;font:700 13px 'Montserrat';text-transform:uppercase;letter-spacing:.05em;cursor:pointer}
@media(max-width:480px){.cta-t{display:none}.cta{padding:0 12px}}
.hero{display:grid;gap:28px;padding-top:30px;padding-bottom:36px;align-items:center}
@media(min-width:900px){.hero{grid-template-columns:1fr 1.05fr;gap:30px;padding-top:44px;padding-bottom:50px}}
.hero h1{font-size:clamp(38px,8.5vw,68px)}
.lead{color:var(--k2);max-width:450px;margin:0 0 24px}
.cta2{display:flex;flex-wrap:wrap;gap:12px}.cta2 svg{width:16px;height:16px;color:var(--o)}
.feat3{display:flex;flex-wrap:wrap;gap:18px 26px;margin-top:28px;font-size:13px;color:var(--k2);line-height:1.3}
.feat3 span{display:flex;align-items:center;gap:10px}.feat3 i{width:52px;height:52px;border-radius:50%;border:1px solid var(--ln);display:grid;place-items:center;color:var(--g);flex:none}
.plate{position:relative;max-width:560px;width:100%;justify-self:center}
.pl{aspect-ratio:1;border-radius:50%;padding:18px;background:#fff;box-shadow:0 40px 70px -40px rgba(60,40,20,.55),0 0 0 1px var(--ln)}
.pl img{width:100%;height:100%;border-radius:50%;object-fit:cover}
.badge{position:absolute;right:4%;top:4%;width:110px;height:110px;border-radius:50%;background:#fff;box-shadow:0 14px 30px -12px rgba(0,0,0,.3);display:grid;place-content:center;text-align:center;font-size:12px;line-height:1.2}.badge b{font:700 30px 'PT Serif'}
.about{background:var(--sf);border-top:1px solid var(--ln);border-bottom:1px solid var(--ln)}
.ab-in{display:grid;gap:28px;padding-top:44px;padding-bottom:44px;align-items:center}@media(min-width:900px){.ab-in{grid-template-columns:1.05fr 1fr .55fr}}
.ab-ph{position:relative;border-radius:20px;overflow:hidden;aspect-ratio:4/3}.ab-ph img{width:100%;height:100%;object-fit:cover}
.ab-b{position:absolute;right:14px;bottom:14px;background:var(--o);color:#fff;border-radius:14px;padding:12px 14px;text-align:center;font-size:12px;line-height:1.3}.ab-b b{display:block;font:700 28px 'PT Serif'}
.about h2{font-size:clamp(30px,6vw,44px)}.about p{color:var(--k2)}.sign{font:28px 'Marck Script';color:var(--k)!important;margin:0 0 14px}
.ab-f{list-style:none;padding:0;margin:0;display:grid;gap:14px}.ab-f li{display:flex;align-items:center;gap:12px;font-weight:600}
.ab-f i{width:56px;height:56px;border-radius:50%;background:#F7EEE3;display:grid;place-items:center;color:var(--g);flex:none}
.sec{padding:50px 16px}
.orn{font-size:clamp(30px,6.5vw,44px);text-align:center;display:flex;align-items:center;justify-content:center;gap:14px}
.orn::before,.orn::after{content:"";width:46px;height:1.5px;background:var(--o);position:relative;flex:none}
.tabs{display:flex;flex-wrap:wrap;justify-content:center;gap:4px 22px;margin:8px 0 22px;border-bottom:1px solid var(--ln)}
.tb{background:none;border:0;border-bottom:2.5px solid transparent;padding:10px 2px;font:600 13px 'Montserrat';text-transform:uppercase;letter-spacing:.06em;color:var(--k2);cursor:pointer;margin-bottom:-1px}
.tb:hover{color:var(--k)}.tb.is-active{color:var(--o);border-color:var(--o)}
.wp{display:none}.wp.is-open{display:block;animation:fade .35s}@keyframes fade{from{opacity:0;transform:translateY(8px)}}
.dishes{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}@media(min-width:760px){.dishes{grid-template-columns:repeat(3,1fr)}}@media(min-width:1050px){.dishes{grid-template-columns:repeat(4,1fr);gap:20px}}
.ds{border:1px solid var(--ln);border-radius:14px;overflow:hidden;display:flex;flex-direction:column;background:#fff;position:relative;transition:box-shadow .2s,transform .2s}
.ds:hover{box-shadow:0 20px 34px -24px rgba(60,40,20,.5);transform:translateY(-3px)}
.ds-ph{aspect-ratio:4/3;background:#F7EEE3}.ds-ph img{width:100%;height:100%;object-fit:cover}.ds-ph .emo{font-size:44px}
.ds-b{padding:12px 12px 14px;display:flex;flex-direction:column;flex:1}.ds h4{font-size:16px;margin:0 0 4px}.ds p{margin:0 0 10px;color:var(--k2);font-size:12.5px;line-height:1.4}
.ds-f{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-top:auto}.ds-f .pr{color:var(--o);font-weight:800;font-size:16px}
.ds .act{width:auto}
.ds .add{width:40px;height:40px;min-height:40px;border-radius:50%;background:var(--g);color:#fff;font-size:22px;padding:0;line-height:1}
.ds .stp{width:110px;min-height:40px;border-radius:999px}.ds .stp button{width:32px;height:32px;border-radius:50%;font-size:17px}
@media(max-width:420px){.ds-f{flex-wrap:wrap}.ds .stp{width:100%}}
.tag{position:absolute;top:10px;left:10px;background:#fff;color:var(--o);font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;padding:4px 8px;border-radius:6px}.t-hit{background:var(--o);color:#fff}
.promo{display:grid;gap:12px;padding-top:10px;padding-bottom:10px}@media(min-width:900px){.promo{grid-template-columns:1.2fr .9fr .55fr 1.1fr}}
.pr-g{background:var(--g);color:#fff;border-radius:16px;padding:26px}.pr-g .kick{color:#F2B98F}.pr-g h3{font-size:30px}.pr-g p{opacity:.85;margin:0 0 18px}
.pr-ph{border-radius:16px;overflow:hidden;min-height:200px}.pr-ph img{width:100%;height:100%;object-fit:cover}
@media(max-width:899px){.pr-ph{display:none}}
.pr-c{border:1px solid var(--ln);border-radius:16px;padding:22px}.pr-c h3{font-size:26px}
.pr-c ul{list-style:none;padding:0;margin:0 0 16px}.pr-c li{display:flex;justify-content:space-between;gap:10px;padding:7px 0;border-bottom:1px dashed var(--ln);font-size:14px}.pr-c .btn{width:100%}
.perks{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;padding-top:26px;padding-bottom:26px}@media(min-width:900px){.perks{grid-template-columns:repeat(4,1fr)}}
.perks div{display:grid;grid-template-columns:auto 1fr;column-gap:12px;align-items:center}.perks i{grid-row:span 2;color:var(--g)}.perks b{font-size:14px}.perks small{color:var(--k2)}
.revs{display:grid;gap:16px;margin-bottom:16px}@media(min-width:860px){.revs{grid-template-columns:repeat(3,1fr)}}
.rv{border:1px solid var(--ln);border-radius:14px;padding:20px}.rv .st{color:var(--o);letter-spacing:2px}.rv p{margin:8px 0 12px;font-size:14.5px}.rv b{font-family:'PT Serif'}.rv small{color:var(--k2)}
.lnk{color:var(--o);font-weight:700}
.ft{background:var(--sf);border-top:1px solid var(--ln);padding:36px 0 96px;font-size:14px}@media(min-width:960px){.ft{padding-bottom:30px}}
.ft-in{display:grid;gap:24px}@media(min-width:800px){.ft-in{grid-template-columns:1.3fr 1fr 1.2fr 1fr}}
.ft h4{font-family:'Montserrat';font-size:13px;text-transform:uppercase;letter-spacing:.1em}.ft ul{list-style:none;padding:0;margin:0;display:grid;gap:6px}.ft a{text-decoration:none}.ft a:hover{color:var(--o)}
.ft p{color:var(--k2)}.ci li{display:flex;gap:8px;align-items:flex-start}.ci svg{color:var(--o);flex:none;width:17px;height:17px;margin-top:2px}
.hours li{display:flex;justify-content:space-between}.hours li.today{color:var(--o);font-weight:700}
.cp{grid-column:1/-1;color:var(--k2);border-top:1px solid var(--ln);padding-top:14px}
'''
    tpl = '{item:p=>`<article class="ds">' + TAG_JS + '<div class="ds-ph">${UI.thumb(p)}</div><div class="ds-b"><h4>${UI.esc(p.name)}</h4>${p.desc?`<p>${UI.esc(p.desc)}</p>`:""}<div class="ds-f"><span class="pr">${UI.fmt(p.price)}</span>${UI.slot(p.id)}</div></div></article>`,' \
          'review:r=>`<article class="rv"><div class="st">★★★★★</div><p>${UI.esc(r.text)}</p><b>${UI.esc(r.name)}</b> <small>· ${r.date}</small></article>`}'
    return dict(file='7-belaya-skatert.html', v='d7', title='Своё бистро — Белая скатерть',
                fonts='family=PT+Serif:ital,wght@0,700;1,700&family=Marck+Script&family=Montserrat:wght@400;500;600;700;800', css=css, body=body, tpl=tpl, add_label='+')
D.append(d7)

# =====================================================================
# 8. FLAVORIA ПОЛНОСТЬЮ — структура референса блок за блоком
# =====================================================================
def d8():
    LEAF = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 19C5 10 11 5 20 4c-1 9-6 15-15 15z"/><path d="M5 19 14 10"/></svg>'
    CHEF = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 14a4 4 0 1 1 1.5-7.7A4 4 0 0 1 16 6.3 4 4 0 1 1 17 14v5H7z"/><path d="M7 16h10"/></svg>'
    HEART = '<svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>'
    HOUSE = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 11 12 4l8 7v9H4z"/><path d="M10 20v-5h4v5"/></svg>'
    FORK = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M7 3v8M5 3v5a2 2 0 0 0 4 0V3M7 11v10M17 3c-2 2-2 6 0 8v10"/></svg>'
    CAL = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/></svg>'
    USERS = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M3 20a6 6 0 0 1 12 0M16 4.5a3.5 3.5 0 0 1 0 7M18 20a6 6 0 0 0-3-5.2"/></svg>'
    BOX = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7h11v9H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/></svg>'
    BAGL = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 8h12l-1 12H7L6 8Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>'
    HEAD = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="13" width="4" height="6" rx="1.5"/><rect x="17" y="13" width="4" height="6" rx="1.5"/><path d="M20 19c0 1.5-2 2-5 2"/></svg>'
    leaves = ''.join(f'<svg class="lf lf{i}" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 19C5 10 11 5 20 4c-1 9-6 15-15 15z" fill="#6E9A3E"/><path d="M5 19 14 10" stroke="#3F6420" stroke-width="1" fill="none"/></svg>' for i in range(1, 5))
    tabs = ''.join(f'<button class="tb" data-open="m-{g["id"]}" data-scope="mt" data-keep>{g["name"]}</button>' for g in GROUPS)
    panels = ''.join(f'<div class="mp{" is-open" if i == 0 else ""}" id="m-{g["id"]}" role="region" aria-label="{g["name"]}"><div class="dishes" data-group-items="{g["id"]}"></div></div>' for i, g in enumerate(GROUPS))
    flinks = ''.join(f'<li><a href="#fullmenu" class="fm" data-g="{g["id"]}">{g["name"]}</a></li>' for g in GROUPS)
    gal = ''.join(f'<div class="gi"><img data-photo="{k}" alt="{a}" loading="lazy"></div>' for k, a in [('hall','Зал'),('vitrine','Витрина с данишами'),('table','Стол с ягодными ветками'),('croissant','Круассаны'),('shelves','Зал с кирпичной стеной'),('window','Вход и логотип')])
    body = f'''
<div class="util"><div class="wrap util-in">
  <span class="u-a">{PIN}<span data-cfg="address"></span></span>
  <span class="u-h">{CLOCK}пн–чт 8–21 · пт 8–22 · сб 9–22 · вс 9–21</span>
  <span class="u-r"><a data-tel>{PHONE}<span data-cfg="phone"></span></a><a data-vk class="soc" aria-label="ВКонтакте">VK</a></span>
</div></div>
<header class="hd"><div class="wrap hd-in">
  <a class="logo" href="#top"><img data-photo="logo" alt="Логотип «Своё бистро»"><span><b>Своё бистро</b><small>— пекарня —</small></span></a>
  <nav class="nav" aria-label="Разделы"><a href="#top" class="on">Главная</a><a href="#about">О нас</a><a href="#popular">Меню</a><a href="#book">Бронь</a><a href="#gallery">Галерея</a><a href="#foot">Контакты</a></nav>
  <a href="#book" class="cta">Забронировать стол</a>
  <button class="cartb" data-open-cart aria-label="Корзина">{BAG}<span class="cnt" data-cart-count>0</span></button>
</div></header>
<main id="top">
<section class="hero"><div class="wrap hero-in">
  <div class="reveal"><p class="kick">своя выпечка | любимые блюда</p>
    <h1>Вкусная еда на&nbsp;любое <span class="scr">настроение</span></h1>
    <p class="lead">Бистро с пекарней в самом сердце Новоселья. Каждое блюдо готовим с любовью — а выпечку печём сами, каждое утро.</p>
    <div class="btns"><a href="#popular" class="btn">{FORK} Смотреть меню</a><a href="#book" class="btn out">{CAL} Забронировать стол</a></div>
    <div class="f3"><span><i>{LEAF}</i>Свежие<br>продукты</span><span><i>{CHEF}</i>Своя<br>кухня</span><span><i>{HEART}</i>Готовим<br>с любовью</span></div></div>
  <div class="plate reveal">{leaves}<div class="pl"><img data-photo="shrimp" alt="Креветки пиль-пиль"></div><span class="badge"><svg width="22" height="14" viewBox="0 0 22 14" aria-hidden="true"><path d="M2 12C6 4 14 2 20 2" stroke="#E8641B" stroke-width="2" fill="none" stroke-linecap="round"/></svg><b>45+</b>блюд<br>в меню</span></div>
</div></section>
<section id="about" class="about"><div class="wrap ab-in">
  <div class="ab-ph reveal"><img data-photo="hall2" alt="Зал и витрина «Своего бистро»" loading="lazy"><span class="ab-b"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/></svg><b data-cfg="rating"></b>на Яндекс<br>Картах</span></div>
  <div class="ab-t reveal"><p class="kick">добро пожаловать в «Своё бистро»</p><h2>Своя выпечка, <span class="scr">своя</span> жизнь</h2>
    <p>Мы верим, что хорошая еда собирает людей вместе. С утра — круассаны, синнабоны и хлеб на закваске из собственной пекарни, днём и вечером — паста, горячее и стейки. Простые блюда в неожиданном исполнении.</p>
    <p class="sign">Своё бистро ♡</p><a href="#gallery" class="btn dk">Подробнее о нас ›</a></div>
  <ul class="ab-f reveal"><li><i>{LEAF}</i>Хорошие<br>продукты</li><li><i>{CHEF}</i>Своя<br>пекарня</li><li><i>{HOUSE}</i>Уютный<br>зал</li></ul>
</div></section>
<section id="popular" class="wrap sec">
  <p class="kick c">выбор гостей</p>
  <div class="pop-h"><h2 class="orn">Популярные блюда</h2><button class="all" data-open="fullmenu">Всё меню <span>›</span></button></div>
  <div class="dishes" id="popularGrid"></div>
  <div class="full" id="fullmenu">
    <div class="full-in"><h3 class="orn sm">Всё меню</h3>
      <div class="tabs" role="tablist" aria-label="Группы меню">{tabs}</div>{panels}
      <p class="c"><button class="all" data-open="fullmenu">Свернуть меню ↑</button></p></div>
  </div>
</section>
<section id="book" class="wrap offer">
  <div class="of-g reveal"><p class="kick">специальное предложение</p><h3>Самовывоз без очереди</h3><p class="of-s">Закажите заранее — соберём к вашему времени</p><button class="btn wh" data-open-cart>Заказать ›</button>
    <div class="of-pl"><img data-photo="tartarCroissant" alt="Тартар с круассаном" loading="lazy"></div></div>
  <div class="of-d reveal"><img data-photo="coffee" alt="Капучино и выпечка" loading="lazy"></div>
  <form class="of-f reveal" id="bookForm" novalidate>
    <h3>Забронируйте столик</h3>
    <div class="bf2"><label class="bf"><span class="sr">Дата</span>{CAL}<input type="date" id="bDate" required></label><label class="bf"><span class="sr">Время</span>{CLOCK}<select id="bTime" required></select></label></div>
    <label class="bf"><span class="sr">Количество гостей</span>{USERS}<select id="bGuests"><option>1 гость</option><option selected>2 гостя</option><option>3 гостя</option><option>4 гостя</option><option>5 гостей</option><option>6+ гостей</option></select></label>
    <div class="bf2"><label class="bf"><span class="sr">Имя</span><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg><input type="text" id="bName" placeholder="Имя" autocomplete="given-name"></label><label class="bf"><span class="sr">Телефон</span>{PHONE}<input type="tel" id="bPhone" placeholder="+7 (___) ___-__-__" inputmode="tel" autocomplete="tel" required></label></div>
    <input type="text" id="bWeb" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px">
    <label class="chk sm"><input type="checkbox" id="bOk"><span>Даю <a href="soglasie.html" target="_blank" rel="noopener">согласие на обработку персональных данных</a></span></label>
    <button class="btn full" type="submit">Забронировать</button><p class="bmsg" id="bMsg" role="status"></p>
  </form>
</section>
<section class="wrap perks">
  <div><i>{BOX}</i><b>Доставка</b><small>по Новоселью, 45–60 мин</small></div>
  <div><i>{BAGL}</i><b>Самовывоз</b><small>без очереди, к времени</small></div>
  <div><i>{icon('bread', 30)}</i><b>Своя выпечка</b><small>каждое утро</small></div>
  <div><i>{HEAD}</i><b>Звоните</b><small><a data-tel data-cfg="phone"></a></small></div>
</section>
<section id="gallery" class="wrap sec"><p class="kick c">галерея</p><h2 class="orn">Атмосфера бистро</h2><div class="gal">{gal}</div></section>
<section id="reviews" class="wrap sec pt0"><p class="kick c">отзывы</p><h2 class="orn">Гости о нас</h2><div class="revs" data-reviews="3"></div><p class="c"><a class="lnk" data-reviews-link>Все отзывы на Яндекс Картах ›</a></p></section>
</main>
<footer class="ft" id="foot"><div class="wrap ft-in">
  <div class="ft-a"><a class="logo" href="#top"><img data-photo="logo" alt=""><span><b>Своё бистро</b><small>— пекарня —</small></span></a><p>Хорошая еда — хорошее настроение. Приходите в гости или закажите домой.</p><a data-vk class="soc">VK</a></div>
  <div><h4>Быстрые ссылки</h4><ul><li><a href="#about">О нас</a></li><li><a href="#popular">Меню</a></li><li><a href="#book">Бронь</a></li><li><a href="#gallery">Галерея</a></li><li><a href="#reviews">Отзывы</a></li></ul></div>
  <div><h4>Наше меню</h4><ul>{flinks}</ul></div>
  <div><h4>Контакты</h4><ul class="ci"><li>{PIN}<span data-cfg="address"></span></li><li>{PHONE}<a data-tel data-cfg="phone"></a></li><li>{CLOCK}<span data-status></span></li></ul></div>
  <div><h4>Новости</h4><p>Подпишитесь — расскажем о новинках выпечки и сезонных блюдах.</p><form id="subForm" novalidate><div class="sub"><label class="sr" for="subMail">E-mail</label><input type="email" id="subMail" placeholder="Ваш e-mail"><button class="btn">Подписаться</button></div><label class="chk sm" style="margin-top:8px"><input type="checkbox" id="subOk"><span>Даю <a href="soglasie.html" target="_blank" rel="noopener">согласие на обработку персональных данных</a></span></label></form><p class="bmsg" id="subMsg" role="status"></p></div>
  <div class="cp"><span>© <span data-year></span> Своё бистро. Демо-концепт сайта.</span><span><a data-privacy>Политика конфиденциальности</a></span></div>
</div></footer>'''
    css = r'''
:root{--w:#fff;--sf:#FBF7F2;--k:#1E1E1E;--k2:#5F5D58;--o:#E8641B;--o-d:#CF5410;--o-s:#FDEEE3;--g:#2C4A1E;--g2:#3F6420;--ln:#EFE8DE;
--ui-bg:var(--sf);--ui-paper:#fff;--ui-ink:var(--k);--ui-ink2:var(--k2);--ui-line:var(--ln);--ui-acc:var(--o);--ui-acc-ink:#fff;--ui-soft:var(--o-s);--ui-r:12px;--ui-btn-r:6px;--ui-bd:0;--ui-font:'Montserrat',sans-serif;--ui-font-h:600 26px 'Playfair Display',serif;--ui-emo-bg:#FBF1E6;--ui-stp-bg:var(--g);--ui-stp-ink:#fff}
body{background:var(--w);color:var(--k);font:15px/1.65 'Montserrat',sans-serif}
h1,h2,h3,h4{font-family:'Playfair Display',serif;font-weight:600;line-height:1.08;margin:0 0 .4em}
.scr{font-family:'Marck Script',cursive;font-weight:400;color:var(--o);font-size:1.12em;line-height:1}
.kick{font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--o);margin:0 0 12px}.c{text-align:center}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:48px;padding:0 22px;border-radius:6px;background:var(--o);color:#fff;font:700 12.5px 'Montserrat';letter-spacing:.07em;text-transform:uppercase;text-decoration:none;border:1.5px solid var(--o);cursor:pointer;transition:background .15s,transform .15s}
.btn:hover{background:var(--o-d);transform:translateY(-1px)}.btn.out{background:#fff;color:var(--k);border-color:#F3C3A3}.btn.out svg{color:var(--o)}.btn.out:hover{border-color:var(--o)}
.btn.dk{background:var(--g);border-color:var(--g)}.btn.dk:hover{background:#21391A}.btn.wh{background:#fff;color:var(--g);border-color:#fff}.btn.full{width:100%}
.util{border-bottom:1px solid var(--ln);font-size:12.5px;color:var(--k2)}
.util-in{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:4px 18px;min-height:40px}
.util-in>span,.util a{display:inline-flex;align-items:center;gap:7px;text-decoration:none}.util svg{color:var(--o);width:15px;height:15px}
.u-r{gap:16px!important}
.soc{display:inline-grid!important;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--k);color:#fff!important;font:800 10px 'Montserrat';text-decoration:none}
@media(max-width:900px){.u-h{display:none!important}}@media(max-width:600px){.u-a{display:none!important}.util-in{justify-content:flex-end}}
.closed{color:#B3261E}
.hd{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.97);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border-bottom:1px solid var(--ln)}
.hd-in{display:flex;align-items:center;gap:14px;height:76px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;margin-right:auto}.logo img{width:50px;height:50px;border-radius:50%}
.logo b{display:block;font:italic 600 24px 'Playfair Display';line-height:1}.logo small{display:block;color:var(--o);font-size:10px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;margin-top:4px;text-align:center}
.nav{display:none;gap:26px}.nav a{text-decoration:none;font-weight:600;font-size:12.5px;text-transform:uppercase;letter-spacing:.06em;padding:8px 0;border-bottom:2px solid transparent}.nav a:hover,.nav a.on{color:var(--o);border-color:var(--o)}
@media(min-width:1080px){.nav{display:flex}}
.cta{display:none;align-items:center;min-height:42px;padding:0 20px;border-radius:999px;background:var(--o);color:#fff;font:700 12px 'Montserrat';text-transform:uppercase;letter-spacing:.05em;text-decoration:none}
@media(min-width:620px){.cta{display:inline-flex}}
.cartb{position:relative;width:44px;height:44px;border-radius:50%;border:1.5px solid var(--ln);background:#fff;color:var(--k);display:grid;place-items:center;cursor:pointer}
.hero{overflow:hidden}
.hero-in{display:grid;gap:26px;padding-top:34px;padding-bottom:40px;align-items:center}
@media(min-width:920px){.hero-in{grid-template-columns:.95fr 1.05fr;gap:20px;padding-top:40px;padding-bottom:54px}}
.hero h1{font-size:clamp(40px,8.5vw,70px)}
.lead{color:var(--k2);max-width:440px;margin:0 0 26px}
.btns{display:flex;flex-wrap:wrap;gap:12px}
.f3{display:flex;flex-wrap:wrap;gap:16px 28px;margin-top:30px;font-size:12.5px;color:var(--k2);line-height:1.35}
.f3 span{display:flex;align-items:center;gap:10px}.f3 i{width:50px;height:50px;border-radius:50%;border:1px solid var(--ln);display:grid;place-items:center;color:var(--g2);flex:none}.f3 span:nth-child(3) i{color:var(--g)}
.plate{position:relative;width:100%;max-width:600px;justify-self:center}
.pl{aspect-ratio:1;border-radius:50%;padding:20px;background:#fff;box-shadow:0 50px 80px -50px rgba(60,40,20,.55),0 0 0 1px #F2ECE3}
.pl img{width:100%;height:100%;border-radius:50%;object-fit:cover}
.badge{position:absolute;right:2%;top:2%;width:118px;height:118px;border-radius:50%;background:#fff;box-shadow:0 16px 34px -14px rgba(0,0,0,.3);display:grid;place-content:center;justify-items:center;text-align:center;font-size:12.5px;line-height:1.2;z-index:2}.badge b{font:600 34px 'Playfair Display';line-height:1}
@media(max-width:520px){.badge{width:92px;height:92px;font-size:11px}.badge b{font-size:26px}}
.lf{position:absolute;width:26px;height:26px;z-index:2}.lf1{left:6%;top:10%;transform:rotate(-30deg)}.lf2{left:-1%;bottom:22%;transform:rotate(60deg);width:20px}.lf3{right:6%;bottom:8%;transform:rotate(140deg)}.lf4{right:30%;top:-1%;transform:rotate(20deg);width:18px}
.about{border-top:1px solid var(--ln);border-bottom:1px solid var(--ln)}
.ab-in{display:grid;gap:28px;padding-top:40px;padding-bottom:40px;align-items:center}@media(min-width:960px){.ab-in{grid-template-columns:1fr 1fr .52fr;gap:36px}}
.ab-ph{position:relative;border-radius:20px;overflow:visible}.ab-ph img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:20px}
.ab-b{position:absolute;right:12px;bottom:-14px;background:var(--o);color:#fff;border-radius:14px;padding:14px 16px;text-align:center;font-size:12px;line-height:1.3;display:grid;justify-items:center;gap:2px;box-shadow:0 14px 26px -12px rgba(232,100,27,.7)}.ab-b b{font:600 30px 'Playfair Display';line-height:1}
.ab-t h2{font-size:clamp(32px,6vw,46px)}.ab-t p{color:var(--k2)}.sign{font:30px 'Marck Script';color:var(--k)!important;margin:0 0 14px}
.ab-f{list-style:none;padding:0;margin:0;display:grid;gap:18px}.ab-f li{display:flex;align-items:center;gap:14px;font-weight:600;font-size:13.5px;line-height:1.3}
.ab-f i{width:60px;height:60px;border-radius:50%;background:#F8EFE4;display:grid;place-items:center;color:var(--g2);flex:none}
@media(max-width:959px){.ab-f{grid-template-columns:repeat(3,1fr)}.ab-f li{flex-direction:column;text-align:center}}
.sec{padding:52px 16px}.pt0{padding-top:10px}
.orn{font-size:clamp(28px,6vw,42px);text-align:center;display:flex;align-items:center;justify-content:center;gap:14px;margin:0}
.orn::before,.orn::after{content:"";width:40px;height:10px;flex:none;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='10'%3E%3Cpath d='M0 5h30' stroke='%23E8641B' stroke-width='1.5'/%3E%3Ccircle cx='34' cy='5' r='3' fill='none' stroke='%23E8641B' stroke-width='1.5'/%3E%3C/svg%3E")}
.orn::after{transform:scaleX(-1)}.orn.sm{font-size:clamp(24px,5vw,32px)}
.pop-h{display:grid;gap:10px;justify-items:center;margin-bottom:24px}
@media(min-width:900px){.pop-h{grid-template-columns:1fr auto 1fr}.pop-h .orn{grid-column:2}.pop-h .all{grid-column:3;justify-self:end}}
.all{background:none;border:0;font:700 12.5px 'Montserrat';text-transform:uppercase;letter-spacing:.08em;color:var(--k);cursor:pointer;display:inline-flex;gap:8px;align-items:center;padding:8px 0}
.all span{color:var(--o);font-size:18px;transition:transform .2s}.all.is-active span{transform:rotate(90deg)}.all:hover{color:var(--o)}
.dishes{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}@media(min-width:760px){.dishes{grid-template-columns:repeat(3,1fr)}}@media(min-width:1050px){.dishes{grid-template-columns:repeat(4,1fr);gap:22px}}
.ds{border:1px solid var(--ln);border-radius:12px;overflow:hidden;display:flex;flex-direction:column;background:#fff;position:relative;box-shadow:0 14px 30px -26px rgba(60,40,20,.6);transition:box-shadow .2s,transform .2s}
.ds:hover{box-shadow:0 24px 40px -26px rgba(60,40,20,.6);transform:translateY(-3px)}
.ds-ph{aspect-ratio:4/3;background:#F7EEE3}.ds-ph img{width:100%;height:100%;object-fit:cover}.ds-ph .emo{font-size:44px}
.ds-b{padding:13px 14px 15px;display:flex;flex-direction:column;flex:1}.ds h4{font-size:17px;margin:0 0 5px}.ds p{margin:0 0 12px;color:var(--k2);font-size:12.5px;line-height:1.45}
.ds-f{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-top:auto}.ds-f .pr{color:var(--o);font-weight:800;font-size:16px}
.ds .act{width:auto}
.ds .add{width:36px;height:36px;min-height:36px;border-radius:50%;background:var(--g);color:#fff;font:400 24px/1 'Montserrat';padding:0}
.ds .stp{width:108px;min-height:36px;border-radius:999px;padding:2px}.ds .stp button{width:30px;height:30px;border-radius:50%;font-size:16px}
@media(max-width:420px){.ds-f{flex-wrap:wrap}.ds .stp{width:100%}}
.tag{position:absolute;top:10px;left:10px;background:#fff;color:var(--o);font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;padding:4px 8px;border-radius:5px}.t-hit{background:var(--o);color:#fff}
.full{display:grid;grid-template-rows:0fr;transition:grid-template-rows .45s ease}.full.is-open{grid-template-rows:1fr}
.full-in{overflow:hidden}.full.is-open .full-in{padding-top:40px}
.tabs{display:flex;flex-wrap:wrap;justify-content:center;gap:4px 22px;margin:14px 0 22px;border-bottom:1px solid var(--ln)}
.tb{background:none;border:0;border-bottom:2.5px solid transparent;padding:10px 2px;font:600 12.5px 'Montserrat';text-transform:uppercase;letter-spacing:.06em;color:var(--k2);cursor:pointer;margin-bottom:-1px}
.tb:hover{color:var(--k)}.tb.is-active{color:var(--o);border-color:var(--o)}
.mp{display:none}.mp.is-open{display:block;animation:fade .35s}@keyframes fade{from{opacity:0;transform:translateY(8px)}}
.offer{display:grid;gap:12px;padding-top:6px;padding-bottom:6px}@media(min-width:960px){.offer{grid-template-columns:1.55fr .6fr 1fr}}
.of-g{position:relative;background:var(--g);color:#fff;border-radius:12px;padding:26px;overflow:hidden;min-height:240px}
.of-g .kick{color:#F3B183}.of-g h3{font-size:clamp(26px,4.5vw,36px);max-width:60%}.of-s{margin:0 0 18px;opacity:.85;max-width:55%}
@media(max-width:600px){.of-g h3,.of-s{max-width:100%}}
.of-pl{position:absolute;right:-60px;top:50%;transform:translateY(-50%);width:270px;aspect-ratio:1;border-radius:50%;padding:8px;background:#fff;box-shadow:0 20px 40px rgba(0,0,0,.35)}
.of-pl img{width:100%;height:100%;border-radius:50%;object-fit:cover}
@media(max-width:600px){.of-pl{position:relative;right:auto;top:auto;transform:none;width:200px;margin:20px auto -70px}}
.of-d{border-radius:12px;overflow:hidden;min-height:220px}.of-d img{width:100%;height:100%;object-fit:cover}
@media(max-width:959px){.of-d{display:none}}
.of-f{border:1px solid var(--ln);border-radius:12px;padding:22px;display:grid;gap:10px;align-content:start}
.of-f h3{font-size:26px;margin:0 0 4px}
.bf2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.bf{display:flex;align-items:center;gap:8px;border:1px solid var(--ln);border-radius:6px;padding:0 10px;min-height:46px;color:var(--k2)}.bf svg{color:var(--k2);flex:none;width:16px;height:16px}
.bf input,.bf select{border:0;outline:0;background:transparent;font:500 14px 'Montserrat';color:var(--k);width:100%;min-height:44px;min-width:0}
.bf:focus-within{border-color:var(--o)}.bf.bad{border-color:#B3261E}
.chk.sm{font-size:12px;color:var(--k2)}
.bmsg{margin:0;font-size:13px;font-weight:600;color:var(--g)}.bmsg.err{color:#B3261E}
.perks{display:grid;grid-template-columns:repeat(2,1fr);gap:18px 10px;padding-top:28px;padding-bottom:28px;border-bottom:1px solid var(--ln)}
@media(min-width:960px){.perks{grid-template-columns:repeat(4,1fr)}.perks>div+div{border-left:1px solid var(--ln);padding-left:24px}}
.perks>div{display:grid;grid-template-columns:auto 1fr;column-gap:12px;align-items:center}.perks i{grid-row:span 2;color:var(--k)}.perks b{font-size:13.5px}.perks small{color:var(--k2);font-size:12.5px}.perks a{color:inherit}
.gal{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-top:24px}@media(min-width:760px){.gal{grid-template-columns:repeat(3,1fr)}}@media(min-width:1050px){.gal{grid-template-columns:repeat(6,1fr)}}
.gi{border-radius:12px;overflow:hidden;aspect-ratio:1}.gi img{width:100%;height:100%;object-fit:cover;transition:transform .5s}.gi:hover img{transform:scale(1.06)}
.revs{display:grid;gap:16px;margin:24px 0 16px}@media(min-width:860px){.revs{grid-template-columns:repeat(3,1fr)}}
.rv{border:1px solid var(--ln);border-radius:12px;padding:20px;background:#fff}.rv .st{color:var(--o);letter-spacing:2px}.rv p{margin:8px 0 12px;font-size:14.5px}.rv b{font-family:'Playfair Display'}.rv small{color:var(--k2)}
.lnk{color:var(--o);font-weight:700;text-transform:uppercase;font-size:12.5px;letter-spacing:.06em}
.ft{background:var(--sf);border-top:1px solid var(--ln);padding:40px 0 96px;font-size:13.5px}@media(min-width:960px){.ft{padding-bottom:20px}}
.ft-in{display:grid;gap:26px}@media(min-width:700px){.ft-in{grid-template-columns:1fr 1fr}}@media(min-width:1050px){.ft-in{grid-template-columns:1.35fr .8fr .9fr 1.2fr 1.35fr}}
.ft h4{font:700 12.5px 'Montserrat';text-transform:uppercase;letter-spacing:.1em;margin-bottom:12px}
.ft ul{list-style:none;padding:0;margin:0;display:grid;gap:6px}.ft a{text-decoration:none}.ft a:hover{color:var(--o)}.ft p{color:var(--k2);margin:10px 0}
.ci li{display:flex;gap:8px;align-items:flex-start}.ci svg{color:var(--o);flex:none;width:16px;height:16px;margin-top:3px}
.sub{display:flex;gap:0}.sub input{flex:1;min-width:0;border:1px solid var(--ln);border-right:0;border-radius:6px 0 0 6px;padding:0 12px;font:14px 'Montserrat';min-height:46px;background:#fff}.sub input:focus{outline:none;border-color:var(--o)}.sub .btn{border-radius:0 6px 6px 0;padding:0 14px;font-size:11.5px}
.cp{grid-column:1/-1;display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px;color:var(--k2);border-top:1px solid var(--ln);padding-top:16px;font-size:12.5px}
'''
    tpl = '{item:p=>`<article class="ds">' + TAG_JS + '<div class="ds-ph">${UI.thumb(p)}</div><div class="ds-b"><h4>${UI.esc(p.name)}</h4>${p.desc?`<p>${UI.esc(p.desc)}</p>`:""}<div class="ds-f"><span class="pr">${UI.fmt(p.price)}</span>${UI.slot(p.id)}</div></div></article>`,' \
          'review:r=>`<article class="rv"><div class="st">★★★★★</div><p>${UI.esc(r.text)}</p><b>${UI.esc(r.name)}</b> <small>· ${r.date}, Яндекс Карты</small></article>`}'
    after = r'''
window.AFTER = function(){
  const $ = s => document.querySelector(s);
  // Популярные блюда — хиты гостей
  const POP = ['z1','k1','m1','s11'];
  $('#popularGrid').innerHTML = POP.map(id => TPL.item(UI.byId[id])).join('');
  // Ссылки меню в подвале: раскрыть полное меню и нужную вкладку
  document.querySelectorAll('.fm').forEach(a => a.addEventListener('click', e => {
    e.preventDefault();
    const full = $('#fullmenu'); if (!full.classList.contains('is-open')) document.querySelector('[data-open="fullmenu"]').click();
    document.querySelector(`[data-open="m-${a.dataset.g}"]`).click();
    setTimeout(() => full.scrollIntoView({ behavior:'smooth', block:'start' }), 120);
  }));
  // Бронь стола (демо)
  const H = window.DATA.cfg.hours, iso = d => { d = new Date(d); d.setMinutes(d.getMinutes() - d.getTimezoneOffset()); return d.toISOString().slice(0,10); };
  const dIn = $('#bDate'), tIn = $('#bTime');
  dIn.min = iso(new Date()); dIn.value = iso(new Date());
  const fillT = () => { const day = new Date(dIn.value + 'T12:00').getDay(), [o, c] = H[day], today = dIn.value === iso(new Date()), nh = new Date().getHours();
    let r = ''; for (let h = o; h < c - 1; h++) for (const m of ['00','30']) { if (today && h <= nh) continue; r += `<option>${String(h).padStart(2,'0')}:${m}</option>`; }
    tIn.innerHTML = r || '<option value="">На сегодня мест нет — выберите другой день</option>'; };
  fillT(); dIn.addEventListener('change', fillT);
  const ph = $('#bPhone');
  ph.addEventListener('focus', () => { if (!ph.value) ph.value = '+7 '; });
  ph.addEventListener('input', () => { let d = ph.value.replace(/\D/g,''); if (d[0]==='7'||d[0]==='8') d = d.slice(1); if (d.length > 10 && (d[0]==='7'||d[0]==='8')) d = d.slice(1); d = d.slice(0,10); let r = '+7'; if (d.length) r += ' (' + d.slice(0,3); if (d.length >= 3) r += ') ' + d.slice(3,6); if (d.length >= 6) r += '-' + d.slice(6,8); if (d.length >= 8) r += '-' + d.slice(8,10); ph.value = r; });
  $('#bookForm').addEventListener('submit', e => { e.preventDefault(); const m = $('#bMsg');
    const okP = ph.value.replace(/\D/g,'').length === 11; ph.closest('.bf').classList.toggle('bad', !okP);
    if (!okP){ m.className = 'bmsg err'; m.textContent = 'Проверьте номер телефона'; return; }
    if (!tIn.value){ m.className = 'bmsg err'; m.textContent = 'Выберите другой день'; return; }
    if (!$('#bOk').checked){ m.className = 'bmsg err'; m.textContent = 'Нужно согласие на обработку данных'; return; }
    const btn = e.target.querySelector('button[type=submit]'), when = `${dIn.value.split('-').reverse().join('.')} в ${tIn.value}, ${$('#bGuests').value}`;
    if (!window.API_URL){ m.className = 'bmsg'; m.textContent = `Заявка принята: ${when}. Мы перезвоним для подтверждения. (Демо — заявка никуда не отправлена.)`; return; }
    btn.disabled = true; btn.textContent = 'Отправляем…'; m.textContent = '';
    fetch(window.API_URL, { method:'POST', headers:{ 'Content-Type':'text/plain;charset=utf-8' }, body: JSON.stringify({ type:'booking', date:dIn.value, time:tIn.value, guests:$('#bGuests').value, name:$('#bName').value.trim(), phone:ph.value, website:$('#bWeb').value }) })
      .then(r => r.json()).then(j => { if (!j.ok) throw new Error(j.error || 'Ошибка сервера');
        m.className = 'bmsg'; m.textContent = `Заявка ${j.number} принята: ${when}. Мы перезвоним для подтверждения.`; e.target.reset(); dIn.value = iso(new Date()); fillT(); })
      .catch(err => { m.className = 'bmsg err'; m.textContent = `Не получилось отправить (${err.message}). Позвоните нам: ${window.DATA.cfg.phone}`; })
      .finally(() => { btn.disabled = false; btn.textContent = 'Забронировать'; }); });
  $('#subForm').addEventListener('submit', e => { e.preventDefault(); const v = $('#subMail').value.trim(), m = $('#subMsg');
    if (!/^\S+@\S+\.\S+$/.test(v)){ m.className = 'bmsg err'; m.textContent = 'Проверьте e-mail'; return; }
    if (!$('#subOk').checked){ m.className = 'bmsg err'; m.textContent = 'Нужно согласие на обработку данных'; return; }
    m.className = 'bmsg'; m.textContent = 'Спасибо! (Демо — подписка не сохранена.)'; });
};'''
    return dict(file='8-flavoria-polnostyu.html', v='d8', title='Своё бистро — в стиле Flavoria',
                fonts='family=Playfair+Display:ital,wght@0,500;0,600;1,600&family=Marck+Script&family=Montserrat:wght@400;500;600;700;800', css=css, body=body, tpl=tpl, add_label='+', after=after)
D.append(d8)

if __name__ == '__main__':
    import os
    out = '/home/claude/six/out'; os.makedirs(out, exist_ok=True)
    for f in D:
        d = f()
        html = page(d['v'], d['title'], d['fonts'], d['css'], d['body'], d['tpl'], d.get('add_label', '+ В корзину'), d.get('after', ''))
        open(f'{out}/{d["file"]}', 'w', encoding='utf-8').write(html)
        print(d['file'], len(html) // 1024, 'KB')
