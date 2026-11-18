# -*- coding: utf-8 -*-
"""11-18 웹 문구 정리(재원님 「A로, 본문도 고쳐」 본부장 경유). 원본(스토어 설명 JSON·first_l10n·geo_l10n)은 그대로 두고
웹 페이지에만 덮어쓴다.
- 제목·설명: 후보 A안(title_meta.json, 근거 volleyball-coach/docs/claude/web-title-candidates-2026-11-18.md)
- 본문: '탭 한 번'(one tap) 주장 삭제, em dash·en dash 없애기(공통 규칙 7-1)
fix()는 언어별 교체를 먼저 하고, 남은 ' — '는 쌍점으로 바꾼다. check()는 안 쓰인 교체 항목이 있으면 멈춘다.
"""
import io
import json
import os

_tm = json.load(io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'title_meta.json'), encoding='utf-8'))
TITLE, META = _tm['T'], _tm['M']

R = {
    'en': [
        (': one tap per rally, offline,', ': offline,'),
        ('Record each rally with one tap, and', 'Record each rally as it happens, and'),
        ('easy to read: one tap per rally, and the app', 'easy to read: you record the rally, and the app'),
        ('ONE TAP PER RALLY', 'RECORD EVERY RALLY'),
        ('One tap per rally: the score', 'Record each rally: the score'),
        ('per player — sorted instantly', 'per player, sorted instantly'),
        ('Works fully offline — record in any gym', 'Works fully offline, so you can record in any gym'),
        ('only while turned on — turn sharing off', 'only while turned on. Turn sharing off'),
        ('an iPhone, iPad and Android app for volleyball stats and score keeping', 'a volleyball stats and score keeping app for iOS (iPhone and iPad) and Android'),
        ('the app keeps the score, rotation and player stats for you', 'the app keeps the score and rotation for you, along with player stats'),
        ('Record each rally: the score, rotation and libero update themselves', 'Record each rally: score and rotation update themselves, and so does the libero'),
        ('Recording works offline, with no account and no ads', 'Works offline. No account needed and no ads'),
        ('iPhone, iPad and Android, in 11 languages', 'iOS (iPhone and iPad) and Android, in 11 languages'),
        ('It depends on what you need after the match.', 'That comes down to what you need after the match.'),
        ("works out each player's points, errors and net points right away", "works out each player's points and errors right away, plus net points"),
        ('to cover the match summary, how points were scored, the most frequent errors, player contributions and priorities for practice', 'to cover the match summary and how points were scored, then the most frequent errors and player contributions, ending with priorities for practice'),
        ('With co-recording, a second coach', 'With co-recording a second coach'),
        ('record kills, aces, blocks, digs and errors as they happen', 'record every point as it happens: kills, aces, blocks, digs, errors'),
        ('shows points, errors and net points per player as soon as', "shows each player's points and errors, plus net points, as soon as"),
        ('Kills, aces, blocks, digs and errors', 'Kills, aces, blocks, digs, errors'),
        ('serving order, substitutions and target score per set', 'serving order, substitutions, target score per set'),
        ('Points, errors and net points per player', 'Points, errors, net points per player'),
        ('Filter by team, date range or a single match', 'Filter by team or date range, or pick a single match'),
        ('No account, no sign-up, no ads, no ad tracking', 'No account or sign-up. No ads and no ad tracking'),
        ('Per-set stats, efficiency metric and charts', 'Per-set stats, plus an efficiency metric with charts'),
        ('per set, efficiency, score flow and rotation, no watermark', 'sets, efficiency, score flow, rotation (no watermark)'),
        ('adds unlimited teams, keyboard code entry, per-set stats, efficiency charts and full report PDFs', 'adds unlimited teams and keyboard code entry, plus per-set stats, efficiency charts, full report PDFs'),
        ('Recording, stats and reports all work offline.', 'Recording, stats, reports: all of it works offline.'),
        ('including the starting lineup, serving order and substitutions', 'including the starting lineup and serving order, plus substitutions'),
        ('iPhone, iPad and Android phones and tablets', 'iOS (iPhone and iPad) and Android phones and tablets'),
        ('French, German and Spanish', 'French, German, Spanish'),
        ('Free printable rotation sheets, lineup cards and stat sheet', 'Free printable sheets: rotation sheets, lineup cards, a stat sheet'),
    ],
    'es': [
        ('UN TOQUE POR JUGADA', 'CADA JUGADA REGISTRADA'),
        (': un toque por jugada, sin conexión,', ': sin conexión,'),
        ('Registra cada jugada con un toque y la app', 'Registra cada jugada y la app'),
        ('Un toque por jugada: el marcador', 'Registra cada jugada: el marcador'),
        ('fácil de leer: un toque por jugada y la app', 'fácil de leer: registras la jugada y la app'),
        ('11 idiomas — totalmente', '11 idiomas, totalmente'),
        ('por jugador — ordenados', 'por jugador, ordenados'),
        ('activados — desactiva', 'activados. Desactiva'),
    ],
    'pt': [
        ('UM TOQUE POR RALLY', 'CADA RALLY REGISTRADO'),
        (': um toque por rali, offline,', ': offline,'),
        ('Registre cada rally com um toque e o app', 'Registre cada rally e o app'),
        ('Um toque por rally: placar', 'Registre cada rally: placar'),
        ('fácil de ler: um toque por rally e o app', 'fácil de ler: você registra o rally e o app'),
        ('11 idiomas — totalmente', '11 idiomas, totalmente'),
        ('por jogador — ordenados', 'por jogador, ordenados'),
        ('ativados — desative', 'ativados. Desative'),
    ],
    'tr': [
        (': her ralliye tek dokunuş, çevrimdışı,', ': çevrimdışı,'),
        ('Her ralliyi tek dokunuşla kaydedin;', 'Her ralliyi kaydedin;'),
        ('Her ralliye tek dokunuş: skor', 'Her ralliyi kaydedin: skor'),
        ('tasarlandı: her ralliye tek dokunuş, uygulama', 'tasarlandı: ralliyi kaydedersiniz, uygulama'),
        ('HER RALLİYE TEK DOKUNUŞ', 'HER RALLİ KAYITTA'),
        ('11 dil — tamamen', '11 dil, tamamen'),
        ('net sayılar — anında', 'net sayılar, anında'),
        ('gönderir — paylaşımı', 'gönderir. Paylaşımı'),
        ('izleyin — RallyStat', 'izleyin, RallyStat'),
    ],
    'fr': [
        ('UN TOUCHER PAR ÉCHANGE', 'CHAQUE ÉCHANGE NOTÉ'),
        (': un toucher par échange, hors ligne,', ': hors ligne,'),
        ("Notez chaque échange d'un toucher :", 'Notez chaque échange :'),
        ('Un toucher par échange : le score', 'Chaque échange noté : le score'),
        ("facile à lire : un toucher par échange, et l'application",
         "facile à lire : vous notez l'échange, et l'application"),
        ('11 langues — entièrement', '11 langues, entièrement'),
        ('par joueur — triés', 'par joueur, triés'),
        ('activées — désactivez', 'activées. Désactivez'),
    ],
    'ja': [
        ('1ラリー1タップ、オフライン', 'オフライン'),
        ('ラリーごとにワンタップで記録すれば', 'ラリーごとに記録すれば'),
        ('ラリーごとにワンタップ：', 'ラリーごとに記録：'),
        ('ラリーごとにワンタップ', 'ラリーごとにすぐ記録'),
        ('サーバーへ送信 — 共有を', 'サーバーへ送信します。共有を'),
    ],
    'ko': [
        ('랠리마다 탭 한 번, 오프라인', '오프라인'),
        ('랠리마다 탭 한 번으로 기록하면', '랠리마다 기록하면'),
        ('랠리마다 탭 한 번: ', '랠리마다 기록: '),
        ('랠리마다 탭 한 번', '랠리마다 바로 기록'),
        ('전체 기록 — 양팀을', '전체 기록. 양팀을'),
        ('11개 언어 — 한국어', '11개 언어, 한국어'),
        ('순득점 — 즉시', '순득점, 즉시'),
        ('작동 — 신호', '작동, 신호'),
        ('응원하든 — 랠리스탯이', '응원하든, 랠리스탯이'),
    ],
    'de': [
        (': ein Tipp pro Ballwechsel, offline,', ': offline,'),
        ('Jeden Ballwechsel mit einem Tipp erfassen, und', 'Jeden Ballwechsel erfassen, und'),
        ('Ein Tipp pro Ballwechsel: Spielstand', 'Jeden Ballwechsel erfassen: Spielstand'),
        ('leicht zu lesen sein: ein Tipp pro Ballwechsel, und die App',
         'leicht zu lesen sein: Sie erfassen den Ballwechsel, und die App'),
        ('EIN TIPP PRO BALLWECHSEL', 'JEDEN BALLWECHSEL ERFASSEN'),
        ('11 Sprachen – vollständig', '11 Sprachen, vollständig'),
        ('pro Spieler — sofort', 'pro Spieler, sofort'),
        ('Server — schalte', 'Server. Schalte'),
        ('verfolgst — RallyStat', 'verfolgst: RallyStat'),
    ],
    'it': [
        (': un tocco per azione, offline,', ': offline,'),
        ('Registra ogni scambio con un tocco:', 'Registra ogni scambio:'),
        ('Un tocco per scambio: punteggio', 'Registra ogni scambio: punteggio'),
        ("facile da leggere: un tocco per scambio, e l'app", "facile da leggere: registri lo scambio, e l'app"),
        ('UN TOCCO PER OGNI SCAMBIO', 'OGNI SCAMBIO REGISTRATO'),
        ('11 lingue — completamente', '11 lingue, completamente'),
        ('per giocatore — ordinati', 'per giocatore, ordinati'),
        ('attive — disattiva', 'attive. Disattiva'),
    ],
    'pl': [
        (': jedno dotknięcie na akcję, offline,', ': offline,'),
        ('Zapisuj każdą akcję jednym dotknięciem, a', 'Zapisuj każdą akcję, a'),
        ('Jedno dotknięcie na akcję: wynik', 'Zapis każdej akcji: wynik'),
        ('łatwy w czytaniu: jedno dotknięcie na akcję, a aplikacja', 'łatwy w czytaniu: zapisujesz akcję, a aplikacja'),
        ('JEDNO DOTKNIĘCIE NA AKCJĘ', 'ZAPIS KAŻDEJ AKCJI'),
        ('11 językach — w pełni', '11 językach, w pełni'),
        ('zawodnika — sortowane', 'zawodnika, sortowane'),
        ('włączone — wyłącz', 'włączone. Wyłącz'),
        ('z trybun — RallyStat', 'z trybun, RallyStat'),
    ],
    'ru': [
        ('RallyStat от SynIna Soft — приложение для', 'RallyStat от SynIna Soft является приложением для'),
        (': одно касание на розыгрыш, офлайн,', ': офлайн,'),
        ('Записывайте каждый розыгрыш одним касанием, а', 'Записывайте каждый розыгрыш, а'),
        ('Одно касание на розыгрыш: счёт', 'Запись каждого розыгрыша: счёт'),
        ('читать легко: одно касание на розыгрыш, и приложение', 'читать легко: вы записываете розыгрыш, и приложение'),
        ('ОДНО КАСАНИЕ — ОДИН РОЗЫГРЫШ', 'ЗАПИСЬ КАЖДОГО РОЗЫГРЫША'),
        ('11 языков — полностью', '11 языков, полностью'),
        ('С Pro — полный журнал', 'С Pro доступен полный журнал'),
        ('RallyStat — это веб-приложение?', 'Является ли RallyStat веб-приложением?'),
        ('RallyStat от SynIna Soft — мобильное приложение', 'RallyStat от SynIna Soft является мобильным приложением'),
        ('кнопки — вести', 'кнопки, вести'),
        ('каждого игрока — мгновенная', 'каждого игрока, мгновенная'),
        ('включены, — выключите', 'включены. Выключите'),
        ('(один матч — бесплатно', '(один матч бесплатно'),
        ('(в бесплатной версии — 2 команды)', '(в бесплатной версии 2 команды)'),
        ('с трибуны — RallyStat', 'с трибуны, RallyStat'),
    ],
}
_used = set()


def fix(code, s):
    for i, (a, b) in enumerate(R[code]):
        if a in s:
            s = s.replace(a, b)
            _used.add((code, i))
    sep = '：' if code == 'ja' else (' : ' if code == 'fr' else ': ')
    s = s.replace(' — ', sep).replace(' – ', sep)
    assert '—' not in s and '–' not in s, (code, s)
    return s


def check():
    miss = [(c, R[c][i][0]) for c in R for i in range(len(R[c])) if (c, i) not in _used]
    assert not miss, miss
