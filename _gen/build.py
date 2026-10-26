# -*- coding: utf-8 -*-
"""RallyStat 소개 페이지 11개 언어 + robots.txt + sitemap.xml 생성.

스토어 설명(정의 문장·기능 목록·맺음말)은 앱 저장소의 store/aso/copy_<버전>.<locale>.json을 그대로 읽어
스토어와 같은 주장을 하게 한다. 새 문장(한눈에 보기·질문형 소제목·FAQ)은 l10n.py.
실행: python -I _gen/build.py  (rallystat-web 폴더에서, 앱 저장소는 ../volleyball-coach)
_gen/ 은 밑줄로 시작해 GitHub Pages(Jekyll)가 공개하지 않는다.
"""
import html
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from l10n import L  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.join(os.path.dirname(ROOT), 'volleyball-coach')
BASE = 'https://syninasoft.github.io/rallystat-web/'
TODAY = '2026-10-27'
ASC_ID = '6790425777'
PKG = 'com.syninasoft.volleyballcoach'

# 페이지 순서 = 언어 메뉴 순서. (코드, hreflang, html lang, 스토어 문구 파일, App Store 나라, Play hl, 언어 이름)
LANGS = [
    ('en', 'en', 'en', 'en-US', 'us', 'en', 'English'),
    ('es', 'es', 'es', 'es-ES', 'es', 'es', 'Español'),
    ('pt', 'pt', 'pt-BR', 'pt-BR', 'br', 'pt-BR', 'Português'),
    ('tr', 'tr', 'tr', 'tr', 'tr', 'tr', 'Türkçe'),
    ('fr', 'fr', 'fr', 'fr-FR', 'fr', 'fr', 'Français'),
    ('ja', 'ja', 'ja', 'ja', 'jp', 'ja', '日本語'),
    ('ko', 'ko', 'ko', 'ko', 'kr', 'ko', '한국어'),
    ('de', 'de', 'de', 'de-DE', 'de', 'de', 'Deutsch'),
    ('it', 'it', 'it', 'it', 'it', 'it', 'Italiano'),
    ('pl', 'pl', 'pl', 'pl', 'pl', 'pl', 'Polski'),
    ('ru', 'ru', 'ru', 'ru', 'ru', 'ru', 'Русский'),
]


def page_name(code):
    return 'index.html' if code == 'en' else 'index.%s.html' % code


def url(code):
    return BASE if code == 'en' else BASE + page_name(code)


def esc(s):
    return html.escape(s, quote=True)


def store_copy(locale):
    p = os.path.join(APP, 'store', 'aso', 'copy_1.1.1.%s.json' % locale)
    return json.load(io.open(p, encoding='utf-8'))


def sections(desc):
    """스토어 설명 → (첫 문단, [(제목, [항목])], 맺음말). 6번째 문단(기기·언어 줄)은 쓰지 않는다 — 웹은 Android도 있다."""
    paras = [p.strip() for p in desc.split('\n\n') if p.strip()]
    assert len(paras) == 8, len(paras)
    secs = []
    for p in paras[1:6]:
        lines = p.split('\n')
        items = [x[1:].strip() for x in lines[1:] if x.startswith('•')]
        assert items, p[:40]
        secs.append((lines[0].strip(), items))
    return paras[0], secs, paras[7]


CSS = """
:root{--bg:#F7F8FA;--card:#FFFFFF;--ink:#16233B;--soft:#4A5872;--line:#DDE3EC;--accent:#FFB703;--accentInk:#1B1300;--link:#0B5CAD}
@media (prefers-color-scheme:dark){:root{--bg:#0F1726;--card:#172238;--ink:#EEF2F8;--soft:#AEB9CC;--line:#2A3956;--accent:#FFB703;--accentInk:#1B1300;--link:#8CC4FF}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"Segoe UI",Roboto,"Apple SD Gothic Neo","Malgun Gothic","Hiragino Sans","Noto Sans",sans-serif;line-height:1.65;font-size:17px}
main{max-width:760px;margin:0 auto;padding:28px 16px 64px}
nav.langs{font-size:14px;color:var(--soft);display:flex;flex-wrap:wrap;gap:4px 12px;margin-bottom:24px}
nav.langs a{color:var(--link);text-decoration:none}
nav.langs b{color:var(--ink)}
h1{font-size:30px;line-height:1.25;margin:0 0 12px}
h2{font-size:21px;line-height:1.35;margin:36px 0 10px}
h3{font-size:17px;margin:20px 0 6px}
p.lead{font-size:19px;margin:0 0 20px}
.stores{display:flex;flex-wrap:wrap;gap:10px;margin:20px 0 8px}
.stores a{display:inline-block;padding:12px 18px;border-radius:12px;background:var(--ink);color:var(--bg);text-decoration:none;font-weight:700}
.stores a.play{background:var(--accent);color:var(--accentInk)}
.glance{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:6px 20px 10px}
ul{padding-left:22px;margin:8px 0}
li{margin:4px 0}
.faq dt{font-weight:700;margin-top:16px}
.faq dd{margin:4px 0 0}
footer{margin-top:48px;padding-top:16px;border-top:1px solid var(--line);font-size:14px;color:var(--soft)}
footer a{color:var(--link)}
a{color:var(--link)}
"""


def jsonld(code, t, copy, lead):
    app = {
        '@context': 'https://schema.org',
        '@type': 'SoftwareApplication',
        'name': 'RallyStat',
        'alternateName': sorted({store_copy(lc[3])['title'] for lc in LANGS} | {'랠리스탯'}),
        'description': lead,
        'url': url(code),
        'applicationCategory': 'SportsApplication',
        'operatingSystem': 'iOS, iPadOS, Android',
        'availableOnDevice': 'iPhone, iPad, Android',
        'inLanguage': ['en', 'ko', 'ja', 'it', 'pl', 'tr', 'pt-BR', 'ru', 'fr', 'de', 'es'],
        'downloadUrl': ['https://apps.apple.com/app/id%s' % ASC_ID,
                        'https://play.google.com/store/apps/details?id=%s' % PKG],
        'offers': [
            {'@type': 'Offer', 'name': 'RallyStat', 'price': '0', 'priceCurrency': 'USD'},
            {'@type': 'Offer', 'name': 'RallyStat Pro (one-time purchase)', 'price': '14.99', 'priceCurrency': 'USD'},
        ],
        'publisher': {'@type': 'Organization', 'name': 'SynIna Soft', 'url': 'https://syninasoft.github.io/',
                      'email': 'syninasoft@gmail.com'},
    }
    faq = {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        'inLanguage': LANGS[[x[0] for x in LANGS].index(code)][2],
        'mainEntity': [{'@type': 'Question', 'name': q,
                        'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in t['qa'] + t['faq']],
    }
    dump = lambda o: json.dumps(o, ensure_ascii=False, indent=1).replace('</', '<\\/')
    return ('<script type="application/ld+json">\n%s\n</script>\n<script type="application/ld+json">\n%s\n</script>'
            % (dump(app), dump(faq)))


def render(lc):
    code, hreflang, htmllang, locale, cc, hl, name = lc
    t = L[code]
    copy = store_copy(locale)
    lead, secs, closing = sections(copy['description'])
    alts = '\n'.join('<link rel="alternate" hreflang="%s" href="%s">' % (x[1], url(x[0])) for x in LANGS)
    alts += '\n<link rel="alternate" hreflang="x-default" href="%s">' % BASE
    nav = ' '.join(('<b>%s</b>' % esc(x[6])) if x[0] == code else
                   '<a href="%s" hreflang="%s" lang="%s">%s</a>' % (page_name(x[0]), x[1], x[2], esc(x[6]))
                   for x in LANGS)
    ios = 'https://apps.apple.com/%s/app/id%s' % (cc, ASC_ID)
    play = 'https://play.google.com/store/apps/details?id=%s&hl=%s' % (PKG, hl)
    stores = ('<div class="stores"><a href="%s">%s</a><a class="play" href="%s">%s</a></div>'
              % (esc(ios), esc(t['ios']), esc(play), esc(t['play'])))
    out = []
    out.append('<!doctype html>\n<html lang="%s">\n<head>\n<meta charset="utf-8">' % htmllang)
    out.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    out.append('<title>%s</title>' % esc(t['title']))
    out.append('<meta name="description" content="%s">' % esc(t['meta']))
    out.append('<link rel="canonical" href="%s">' % url(code))
    out.append(alts)
    out.append('<meta property="og:type" content="website">\n<meta property="og:site_name" content="RallyStat">')
    out.append('<meta property="og:title" content="%s">' % esc(t['title']))
    out.append('<meta property="og:description" content="%s">' % esc(t['meta']))
    out.append('<meta property="og:url" content="%s">' % url(code))
    out.append('<meta name="color-scheme" content="light dark">')
    out.append('<style>%s</style>' % CSS.strip())
    out.append(jsonld(code, t, copy, lead))
    out.append('</head>\n<body>\n<main>')
    out.append('<nav class="langs" aria-label="%s">%s</nav>' % (esc(t['langs']), nav))
    out.append('<h1>%s</h1>' % esc(copy['title']))
    out.append('<p class="lead">%s</p>' % esc(lead))
    out.append(stores)
    out.append('<section class="glance"><h2>%s</h2><ul>%s</ul></section>'
               % (esc(t['glance_h']), ''.join('<li>%s</li>' % esc(g) for g in t['glance'])))
    for q, a in t['qa']:
        out.append('<h2>%s</h2>\n<p>%s</p>' % (esc(q), esc(a)))
    out.append('<h2>%s</h2>' % esc(t['features_h']))
    for h, items in secs:
        out.append('<h3>%s</h3>\n<ul>%s</ul>' % (esc(h), ''.join('<li>%s</li>' % esc(i) for i in items)))
    out.append('<h2>%s</h2>\n<dl class="faq">%s</dl>'
               % (esc(t['faq_h']), ''.join('<dt>%s</dt><dd>%s</dd>' % (esc(q), esc(a)) for q, a in t['faq'])))
    out.append('<p>%s</p>' % esc(closing))
    out.append(stores)
    out.append('<footer><a href="support.html">%s</a> · <a href="privacy.html">%s</a> · %s · '
               '<a href="mailto:syninasoft@gmail.com">syninasoft@gmail.com</a></footer>'
               % (esc(t['support']), esc(t['privacy']), esc(t['by'])))
    out.append('</main>\n</body>\n</html>\n')
    return '\n'.join(out)


def sitemap():
    alts = ''.join('\n    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (x[1], url(x[0])) for x in LANGS)
    alts += '\n    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>' % BASE
    urls = ''.join('\n  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>%s\n  </url>' % (url(x[0]), TODAY, alts)
                   for x in LANGS)
    for extra in ('support.html', 'privacy.html'):
        urls += '\n  <url>\n    <loc>%s%s</loc>\n  </url>' % (BASE, extra)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
            '%s\n</urlset>\n' % urls)


def main():
    assert set(L) == {x[0] for x in LANGS}
    for lc in LANGS:
        io.open(os.path.join(ROOT, page_name(lc[0])), 'w', encoding='utf-8', newline='\n').write(render(lc))
    io.open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n').write(sitemap())
    io.open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8', newline='\n').write(
        'User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n' % BASE)
    print('ok', len(LANGS), 'pages')


if __name__ == '__main__':
    main()
