# Страница-оглавление со ссылками на все варианты (файлы лежат рядом)
V=[('1-shalfey.html','Шалфей','Органика, круглые фото, шалфей и оранжевый. Группы — карточки, меню открывается ниже.','#D4DCC8','#E8742F'),
('2-rvanaya-bumaga.html','Рваная бумага','Мокко, пастельные карточки, «рваные» края, антиква. Группа открывается всплывающим листом.','#A27E7A','#F1CFCB'),
('3-listva.html','Листва','Фото на весь экран, крупная антиква с оранжевой точкой, стеклянные панели с картой. Вкладки.','#F6ECDF','#E2582F'),
('4-yarkiy-pop.html','Яркий поп','Терракота, салатовый, чёрные обводки. Группы — аккордеон из «стикеров».','#D85F44','#C9EA6B'),
('5-grifelnaya-doska.html','Грифельная доска','Меню мелом на доске в деревянной раме, крафт-карточка с адресом. «Показать всё» в каждом разделе.','#24302B','#F3D677'),
('6-bento.html','Бенто','Вся страница — сетка плиток. Плитка группы раскрывается прямо в сетке.','#F3F1EC','#D85F44'),
('8-flavoria-polnostyu.html','Flavoria — полностью','Точно по структуре референса: тарелка в круге, «О нас» с бейджем, популярные блюда + раскрывающееся полное меню, бронь стола, подписка.','#FFFFFF','#2C4A1E'),
('7-belaya-skatert.html','Белая скатерть','Белый, оранжевый и тёмно-зелёный, тарелка в круге, вкладки с подчёркиванием, блок доставки.','#FFFFFF','#E8641B')]
V=sorted(V)
cards=''.join(f'<a class="c" href="{f}"><span class="sw" style="background:linear-gradient(135deg,{a} 0 60%,{b} 60%)"></span><b>{i+1}. {n}</b><span>{d}</span><em>Открыть →</em></a>' for i,(f,n,d,a,b) in enumerate(V))
html=f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Своё бистро — 8 вариантов дизайна</title>
<style>body{{margin:0;background:#F2EFEA;color:#222;font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}}.w{{max-width:1100px;margin:0 auto;padding:28px 16px 40px}}h1{{margin:0 0 6px;font-size:28px}}p.s{{margin:0 0 22px;color:#666}}
.g{{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(250px,1fr))}}.c{{display:flex;flex-direction:column;gap:6px;background:#fff;border-radius:16px;padding:14px;text-decoration:none;color:inherit;box-shadow:0 10px 24px -18px rgba(0,0,0,.5);transition:transform .15s}}.c:hover{{transform:translateY(-3px)}}
.sw{{height:90px;border-radius:10px;border:1px solid #0001}}.c b{{font-size:17px}}.c span:not(.sw){{color:#666;font-size:13.5px}}.c em{{font-style:normal;font-weight:700;color:#C24B31;margin-top:auto}}</style></head>
<body><div class="w"><h1>Своё бистро — 8 вариантов дизайна</h1><p class="s">Компактные одностраничники с меню по группам, корзиной и оформлением заказа. Все файлы должны лежать в одной папке.</p><div class="g">{cards}</div></div></body></html>'''
open('out/0-vse-varianty.html','w',encoding='utf-8').write(html);print('index ok')
