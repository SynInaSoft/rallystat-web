# -*- coding: utf-8 -*-
# 소개 페이지 첫 화면(10-27 총괄 지시, 재원님 "전부 추천대로"): 메시지 순서 ① AI 분석 ② 공동 기록 ③ 기본 기능.
# ⛔ 앱 안에는 AI가 없다(재원님 10-27). 앱은 기록·통계를 계산하고, AI 분석은 내보낸 요청문을 사용자의 AI 채팅에 넣어야 나온다.
#   상대팀 분석은 "양팀 모두 기록" + Pro 원본 로그일 때. 이 구분을 흐리는 문장을 쓰지 않는다.
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
    lead='RallyStat is a volleyball stats app for coaches, team staff and parents. Record each rally with one tap, and the app keeps the score, rotation and player stats for you. For a deeper look, RallyStat exports your match record together with a ready-made analysis prompt. Send it to the AI chat you already use, and the AI breaks down how points were won and lost and what to work on next, with the numbers behind each point.',
    meta='RallyStat is a volleyball stats app for coaches and parents on iPhone, iPad and Android. One tap per rally, automatic rotation and player stats, an analysis prompt for your own AI chat, live co-recording, 6- and 9-player, pay once.',
    glance=[
        'AI analysis prompt: export your match with a ready-made prompt and paste it into the AI chat you use (free: match totals; Pro: the full rally-by-rally log, including your opponent if you track both teams)',
        'Co-recording: a second coach records on their own phone and the entries merge live',
        'One tap per rally: the score, rotation and libero update themselves',
        '6-player and 9-player volleyball',
        'Recording works offline, with no account and no ads',
        'Free for up to 2 teams; RallyStat Pro is a one-time purchase, US$14.99 in the US (prices vary by country), no subscription',
        'iPhone, iPad and Android, in 11 languages',
    ],
    qa=[
        ('What is the best volleyball stats app?',
         'It depends on what you need after the match. RallyStat is built to be quick to record and easy to read: one tap per rally, and the app works out each player\'s points, errors and net points right away. For a deeper look, it exports your match with an analysis prompt for the AI chat you already use, which explains where points were won and lost with the numbers behind each finding. If you need touch-by-touch scouting of every pass and set, or video analysis, a dedicated scouting tool may suit you better.'),
        ('Does RallyStat analyze matches with AI?',
         'There is no AI inside the app: the app calculates your stats and reports itself. For an AI analysis, export the AI analysis prompt from the Stats tab. It is a text file with your match record, what each stat means and the order of the analysis. Send it to, or paste it into, the AI chat you already use. The prompt asks the AI to count from the data, back every claim with a number and not to guess, and to cover the match summary, how points were scored, the most frequent errors, player contributions and priorities for practice. On the free plan the file holds per-player and per-team totals for each set. With Pro it holds the full rally-by-rally log, so the analysis can also follow momentum, such as runs of points lost in a row. If you record with "Track both teams", your opponent\'s actions are in the log too, so the analysis covers them as well.'),
        ('Rallies are fast. Can two people record together?',
         'Yes. Recording alone, you miss things when rallies are fast. With co-recording, a second coach or team manager joins from their own phone with a code or link and the entries merge live, for example one person on the score and one on player stats. The helper phone only needs the free app. The main device can start co-recording free for 3 matches, then with Pro. Both phones need an internet connection while co-recording is on.'),
    ],
    tested='RallyStat has been tested with real school and club match records and improved at coaches\' requests, for example two liberos who swap during a match, and serve stats with attempts and points won on serve.',
    codes=('For experienced scorers: code entry',
           'If you already keep stats with codes, Pro adds keyboard code entry: short codes in the style professional analysts use, such as "11KL", so you can record at rally speed. You can try it free for one match.'),
)

F['ko'] = dict(
    lead='랠리스탯은 코치·팀 스태프·학부모를 위한 배구 기록 앱입니다. 랠리마다 탭 한 번으로 기록하면 점수·로테이션·선수 기록은 앱이 알아서 정리합니다. 더 깊이 보고 싶다면 랠리스탯이 경기 기록과 분석 요청문을 한 파일로 만들어 줍니다. 평소 쓰는 AI 채팅에 보내거나 붙여 넣으면, AI가 무엇으로 득점하고 실점했는지와 다음에 보완할 점을 근거 숫자와 함께 정리해 줍니다.',
    meta='랠리스탯은 코치·학부모를 위한 배구 기록·통계 앱입니다. 랠리마다 탭 한 번, 로테이션·선수 기록 자동, 내 AI 채팅에 넣는 분석 요청문, 실시간 공동 기록, 9인제·6인제, 한 번 구매. iPhone·iPad·Android, 한국어 완전 지원.',
    glance=[
        'AI 분석 요청문: 경기 기록과 요청문을 내보내 평소 쓰는 AI 채팅에 붙여 넣기(무료는 경기 집계, Pro는 랠리 단위 전체 기록 — 양팀을 기록하면 상대팀까지)',
        '공동 기록: 두 번째 코치가 자기 폰으로 같이 기록하면 실시간으로 합쳐짐',
        '랠리마다 탭 한 번: 점수·로테이션·리베로가 알아서 바뀜',
        '9인제·6인제 배구 모두 지원',
        '기록은 오프라인으로 작동, 계정·광고 없음',
        '팀 2개까지 무료, 랠리스탯 Pro는 한 번 구매(미국 US$14.99, 나라별 가격 다름), 구독 없음',
        'iPhone·iPad·Android, 11개 언어 — 한국어 완전 지원',
    ],
    qa=[
        ('배구 기록 앱 추천 — 어떤 앱이 좋을까?',
         '경기 뒤에 무엇이 필요한지에 따라 다릅니다. 랠리스탯은 기록은 빠르게, 결과는 읽기 쉽게 만드는 데 집중했습니다. 랠리마다 탭 한 번으로 기록하면 선수별 득점·범실·순득점은 앱이 바로 계산합니다. 더 깊이 보고 싶다면 경기 기록과 분석 요청문을 내보내 평소 쓰는 AI 채팅에 넣으면, 어디서 득점하고 실점했는지를 근거 숫자와 함께 설명받을 수 있습니다. 리시브·토스까지 터치 하나하나를 기록하는 정밀 스카우팅이나 영상 분석이 필요하다면 전문 스카우팅 도구가 더 맞을 수 있습니다.'),
        ('랠리스탯이 AI로 경기를 분석해 주나요?',
         '앱 안에는 AI가 없습니다. 선수 스탯과 리포트는 앱이 직접 계산합니다. AI 분석을 받으려면 통계 탭에서 AI 분석 프롬프트를 내보내세요. 경기 기록, 기록 항목의 뜻, 분석 순서가 담긴 텍스트 파일입니다. 이 파일을 평소 쓰는 AI 채팅에 보내거나 붙여 넣으면 됩니다. 요청문은 AI에게 데이터에서 직접 세고, 주장마다 근거 숫자를 적고, 추측하지 말라고 요청하며, 경기 요약·득점 구성·가장 잦은 범실·선수 기여·우선 보완점을 차례로 다루게 합니다. 무료는 선수별·팀별 세트 집계를 담고, Pro는 랠리 단위 전체 기록을 담아 연속 실점 같은 흐름까지 분석할 수 있습니다. "양팀 모두 기록"으로 기록하면 상대팀 기록도 들어가 상대팀 분석까지 받을 수 있습니다.'),
        ('랠리가 빠른데, 두 사람이 같이 기록할 수 있나요?',
         '네. 혼자 기록하면 빠른 랠리에서 놓치는 게 생깁니다. 공동 기록을 켜면 두 번째 코치나 매니저가 자기 폰에서 코드나 링크로 들어와 함께 기록하고, 입력이 실시간으로 합쳐집니다. 예를 들어 한 명은 점수, 한 명은 선수 스탯을 맡을 수 있습니다. 보조 기기는 무료 앱만 있으면 됩니다. 공동 기록을 여는 기기는 3경기까지 무료로 써 보고, 그 뒤에는 Pro가 필요합니다. 공동 기록을 켠 동안에는 두 기기 모두 인터넷이 필요합니다.'),
    ],
    tested='학교·클럽의 실제 경기 기록으로 시험했고, 현장 코치들의 요청을 받아 고쳐 왔습니다. 경기 중 교대하는 리베로 2명, 서브 시도와 서브권 득점 통계가 그 예입니다.',
    codes=('숙련 기록원을 위한 코드 입력',
           '이미 코드로 기록해 보셨다면 Pro의 키보드 코드 입력을 쓸 수 있습니다. 전문 분석가들이 쓰는 방식의 짧은 코드(예: "11KL")로 랠리 속도에 맞춰 기록합니다. 1경기는 무료로 써 볼 수 있습니다.'),
)

F['ja'] = dict(
    lead='RallyStatは、コーチ・チームスタッフ・保護者のためのバレーボール記録アプリです。ラリーごとにワンタップで記録すれば、スコア・ローテーション・選手の記録はアプリが自動でまとめます。さらに詳しく見たいときは、試合記録と分析の依頼文をひとつのファイルにします。ふだん使っているAIチャットに送るか貼り付ければ、どこで得点・失点したかと次に直すべき点を、AIが根拠の数字つきで整理します。',
    meta='RallyStatは、コーチと保護者のためのバレーボール記録・スコアアプリです。ラリーごとにワンタップ、ローテーションと選手記録は自動、自分のAIチャットに入れる分析の依頼文、リアルタイムの共同記録、6人制・9人制、買い切り。iPhone・iPad・Android対応。',
    glance=[
        'AI分析の依頼文：試合記録と依頼文を書き出して、ふだん使っているAIチャットに貼り付け（無料は試合の集計、Proはラリー単位の全記録。両チームを記録すれば相手チームも）',
        '共同記録：2人目のコーチが自分のスマホで一緒に記録し、リアルタイムで合流',
        'ラリーごとにワンタップ：スコア・ローテーション・リベロは自動で更新',
        '6人制・9人制の両方に対応',
        '記録はオフラインで動作、アカウント・広告なし',
        '2チームまで無料。RallyStat Proは買い切り（米国ではUS$14.99、国により価格は異なります）、サブスクなし',
        'iPhone・iPad・Android、11言語 — 日本語に完全対応',
    ],
    qa=[
        ('おすすめのバレーボール記録アプリは？',
         '試合後に何が欲しいかで変わります。RallyStatは「記録は速く、結果は読みやすく」を目指しました。ラリーごとにワンタップで記録すれば、選手ごとの得点・ミス・純得点はアプリがすぐに計算します。さらに詳しく見たいときは、試合記録と分析の依頼文を書き出してふだん使っているAIチャットに入れれば、どこで得点・失点したかを根拠の数字つきで説明してもらえます。レセプションやトスまで1本ずつ記録する精密なスカウティングや映像分析が必要なら、専用のスカウティングツールのほうが合うかもしれません。'),
        ('RallyStatはAIで試合を分析してくれるの？',
         'アプリの中にAIはありません。選手のスタッツとレポートはアプリが自分で計算します。AI分析を受けたいときは、成績タブから「AI分析プロンプト」を書き出してください。試合記録、各記録項目の意味、分析の順序が入ったテキストファイルです。これをふだん使っているAIチャットに送るか貼り付けます。依頼文はAIに、データから直接数え、主張ごとに根拠の数字を書き、推測しないよう求め、試合のまとめ・得点の内訳・多かったミス・選手の貢献・優先して直す点を順に扱わせます。無料版は選手別・チーム別のセット集計を、Proはラリー単位の全記録を入れるので、連続失点のような流れまで分析できます。「両チームを記録」で記録すれば相手チームの記録も入り、相手チームの分析まで受けられます。'),
        ('ラリーが速くて追いつけない。2人で記録できる？',
         'できます。ひとりで記録すると、速いラリーで取りこぼしが出ます。共同記録をオンにすると、2人目のコーチやマネージャーが自分のスマホからコードかリンクで参加し、入力がリアルタイムで合流します。たとえば1人がスコア、もう1人が選手のスタッツを担当できます。補助の端末は無料アプリだけで参加できます。共同記録を開く端末は3試合まで無料で試せて、その後はProが必要です。共同記録中は両方の端末にインターネット接続が必要です。'),
    ],
    tested='学校やクラブの実際の試合記録で試し、現場のコーチの要望を受けて改良してきました。試合中に交代するリベロ2人、サーブ本数とサーブ時の得点のスタッツがその例です。',
    codes=('記録に慣れた方へ：コード入力',
           'コードで記録した経験があれば、Proのキーボードコード入力が使えます。プロのアナリストが使う方式の短いコード（例：「11KL」）で、ラリーの速さに合わせて記録できます。1試合は無料で試せます。'),
)

F['de'] = dict(
    lead='RallyStat ist eine Volleyball-Statistik-App für Trainer, Teambetreuer und Eltern. Jeden Ballwechsel mit einem Tipp erfassen, und die App führt Spielstand, Rotation und Spielerstatistik für Sie. Für eine tiefere Auswertung exportiert RallyStat Ihre Spielaufzeichnung zusammen mit einer fertigen Analyse-Anfrage. Schicken Sie sie an den KI-Chat, den Sie schon nutzen, und die KI zeigt, womit Punkte gewonnen und verloren wurden und was als Nächstes zu verbessern ist, jeweils mit den Zahlen dazu.',
    meta='RallyStat ist eine Volleyball-Statistik-App für Trainer und Eltern auf iPhone, iPad und Android. Ein Tipp pro Ballwechsel, Rotation und Spielerstatistik automatisch, eine Analyse-Anfrage für Ihren eigenen KI-Chat, gemeinsames Erfassen in Echtzeit, offline, einmal zahlen.',
    glance=[
        'KI-Analyse-Anfrage: Spiel mit fertiger Anfrage exportieren und in Ihren KI-Chat einfügen (kostenlos: Spielsummen; Pro: das vollständige Protokoll Ballwechsel für Ballwechsel, mit dem Gegner, wenn Sie beide Teams erfassen)',
        'Gemeinsam erfassen: Ein zweiter Trainer erfasst auf dem eigenen Handy mit, alles wird live zusammengeführt',
        'Ein Tipp pro Ballwechsel: Spielstand, Rotation und Libero aktualisieren sich selbst',
        'Volleyball mit 6 und mit 9 Spielern',
        'Erfassen funktioniert offline, ohne Konto und ohne Werbung',
        'Kostenlos für bis zu 2 Teams; RallyStat Pro ist ein Einmalkauf, 14,99 US$ in den USA (Preise je nach Land), kein Abo',
        'iPhone, iPad und Android, in 11 Sprachen – vollständig auf Deutsch',
    ],
    qa=[
        ('Welche Volleyball-Statistik-App ist die beste?',
         'Das hängt davon ab, was Sie nach dem Spiel brauchen. RallyStat soll schnell zu erfassen und leicht zu lesen sein: ein Tipp pro Ballwechsel, und die App berechnet sofort Punkte, Fehler und Netto-Punkte jedes Spielers. Für eine tiefere Auswertung exportiert sie Ihr Spiel mit einer Analyse-Anfrage für Ihren KI-Chat, der dann mit Zahlen erklärt, wo Punkte gewonnen und verloren wurden. Wer jede Ballberührung scouten oder Videos analysieren will, ist mit einem spezialisierten Scouting-Tool besser bedient.'),
        ('Analysiert RallyStat Spiele mit KI?',
         'In der App selbst steckt keine KI: Statistiken und Berichte berechnet die App selbst. Für eine KI-Analyse exportieren Sie im Statistik-Tab den KI-Analyse-Prompt. Das ist eine Textdatei mit Ihrer Spielaufzeichnung, der Bedeutung jeder Statistik und der Reihenfolge der Auswertung. Schicken Sie sie an den KI-Chat, den Sie nutzen, oder fügen Sie sie dort ein. Die Anfrage bittet die KI, direkt aus den Daten zu zählen, jede Aussage mit einer Zahl zu belegen und nichts zu raten, und führt sie durch Spielzusammenfassung, Punkteverteilung, häufigste Fehler, Spielerbeiträge und Trainingsschwerpunkte. In der kostenlosen Version enthält die Datei Summen pro Spieler und Team je Satz. Mit Pro enthält sie das vollständige Protokoll Ballwechsel für Ballwechsel, sodass die Analyse auch den Spielverlauf verfolgen kann, etwa Serien verlorener Punkte. Wenn Sie mit „Beide Teams erfassen“ aufzeichnen, stehen auch die Aktionen des Gegners im Protokoll, und die Analyse deckt ihn mit ab.'),
        ('Die Ballwechsel sind schnell. Können zwei Personen gemeinsam erfassen?',
         'Ja. Wer allein erfasst, verpasst bei schnellen Ballwechseln etwas. Beim gemeinsamen Erfassen tritt ein zweiter Trainer oder Teambetreuer mit Code oder Link vom eigenen Handy bei, und die Eingaben werden live zusammengeführt, zum Beispiel eine Person für den Spielstand und eine für die Spielerstatistik. Das Helfer-Handy braucht nur die kostenlose App. Das Hauptgerät kann das gemeinsame Erfassen 3 Spiele lang kostenlos starten, danach mit Pro. Solange es eingeschaltet ist, brauchen beide Handys eine Internetverbindung.'),
    ],
    tested='RallyStat wurde mit echten Spielaufzeichnungen aus Schule und Verein getestet und auf Wunsch von Trainern verbessert, etwa um zwei Liberos, die während des Spiels wechseln, und um Aufschlagstatistiken mit Versuchen und Punkten bei eigenem Aufschlag.',
    codes=('Für erfahrene Statistiker: Code-Eingabe',
           'Wenn Sie schon mit Codes erfassen, bietet Pro die Tastatur-Code-Eingabe: kurze Codes nach der Art professioneller Analysten, etwa „11KL“, damit Sie im Tempo der Ballwechsel erfassen. Ein Spiel lang kostenlos ausprobieren.'),
)

F['fr'] = dict(
    lead='RallyStat est une application de statistiques de volley pour entraîneurs, staff et parents. Notez chaque échange d\'un toucher : l\'application tient le score, la rotation et les stats des joueurs pour vous. Pour aller plus loin, RallyStat exporte votre match avec une demande d\'analyse prête à l\'emploi. Envoyez-la au chat d\'IA que vous utilisez déjà, et l\'IA détaille comment les points ont été gagnés et perdus et quoi travailler ensuite, chiffres à l\'appui.',
    meta='RallyStat est une application de stats de volley pour entraîneurs et parents sur iPhone, iPad et Android. Un toucher par échange, rotation et stats des joueurs automatiques, une demande d\'analyse pour votre propre chat d\'IA, saisie à plusieurs en direct, hors ligne, achat unique.',
    glance=[
        'Demande d\'analyse IA : exportez le match avec une demande toute prête et collez-la dans votre chat d\'IA (gratuit : totaux du match ; Pro : le journal complet échange par échange, adversaire compris si vous suivez les deux équipes)',
        'Saisie à plusieurs : un deuxième entraîneur saisit sur son propre téléphone et tout se fusionne en direct',
        'Un toucher par échange : le score, la rotation et le libéro se mettent à jour seuls',
        'Volley à 6 et à 9',
        'La saisie fonctionne hors ligne, sans compte ni publicité',
        'Gratuit jusqu\'à 2 équipes ; RallyStat Pro est un achat unique, 14,99 US$ aux États-Unis (prix selon le pays), sans abonnement',
        'iPhone, iPad et Android, en 11 langues — entièrement en français',
    ],
    qa=[
        ('Quelle est la meilleure application de stats de volley ?',
         'Cela dépend de ce dont vous avez besoin après le match. RallyStat veut être rapide à saisir et facile à lire : un toucher par échange, et l\'application calcule aussitôt les points, fautes et points nets de chaque joueur. Pour aller plus loin, elle exporte votre match avec une demande d\'analyse pour votre chat d\'IA, qui explique ensuite, chiffres à l\'appui, où les points ont été gagnés et perdus. Pour un scouting touche par touche ou l\'analyse vidéo, un outil de scouting dédié vous conviendra mieux.'),
        ('RallyStat analyse-t-elle les matchs avec l\'IA ?',
         'L\'application ne contient pas d\'IA : elle calcule elle-même les stats et les rapports. Pour une analyse par IA, exportez le prompt d\'analyse IA depuis l\'onglet Stats. C\'est un fichier texte avec votre match, la signification de chaque stat et l\'ordre de l\'analyse. Envoyez-le ou collez-le dans le chat d\'IA que vous utilisez déjà. La demande invite l\'IA à compter à partir des données, à chiffrer chaque affirmation et à ne rien supposer, et à traiter le résumé du match, la répartition des points, les fautes les plus fréquentes, la contribution des joueurs et les priorités d\'entraînement. En version gratuite, le fichier contient les totaux par joueur et par équipe pour chaque set. Avec Pro, il contient le journal complet échange par échange, ce qui permet aussi de suivre la dynamique, comme les séries de points perdus. Si vous notez avec « Les deux équipes », les actions de l\'adversaire figurent aussi dans le journal et l\'analyse le couvre également.'),
        ('Les échanges vont vite. Peut-on noter à deux ?',
         'Oui. Seul, on rate des actions quand les échanges vont vite. Avec la saisie à plusieurs, un deuxième entraîneur ou un responsable d\'équipe rejoint le match depuis son téléphone avec un code ou un lien, et les saisies se fusionnent en direct : par exemple l\'un tient le score, l\'autre les stats des joueurs. Le téléphone d\'appoint n\'a besoin que de l\'application gratuite. L\'appareil principal peut lancer la saisie à plusieurs gratuitement pendant 3 matchs, puis avec Pro. Les deux téléphones doivent être connectés à Internet tant qu\'elle est activée.'),
    ],
    tested='RallyStat a été testée sur de vrais relevés de matchs scolaires et de club, et améliorée à la demande d\'entraîneurs : par exemple deux libéros qui alternent pendant le match, et des stats de service avec les tentatives et les points marqués au service.',
    codes=('Pour les statisticiens expérimentés : saisie par codes',
           'Si vous notez déjà avec des codes, Pro ajoute la saisie par codes au clavier : des codes courts, à la manière des analystes professionnels, comme « 11KL », pour suivre le rythme des échanges. Essai gratuit sur un match.'),
)

F['it'] = dict(
    lead='RallyStat è un\'app di statistiche di pallavolo per allenatori, staff e genitori. Registra ogni scambio con un tocco: punteggio, rotazione e statistiche dei giocatori le tiene l\'app. Per un\'analisi più approfondita, RallyStat esporta la partita insieme a una richiesta di analisi già pronta. Inviala alla chat IA che usi già e l\'IA spiega come sono stati vinti e persi i punti e su cosa lavorare, con i numeri a supporto.',
    meta='RallyStat è un\'app di statistiche di pallavolo per allenatori e genitori su iPhone, iPad e Android. Un tocco per scambio, rotazione e statistiche dei giocatori automatiche, una richiesta di analisi per la tua chat IA, registrazione condivisa in tempo reale, offline, acquisto unico.',
    glance=[
        'Richiesta di analisi IA: esporta la partita con una richiesta già pronta e incollala nella tua chat IA (gratis: totali della partita; Pro: il registro completo scambio per scambio, avversari compresi se registri entrambe le squadre)',
        'Registrazione condivisa: un secondo allenatore registra dal proprio telefono e tutto si unisce in tempo reale',
        'Un tocco per scambio: punteggio, rotazione e libero si aggiornano da soli',
        'Pallavolo a 6 e a 9',
        'La registrazione funziona offline, senza account e senza pubblicità',
        'Gratis fino a 2 squadre; RallyStat Pro è un acquisto unico, 14,99 US$ negli Stati Uniti (prezzi diversi per paese), nessun abbonamento',
        'iPhone, iPad e Android, in 11 lingue — completamente in italiano',
    ],
    qa=[
        ('Qual è la migliore app di statistiche di pallavolo?',
         'Dipende da cosa ti serve dopo la partita. RallyStat punta a essere veloce da registrare e facile da leggere: un tocco per scambio, e l\'app calcola subito punti, errori e punti netti di ogni giocatore. Per un\'analisi più approfondita, esporta la partita con una richiesta di analisi per la tua chat IA, che spiega con i numeri dove sono stati vinti e persi i punti. Se ti serve lo scouting tocco per tocco o l\'analisi video, uno strumento di scouting dedicato può essere più adatto.'),
        ('RallyStat analizza le partite con l\'IA?',
         'Nell\'app non c\'è un\'IA: statistiche e referti li calcola l\'app stessa. Per un\'analisi con l\'IA, esporta il prompt di analisi IA dalla scheda Statistiche. È un file di testo con la tua partita, il significato di ogni statistica e l\'ordine dell\'analisi. Invialo o incollalo nella chat IA che usi già. La richiesta chiede all\'IA di contare dai dati, di indicare un numero per ogni affermazione e di non tirare a indovinare, e la guida tra riepilogo, composizione dei punti, errori più frequenti, contributo dei giocatori e priorità di allenamento. Nella versione gratuita il file contiene i totali per giocatore e per squadra di ogni set. Con Pro contiene il registro completo scambio per scambio, così l\'analisi può seguire anche l\'andamento, come le serie di punti persi. Se registri con "Entrambe le squadre", nel registro ci sono anche le azioni degli avversari e l\'analisi copre anche loro.'),
        ('Gli scambi sono veloci. Si può registrare in due?',
         'Sì. Da soli, negli scambi veloci qualcosa sfugge. Con la registrazione condivisa, un secondo allenatore o un dirigente entra dal proprio telefono con un codice o un link e gli inserimenti si uniscono in tempo reale: per esempio uno segue il punteggio e l\'altro le statistiche dei giocatori. Al telefono di supporto basta l\'app gratuita. Il dispositivo principale può avviare la registrazione condivisa gratis per 3 partite, poi con Pro. Finché è attiva, entrambi i telefoni devono essere connessi a Internet.'),
    ],
    tested='RallyStat è stata provata con registrazioni reali di partite scolastiche e di società e migliorata su richiesta degli allenatori: per esempio due liberi che si alternano durante la partita e le statistiche di battuta, con tentativi e punti fatti in battuta.',
    codes=('Per gli statistici esperti: inserimento a codici',
           'Se registri già con i codici, Pro aggiunge l\'inserimento a codici da tastiera: codici brevi, nello stile usato dagli analisti professionisti, come "11KL", per registrare alla velocità dello scambio. Provalo gratis per una partita.'),
)

F['es'] = dict(
    lead='RallyStat es una app de estadísticas de voleibol para entrenadores, cuerpo técnico y padres. Registra cada jugada con un toque y la app lleva el marcador, la rotación y las estadísticas de los jugadores por ti. Para un análisis más profundo, RallyStat exporta tu partido junto con una solicitud de análisis lista para usar. Envíala al chat de IA que ya usas y la IA desglosa cómo se ganaron y perdieron los puntos y qué trabajar después, con los números que lo respaldan.',
    meta='RallyStat es una app de estadísticas de voleibol para entrenadores y padres en iPhone, iPad y Android. Un toque por jugada, rotación y estadísticas de jugadores automáticas, una solicitud de análisis para tu propio chat de IA, registro compartido en vivo, sin conexión, pago único.',
    glance=[
        'Solicitud de análisis con IA: exporta el partido con una solicitud lista y pégala en tu chat de IA (gratis: totales del partido; Pro: el registro completo jugada a jugada, rival incluido si registras ambos equipos)',
        'Registro compartido: un segundo entrenador registra desde su propio teléfono y todo se une en vivo',
        'Un toque por jugada: el marcador, la rotación y el líbero se actualizan solos',
        'Voleibol de 6 y de 9 jugadores',
        'El registro funciona sin conexión, sin cuenta y sin anuncios',
        'Gratis hasta 2 equipos; RallyStat Pro es un pago único, US$14,99 en EE. UU. (el precio varía según el país), sin suscripción',
        'iPhone, iPad y Android, en 11 idiomas — totalmente en español',
    ],
    qa=[
        ('¿Cuál es la mejor app de estadísticas de voleibol?',
         'Depende de lo que necesites después del partido. RallyStat busca ser rápida de registrar y fácil de leer: un toque por jugada y la app calcula al momento los puntos, errores y puntos netos de cada jugador. Para un análisis más profundo, exporta tu partido con una solicitud de análisis para tu chat de IA, que explica con números dónde se ganaron y perdieron los puntos. Si necesitas scouting toque a toque o análisis de vídeo, una herramienta de scouting específica puede encajarte mejor.'),
        ('¿RallyStat analiza los partidos con IA?',
         'La app no lleva IA dentro: las estadísticas y los informes los calcula la propia app. Para un análisis con IA, exporta el prompt de análisis de IA desde la pestaña de estadísticas. Es un archivo de texto con tu partido, qué significa cada estadística y el orden del análisis. Envíalo o pégalo en el chat de IA que ya usas. La solicitud pide a la IA que cuente a partir de los datos, respalde cada afirmación con un número y no suponga nada, y la guía por el resumen del partido, cómo se lograron los puntos, los errores más frecuentes, el aporte de los jugadores y las prioridades de entrenamiento. En el plan gratuito el archivo contiene los totales por jugador y por equipo de cada set. Con Pro contiene el registro completo jugada a jugada, así que el análisis también puede seguir la dinámica, como las rachas de puntos perdidos. Si registras con "Registrar ambos equipos", las acciones del rival también están en el registro y el análisis las cubre.'),
        ('Las jugadas son rápidas. ¿Pueden registrar dos personas a la vez?',
         'Sí. Quien registra solo pierde acciones cuando las jugadas van rápido. Con el registro compartido, un segundo entrenador o delegado se une desde su propio teléfono con un código o un enlace, y las entradas se combinan en vivo: por ejemplo, uno lleva el marcador y otro las estadísticas de los jugadores. El teléfono de apoyo solo necesita la app gratuita. El dispositivo principal puede iniciar el registro compartido gratis durante 3 partidos y después con Pro. Mientras está activo, ambos teléfonos necesitan conexión a internet.'),
    ],
    tested='RallyStat se probó con registros reales de partidos escolares y de club y se mejoró a petición de entrenadores: por ejemplo, dos líberos que se alternan durante el partido y estadísticas de saque, con intentos y puntos ganados con el saque propio.',
    codes=('Para estadísticos con experiencia: entrada por códigos',
           'Si ya registras con códigos, Pro añade la entrada por códigos con teclado: códigos cortos al estilo de los analistas profesionales, como "11KL", para registrar al ritmo de la jugada. Pruébala gratis durante un partido.'),
)

F['pt'] = dict(
    lead='O RallyStat é um app de estatísticas de vôlei para técnicos, comissão técnica e pais. Registre cada rally com um toque e o app cuida do placar, do rodízio e das estatísticas dos jogadores. Para uma análise mais profunda, o RallyStat exporta a sua partida junto com um pedido de análise pronto. Envie para o chat de IA que você já usa e a IA mostra como os pontos foram ganhos e perdidos e o que treinar a seguir, com os números que comprovam.',
    meta='O RallyStat é um app de estatísticas de vôlei para técnicos e pais no iPhone, iPad e Android. Um toque por rally, rodízio e estatísticas dos jogadores automáticos, um pedido de análise para o seu próprio chat de IA, registro compartilhado ao vivo, offline, pagamento único.',
    glance=[
        'Pedido de análise com IA: exporte a partida com um pedido pronto e cole no seu chat de IA (grátis: totais da partida; Pro: o registro completo rally a rally, incluindo o adversário se você registrar os dois times)',
        'Registro compartilhado: um segundo técnico registra no próprio celular e tudo se junta ao vivo',
        'Um toque por rally: placar, rodízio e líbero se atualizam sozinhos',
        'Vôlei de 6 e de 9 jogadores',
        'O registro funciona offline, sem conta e sem anúncios',
        'Grátis para até 2 times; o RallyStat Pro é pagamento único, US$ 14,99 nos EUA (preço varia por país), sem assinatura',
        'iPhone, iPad e Android, em 11 idiomas — totalmente em português',
    ],
    qa=[
        ('Qual é o melhor app de estatísticas de vôlei?',
         'Depende do que você precisa depois da partida. O RallyStat quer ser rápido de registrar e fácil de ler: um toque por rally e o app calcula na hora os pontos, erros e saldo de cada jogador. Para uma análise mais profunda, ele exporta a partida com um pedido de análise para o seu chat de IA, que explica com números onde os pontos foram ganhos e perdidos. Se você precisa de scout toque a toque ou análise de vídeo, uma ferramenta de scout dedicada pode ser melhor.'),
        ('O RallyStat analisa as partidas com IA?',
         'Não há IA dentro do app: as estatísticas e os relatórios são calculados pelo próprio app. Para uma análise com IA, exporte o prompt de análise de IA na aba de estatísticas. É um arquivo de texto com a sua partida, o significado de cada estatística e a ordem da análise. Envie ou cole no chat de IA que você já usa. O pedido orienta a IA a contar a partir dos dados, mostrar um número para cada afirmação e não chutar nada, passando por resumo da partida, composição dos pontos, erros mais frequentes, contribuição dos jogadores e prioridades de treino. No plano grátis, o arquivo traz os totais por jogador e por time em cada set. Com o Pro, traz o registro completo rally a rally, e a análise também acompanha o andamento, como sequências de pontos perdidos. Se você registrar com "Registrar os dois times", as ações do adversário também entram no registro e a análise cobre o adversário.'),
        ('Os rallies são rápidos. Duas pessoas podem registrar juntas?',
         'Sim. Quem registra sozinho perde lances quando o rally é rápido. Com o registro compartilhado, um segundo técnico ou auxiliar entra pelo próprio celular com um código ou link, e os registros se juntam ao vivo: por exemplo, um cuida do placar e o outro das estatísticas dos jogadores. O celular de apoio só precisa do app grátis. O aparelho principal pode iniciar o registro compartilhado grátis por 3 partidas e depois com o Pro. Enquanto estiver ligado, os dois celulares precisam de internet.'),
    ],
    tested='O RallyStat foi testado com registros reais de partidas de escola e de clube e melhorado a pedido de técnicos: por exemplo, dois líberos que se revezam durante a partida e estatísticas de saque, com tentativas e pontos feitos no próprio saque.',
    codes=('Para estatísticos experientes: registro por códigos',
           'Se você já registra com códigos, o Pro traz o registro por códigos no teclado: códigos curtos no estilo usado por analistas profissionais, como "11KL", para registrar no ritmo do rally. Experimente grátis em uma partida.'),
)

F['pl'] = dict(
    lead='RallyStat to aplikacja do statystyk siatkówki dla trenerów, sztabu i rodziców. Zapisuj każdą akcję jednym dotknięciem, a wynik, rotację i statystyki zawodników aplikacja prowadzi sama. Jeśli chcesz zajrzeć głębiej, RallyStat eksportuje zapis meczu razem z gotową prośbą o analizę. Wyślij ją do czatu AI, którego już używasz, a AI rozpisze, jak zdobywano i tracono punkty i nad czym pracować dalej, z liczbami na poparcie.',
    meta='RallyStat to aplikacja do statystyk siatkówki dla trenerów i rodziców na iPhone, iPad i Android. Jedno dotknięcie na akcję, automatyczna rotacja i statystyki zawodników, prośba o analizę dla Twojego czatu AI, wspólny zapis na żywo, offline, jednorazowy zakup.',
    glance=[
        'Prośba o analizę AI: wyeksportuj mecz z gotową prośbą i wklej ją do swojego czatu AI (za darmo: sumy meczu; Pro: pełny zapis akcja po akcji, łącznie z rywalem, jeśli zapisujesz obie drużyny)',
        'Wspólny zapis: drugi trener zapisuje na własnym telefonie, a wszystko łączy się na żywo',
        'Jedno dotknięcie na akcję: wynik, rotacja i libero aktualizują się same',
        'Siatkówka 6- i 9-osobowa',
        'Zapis działa offline, bez konta i bez reklam',
        'Za darmo do 2 drużyn; RallyStat Pro to jednorazowy zakup, 14,99 USD w USA (ceny zależą od kraju), bez subskrypcji',
        'iPhone, iPad i Android, w 11 językach — w pełni po polsku',
    ],
    qa=[
        ('Jaka jest najlepsza aplikacja do statystyk siatkówki?',
         'To zależy od tego, czego potrzebujesz po meczu. RallyStat ma być szybki w zapisie i łatwy w czytaniu: jedno dotknięcie na akcję, a aplikacja od razu liczy punkty, błędy i bilans każdego zawodnika. Jeśli chcesz zajrzeć głębiej, eksportuje mecz z prośbą o analizę dla Twojego czatu AI, który wyjaśnia z liczbami, gdzie zdobyto i stracono punkty. Jeśli potrzebujesz scoutingu każdego dotknięcia albo analizy wideo, lepiej sprawdzi się wyspecjalizowane narzędzie do scoutingu.'),
        ('Czy RallyStat analizuje mecze za pomocą AI?',
         'W aplikacji nie ma AI: statystyki i raporty aplikacja liczy sama. Aby uzyskać analizę AI, wyeksportuj prompt analizy AI z karty statystyk. To plik tekstowy z zapisem meczu, znaczeniem każdej statystyki i kolejnością analizy. Wyślij go lub wklej do czatu AI, którego już używasz. Prośba każe AI liczyć bezpośrednio z danych, podawać liczbę przy każdym stwierdzeniu i niczego nie zgadywać, i prowadzi ją przez podsumowanie meczu, skład zdobytych punktów, najczęstsze błędy, wkład zawodników i priorytety treningowe. W wersji darmowej plik zawiera sumy dla zawodników i drużyn w każdym secie. Z Pro zawiera pełny zapis akcja po akcji, więc analiza może też śledzić przebieg, np. serie straconych punktów. Jeśli zapisujesz w trybie „Obie drużyny”, w zapisie są też akcje rywala i analiza obejmuje również jego.'),
        ('Akcje są szybkie. Czy dwie osoby mogą zapisywać razem?',
         'Tak. Zapisując w pojedynkę, przy szybkich akcjach coś umyka. Dzięki wspólnemu zapisowi drugi trener lub kierownik drużyny dołącza z własnego telefonu za pomocą kodu lub linku, a wpisy łączą się na żywo: na przykład jedna osoba prowadzi wynik, a druga statystyki zawodników. Telefon pomocniczy potrzebuje tylko darmowej aplikacji. Urządzenie główne może uruchomić wspólny zapis za darmo przez 3 mecze, potem z Pro. Gdy jest włączony, oba telefony potrzebują internetu.'),
    ],
    tested='RallyStat testowaliśmy na prawdziwych zapisach meczów szkolnych i klubowych i poprawialiśmy na prośbę trenerów: na przykład dwóch libero zmieniających się w trakcie meczu oraz statystyki zagrywki z liczbą zagrywek i punktów zdobytych przy własnej zagrywce.',
    codes=('Dla doświadczonych statystyków: wpisywanie kodów',
           'Jeśli już zapisujesz kodami, Pro dodaje wpisywanie kodów z klawiatury: krótkie kody w stylu, jakiego używają profesjonalni analitycy, np. "11KL", aby nadążyć za tempem akcji. Wypróbuj za darmo przez jeden mecz.'),
)

F['ru'] = dict(
    lead='RallyStat — приложение для статистики волейбола для тренеров, штаба и родителей. Записывайте каждый розыгрыш одним касанием, а счёт, расстановку и статистику игроков приложение ведёт само. Для более глубокого разбора RallyStat экспортирует запись матча вместе с готовым запросом на анализ. Отправьте его в ИИ-чат, которым вы уже пользуетесь, и ИИ разберёт, как набирались и терялись очки и над чем работать дальше, с подтверждающими цифрами.',
    meta='RallyStat — приложение для статистики волейбола для тренеров и родителей на iPhone, iPad и Android. Одно касание на розыгрыш, автоматические расстановка и статистика игроков, запрос на анализ для вашего ИИ-чата, совместная запись в реальном времени, офлайн, разовая покупка.',
    glance=[
        'Запрос на анализ ИИ: экспортируйте матч с готовым запросом и вставьте в свой ИИ-чат (бесплатно: итоги матча; Pro: полный журнал по розыгрышам, вместе с соперником, если вы записываете обе команды)',
        'Совместная запись: второй тренер записывает со своего телефона, и всё объединяется в реальном времени',
        'Одно касание на розыгрыш: счёт, переход и либеро обновляются сами',
        'Волейбол 6×6 и 9×9',
        'Запись работает офлайн, без аккаунта и рекламы',
        'Бесплатно до 2 команд; RallyStat Pro — разовая покупка, 14,99 $ в США (цена зависит от страны), без подписки',
        'iPhone, iPad и Android, 11 языков — полностью на русском',
    ],
    qa=[
        ('Какое приложение для статистики волейбола лучшее?',
         'Зависит от того, что вам нужно после матча. RallyStat задуман так, чтобы записывать было быстро, а читать легко: одно касание на розыгрыш, и приложение сразу считает очки, ошибки и чистые очки каждого игрока. Для более глубокого разбора оно экспортирует матч с запросом на анализ для вашего ИИ-чата, который с цифрами объяснит, где очки были выиграны и потеряны. Если нужен скаутинг каждого касания или видеоанализ, лучше подойдёт специализированный инструмент для скаутинга.'),
        ('RallyStat анализирует матчи с помощью ИИ?',
         'Внутри приложения ИИ нет: статистику и отчёты приложение считает само. Чтобы получить анализ ИИ, экспортируйте промпт для ИИ-анализа на вкладке статистики. Это текстовый файл с записью матча, значением каждого показателя и порядком разбора. Отправьте его или вставьте в ИИ-чат, которым вы уже пользуетесь. Запрос просит ИИ считать прямо по данным, подкреплять каждое утверждение цифрой и ничего не додумывать, и ведёт его через итог матча, состав очков, самые частые ошибки, вклад игроков и приоритеты для тренировок. В бесплатной версии в файле итоги по игрокам и командам за каждую партию. С Pro — полный журнал по розыгрышам, поэтому анализ может проследить и ход игры, например серии проигранных очков. Если вы записываете в режиме «Обе команды», действия соперника тоже попадают в журнал, и анализ охватывает и его.'),
        ('Розыгрыши быстрые. Можно записывать вдвоём?',
         'Да. В одиночку на быстрых розыгрышах что-то упускаешь. С совместной записью второй тренер или администратор команды подключается со своего телефона по коду или ссылке, и записи объединяются в реальном времени: например, один ведёт счёт, другой статистику игроков. На телефоне помощника достаточно бесплатного приложения. Основное устройство может запускать совместную запись бесплатно 3 матча, дальше с Pro. Пока она включена, обоим телефонам нужен интернет.'),
    ],
    tested='RallyStat проверяли на реальных записях школьных и клубных матчей и дорабатывали по просьбам тренеров: например, два либеро, которые сменяют друг друга по ходу матча, и статистика подачи с попытками и очками на своей подаче.',
    codes=('Для опытных статистиков: ввод кодами',
           'Если вы уже ведёте статистику кодами, Pro добавляет ввод кодов с клавиатуры: короткие коды в стиле, которым пользуются профессиональные аналитики, например «11KL», чтобы успевать за темпом розыгрыша. Попробуйте бесплатно на одном матче.'),
)

F['tr'] = dict(
    lead='RallyStat; antrenörler, takım ekibi ve veliler için bir voleybol istatistik uygulamasıdır. Her ralliyi tek dokunuşla kaydedin; skoru, rotasyonu ve oyuncu istatistiklerini uygulama sizin için tutar. Daha derin bir bakış için RallyStat maç kaydınızı hazır bir analiz isteğiyle birlikte dışa aktarır. Bunu zaten kullandığınız yapay zekâ sohbetine gönderin; yapay zekâ sayıların nasıl kazanılıp kaybedildiğini ve sırada neye çalışılacağını destekleyen sayılarla açıklar.',
    meta='RallyStat, iPhone, iPad ve Android\'de antrenörler ve veliler için voleybol istatistik uygulamasıdır. Her ralliye tek dokunuş, otomatik rotasyon ve oyuncu istatistikleri, kendi yapay zekâ sohbetiniz için analiz isteği, canlı ortak kayıt, çevrimdışı, tek seferlik ödeme.',
    glance=[
        'Yapay zekâ analiz isteği: maçı hazır bir istekle dışa aktarın ve kendi yapay zekâ sohbetinize yapıştırın (ücretsiz: maç toplamları; Pro: ralli ralli tam kayıt, iki takımı da kaydederseniz rakip dahil)',
        'Ortak kayıt: ikinci bir antrenör kendi telefonundan kaydeder, hepsi canlı birleşir',
        'Her ralliye tek dokunuş: skor, rotasyon ve libero kendiliğinden güncellenir',
        '6 ve 9 kişilik voleybol',
        'Kayıt çevrimdışı çalışır; hesap ve reklam yok',
        '2 takıma kadar ücretsiz; RallyStat Pro tek seferlik satın alma, ABD\'de 14,99 US$ (fiyat ülkeye göre değişir), abonelik yok',
        'iPhone, iPad ve Android, 11 dil — tamamen Türkçe',
    ],
    qa=[
        ('En iyi voleybol istatistik uygulaması hangisi?',
         'Maçtan sonra neye ihtiyacınız olduğuna bağlı. RallyStat kaydı hızlı, sonucu kolay okunur olacak şekilde tasarlandı: her ralliye tek dokunuş, uygulama her oyuncunun sayı, hata ve net sayısını hemen hesaplar. Daha derin bir bakış için maçı, kendi yapay zekâ sohbetinize yönelik bir analiz isteğiyle dışa aktarır; sohbet de sayıların nerede kazanılıp kaybedildiğini rakamlarla açıklar. Her dokunuşu kaydeden scouting ya da video analizi gerekiyorsa, özel bir scouting aracı daha uygun olabilir.'),
        ('RallyStat maçları yapay zekâ ile analiz ediyor mu?',
         'Uygulamanın içinde yapay zekâ yok: istatistikleri ve raporları uygulama kendisi hesaplar. Yapay zekâ analizi için İstatistik sekmesinden yapay zekâ analiz istemini dışa aktarın. Bu; maç kaydınızı, her istatistiğin anlamını ve analiz sırasını içeren bir metin dosyasıdır. Dosyayı zaten kullandığınız yapay zekâ sohbetine gönderin veya yapıştırın. İstek, yapay zekâdan verilerden doğrudan saymasını, her iddiayı bir sayıyla desteklemesini ve tahmin yürütmemesini ister; maç özeti, sayıların dağılımı, en sık hatalar, oyuncu katkıları ve antrenman öncelikleri üzerinden ilerletir. Ücretsiz sürümde dosya her set için oyuncu ve takım toplamlarını içerir. Pro ile ralli ralli tam kaydı içerir; böylece analiz üst üste kaybedilen sayılar gibi akışı da izleyebilir. "İki takımı da kaydet" ile kayıt tutarsanız rakibin hareketleri de kayda girer ve analiz rakibi de kapsar.'),
        ('Ralliler hızlı. İki kişi birlikte kayıt tutabilir mi?',
         'Evet. Tek başına kayıt tutarken hızlı rallilerde bir şeyler kaçar. Ortak kayıtla ikinci bir antrenör ya da takım sorumlusu kendi telefonundan bir kod veya bağlantıyla katılır ve girişler canlı olarak birleşir: örneğin biri skoru, diğeri oyuncu istatistiklerini tutar. Yardımcı telefonda yalnızca ücretsiz uygulama yeterlidir. Ana cihaz ortak kaydı 3 maç boyunca ücretsiz başlatabilir, sonrasında Pro gerekir. Açık olduğu sürece iki telefonun da internete bağlı olması gerekir.'),
    ],
    tested='RallyStat gerçek okul ve kulüp maç kayıtlarıyla test edildi ve antrenörlerin istekleriyle geliştirildi: örneğin maç içinde değişen iki libero ve servis denemeleriyle kendi servisimizde kazanılan sayıları gösteren servis istatistikleri.',
    codes=('Deneyimli istatistikçiler için: kodla giriş',
           'Zaten kodlarla kayıt tutuyorsanız, Pro klavyeyle kod girişini ekler: profesyonel analistlerin kullandığı tarzda kısa kodlarla, örneğin "11KL", ralli hızında kayıt tutarsınız. Bir maç boyunca ücretsiz deneyin.'),
)

# 경험 문장(10-28 재원님 "넣어줘", 총괄 전달): 양 팀을 기록한 실제 경기 로그로 시험한 결과. AI 질문(qa[1]) 답 끝에 붙인다.
# 근거: 요청문 점검(volleyball-coach 82a32e7) 뒤 시험에서 양 팀 강약점·가장 강한/약한 로테이션·경기 중 대응·훈련이 나옴.
AI_TESTED = {
    'en': "In tests with real match logs that included both teams, the AI analysis pointed out each team's strengths and weaknesses and its strongest and weakest rotations, with the numbers behind them, and suggested in-match adjustments and practice drills.",
    'ko': '양 팀을 모두 기록한 실제 경기 로그로 시험해 보니, AI 분석이 양 팀의 강점과 약점, 가장 강한 로테이션과 가장 약한 로테이션을 근거 숫자와 함께 짚고, 경기 중 대응과 훈련까지 추천해 줬습니다.',
    'ja': '両チームを記録した実際の試合ログで試したところ、AI分析は両チームの強みと弱み、最も強いローテーションと最も弱いローテーションを根拠の数字とともに指摘し、試合中の対応と練習メニューまで提案しました。',
    'de': 'In Tests mit echten Spielprotokollen, in denen beide Teams erfasst waren, zeigte die KI-Analyse die Stärken und Schwächen jedes Teams sowie seine stärksten und schwächsten Rotationen mit den zugehörigen Zahlen und schlug Anpassungen während des Spiels und Trainingsübungen vor.',
    'fr': "Lors de tests avec de vrais journaux de match où les deux équipes étaient notées, l'analyse IA a relevé les points forts et faibles de chaque équipe ainsi que ses meilleures et ses moins bonnes rotations, chiffres à l'appui, et a proposé des ajustements en cours de match et des exercices d'entraînement.",
    'it': "Nei test con registri reali di partite in cui erano state registrate entrambe le squadre, l'analisi IA ha indicato punti di forza e debolezze di ciascuna squadra e le sue rotazioni migliori e peggiori, con i numeri a supporto, e ha suggerito aggiustamenti durante la partita ed esercizi di allenamento.",
    'es': 'En pruebas con registros reales de partidos en los que se anotaron ambos equipos, el análisis con IA señaló las fortalezas y debilidades de cada equipo y sus rotaciones más fuertes y más débiles, con los números que lo respaldan, y sugirió ajustes durante el partido y ejercicios de entrenamiento.',
    'pt': 'Em testes com registros reais de partidas em que os dois times foram registrados, a análise de IA apontou os pontos fortes e fracos de cada time e seus rodízios mais fortes e mais fracos, com os números por trás, e sugeriu ajustes durante a partida e exercícios de treino.',
    'pl': 'W testach na prawdziwych zapisach meczów, w których zapisano obie drużyny, analiza AI wskazała mocne i słabe strony każdej drużyny oraz jej najmocniejsze i najsłabsze rotacje, podając stojące za tym liczby, i zaproponowała zmiany w trakcie meczu oraz ćwiczenia treningowe.',
    'ru': 'В тестах на реальных журналах матчей, где были записаны обе команды, ИИ-анализ указал сильные и слабые стороны каждой команды и её самые сильные и самые слабые расстановки с цифрами в подтверждение, а также предложил действия по ходу матча и тренировочные упражнения.',
    'tr': 'Her iki takımın da kaydedildiği gerçek maç kayıtlarıyla yapılan testlerde yapay zekâ analizi, her takımın güçlü ve zayıf yönlerini ve en güçlü ve en zayıf rotasyonlarını arkasındaki sayılarla birlikte gösterdi; maç içi müdahaleler ve antrenman alıştırmaları önerdi.',
}
for _k, _t in AI_TESTED.items():
    _q, _a = F[_k]['qa'][1]
    F[_k]['qa'][1] = (_q, _a + ' ' + _t)
