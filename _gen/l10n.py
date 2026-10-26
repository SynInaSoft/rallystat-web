# -*- coding: utf-8 -*-
# 소개 페이지 언어별 문구. 스토어 설명(volleyball-coach/store/aso/copy_*.json)에 없는 새 문장만 여기 둔다.
# 사실 근거: 가격 US$14.99(PostHog pro_purchased 10-13~10-23 APP_STORE 14.99 USD), 무료 팀 2개,
# 라이브 중계·공동 기록 3경기 무료, 키보드 코드 1경기 무료, 6·9인제, 11개 언어(앱 Lang 타입).

L = {}

L['en'] = dict(
    title='RallyStat: volleyball stats app and score keeper for coaches and parents',
    glance_h='RallyStat at a glance',
    qa=[
        ('A volleyball stats app for club and high school coaches',
         'Add your roster once, pick a starting lineup and record kills, aces, blocks, digs and errors as they happen. RallyStat follows the rotation and the libero automatically and shows points, errors and net points per player as soon as the match ends.'),
        ('An offline volleyball scorekeeper for parents in the stands',
         'No signal in the gym? RallyStat records fully offline. Parents can keep the score and stats for their child\'s team, share a one-page match report PDF and, with Pro, let family follow the live score with a code.'),
    ],
    faq_h='Frequently asked questions',
    faq=[
        ('Is RallyStat free?',
         'Yes. The download is free and you can record matches for up to 2 teams. RallyStat Pro is a one-time purchase (US$14.99 in the US; local prices vary) that adds unlimited teams, keyboard code entry, per-set stats, efficiency charts and full report PDFs. Live broadcast and co-recording can be tried free for 3 matches.'),
        ('Does it work without internet?',
         'Yes. Recording, stats and reports all work offline. Only live broadcast and co-recording use the internet, and only while you turn them on.'),
        ('Does RallyStat support 9-player volleyball?',
         'Yes. Both 6-player and 9-player volleyball are supported, including the starting lineup, serving order and substitutions.'),
        ('Do I need an account?',
         'No. There is no sign-up and there are no ads. Your data stays on your device.'),
        ('Which devices and languages are supported?',
         'iPhone, iPad and Android phones and tablets, in 11 languages: English, Korean, Japanese, Italian, Polish, Turkish, Portuguese (Brazil), Russian, French, German and Spanish.'),
    ],
    features_h='Features',
    ios='Download on the App Store', play='Get it on Google Play',
    support='Support', privacy='Privacy policy', langs='Languages', by='Made by SynIna Soft',
    compare='Compare volleyball stats apps',
)

L['ko'] = dict(
    title='랠리스탯: 배구 기록·통계 앱 — 코치·동호회·학부모용 점수 기록',
    glance_h='한눈에 보는 랠리스탯',
    qa=[
        ('동호회·학교 배구부 코치를 위한 배구 기록 앱',
         '선수 명단을 한 번 넣고 선발 라인업을 고른 뒤 공격 득점·서브 에이스·블로킹·디그·범실을 바로 기록합니다. 로테이션과 리베로는 자동으로 따라가고, 경기가 끝나면 선수별 득점·범실·순득점이 바로 나옵니다. 9인제 배구도 그대로 기록합니다.'),
        ('관중석 학부모를 위한 오프라인 배구 점수 기록',
         '체육관에 신호가 없어도 괜찮습니다. 랠리스탯은 완전히 오프라인으로 기록합니다. 학부모는 아이 팀의 점수와 스탯을 기록하고 한 장짜리 경기 리포트 PDF를 나눌 수 있으며, Pro에서는 코드 하나로 가족에게 실시간 점수를 보여 줄 수 있습니다.'),
    ],
    faq_h='자주 묻는 질문',
    faq=[
        ('랠리스탯은 무료인가요?',
         '네. 내려받기는 무료이고 팀 2개까지 경기를 기록할 수 있습니다. 랠리스탯 Pro는 한 번 구매(미국 US$14.99, 나라별 가격 다름)로 팀 무제한, 키보드 코드 입력, 세트별 스탯, 효율 차트, 전체 분석 리포트 PDF를 더합니다. 라이브 중계와 공동 기록은 3경기 무료로 써 볼 수 있습니다.'),
        ('인터넷 없이도 되나요?',
         '네. 기록·스탯·리포트가 모두 오프라인으로 됩니다. 라이브 중계와 공동 기록만 인터넷을 쓰고, 켜 둔 동안에만 씁니다.'),
        ('9인제 배구도 기록할 수 있나요?',
         '네. 9인제와 6인제를 모두 지원합니다. 선발 라인업, 서브 순서(오더지), 선수 교체까지 기록합니다.'),
        ('계정이 필요한가요?',
         '아니요. 가입도 광고도 없습니다. 데이터는 내 기기에 저장됩니다.'),
        ('어떤 기기와 언어를 지원하나요?',
         'iPhone, iPad, Android 폰·태블릿에서 쓸 수 있고, 한국어를 포함한 11개 언어를 지원합니다. 앱 화면과 기록 용어가 모두 한국어로 나옵니다.'),
    ],
    features_h='기능',
    ios='App Store에서 받기', play='Google Play에서 받기',
    support='지원', privacy='개인정보처리방침', langs='언어', by='SynIna Soft 제작',
    compare='배구 기록 앱 비교',
)

L['ja'] = dict(
    title='RallyStat：バレーボール記録・スコアアプリ（6人制・9人制）',
    glance_h='RallyStatの特長',
    qa=[
        ('部活・クラブのコーチ向けバレーボール記録アプリ',
         '選手名簿を一度登録し、スターティングラインアップを選んだら、スパイク決定・サービスエース・ブロック・ディグ・ミスをその場で記録します。ローテーションとリベロは自動で追跡し、試合が終わるとすぐに選手ごとの得点・ミス・純得点が出ます。9人制もそのまま記録できます。'),
        ('観客席の保護者向け、オフラインのスコア記録',
         '体育館で電波が届かなくても大丈夫です。RallyStatは完全オフラインで記録します。保護者はわが子のチームのスコアとスタッツを記録し、1ページの試合レポートPDFを共有できます。Proなら、コードひとつで家族にライブのスコアを見せられます。'),
    ],
    faq_h='よくある質問',
    faq=[
        ('RallyStatは無料ですか？',
         'はい。ダウンロードは無料で、2チームまで試合を記録できます。RallyStat Proは買い切り（米国ではUS$14.99、国により価格は異なります）で、チーム数無制限、キーボードコード入力、セット別スタッツ、効率グラフ、フル分析レポートPDFが加わります。ライブ中継と共同記録は3試合まで無料で試せます。'),
        ('インターネットがなくても使えますか？',
         'はい。記録・スタッツ・レポートはすべてオフラインで使えます。インターネットを使うのはライブ中継と共同記録だけで、オンにしている間だけです。'),
        ('9人制バレーボールに対応していますか？',
         'はい。6人制と9人制の両方に対応し、スターティングラインアップ、サービスオーダー、選手交代まで記録できます。'),
        ('アカウントは必要ですか？',
         'いいえ。登録も広告もありません。データは端末内に保存されます。'),
        ('対応端末と言語は？',
         'iPhone・iPad・Androidのスマホとタブレットで使え、日本語を含む11言語に対応しています。'),
    ],
    features_h='機能',
    ios='App Storeからダウンロード', play='Google Playで手に入れよう',
    support='サポート', privacy='プライバシーポリシー', langs='言語', by='SynIna Soft',
    compare='バレーボール記録アプリの比較',
)

L['de'] = dict(
    title='RallyStat: Volleyball-Statistik-App und Spielprotokoll für Trainer und Eltern',
    glance_h='RallyStat auf einen Blick',
    qa=[
        ('Volleyball-Statistik-App für Vereins- und Schultrainer',
         'Kader einmal anlegen, Startaufstellung wählen und Angriffspunkte, Asse, Blocks, Abwehraktionen und Fehler direkt erfassen. RallyStat verfolgt Rotation und Libero automatisch und zeigt nach dem Spiel sofort Punkte, Fehler und Netto-Punkte pro Spieler.'),
        ('Offline-Spielprotokoll für Eltern auf der Tribüne',
         'Kein Empfang in der Halle? RallyStat zeichnet komplett offline auf. Eltern führen Spielstand und Statistik für das Team ihres Kindes, teilen einen einseitigen Spielbericht als PDF und lassen mit Pro die Familie den Live-Spielstand per Code verfolgen.'),
    ],
    faq_h='Häufige Fragen',
    faq=[
        ('Ist RallyStat kostenlos?',
         'Ja. Der Download ist kostenlos und du kannst Spiele für bis zu 2 Teams aufzeichnen. RallyStat Pro ist ein Einmalkauf (US$14,99 in den USA, Preise je nach Land) und bringt unbegrenzte Teams, Code-Eingabe per Tastatur, Statistiken pro Satz, Effizienz-Diagramme und vollständige PDF-Berichte. Live-Übertragung und gemeinsames Aufzeichnen kannst du 3 Spiele lang kostenlos testen.'),
        ('Funktioniert die App ohne Internet?',
         'Ja. Aufzeichnen, Statistiken und Berichte funktionieren offline. Nur Live-Übertragung und gemeinsames Aufzeichnen nutzen das Internet, und nur solange du sie einschaltest.'),
        ('Unterstützt RallyStat 9er-Volleyball?',
         'Ja. Volleyball mit 6 und mit 9 Spielern wird unterstützt, inklusive Startaufstellung, Aufschlagreihenfolge und Wechseln.'),
        ('Brauche ich ein Konto?',
         'Nein. Keine Anmeldung, keine Werbung. Deine Daten bleiben auf deinem Gerät.'),
        ('Welche Geräte und Sprachen?',
         'iPhone, iPad sowie Android-Smartphones und -Tablets, in 11 Sprachen, darunter Deutsch.'),
    ],
    features_h='Funktionen',
    ios='Laden im App Store', play='Jetzt bei Google Play',
    support='Support', privacy='Datenschutz', langs='Sprachen', by='Von SynIna Soft',
    compare='Volleyball-Statistik-Apps im Vergleich',
)

L['fr'] = dict(
    title='RallyStat : application de statistiques de volley et feuille de match pour entraîneurs et parents',
    glance_h='RallyStat en bref',
    qa=[
        ('Une application de stats de volley pour entraîneurs de club et de lycée',
         'Saisissez votre effectif une fois, choisissez la composition de départ et notez attaques gagnantes, aces, contres, défenses et fautes au fil du jeu. RallyStat suit la rotation et le libéro automatiquement et affiche points, fautes et points nets par joueur dès la fin du match.'),
        ('Une feuille de score de volley hors ligne pour les parents en tribune',
         'Pas de réseau dans le gymnase ? RallyStat enregistre entièrement hors ligne. Les parents tiennent le score et les stats de l\'équipe de leur enfant, partagent un rapport de match PDF d\'une page et, avec Pro, laissent la famille suivre le score en direct avec un code.'),
    ],
    faq_h='Questions fréquentes',
    faq=[
        ('RallyStat est-elle gratuite ?',
         'Oui. Le téléchargement est gratuit et vous pouvez enregistrer des matchs pour 2 équipes. RallyStat Pro est un achat unique (14,99 $ US aux États-Unis ; prix selon le pays) qui ajoute les équipes illimitées, la saisie par codes au clavier, les stats par set, les graphiques d\'efficacité et les rapports PDF complets. Le direct et l\'enregistrement à plusieurs s\'essaient gratuitement sur 3 matchs.'),
        ('Fonctionne-t-elle sans Internet ?',
         'Oui. L\'enregistrement, les stats et les rapports fonctionnent hors ligne. Seuls le direct et l\'enregistrement à plusieurs utilisent Internet, et uniquement lorsque vous les activez.'),
        ('RallyStat gère-t-elle le volley à 9 ?',
         'Oui. Le volley à 6 et à 9 joueurs est pris en charge, avec composition de départ, ordre de service et remplacements.'),
        ('Faut-il un compte ?',
         'Non. Pas d\'inscription, pas de publicité. Vos données restent sur votre appareil.'),
        ('Quels appareils et quelles langues ?',
         'iPhone, iPad et smartphones et tablettes Android, en 11 langues dont le français.'),
    ],
    features_h='Fonctionnalités',
    ios='Télécharger dans l\'App Store', play='Disponible sur Google Play',
    support='Assistance', privacy='Confidentialité', langs='Langues', by='Par SynIna Soft',
    compare='Comparatif des applications de stats de volley',
)

L['it'] = dict(
    title='RallyStat: app per statistiche di pallavolo e segnapunti per allenatori e genitori',
    glance_h='RallyStat in breve',
    qa=[
        ('App di statistiche di pallavolo per allenatori di società e scuola',
         'Inserisci la rosa una volta, scegli la formazione iniziale e registra attacchi vincenti, ace, muri, difese ed errori mentre succedono. RallyStat segue rotazione e libero in automatico e mostra punti, errori e punti netti per giocatore appena finisce la partita.'),
        ('Segnapunti di pallavolo offline per i genitori in tribuna',
         'Niente campo in palestra? RallyStat registra completamente offline. I genitori tengono punteggio e statistiche della squadra del figlio, condividono un referto PDF di una pagina e, con Pro, fanno seguire il punteggio in diretta alla famiglia con un codice.'),
    ],
    faq_h='Domande frequenti',
    faq=[
        ('RallyStat è gratis?',
         'Sì. Il download è gratuito e puoi registrare partite per 2 squadre. RallyStat Pro è un acquisto unico (14,99 USD negli Stati Uniti; prezzi diversi per paese) che aggiunge squadre illimitate, inserimento a codici da tastiera, statistiche per set, grafici di efficienza e report PDF completi. Diretta e registrazione condivisa si provano gratis per 3 partite.'),
        ('Funziona senza Internet?',
         'Sì. Registrazione, statistiche e report funzionano offline. Solo la diretta e la registrazione condivisa usano Internet, e solo mentre le attivi.'),
        ('RallyStat supporta la pallavolo a 9?',
         'Sì. Sono supportate la pallavolo a 6 e a 9 giocatori, con formazione iniziale, ordine di battuta e sostituzioni.'),
        ('Serve un account?',
         'No. Nessuna registrazione e nessuna pubblicità. I dati restano sul tuo dispositivo.'),
        ('Quali dispositivi e lingue?',
         'iPhone, iPad e smartphone e tablet Android, in 11 lingue tra cui l\'italiano.'),
    ],
    features_h='Funzioni',
    ios='Scarica su App Store', play='Disponibile su Google Play',
    support='Assistenza', privacy='Privacy', langs='Lingue', by='Di SynIna Soft',
    compare='Confronto tra app di statistiche di pallavolo',
)

L['es'] = dict(
    title='RallyStat: app de estadísticas de voleibol y marcador para entrenadores y padres',
    glance_h='RallyStat en resumen',
    qa=[
        ('App de estadísticas de voleibol para entrenadores de club y colegio',
         'Carga tu plantilla una vez, elige la alineación inicial y registra remates, aces, bloqueos, defensas y errores en el momento. RallyStat sigue la rotación y el líbero automáticamente y muestra puntos, errores y puntos netos por jugador en cuanto termina el partido.'),
        ('Marcador de voleibol sin conexión para padres en la grada',
         '¿Sin señal en el pabellón? RallyStat registra totalmente sin conexión. Los padres llevan el marcador y las estadísticas del equipo de su hijo, comparten un informe del partido en PDF de una página y, con Pro, la familia sigue el marcador en vivo con un código.'),
    ],
    faq_h='Preguntas frecuentes',
    faq=[
        ('¿RallyStat es gratis?',
         'Sí. La descarga es gratuita y puedes registrar partidos de hasta 2 equipos. RallyStat Pro es un pago único (US$14,99 en EE. UU.; el precio varía según el país) que añade equipos ilimitados, registro con códigos de teclado, estadísticas por set, gráficos de eficiencia e informes PDF completos. La transmisión en vivo y el registro compartido se prueban gratis durante 3 partidos.'),
        ('¿Funciona sin internet?',
         'Sí. El registro, las estadísticas y los informes funcionan sin conexión. Solo la transmisión en vivo y el registro compartido usan internet, y solo mientras los activas.'),
        ('¿RallyStat sirve para voleibol de 9 jugadores?',
         'Sí. Admite voleibol de 6 y de 9 jugadores, con alineación inicial, orden de saque y sustituciones.'),
        ('¿Necesito una cuenta?',
         'No. Sin registro y sin anuncios. Tus datos se quedan en tu dispositivo.'),
        ('¿Qué dispositivos e idiomas admite?',
         'iPhone, iPad y teléfonos y tabletas Android, en 11 idiomas, incluido el español.'),
    ],
    features_h='Funciones',
    ios='Descargar en App Store', play='Disponible en Google Play',
    support='Soporte', privacy='Privacidad', langs='Idiomas', by='De SynIna Soft',
    compare='Comparativa de apps de estadísticas de voleibol',
)

L['pt'] = dict(
    title='RallyStat: app de estatísticas de vôlei e placar para técnicos e pais',
    glance_h='RallyStat em resumo',
    qa=[
        ('App de estatísticas de vôlei para técnicos de clube e escola',
         'Cadastre o elenco uma vez, escolha a escalação inicial e registre ataques, aces, bloqueios, defesas e erros na hora. O RallyStat acompanha o rodízio e o líbero automaticamente e mostra pontos, erros e saldo de pontos por jogador assim que a partida termina.'),
        ('Placar de vôlei offline para pais na arquibancada',
         'Sem sinal no ginásio? O RallyStat registra totalmente offline. Os pais anotam o placar e as estatísticas do time do filho, compartilham um relatório da partida em PDF de uma página e, com o Pro, a família acompanha o placar ao vivo com um código.'),
    ],
    faq_h='Perguntas frequentes',
    faq=[
        ('O RallyStat é grátis?',
         'Sim. O download é grátis e você pode registrar partidas de até 2 times. O RallyStat Pro é um pagamento único (US$14,99 nos EUA; o preço varia por país) que adiciona times ilimitados, registro por códigos no teclado, estatísticas por set, gráficos de eficiência e relatórios PDF completos. A transmissão ao vivo e o registro em conjunto podem ser testados grátis por 3 partidas.'),
        ('Funciona sem internet?',
         'Sim. Registro, estatísticas e relatórios funcionam offline. Só a transmissão ao vivo e o registro em conjunto usam a internet, e só enquanto você os liga.'),
        ('O RallyStat funciona para vôlei de 9 jogadores?',
         'Sim. Vôlei de 6 e de 9 jogadores, com escalação inicial, ordem de saque e substituições.'),
        ('Preciso de uma conta?',
         'Não. Sem cadastro e sem anúncios. Seus dados ficam no seu aparelho.'),
        ('Quais aparelhos e idiomas?',
         'iPhone, iPad e celulares e tablets Android, em 11 idiomas, incluindo português do Brasil.'),
    ],
    features_h='Recursos',
    ios='Baixar na App Store', play='Disponível no Google Play',
    support='Suporte', privacy='Privacidade', langs='Idiomas', by='Feito por SynIna Soft',
    compare='Comparação de apps de estatísticas de vôlei',
)

L['pl'] = dict(
    title='RallyStat: aplikacja do statystyk siatkówki i protokół meczu dla trenerów i rodziców',
    glance_h='RallyStat w skrócie',
    qa=[
        ('Aplikacja do statystyk siatkówki dla trenerów klubowych i szkolnych',
         'Wpisz skład raz, wybierz ustawienie wyjściowe i zapisuj ataki, asy, bloki, obrony i błędy na bieżąco. RallyStat sam śledzi rotację i libero, a po meczu od razu pokazuje punkty, błędy i bilans punktów każdego zawodnika.'),
        ('Protokół siatkówki offline dla rodziców na trybunach',
         'Brak zasięgu w hali? RallyStat zapisuje całkowicie offline. Rodzice prowadzą wynik i statystyki drużyny dziecka, udostępniają jednostronicowy raport z meczu w PDF, a z Pro rodzina śledzi wynik na żywo za pomocą kodu.'),
    ],
    faq_h='Najczęstsze pytania',
    faq=[
        ('Czy RallyStat jest darmowy?',
         'Tak. Pobranie jest darmowe i możesz zapisywać mecze dla 2 drużyn. RallyStat Pro to jednorazowy zakup (14,99 USD w USA; ceny zależą od kraju), który dodaje nieograniczoną liczbę drużyn, wpisywanie kodów z klawiatury, statystyki dla setów, wykresy skuteczności i pełne raporty PDF. Transmisję na żywo i wspólne zapisywanie można wypróbować za darmo przez 3 mecze.'),
        ('Czy działa bez internetu?',
         'Tak. Zapis, statystyki i raporty działają offline. Internetu używają tylko transmisja na żywo i wspólne zapisywanie, i tylko gdy je włączysz.'),
        ('Czy RallyStat obsługuje siatkówkę 9-osobową?',
         'Tak. Obsługuje siatkówkę 6- i 9-osobową, z ustawieniem wyjściowym, kolejnością zagrywki i zmianami.'),
        ('Czy potrzebuję konta?',
         'Nie. Bez rejestracji i bez reklam. Dane zostają na Twoim urządzeniu.'),
        ('Jakie urządzenia i języki?',
         'iPhone, iPad oraz telefony i tablety z Androidem, w 11 językach, w tym po polsku.'),
    ],
    features_h='Funkcje',
    ios='Pobierz w App Store', play='Pobierz z Google Play',
    support='Pomoc', privacy='Prywatność', langs='Języki', by='SynIna Soft',
    compare='Porównanie aplikacji do statystyk siatkówki',
)

L['ru'] = dict(
    title='RallyStat: приложение для статистики волейбола и протокола матча для тренеров и родителей',
    glance_h='RallyStat коротко',
    qa=[
        ('Приложение для статистики волейбола для тренеров клубов и школ',
         'Один раз внесите состав, выберите стартовую расстановку и отмечайте атаки, эйсы, блоки, защиту и ошибки по ходу игры. RallyStat сам следит за переходами и либеро и сразу после матча показывает очки, ошибки и чистые очки каждого игрока.'),
        ('Офлайн-протокол волейбольного матча для родителей на трибуне',
         'Нет связи в зале? RallyStat записывает полностью офлайн. Родители ведут счёт и статистику команды ребёнка, делятся одностраничным отчётом о матче в PDF, а с Pro семья следит за счётом в реальном времени по коду.'),
    ],
    faq_h='Частые вопросы',
    faq=[
        ('RallyStat бесплатный?',
         'Да. Скачивание бесплатное, можно записывать матчи для 2 команд. RallyStat Pro — разовая покупка (14,99 долл. США в США; цена зависит от страны): неограниченное число команд, ввод кодами с клавиатуры, статистика по партиям, графики эффективности и полные PDF-отчёты. Трансляцию и совместную запись можно бесплатно попробовать на 3 матчах.'),
        ('Работает ли без интернета?',
         'Да. Запись, статистика и отчёты работают офлайн. Интернет нужен только для трансляции и совместной записи и только пока они включены.'),
        ('Поддерживается ли волейбол 9 на 9?',
         'Да. Поддерживается волейбол 6 на 6 и 9 на 9, включая стартовую расстановку, порядок подачи и замены.'),
        ('Нужен ли аккаунт?',
         'Нет. Без регистрации и без рекламы. Данные остаются на вашем устройстве.'),
        ('Какие устройства и языки?',
         'iPhone, iPad, а также телефоны и планшеты на Android; 11 языков, включая русский.'),
    ],
    features_h='Возможности',
    ios='Загрузите в App Store', play='Доступно в Google Play',
    support='Поддержка', privacy='Конфиденциальность', langs='Языки', by='SynIna Soft',
    compare='Сравнение приложений для статистики волейбола',
)

L['tr'] = dict(
    title='RallyStat: antrenörler ve veliler için voleybol istatistik ve skor takip uygulaması',
    glance_h='Kısaca RallyStat',
    qa=[
        ('Kulüp ve okul antrenörleri için voleybol istatistik uygulaması',
         'Kadronuzu bir kez girin, başlangıç dizilişini seçin; smaçları, servis aslarını, blokları, savunmaları ve hataları anında kaydedin. RallyStat rotasyonu ve liberoyu otomatik izler, maç biter bitmez oyuncu başına sayıları, hataları ve net sayıları gösterir.'),
        ('Tribündeki veliler için çevrimdışı voleybol skor takibi',
         'Salonda çekmiyor mu? RallyStat tamamen çevrimdışı kayıt tutar. Veliler çocuklarının takımının skorunu ve istatistiklerini tutar, tek sayfalık PDF maç raporunu paylaşır; Pro ile aile canlı skoru bir kodla takip eder.'),
    ],
    faq_h='Sık sorulan sorular',
    faq=[
        ('RallyStat ücretsiz mi?',
         'Evet. İndirmek ücretsizdir ve 2 takıma kadar maç kaydedebilirsiniz. RallyStat Pro tek seferlik bir satın almadır (ABD\'de 14,99 USD; fiyat ülkeye göre değişir) ve sınırsız takım, klavye kodlarıyla giriş, set bazında istatistik, verimlilik grafikleri ve tam PDF raporları ekler. Canlı yayın ve ortak kayıt 3 maç boyunca ücretsiz denenebilir.'),
        ('İnternet olmadan çalışır mı?',
         'Evet. Kayıt, istatistikler ve raporlar çevrimdışı çalışır. İnterneti yalnızca canlı yayın ve ortak kayıt kullanır, o da yalnızca siz açtığınızda.'),
        ('RallyStat 9 kişilik voleybolu destekliyor mu?',
         'Evet. 6 ve 9 kişilik voleybol desteklenir; başlangıç dizilişi, servis sırası ve oyuncu değişiklikleri dahil.'),
        ('Hesap gerekiyor mu?',
         'Hayır. Kayıt yok, reklam yok. Verileriniz cihazınızda kalır.'),
        ('Hangi cihazlar ve diller destekleniyor?',
         'iPhone, iPad ve Android telefon ve tabletler; Türkçe dahil 11 dil.'),
    ],
    features_h='Özellikler',
    ios='App Store\'dan indirin', play='Google Play\'den alın',
    support='Destek', privacy='Gizlilik', langs='Diller', by='SynIna Soft',
    compare='Voleybol istatistik uygulamaları karşılaştırması',
)


# 첫 화면(10-27 총괄 지시): meta·한눈에·질문 단락은 first_l10n.py. 기존 코치·학부모 단락은 그대로 이어 붙인다.
from first_l10n import F  # noqa: E402
for _k, _f in F.items():
    _coach, _parents = L[_k]['qa']
    L[_k].update(meta=_f['meta'], glance=_f['glance'], lead=_f['lead'],
                 qa=_f['qa'] + [(_coach[0], _coach[1] + ' ' + _f['tested']), _parents, _f['codes']])
