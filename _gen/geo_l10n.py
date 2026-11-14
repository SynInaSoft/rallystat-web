# -*- coding: utf-8 -*-
# 11-15 GEO(보고서 dev/reports/2026-11-15_rallystat_GEO.md 제안 2, 재원님 「geo 결정대로」 본부장 경유):
# 이름이 같은 다른 제품(웹 기록 서비스 등)과 구별되게 — 첫 문장에 "RallyStat by SynIna Soft"·모바일 앱,
# FAQ 앞에 "웹앱인가요? → 아니요, 모바일 앱", 비치발리볼(1.3) 문항, 인쇄 양식 링크. 다른 제품 이름은 쓰지 않는다.
# 사실 근거: 비치 문장 = store.config.json 1.3.0 설명("pair·serve order each set·court-switch every 7 points·
# side-out and break rates"). 무료 팀 제한 2(src/lib/pro.tsx FREE_TEAM_LIMIT, teams.length로 셈 — 비치 페어 포함).
# first = 첫 문장을 이 문장으로 바꾼다(뒤 문장은 그대로).

G = {}

G['en'] = dict(
    first='RallyStat by SynIna Soft is an iPhone, iPad and Android app for volleyball stats and score keeping: one tap per rally, offline, no account, pay once.',
    glance69='6-player, 9-player and beach (2-player) volleyball',
    webapp=('Is RallyStat a web app?',
            'No. RallyStat by SynIna Soft is a mobile app on the App Store and Google Play. Recording works offline on your phone or tablet.'),
    beach=('Does RallyStat support beach volleyball?',
           'Yes. Since version 1.3 there is a beach volleyball (2-player) mode: set your pair and serve order each set, get court-switch alerts every 7 points, and track side-out and break rates. A beach pair counts as a team, so the free app covers up to 2 teams or pairs.'),
    print='Free printable rotation sheets, lineup cards and stat sheet (PDF, English)',
)

G['ko'] = dict(
    first='SynIna Soft의 랠리스탯(RallyStat)은 배구 기록·점수 기록용 iPhone·iPad·Android 앱입니다. 랠리마다 탭 한 번, 오프라인, 계정 없음, 한 번 구매.',
    glance69='6인제·9인제·비치발리볼(2인) 모두 지원',
    webapp=('랠리스탯은 웹앱인가요?',
            '아니요. SynIna Soft의 랠리스탯은 App Store와 Google Play에 있는 모바일 앱입니다. 기록은 휴대폰·태블릿에서 오프라인으로 됩니다.'),
    beach=('비치발리볼도 기록할 수 있나요?',
           '네. 1.3 버전부터 비치발리볼(2인) 모드가 있습니다. 세트마다 페어와 서브 순서를 정하고, 합계 7점마다 코트 교대를 알려 주며, 사이드아웃·브레이크 성공률을 기록합니다. 비치 페어도 팀 하나로 세므로 무료로 팀·페어 2개까지 쓸 수 있습니다.'),
    print='무료 인쇄 양식: 로테이션표·라인업 카드·기록지(PDF, 영어)',
)

G['ja'] = dict(
    first='SynIna SoftのRallyStatは、バレーボールの記録・スコア付けのためのiPhone・iPad・Androidアプリです。1ラリー1タップ、オフライン、アカウント不要、買い切り。',
    glance69='6人制・9人制・ビーチバレー（2人制）に対応',
    webapp=('RallyStatはWebアプリですか？',
            'いいえ。SynIna SoftのRallyStatはApp StoreとGoogle Playで配信しているモバイルアプリです。記録はスマートフォンやタブレットでオフラインで行えます。'),
    beach=('ビーチバレーにも対応していますか？',
           'はい。バージョン1.3からビーチバレー（2人制）モードがあります。セットごとにペアとサーブ順を決め、合計7点ごとにコートチェンジをお知らせし、サイドアウト率・ブレイク率を記録します。ビーチのペアも1チームとして数えるため、無料でチーム・ペア合わせて2つまで使えます。'),
    print='無料の印刷用シート：ローテーション表・ラインナップカード・記録用紙（PDF、英語）',
)

G['de'] = dict(
    first='RallyStat von SynIna Soft ist eine App für iPhone, iPad und Android für Volleyball-Statistiken und Spielstand: ein Tipp pro Ballwechsel, offline, ohne Konto, einmal bezahlen.',
    glance69='Volleyball mit 6 und mit 9 Spielern sowie Beachvolleyball (2 Spieler)',
    webapp=('Ist RallyStat eine Web-App?',
            'Nein. RallyStat von SynIna Soft ist eine mobile App im App Store und bei Google Play. Die Aufzeichnung funktioniert offline auf Ihrem Smartphone oder Tablet.'),
    beach=('Unterstützt RallyStat Beachvolleyball?',
           'Ja. Seit Version 1.3 gibt es einen Beachvolleyball-Modus (2 Spieler): Paar und Aufschlagreihenfolge für jeden Satz festlegen, Hinweis zum Seitenwechsel alle 7 Punkte und Side-out- und Break-Quoten. Ein Beach-Paar zählt als Team, die kostenlose App reicht also für bis zu 2 Teams oder Paare.'),
    print='Kostenlose Druckvorlagen: Rotationsbögen, Aufstellungskarten und Statistikbogen (PDF, Englisch)',
)

G['fr'] = dict(
    first='RallyStat de SynIna Soft est une application iPhone, iPad et Android pour les statistiques et le score au volley : un toucher par échange, hors ligne, sans compte, un seul achat.',
    glance69='Volley à 6, à 9 et beach-volley (2 joueurs)',
    webapp=('RallyStat est-elle une application web ?',
            'Non. RallyStat de SynIna Soft est une application mobile disponible sur l\'App Store et Google Play. La saisie fonctionne hors ligne sur votre téléphone ou votre tablette.'),
    beach=('RallyStat gère-t-elle le beach-volley ?',
           'Oui. Depuis la version 1.3, un mode beach-volley (2 joueurs) permet de choisir la paire et l\'ordre de service à chaque set, signale le changement de côté tous les 7 points et suit les taux de side-out et de break. Une paire compte comme une équipe : la version gratuite couvre jusqu\'à 2 équipes ou paires.'),
    print='Fiches gratuites à imprimer : rotations, cartes de composition et feuille de stats (PDF, en anglais)',
)

G['it'] = dict(
    first='RallyStat di SynIna Soft è un\'app per iPhone, iPad e Android per statistiche e punteggio della pallavolo: un tocco per azione, offline, senza account, si paga una volta.',
    glance69='Pallavolo a 6, a 9 e beach volley (2 giocatori)',
    webapp=('RallyStat è un\'app web?',
            'No. RallyStat di SynIna Soft è un\'app per dispositivi mobili su App Store e Google Play. La registrazione funziona offline sul telefono o sul tablet.'),
    beach=('RallyStat supporta il beach volley?',
           'Sì. Dalla versione 1.3 c\'è una modalità beach volley (2 giocatori): scegli la coppia e l\'ordine di battuta a ogni set, ricevi l\'avviso di cambio campo ogni 7 punti e segui le percentuali di side-out e break. Una coppia conta come una squadra, quindi la versione gratuita copre fino a 2 squadre o coppie.'),
    print='Schede gratuite da stampare: rotazioni, cartellini formazione e foglio statistiche (PDF, in inglese)',
)

G['es'] = dict(
    first='RallyStat de SynIna Soft es una app para iPhone, iPad y Android de estadísticas y marcador de voleibol: un toque por jugada, sin conexión, sin cuenta y un solo pago.',
    glance69='Voleibol de 6 y de 9 jugadores y vóley playa (2 jugadores)',
    webapp=('¿RallyStat es una app web?',
            'No. RallyStat de SynIna Soft es una app móvil en App Store y Google Play. El registro funciona sin conexión en tu teléfono o tableta.'),
    beach=('¿RallyStat sirve para vóley playa?',
           'Sí. Desde la versión 1.3 hay un modo de vóley playa (2 jugadores): eliges la pareja y el orden de saque en cada set, recibes el aviso de cambio de campo cada 7 puntos y registras los porcentajes de side-out y break. Una pareja cuenta como un equipo, así que la versión gratuita cubre hasta 2 equipos o parejas.'),
    print='Plantillas gratis para imprimir: rotaciones, tarjetas de alineación y hoja de estadísticas (PDF, en inglés)',
)

G['pt'] = dict(
    first='O RallyStat, da SynIna Soft, é um app para iPhone, iPad e Android de estatísticas e placar de vôlei: um toque por rali, offline, sem conta, pagamento único.',
    glance69='Vôlei de 6 e de 9 jogadores e vôlei de praia (2 jogadores)',
    webapp=('O RallyStat é um app web?',
            'Não. O RallyStat, da SynIna Soft, é um app para celular na App Store e no Google Play. O registro funciona offline no celular ou tablet.'),
    beach=('O RallyStat funciona para vôlei de praia?',
           'Sim. Desde a versão 1.3 há um modo de vôlei de praia (2 jogadores): defina a dupla e a ordem de saque em cada set, receba o aviso de troca de lado a cada 7 pontos e acompanhe as taxas de side-out e break. Uma dupla conta como um time, então a versão gratuita cobre até 2 times ou duplas.'),
    print='Fichas grátis para imprimir: rodízios, cartões de escalação e súmula de estatísticas (PDF, em inglês)',
)

G['pl'] = dict(
    first='RallyStat od SynIna Soft to aplikacja na iPhone\'a, iPada i Androida do statystyk i wyniku w siatkówce: jedno dotknięcie na akcję, offline, bez konta, jednorazowa opłata.',
    glance69='Siatkówka 6- i 9-osobowa oraz plażowa (2 osoby)',
    webapp=('Czy RallyStat to aplikacja webowa?',
            'Nie. RallyStat od SynIna Soft to aplikacja mobilna w App Store i Google Play. Zapis działa offline na telefonie lub tablecie.'),
    beach=('Czy RallyStat obsługuje siatkówkę plażową?',
           'Tak. Od wersji 1.3 jest tryb siatkówki plażowej (2 osoby): ustawiasz parę i kolejność zagrywki w każdym secie, dostajesz przypomnienie o zmianie stron co 7 punktów i śledzisz skuteczność side-outu i breaku. Para liczy się jako drużyna, więc wersja darmowa obejmuje do 2 drużyn lub par.'),
    print='Darmowe arkusze do druku: rotacje, karty ustawień i arkusz statystyk (PDF, po angielsku)',
)

G['ru'] = dict(
    first='RallyStat от SynIna Soft — приложение для iPhone, iPad и Android для статистики и счёта в волейболе: одно касание на розыгрыш, офлайн, без аккаунта, одна покупка.',
    glance69='Волейбол 6×6, 9×9 и пляжный (2×2)',
    webapp=('RallyStat — это веб-приложение?',
            'Нет. RallyStat от SynIna Soft — мобильное приложение в App Store и Google Play. Запись работает офлайн на телефоне или планшете.'),
    beach=('Поддерживается ли пляжный волейбол?',
           'Да. С версии 1.3 есть режим пляжного волейбола (2×2): пара и порядок подачи на каждую партию, напоминание о смене сторон каждые 7 очков, процент сайд-аута и брейка. Пара считается командой, поэтому бесплатная версия охватывает до 2 команд или пар.'),
    print='Бесплатные бланки для печати: расстановки, карточки состава и лист статистики (PDF, на английском)',
)

G['tr'] = dict(
    first='SynIna Soft\'un RallyStat uygulaması, voleybol istatistiği ve skor tutmak için bir iPhone, iPad ve Android uygulamasıdır: her ralliye tek dokunuş, çevrimdışı, hesap yok, tek seferlik ödeme.',
    glance69='6 ve 9 kişilik voleybol ile plaj voleybolu (2 kişilik)',
    webapp=('RallyStat bir web uygulaması mı?',
            'Hayır. SynIna Soft\'un RallyStat\'ı App Store ve Google Play\'de bulunan bir mobil uygulamadır. Kayıt, telefonunuzda veya tabletinizde çevrimdışı çalışır.'),
    beach=('RallyStat plaj voleybolunu destekliyor mu?',
           'Evet. 1.3 sürümünden beri plaj voleybolu (2 kişilik) modu var: her sette ikiliyi ve servis sırasını belirleyin, her 7 sayıda saha değişimi uyarısı alın, side-out ve break oranlarını takip edin. Bir plaj ikilisi bir takım sayılır; ücretsiz sürüm 2 takım veya ikiliye kadar yeterlidir.'),
    print='Ücretsiz yazdırılabilir formlar: rotasyon sayfaları, diziliş kartları ve istatistik sayfası (PDF, İngilizce)',
)
