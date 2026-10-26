# -*- coding: utf-8 -*-
# 소개 페이지 첫 화면(10-27 총괄 지시, 재원님 "전부 추천대로"): 메시지 순서 ① AI 분석 ② 공동 기록 ③ 기본 기능.
# 키보드 코드는 맨 뒤 숙련 기록원용 단락에만. 타사 이름 금지(비교 페이지 링크만), 훈련 일지·소감은 출시 앱에 없어 쓰지 않는다.
# 사실 근거(코드로 확인):
# - AI 분석 요청문 src/lib/aiPrompt.ts: 무료 = 선수×세트·팀×세트 집계, Pro = 원본 로그(3점 이상 연속 실점 구간까지).
#   "데이터에서 직접 세고 주장마다 근거 숫자" 규칙이 요청문에 들어 있다. .txt로 공유해 쓰는 AI 채팅에 붙인다.
# - 공동 기록 app/match/[id].tsx onCorecToggle: 여는 기기는 Pro 또는 3경기 체험. 보조 기기 app/corec/pad.tsx는 Pro 확인 없음
#   (화면으로는 미확인). 둘 다 인터넷(supabase realtime) 필요.
# - 리베로 2명·서브 시도/서브 중 득점: 6baa7f3, 현장 코치 요청으로 고친 예.
# l10n.py가 이 값으로 meta·glance를 바꾸고, qa는 F.qa + (기존 코치 문단 + tested) + 기존 학부모 문단 + codes로 조립한다.

F = {}

F['en'] = dict(
    lead='RallyStat is a volleyball stats app for coaches, team staff and parents. Record each rally with one tap, then turn the match into an AI analysis: how points were won and lost, the most frequent errors and what to work on next, each with the numbers behind it. You can try it free on your own match.',
    meta='RallyStat is a volleyball stats app for coaches and parents on iPhone, iPad and Android. One tap per rally, an AI analysis backed by your numbers, live co-recording, 6- and 9-player, offline, pay once.',
    glance=[
        'AI analysis: findings backed by numbers from the AI chat you already use (free with match totals; Pro adds the rally-by-rally flow)',
        'Co-recording: a second coach records on their own phone and the entries merge live',
        'One tap per rally: the score, rotation and libero update themselves',
        '6-player and 9-player volleyball',
        'Recording works offline, with no account and no ads',
        'Free for up to 2 teams; RallyStat Pro is a one-time purchase, US$14.99 in the US (prices vary by country), no subscription',
        'iPhone, iPad and Android, in 11 languages',
    ],
    qa=[
        ('What is the best volleyball stats app?',
         'It depends on what you need after the match. RallyStat is built to be quick to record and easy to read: one tap per rally, then an AI analysis request that shows where points were won and lost, with the numbers behind each finding. You can try it free on your own match. If you need touch-by-touch scouting of every pass and set, or video analysis, a dedicated scouting tool may suit you better.'),
        ('How does the AI analysis work?',
         'From the Stats tab, RallyStat prepares a ready-to-use analysis request: your match data, what each stat means and the order of the analysis: match summary, how points were scored, the most frequent errors, player contributions and 2 to 3 priorities for practice. It asks the AI to count from the data, back every claim with a number and not to guess. Just share it with the AI chat you use. The free version uses per-player and per-team totals for each set; Pro uses the full rally log, so the analysis can also find runs of three or more points lost in a row.'),
        ('Rallies are fast. Can two people record together?',
         'Yes. Recording alone, you miss things when rallies are fast. With co-recording, a second coach or team manager joins from their own phone with a code or link and the entries merge live, for example one person on the score and one on player stats. The helper phone only needs the free app. The main device can start co-recording free for 3 matches, then with Pro. Both phones need an internet connection while co-recording is on.'),
    ],
    tested='RallyStat has been tested with real school and club match records and improved at coaches\' requests, for example two liberos who swap during a match, and serve stats with attempts and points won on serve.',
    codes=('For experienced scorers: code entry',
           'If you already keep stats with codes, Pro adds keyboard code entry: short codes in the style professional analysts use, such as "11KL", so you can record at rally speed. You can try it free for one match.'),
)

F['ko'] = dict(
    lead='랠리스탯은 코치·팀 스태프·학부모를 위한 배구 기록 앱입니다. 랠리마다 탭 한 번으로 기록하고, 경기가 끝나면 AI 분석으로 무엇으로 득점하고 실점했는지, 가장 잦은 범실과 다음에 보완할 점을 근거 숫자와 함께 받아 볼 수 있습니다. 내 경기로 무료로 체험할 수 있습니다.',
    meta='랠리스탯은 코치·학부모를 위한 배구 기록·통계 앱입니다. 랠리마다 탭 한 번, 근거 숫자와 함께 받는 AI 분석, 실시간 공동 기록, 9인제·6인제, 오프라인, 한 번 구매. iPhone·iPad·Android, 한국어 완전 지원.',
    glance=[
        'AI 분석: 평소 쓰는 AI 채팅에서 근거 숫자와 함께 분석을 받음(무료는 경기 집계, Pro는 랠리 흐름까지)',
        '공동 기록: 두 번째 코치가 자기 폰으로 같이 기록하면 실시간으로 합쳐짐',
        '랠리마다 탭 한 번: 점수·로테이션·리베로가 알아서 바뀜',
        '9인제·6인제 배구 모두 지원',
        '기록은 오프라인으로 작동, 계정·광고 없음',
        '팀 2개까지 무료, 랠리스탯 Pro는 한 번 구매(미국 US$14.99, 나라별 가격 다름), 구독 없음',
        'iPhone·iPad·Android, 11개 언어 — 한국어 완전 지원',
    ],
    qa=[
        ('배구 기록 앱 추천 — 어떤 앱이 좋을까?',
         '경기 뒤에 무엇이 필요한지에 따라 다릅니다. 랠리스탯은 기록은 빠르게, 결과는 읽기 쉽게 만드는 데 집중했습니다. 랠리마다 탭 한 번으로 기록하고, AI 분석 요청문으로 어디서 득점하고 실점했는지를 근거 숫자와 함께 받아 봅니다. 내 경기로 무료로 체험할 수 있습니다. 리시브·토스까지 터치 하나하나를 기록하는 정밀 스카우팅이나 영상 분석이 필요하다면 전문 스카우팅 도구가 더 맞을 수 있습니다.'),
        ('AI 분석은 어떻게 하나요?',
         '통계 탭에서 랠리스탯이 바로 쓸 수 있는 분석 요청문을 만들어 줍니다. 경기 데이터, 기록 항목의 뜻, 분석 순서(경기 요약, 득점 구성, 가장 잦은 범실, 선수 기여, 우선 보완점 2~3개)가 들어 있고, AI에게 데이터에서 직접 세고 주장마다 근거 숫자를 적으며 추측하지 말라고 요청합니다. 평소 쓰는 AI 채팅에 공유하면 됩니다. 무료는 선수별·팀별 세트 집계를, Pro는 랠리 원본 기록을 써서 3점 이상 연속 실점 구간 같은 흐름까지 분석합니다.'),
        ('랠리가 빠른데, 두 사람이 같이 기록할 수 있나요?',
         '네. 혼자 기록하면 빠른 랠리에서 놓치는 게 생깁니다. 공동 기록을 켜면 두 번째 코치나 매니저가 자기 폰에서 코드나 링크로 들어와 함께 기록하고, 입력이 실시간으로 합쳐집니다. 예를 들어 한 명은 점수, 한 명은 선수 스탯을 맡을 수 있습니다. 보조 기기는 무료 앱만 있으면 됩니다. 공동 기록을 여는 기기는 3경기까지 무료로 써 보고, 그 뒤에는 Pro가 필요합니다. 공동 기록을 켠 동안에는 두 기기 모두 인터넷이 필요합니다.'),
    ],
    tested='학교·클럽의 실제 경기 기록으로 시험했고, 현장 코치들의 요청을 받아 고쳐 왔습니다. 경기 중 교대하는 리베로 2명, 서브 시도와 서브권 득점 통계가 그 예입니다.',
    codes=('숙련 기록원을 위한 코드 입력',
           '이미 코드로 기록해 보셨다면 Pro의 키보드 코드 입력을 쓸 수 있습니다. 전문 분석가들이 쓰는 방식의 짧은 코드(예: "11KL")로 랠리 속도에 맞춰 기록합니다. 1경기는 무료로 써 볼 수 있습니다.'),
)

F['ja'] = dict(
    lead='RallyStatは、コーチ・チームスタッフ・保護者のためのバレーボール記録アプリです。ラリーごとにワンタップで記録し、試合後はAI分析で、どこで得点・失点したか、多かったミス、次に直すべき点を根拠の数字つきで受け取れます。自分の試合で無料で試せます。',
    meta='RallyStatは、コーチと保護者のためのバレーボール記録・スコアアプリです。ラリーごとにワンタップ、根拠の数字つきのAI分析、リアルタイムの共同記録、6人制・9人制、オフライン、買い切り。iPhone・iPad・Android対応。',
    glance=[
        'AI分析：ふだん使っているAIチャットで、根拠の数字つきの分析を受け取れる（無料は試合の集計、Proはラリーの流れまで）',
        '共同記録：2人目のコーチが自分のスマホで一緒に記録し、リアルタイムで合流',
        'ラリーごとにワンタップ：スコア・ローテーション・リベロは自動で更新',
        '6人制・9人制の両方に対応',
        '記録はオフラインで動作、アカウント・広告なし',
        '2チームまで無料。RallyStat Proは買い切り（米国ではUS$14.99、国により価格は異なります）、サブスクなし',
        'iPhone・iPad・Android、11言語 — 日本語に完全対応',
    ],
    qa=[
        ('おすすめのバレーボール記録アプリは？',
         '試合後に何が欲しいかで変わります。RallyStatは「記録は速く、結果は読みやすく」を目指しました。ラリーごとにワンタップで記録し、AI分析の依頼文で、どこで得点・失点したかを根拠の数字つきで確認できます。自分の試合で無料で試せます。レセプションやトスまで1本ずつ記録する精密なスカウティングや映像分析が必要なら、専用のスカウティングツールのほうが合うかもしれません。'),
        ('AI分析はどう使うの？',
         'スタッツタブから、RallyStatがそのまま使える分析の依頼文を作ります。試合データ、各記録項目の意味、分析の順序（試合のまとめ、得点の内訳、多かったミス、選手の貢献、優先して直す点2〜3個）が入っていて、AIにはデータから直接数え、主張ごとに根拠の数字を書き、推測しないよう求めます。ふだん使っているAIチャットに共有するだけです。無料版は選手別・チーム別のセット集計を、Proはラリーの元記録を使うので、3点以上の連続失点のような流れまで分析できます。'),
        ('ラリーが速くて追いつけない。2人で記録できる？',
         'できます。ひとりで記録すると、速いラリーで取りこぼしが出ます。共同記録をオンにすると、2人目のコーチやマネージャーが自分のスマホからコードかリンクで参加し、入力がリアルタイムで合流します。たとえば1人がスコア、もう1人が選手のスタッツを担当できます。補助の端末は無料アプリだけで参加できます。共同記録を開く端末は3試合まで無料で試せて、その後はProが必要です。共同記録中は両方の端末にインターネット接続が必要です。'),
    ],
    tested='学校やクラブの実際の試合記録で試し、現場のコーチの要望を受けて改良してきました。試合中に交代するリベロ2人、サーブ本数とサーブ時の得点のスタッツがその例です。',
    codes=('記録に慣れた方へ：コード入力',
           'コードで記録した経験があれば、Proのキーボードコード入力が使えます。プロのアナリストが使う方式の短いコード（例：「11KL」）で、ラリーの速さに合わせて記録できます。1試合は無料で試せます。'),
)

F['de'] = dict(
    lead='RallyStat ist eine Volleyball-Statistik-App für Trainer, Teambetreuer und Eltern. Jeden Ballwechsel mit einem Tipp erfassen und nach dem Spiel eine KI-Analyse erhalten: womit Punkte gewonnen und verloren wurden, die häufigsten Fehler und was als Nächstes zu verbessern ist, jeweils mit den Zahlen dazu. Mit dem eigenen Spiel kostenlos ausprobieren.',
    meta='RallyStat ist eine Volleyball-Statistik-App für Trainer und Eltern auf iPhone, iPad und Android. Ein Tipp pro Ballwechsel, KI-Analyse mit belegenden Zahlen, gemeinsames Erfassen in Echtzeit, offline, einmal zahlen.',
    glance=[
        'KI-Analyse: Ergebnisse mit belegenden Zahlen aus dem KI-Chat, den Sie schon nutzen (kostenlos mit Spielsummen; Pro zusätzlich mit dem Verlauf Ballwechsel für Ballwechsel)',
        'Gemeinsam erfassen: Ein zweiter Trainer erfasst auf dem eigenen Handy mit, alles wird live zusammengeführt',
        'Ein Tipp pro Ballwechsel: Spielstand, Rotation und Libero aktualisieren sich selbst',
        'Volleyball mit 6 und mit 9 Spielern',
        'Erfassen funktioniert offline, ohne Konto und ohne Werbung',
        'Kostenlos für bis zu 2 Teams; RallyStat Pro ist ein Einmalkauf, 14,99 US$ in den USA (Preise je nach Land), kein Abo',
        'iPhone, iPad und Android, in 11 Sprachen – vollständig auf Deutsch',
    ],
    qa=[
        ('Welche Volleyball-Statistik-App ist die beste?',
         'Das hängt davon ab, was Sie nach dem Spiel brauchen. RallyStat soll schnell zu erfassen und leicht zu lesen sein: ein Tipp pro Ballwechsel, danach eine KI-Analyse-Anfrage, die zeigt, wo Punkte gewonnen und verloren wurden, mit den Zahlen dazu. Mit dem eigenen Spiel kostenlos ausprobieren. Wer jede Ballberührung scouten oder Videos analysieren will, ist mit einem spezialisierten Scouting-Tool besser bedient.'),
        ('Wie funktioniert die KI-Analyse?',
         'Im Statistik-Tab erstellt RallyStat eine fertige Analyse-Anfrage: Ihre Spieldaten, die Bedeutung jeder Statistik und die Reihenfolge der Auswertung: Spielzusammenfassung, Punkteverteilung, häufigste Fehler, Beiträge der Spieler und 2 bis 3 Schwerpunkte fürs Training. Die KI wird gebeten, direkt aus den Daten zu zählen, jede Aussage mit einer Zahl zu belegen und nichts zu raten. Teilen Sie sie einfach mit dem KI-Chat, den Sie nutzen. Die kostenlose Version nutzt Summen pro Spieler und Team je Satz; Pro nutzt das vollständige Ballwechsel-Protokoll und findet so auch Serien von drei oder mehr verlorenen Punkten in Folge.'),
        ('Die Ballwechsel sind schnell. Können zwei Personen gemeinsam erfassen?',
         'Ja. Wer allein erfasst, verpasst bei schnellen Ballwechseln etwas. Beim gemeinsamen Erfassen tritt ein zweiter Trainer oder Teambetreuer mit Code oder Link vom eigenen Handy bei, und die Eingaben werden live zusammengeführt, zum Beispiel eine Person für den Spielstand und eine für die Spielerstatistik. Das Helfer-Handy braucht nur die kostenlose App. Das Hauptgerät kann das gemeinsame Erfassen 3 Spiele lang kostenlos starten, danach mit Pro. Solange es eingeschaltet ist, brauchen beide Handys eine Internetverbindung.'),
    ],
    tested='RallyStat wurde mit echten Spielaufzeichnungen aus Schule und Verein getestet und auf Wunsch von Trainern verbessert, etwa um zwei Liberos, die während des Spiels wechseln, und um Aufschlagstatistiken mit Versuchen und Punkten bei eigenem Aufschlag.',
    codes=('Für erfahrene Statistiker: Code-Eingabe',
           'Wenn Sie schon mit Codes erfassen, bietet Pro die Tastatur-Code-Eingabe: kurze Codes nach der Art professioneller Analysten, etwa „11KL“, damit Sie im Tempo der Ballwechsel erfassen. Ein Spiel lang kostenlos ausprobieren.'),
)

F['fr'] = dict(
    lead='RallyStat est une application de statistiques de volley pour entraîneurs, staff et parents. Notez chaque échange d\'un toucher, puis obtenez après le match une analyse par IA : comment les points ont été gagnés et perdus, les fautes les plus fréquentes et quoi travailler ensuite, chiffres à l\'appui. Essayez-la gratuitement sur votre propre match.',
    meta='RallyStat est une application de stats de volley pour entraîneurs et parents sur iPhone, iPad et Android. Un toucher par échange, analyse par IA chiffres à l\'appui, saisie à plusieurs en direct, hors ligne, achat unique.',
    glance=[
        'Analyse par IA : des conclusions chiffrées depuis le chat d\'IA que vous utilisez déjà (gratuit avec les totaux du match ; Pro ajoute le déroulé échange par échange)',
        'Saisie à plusieurs : un deuxième entraîneur saisit sur son propre téléphone et tout se fusionne en direct',
        'Un toucher par échange : le score, la rotation et le libéro se mettent à jour seuls',
        'Volley à 6 et à 9',
        'La saisie fonctionne hors ligne, sans compte ni publicité',
        'Gratuit jusqu\'à 2 équipes ; RallyStat Pro est un achat unique, 14,99 US$ aux États-Unis (prix selon le pays), sans abonnement',
        'iPhone, iPad et Android, en 11 langues — entièrement en français',
    ],
    qa=[
        ('Quelle est la meilleure application de stats de volley ?',
         'Cela dépend de ce dont vous avez besoin après le match. RallyStat veut être rapide à saisir et facile à lire : un toucher par échange, puis une demande d\'analyse par IA qui montre où les points ont été gagnés et perdus, chiffres à l\'appui. Essayez-la gratuitement sur votre propre match. Pour un scouting touche par touche ou l\'analyse vidéo, un outil de scouting dédié vous conviendra mieux.'),
        ('Comment fonctionne l\'analyse par IA ?',
         'Depuis l\'onglet Stats, RallyStat prépare une demande d\'analyse prête à l\'emploi : les données du match, la signification de chaque stat et l\'ordre de l\'analyse : résumé du match, répartition des points, fautes les plus fréquentes, contribution des joueurs et 2 à 3 priorités d\'entraînement. Elle demande à l\'IA de compter à partir des données, de chiffrer chaque affirmation et de ne rien supposer. Partagez-la simplement avec le chat d\'IA que vous utilisez. La version gratuite utilise les totaux par joueur et par équipe pour chaque set ; Pro utilise le journal complet des échanges et repère aussi les séries de trois points perdus ou plus.'),
        ('Les échanges vont vite. Peut-on noter à deux ?',
         'Oui. Seul, on rate des actions quand les échanges vont vite. Avec la saisie à plusieurs, un deuxième entraîneur ou un responsable d\'équipe rejoint le match depuis son téléphone avec un code ou un lien, et les saisies se fusionnent en direct : par exemple l\'un tient le score, l\'autre les stats des joueurs. Le téléphone d\'appoint n\'a besoin que de l\'application gratuite. L\'appareil principal peut lancer la saisie à plusieurs gratuitement pendant 3 matchs, puis avec Pro. Les deux téléphones doivent être connectés à Internet tant qu\'elle est activée.'),
    ],
    tested='RallyStat a été testée sur de vrais relevés de matchs scolaires et de club, et améliorée à la demande d\'entraîneurs : par exemple deux libéros qui alternent pendant le match, et des stats de service avec les tentatives et les points marqués au service.',
    codes=('Pour les statisticiens expérimentés : saisie par codes',
           'Si vous notez déjà avec des codes, Pro ajoute la saisie par codes au clavier : des codes courts, à la manière des analystes professionnels, comme « 11KL », pour suivre le rythme des échanges. Essai gratuit sur un match.'),
)

F['it'] = dict(
    lead='RallyStat è un\'app di statistiche di pallavolo per allenatori, staff e genitori. Registra ogni scambio con un tocco e, a fine partita, ottieni un\'analisi con l\'IA: come sono stati vinti e persi i punti, gli errori più frequenti e su cosa lavorare, con i numeri a supporto. Provala gratis sulla tua partita.',
    meta='RallyStat è un\'app di statistiche di pallavolo per allenatori e genitori su iPhone, iPad e Android. Un tocco per scambio, analisi con l\'IA supportata dai numeri, registrazione condivisa in tempo reale, offline, acquisto unico.',
    glance=[
        'Analisi con l\'IA: risultati supportati dai numeri dalla chat IA che usi già (gratis con i totali della partita; Pro aggiunge l\'andamento scambio per scambio)',
        'Registrazione condivisa: un secondo allenatore registra dal proprio telefono e tutto si unisce in tempo reale',
        'Un tocco per scambio: punteggio, rotazione e libero si aggiornano da soli',
        'Pallavolo a 6 e a 9',
        'La registrazione funziona offline, senza account e senza pubblicità',
        'Gratis fino a 2 squadre; RallyStat Pro è un acquisto unico, 14,99 US$ negli Stati Uniti (prezzi diversi per paese), nessun abbonamento',
        'iPhone, iPad e Android, in 11 lingue — completamente in italiano',
    ],
    qa=[
        ('Qual è la migliore app di statistiche di pallavolo?',
         'Dipende da cosa ti serve dopo la partita. RallyStat punta a essere veloce da registrare e facile da leggere: un tocco per scambio, poi una richiesta di analisi per l\'IA che mostra dove sono stati vinti e persi i punti, con i numeri a supporto. Provala gratis sulla tua partita. Se ti serve lo scouting tocco per tocco o l\'analisi video, uno strumento di scouting dedicato può essere più adatto.'),
        ('Come funziona l\'analisi con l\'IA?',
         'Dalla scheda Statistiche, RallyStat prepara una richiesta di analisi pronta all\'uso: i dati della partita, il significato di ogni statistica e l\'ordine dell\'analisi: riepilogo, composizione dei punti, errori più frequenti, contributo dei giocatori e 2 o 3 priorità di allenamento. Chiede all\'IA di contare dai dati, di indicare un numero per ogni affermazione e di non tirare a indovinare. Basta condividerla con la chat IA che usi. La versione gratuita usa i totali per giocatore e per squadra di ogni set; Pro usa il registro completo degli scambi e trova anche le serie di tre o più punti persi di fila.'),
        ('Gli scambi sono veloci. Si può registrare in due?',
         'Sì. Da soli, negli scambi veloci qualcosa sfugge. Con la registrazione condivisa, un secondo allenatore o un dirigente entra dal proprio telefono con un codice o un link e gli inserimenti si uniscono in tempo reale: per esempio uno segue il punteggio e l\'altro le statistiche dei giocatori. Al telefono di supporto basta l\'app gratuita. Il dispositivo principale può avviare la registrazione condivisa gratis per 3 partite, poi con Pro. Finché è attiva, entrambi i telefoni devono essere connessi a Internet.'),
    ],
    tested='RallyStat è stata provata con registrazioni reali di partite scolastiche e di società e migliorata su richiesta degli allenatori: per esempio due liberi che si alternano durante la partita e le statistiche di battuta, con tentativi e punti fatti in battuta.',
    codes=('Per gli statistici esperti: inserimento a codici',
           'Se registri già con i codici, Pro aggiunge l\'inserimento a codici da tastiera: codici brevi, nello stile usato dagli analisti professionisti, come "11KL", per registrare alla velocità dello scambio. Provalo gratis per una partita.'),
)

F['es'] = dict(
    lead='RallyStat es una app de estadísticas de voleibol para entrenadores, cuerpo técnico y padres. Registra cada jugada con un toque y, al terminar el partido, obtén un análisis con IA: cómo se ganaron y perdieron los puntos, los errores más frecuentes y qué trabajar después, con los números que lo respaldan. Pruébala gratis con tu propio partido.',
    meta='RallyStat es una app de estadísticas de voleibol para entrenadores y padres en iPhone, iPad y Android. Un toque por jugada, análisis con IA respaldado por números, registro compartido en vivo, sin conexión, pago único.',
    glance=[
        'Análisis con IA: conclusiones respaldadas por números desde el chat de IA que ya usas (gratis con los totales del partido; Pro añade el desarrollo jugada a jugada)',
        'Registro compartido: un segundo entrenador registra desde su propio teléfono y todo se une en vivo',
        'Un toque por jugada: el marcador, la rotación y el líbero se actualizan solos',
        'Voleibol de 6 y de 9 jugadores',
        'El registro funciona sin conexión, sin cuenta y sin anuncios',
        'Gratis hasta 2 equipos; RallyStat Pro es un pago único, US$14,99 en EE. UU. (el precio varía según el país), sin suscripción',
        'iPhone, iPad y Android, en 11 idiomas — totalmente en español',
    ],
    qa=[
        ('¿Cuál es la mejor app de estadísticas de voleibol?',
         'Depende de lo que necesites después del partido. RallyStat busca ser rápida de registrar y fácil de leer: un toque por jugada y luego una solicitud de análisis para la IA que muestra dónde se ganaron y perdieron los puntos, con los números que lo respaldan. Pruébala gratis con tu propio partido. Si necesitas scouting toque a toque o análisis de vídeo, una herramienta de scouting específica puede encajarte mejor.'),
        ('¿Cómo funciona el análisis con IA?',
         'Desde la pestaña de estadísticas, RallyStat prepara una solicitud de análisis lista para usar: los datos del partido, qué significa cada estadística y el orden del análisis: resumen del partido, cómo se lograron los puntos, errores más frecuentes, aporte de cada jugador y 2 o 3 prioridades para entrenar. Pide a la IA que cuente a partir de los datos, respalde cada afirmación con un número y no suponga nada. Solo compártela con el chat de IA que uses. La versión gratuita usa los totales por jugador y por equipo de cada set; Pro usa el registro completo de jugadas, así que también detecta rachas de tres o más puntos perdidos seguidos.'),
        ('Las jugadas son rápidas. ¿Pueden registrar dos personas a la vez?',
         'Sí. Quien registra solo pierde acciones cuando las jugadas van rápido. Con el registro compartido, un segundo entrenador o delegado se une desde su propio teléfono con un código o un enlace, y las entradas se combinan en vivo: por ejemplo, uno lleva el marcador y otro las estadísticas de los jugadores. El teléfono de apoyo solo necesita la app gratuita. El dispositivo principal puede iniciar el registro compartido gratis durante 3 partidos y después con Pro. Mientras está activo, ambos teléfonos necesitan conexión a internet.'),
    ],
    tested='RallyStat se probó con registros reales de partidos escolares y de club y se mejoró a petición de entrenadores: por ejemplo, dos líberos que se alternan durante el partido y estadísticas de saque, con intentos y puntos ganados con el saque propio.',
    codes=('Para estadísticos con experiencia: entrada por códigos',
           'Si ya registras con códigos, Pro añade la entrada por códigos con teclado: códigos cortos al estilo de los analistas profesionales, como "11KL", para registrar al ritmo de la jugada. Pruébala gratis durante un partido.'),
)

F['pt'] = dict(
    lead='O RallyStat é um app de estatísticas de vôlei para técnicos, comissão técnica e pais. Registre cada rally com um toque e, depois da partida, receba uma análise com IA: como os pontos foram ganhos e perdidos, os erros mais frequentes e o que treinar a seguir, com os números que comprovam. Experimente grátis com a sua própria partida.',
    meta='O RallyStat é um app de estatísticas de vôlei para técnicos e pais no iPhone, iPad e Android. Um toque por rally, análise com IA baseada em números, registro compartilhado ao vivo, offline, pagamento único.',
    glance=[
        'Análise com IA: conclusões baseadas em números no chat de IA que você já usa (grátis com os totais da partida; o Pro acrescenta o andamento rally a rally)',
        'Registro compartilhado: um segundo técnico registra no próprio celular e tudo se junta ao vivo',
        'Um toque por rally: placar, rodízio e líbero se atualizam sozinhos',
        'Vôlei de 6 e de 9 jogadores',
        'O registro funciona offline, sem conta e sem anúncios',
        'Grátis para até 2 times; o RallyStat Pro é pagamento único, US$ 14,99 nos EUA (preço varia por país), sem assinatura',
        'iPhone, iPad e Android, em 11 idiomas — totalmente em português',
    ],
    qa=[
        ('Qual é o melhor app de estatísticas de vôlei?',
         'Depende do que você precisa depois da partida. O RallyStat quer ser rápido de registrar e fácil de ler: um toque por rally e depois um pedido de análise para a IA que mostra onde os pontos foram ganhos e perdidos, com os números que comprovam. Experimente grátis com a sua própria partida. Se você precisa de scout toque a toque ou análise de vídeo, uma ferramenta de scout dedicada pode ser melhor.'),
        ('Como funciona a análise com IA?',
         'Na aba de estatísticas, o RallyStat prepara um pedido de análise pronto para usar: os dados da partida, o significado de cada estatística e a ordem da análise: resumo da partida, composição dos pontos, erros mais frequentes, contribuição dos jogadores e 2 a 3 prioridades de treino. Ele pede que a IA conte a partir dos dados, mostre um número para cada afirmação e não chute nada. É só compartilhar com o chat de IA que você usa. A versão grátis usa os totais por jogador e por time em cada set; o Pro usa o registro completo dos rallies e também encontra sequências de três ou mais pontos perdidos seguidos.'),
        ('Os rallies são rápidos. Duas pessoas podem registrar juntas?',
         'Sim. Quem registra sozinho perde lances quando o rally é rápido. Com o registro compartilhado, um segundo técnico ou auxiliar entra pelo próprio celular com um código ou link, e os registros se juntam ao vivo: por exemplo, um cuida do placar e o outro das estatísticas dos jogadores. O celular de apoio só precisa do app grátis. O aparelho principal pode iniciar o registro compartilhado grátis por 3 partidas e depois com o Pro. Enquanto estiver ligado, os dois celulares precisam de internet.'),
    ],
    tested='O RallyStat foi testado com registros reais de partidas de escola e de clube e melhorado a pedido de técnicos: por exemplo, dois líberos que se revezam durante a partida e estatísticas de saque, com tentativas e pontos feitos no próprio saque.',
    codes=('Para estatísticos experientes: registro por códigos',
           'Se você já registra com códigos, o Pro traz o registro por códigos no teclado: códigos curtos no estilo usado por analistas profissionais, como "11KL", para registrar no ritmo do rally. Experimente grátis em uma partida.'),
)

F['pl'] = dict(
    lead='RallyStat to aplikacja do statystyk siatkówki dla trenerów, sztabu i rodziców. Zapisuj każdą akcję jednym dotknięciem, a po meczu otrzymaj analizę AI: jak zdobywano i tracono punkty, najczęstsze błędy i nad czym pracować dalej, z liczbami na poparcie. Wypróbuj za darmo na własnym meczu.',
    meta='RallyStat to aplikacja do statystyk siatkówki dla trenerów i rodziców na iPhone, iPad i Android. Jedno dotknięcie na akcję, analiza AI poparta liczbami, wspólny zapis na żywo, offline, jednorazowy zakup.',
    glance=[
        'Analiza AI: wnioski poparte liczbami z czatu AI, którego już używasz (za darmo na podstawie sum meczu; Pro dodaje przebieg akcja po akcji)',
        'Wspólny zapis: drugi trener zapisuje na własnym telefonie, a wszystko łączy się na żywo',
        'Jedno dotknięcie na akcję: wynik, rotacja i libero aktualizują się same',
        'Siatkówka 6- i 9-osobowa',
        'Zapis działa offline, bez konta i bez reklam',
        'Za darmo do 2 drużyn; RallyStat Pro to jednorazowy zakup, 14,99 USD w USA (ceny zależą od kraju), bez subskrypcji',
        'iPhone, iPad i Android, w 11 językach — w pełni po polsku',
    ],
    qa=[
        ('Jaka jest najlepsza aplikacja do statystyk siatkówki?',
         'To zależy od tego, czego potrzebujesz po meczu. RallyStat ma być szybki w zapisie i łatwy w czytaniu: jedno dotknięcie na akcję, a potem prośba o analizę dla AI, która pokazuje, gdzie zdobyto i stracono punkty, z liczbami na poparcie. Wypróbuj za darmo na własnym meczu. Jeśli potrzebujesz scoutingu każdego dotknięcia albo analizy wideo, lepiej sprawdzi się wyspecjalizowane narzędzie do scoutingu.'),
        ('Jak działa analiza AI?',
         'Na karcie statystyk RallyStat przygotowuje gotową prośbę o analizę: dane meczu, znaczenie każdej statystyki i kolejność analizy: podsumowanie meczu, skład zdobytych punktów, najczęstsze błędy, wkład zawodników i 2–3 priorytety treningowe. Prosi AI, by liczyła bezpośrednio z danych, podawała liczbę przy każdym stwierdzeniu i niczego nie zgadywała. Wystarczy udostępnić ją w czacie AI, którego używasz. Wersja darmowa korzysta z sum dla zawodników i drużyn w każdym secie; Pro korzysta z pełnego zapisu akcji, więc znajduje też serie trzech lub więcej straconych punktów z rzędu.'),
        ('Akcje są szybkie. Czy dwie osoby mogą zapisywać razem?',
         'Tak. Zapisując w pojedynkę, przy szybkich akcjach coś umyka. Dzięki wspólnemu zapisowi drugi trener lub kierownik drużyny dołącza z własnego telefonu za pomocą kodu lub linku, a wpisy łączą się na żywo: na przykład jedna osoba prowadzi wynik, a druga statystyki zawodników. Telefon pomocniczy potrzebuje tylko darmowej aplikacji. Urządzenie główne może uruchomić wspólny zapis za darmo przez 3 mecze, potem z Pro. Gdy jest włączony, oba telefony potrzebują internetu.'),
    ],
    tested='RallyStat testowaliśmy na prawdziwych zapisach meczów szkolnych i klubowych i poprawialiśmy na prośbę trenerów: na przykład dwóch libero zmieniających się w trakcie meczu oraz statystyki zagrywki z liczbą zagrywek i punktów zdobytych przy własnej zagrywce.',
    codes=('Dla doświadczonych statystyków: wpisywanie kodów',
           'Jeśli już zapisujesz kodami, Pro dodaje wpisywanie kodów z klawiatury: krótkie kody w stylu, jakiego używają profesjonalni analitycy, np. "11KL", aby nadążyć za tempem akcji. Wypróbuj za darmo przez jeden mecz.'),
)

F['ru'] = dict(
    lead='RallyStat — приложение для статистики волейбола для тренеров, штаба и родителей. Записывайте каждый розыгрыш одним касанием, а после матча получайте анализ с помощью ИИ: как набирались и терялись очки, самые частые ошибки и над чем работать дальше, с подтверждающими цифрами. Попробуйте бесплатно на своём матче.',
    meta='RallyStat — приложение для статистики волейбола для тренеров и родителей на iPhone, iPad и Android. Одно касание на розыгрыш, анализ ИИ с подтверждающими цифрами, совместная запись в реальном времени, офлайн, разовая покупка.',
    glance=[
        'Анализ ИИ: выводы с цифрами в том ИИ-чате, которым вы уже пользуетесь (бесплатно по итогам матча; Pro добавляет ход игры по розыгрышам)',
        'Совместная запись: второй тренер записывает со своего телефона, и всё объединяется в реальном времени',
        'Одно касание на розыгрыш: счёт, переход и либеро обновляются сами',
        'Волейбол 6×6 и 9×9',
        'Запись работает офлайн, без аккаунта и рекламы',
        'Бесплатно до 2 команд; RallyStat Pro — разовая покупка, 14,99 $ в США (цена зависит от страны), без подписки',
        'iPhone, iPad и Android, 11 языков — полностью на русском',
    ],
    qa=[
        ('Какое приложение для статистики волейбола лучшее?',
         'Зависит от того, что вам нужно после матча. RallyStat задуман так, чтобы записывать было быстро, а читать легко: одно касание на розыгрыш, а затем запрос на анализ для ИИ, который показывает, где очки были выиграны и потеряны, с подтверждающими цифрами. Попробуйте бесплатно на своём матче. Если нужен скаутинг каждого касания или видеоанализ, лучше подойдёт специализированный инструмент для скаутинга.'),
        ('Как работает анализ ИИ?',
         'На вкладке статистики RallyStat готовит запрос на анализ: данные матча, значение каждого показателя и порядок разбора: итог матча, из чего сложились очки, самые частые ошибки, вклад игроков и 2–3 приоритета для тренировок. ИИ просят считать прямо по данным, подкреплять каждое утверждение цифрой и ничего не додумывать. Просто поделитесь запросом с ИИ-чатом, которым пользуетесь. Бесплатная версия использует итоги по игрокам и командам за каждую партию; Pro использует полный журнал розыгрышей и находит также серии из трёх и более проигранных очков подряд.'),
        ('Розыгрыши быстрые. Можно записывать вдвоём?',
         'Да. В одиночку на быстрых розыгрышах что-то упускаешь. С совместной записью второй тренер или администратор команды подключается со своего телефона по коду или ссылке, и записи объединяются в реальном времени: например, один ведёт счёт, другой статистику игроков. На телефоне помощника достаточно бесплатного приложения. Основное устройство может запускать совместную запись бесплатно 3 матча, дальше с Pro. Пока она включена, обоим телефонам нужен интернет.'),
    ],
    tested='RallyStat проверяли на реальных записях школьных и клубных матчей и дорабатывали по просьбам тренеров: например, два либеро, которые сменяют друг друга по ходу матча, и статистика подачи с попытками и очками на своей подаче.',
    codes=('Для опытных статистиков: ввод кодами',
           'Если вы уже ведёте статистику кодами, Pro добавляет ввод кодов с клавиатуры: короткие коды в стиле, которым пользуются профессиональные аналитики, например «11KL», чтобы успевать за темпом розыгрыша. Попробуйте бесплатно на одном матче.'),
)

F['tr'] = dict(
    lead='RallyStat; antrenörler, takım ekibi ve veliler için bir voleybol istatistik uygulamasıdır. Her ralliyi tek dokunuşla kaydedin, maçtan sonra yapay zekâ analizi alın: sayıların nasıl kazanılıp kaybedildiği, en sık hatalar ve sırada neye çalışılacağı, hepsi destekleyen sayılarla. Kendi maçınızla ücretsiz deneyin.',
    meta='RallyStat, iPhone, iPad ve Android\'de antrenörler ve veliler için voleybol istatistik uygulamasıdır. Her ralliye tek dokunuş, sayılarla desteklenen yapay zekâ analizi, canlı ortak kayıt, çevrimdışı, tek seferlik ödeme.',
    glance=[
        'Yapay zekâ analizi: zaten kullandığınız yapay zekâ sohbetinden sayılarla desteklenen sonuçlar (ücretsizde maç toplamlarıyla; Pro ralli ralli akışı da ekler)',
        'Ortak kayıt: ikinci bir antrenör kendi telefonundan kaydeder, hepsi canlı birleşir',
        'Her ralliye tek dokunuş: skor, rotasyon ve libero kendiliğinden güncellenir',
        '6 ve 9 kişilik voleybol',
        'Kayıt çevrimdışı çalışır; hesap ve reklam yok',
        '2 takıma kadar ücretsiz; RallyStat Pro tek seferlik satın alma, ABD\'de 14,99 US$ (fiyat ülkeye göre değişir), abonelik yok',
        'iPhone, iPad ve Android, 11 dil — tamamen Türkçe',
    ],
    qa=[
        ('En iyi voleybol istatistik uygulaması hangisi?',
         'Maçtan sonra neye ihtiyacınız olduğuna bağlı. RallyStat kaydı hızlı, sonucu kolay okunur olacak şekilde tasarlandı: her ralliye tek dokunuş, ardından sayıların nerede kazanılıp kaybedildiğini destekleyen sayılarla gösteren bir yapay zekâ analiz isteği. Kendi maçınızla ücretsiz deneyin. Her dokunuşu kaydeden scouting ya da video analizi gerekiyorsa, özel bir scouting aracı daha uygun olabilir.'),
        ('Yapay zekâ analizi nasıl çalışır?',
         'İstatistik sekmesinde RallyStat kullanıma hazır bir analiz isteği hazırlar: maç verileriniz, her istatistiğin anlamı ve analiz sırası: maç özeti, sayıların dağılımı, en sık hatalar, oyuncu katkıları ve antrenman için 2–3 öncelik. Yapay zekâdan verilerden doğrudan saymasını, her iddiayı bir sayıyla desteklemesini ve tahmin yürütmemesini ister. Kullandığınız yapay zekâ sohbetiyle paylaşmanız yeterli. Ücretsiz sürüm her set için oyuncu ve takım toplamlarını kullanır; Pro tam ralli kaydını kullandığı için üst üste üç veya daha fazla sayı kaybedilen serileri de bulur.'),
        ('Ralliler hızlı. İki kişi birlikte kayıt tutabilir mi?',
         'Evet. Tek başına kayıt tutarken hızlı rallilerde bir şeyler kaçar. Ortak kayıtla ikinci bir antrenör ya da takım sorumlusu kendi telefonundan bir kod veya bağlantıyla katılır ve girişler canlı olarak birleşir: örneğin biri skoru, diğeri oyuncu istatistiklerini tutar. Yardımcı telefonda yalnızca ücretsiz uygulama yeterlidir. Ana cihaz ortak kaydı 3 maç boyunca ücretsiz başlatabilir, sonrasında Pro gerekir. Açık olduğu sürece iki telefonun da internete bağlı olması gerekir.'),
    ],
    tested='RallyStat gerçek okul ve kulüp maç kayıtlarıyla test edildi ve antrenörlerin istekleriyle geliştirildi: örneğin maç içinde değişen iki libero ve servis denemeleriyle kendi servisimizde kazanılan sayıları gösteren servis istatistikleri.',
    codes=('Deneyimli istatistikçiler için: kodla giriş',
           'Zaten kodlarla kayıt tutuyorsanız, Pro klavyeyle kod girişini ekler: profesyonel analistlerin kullandığı tarzda kısa kodlarla, örneğin "11KL", ralli hızında kayıt tutarsınız. Bir maç boyunca ücretsiz deneyin.'),
)
