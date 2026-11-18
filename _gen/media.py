# -*- coding: utf-8 -*-
"""소개 페이지 이미지(11-18): 기존 스토어 스크린샷·Play 피처 그래픽을 줄여 img/에 둔다. 새로 찍지 않는다.

- 본문 스크린샷: 앱 저장소 스크린샷/최종/<lang>-iphone-0N.png(1290x2796, 캡션 포함) → img/<lang>-shot-N.webp(480px 폭)
  1번(캡션 'one tap')은 쓰지 않는다. 2=함께 기록, 4=통계, 6=로테이션 자동.
- 공유 이미지(og:image): 스크린샷/play/<lang>/feature-graphic.png(1024x500) → img/og-<lang>.jpg
- alt 문장은 스크린샷에 이미 들어간 캡션(store/gen-store-shots.py LOCALES·store/captions_i18n.json)을 그대로 쓴다.
실행: python -I _gen/media.py  (rallystat-web 폴더, 앱 저장소는 ../volleyball-coach). 결과 이미지는 커밋한다.
"""
import io
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.join(os.path.dirname(ROOT), 'volleyball-coach')
OUT = os.path.join(ROOT, 'img')
SHOTS = [2, 4, 6]          # 스크린샷/최종 슬롯 번호
SHOT_W = 480
LANGS = ['en', 'es', 'pt', 'tr', 'fr', 'ja', 'ko', 'de', 'it', 'pl', 'ru']

# 슬롯 → 캡션 키(captions_i18n.json). 최종 순서: 01=s1, 02=공동 기록, 03=s2, 04=s3, 05=s4, 06=s5, 07=s6, 08=맺음
SLOT_KEYS = {2: ('co_main', 'co_sub'), 4: ('s3_main', 's3_sub'), 6: ('s5_main', 's5_sub')}
# en·ko는 gen-store-shots.py LOCALES에 직접 적혀 있음(같은 문장을 옮겨 둔다)
BASE_CAPS = {
    'en': {2: ('Record *together*', "A second device's input merges live"),
           4: ('Stats that tell the *story*', 'Points, errors and player impact'),
           6: ('Rotation & libero, *automatic*', 'Positions, serve and subs tracked')},
    'ko': {2: ('여러 기기로 *함께* 기록', '보조 기기 입력이 실시간으로 합쳐져요'),
           4: ('기록이 쌓이면 *인사이트*가 된다', '득점 구성 · 범실 · 선수 기여'),
           6: ('로테이션·리베로는 *앱이 알아서*', '포지션 · 서브 · 교체 자동 추적')},
}


def captions():
    """{lang: [(slot, alt)]}"""
    i18n = json.load(io.open(os.path.join(APP, 'store', 'captions_i18n.json'), encoding='utf-8'))
    out = {}
    for lang in LANGS:
        rows = []
        for n in SHOTS:
            if lang in BASE_CAPS:
                main, sub = BASE_CAPS[lang][n]
            else:
                km, ks = SLOT_KEYS[n]
                main, sub = i18n[lang][km], i18n[lang][ks]
            main = re.sub(r'\*', '', main).strip()
            if lang == 'ja':  # 일본어 캡션의 줄바꿈용 공백 제거
                main, sub = main.replace(' ', ''), sub.replace(' ', '')
            dot = '。' if lang == 'ja' else '. '
            rows.append((n, 'RallyStat: %s%s%s' % (main, dot, sub.strip())))
        out[lang] = rows
    return out


def build():
    from PIL import Image
    os.makedirs(OUT, exist_ok=True)
    for lang in LANGS:
        for n in SHOTS:
            src = os.path.join(APP, '스크린샷', '최종', '%s-iphone-%02d.png' % (lang, n))
            im = Image.open(src).convert('RGB')
            h = round(im.height * SHOT_W / im.width)
            im.resize((SHOT_W, h), Image.LANCZOS).save(
                os.path.join(OUT, '%s-shot-%d.webp' % (lang, n)), 'WEBP', quality=78, method=6)
        fg = os.path.join(APP, '스크린샷', 'play', lang, 'feature-graphic.png')
        Image.open(fg).convert('RGB').save(os.path.join(OUT, 'og-%s.jpg' % lang), 'JPEG', quality=86,
                                           optimize=True, progressive=True)
    total = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT))
    print('ok', len(os.listdir(OUT)), 'files', total // 1024, 'KB')


if __name__ == '__main__':
    build()
