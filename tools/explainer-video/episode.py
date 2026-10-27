# -*- coding: utf-8 -*-
"""Episode content: slides (HTML bodies with reveal steps) and the two-voice script.

Each slide body marks elements with data-s="n" (appear at step n),
data-on="n" (highlighted from step n) or data-dim="n" (dimmed from step n).
Each script line is (speaker, step, text). V = Vivienne (host), R = Rémy (explains).
"""

TITLE = "Le Brain : comment fonctionne ton workspace"

SLIDES = []

def slide(kicker, title, body, lines):
    SLIDES.append({"kicker": kicker, "title": title, "body": body, "lines": lines})

# 0 ─ Title
slide("", "", """
<div class="cover">
  <div class="cover-k">Podcast · 27 octobre 2026</div>
  <h1 class="cover-t">Le Brain</h1>
  <div class="cover-s">Comment fonctionne ton workspace IA, et pourquoi il est construit comme ça</div>
  <div class="cover-v">avec Vivienne &amp; Rémy</div>
</div>""", [
 ("V", 0, "Bonjour et bienvenue. Aujourd'hui, on décortique le nouveau workspace d'Aurélien, celui qu'on a appelé le brain. L'objectif : qu'à la fin de cet épisode, il comprenne exactement comment tout fonctionne, et pourquoi."),
 ("R", 0, "Et c'est important, parce que ce workspace va servir de base à tout ce qu'il va faire avec l'IA dans les prochains mois. Les expéditions, le sport, le contenu, le travail chez UnifyApps, l'administratif. Tout."),
])

# 1 ─ Starting point
slide("Chapitre 1", "Le point de départ", """
<div class="stats">
  <div class="stat" data-s="1"><b>~60</b><span>sessions Claude, dont la moitié rangées nulle part</span></div>
  <div class="stat" data-s="2"><b>55</b><span>mémoires réparties dans 23 dossiers locaux, souvent temporaires</span></div>
  <div class="stat" data-s="3"><b>1</b><span>seule mémoire dans la base Notion</span></div>
  <div class="stat" data-s="4"><b>2 · 4 · 1</b><span>Drive · boîtes mail · Mac pro qui lit GitHub perso mais n'y écrit pas</span></div>
  <div class="stat warn" data-s="5"><b>!</b><span>Clé de récupération FileVault en clair dans une page Notion</span></div>
</div>
<div class="punch" data-s="6">Le problème n'est pas le manque d'outils. C'est que rien n'a de place attitrée.</div>
""", [
 ("V", 0, "Commençons par le constat. Rémy, c'était quoi, la situation de départ ?"),
 ("R", 1, "Une soixantaine de sessions Claude, dont la moitié ne sont rangées dans aucun groupe."),
 ("R", 2, "Ensuite, la mémoire. Cinquante-cinq petits fichiers de mémoire, répartis dans vingt-trois dossiers, la plupart temporaires. Si on supprime la session, ou si on perd le Mac, tout part avec."),
 ("R", 3, "Et à l'inverse, dans Notion, la base de mémoires ne contient qu'une seule ligne."),
 ("R", 4, "Ajoute à ça deux Drive, un pro et un perso, quatre boîtes mail, et un Mac pro qui peut lire le GitHub perso, mais pas y écrire. On l'a testé aujourd'hui : l'envoi est bloqué par le réseau de l'entreprise."),
 ("R", 5, "Et l'audit a trouvé une clé de récupération FileVault en clair dans une page Notion. Ça, c'est à corriger tout de suite, indépendamment du reste."),
 ("V", 6, "Donc le problème, ce n'est pas le manque d'outils. C'est que rien n'a de place attitrée."),
 ("R", 6, "Exactement. Tout le reste de l'épisode, c'est la réponse à ça."),
])

# 2 ─ Three layers
slide("Chapitre 2", "L'idée centrale : trois couches", """
<div class="layers">
  <div class="stack">
    <div class="layer l-run" data-s="3"><em>Exécution</em><strong>L'IA qui travaille</strong><span>Claude Code sur le Mac · dans le cloud · piloté depuis l'iPad · demain ChatGPT, un Mac mini…</span></div>
    <div class="layer l-harn" data-s="2"><em>Harnais · GitHub</em><strong>Comment on travaille</strong><span>repo privé « brain » : règles, agents, skills, templates</span></div>
    <div class="layer l-know" data-s="1"><em>Savoir &amp; état · Notion</em><strong>Ce qu'on sait, où on en est</strong><span>profil, mémoires, projets, tâches, contexte par domaine</span></div>
  </div>
  <div class="side" data-s="4"><em>Fichiers · Drive</em><strong>Decks, documents, vidéos</strong><span>Drive pro<br/>Drive perso</span></div>
</div>
<div class="chips" data-s="5"><span>AGENTS.md</span><span>SKILL.md</span><span>MCP</span><i>formats ouverts, lus par Claude, ChatGPT, Codex, Gemini</i></div>
""", [
 ("V", 0, "Alors, l'idée centrale ?"),
 ("R", 1, "Séparer trois choses. Première couche : le savoir et l'état. Qui est Aurélien, où en est chaque projet, quelles sont les tâches. Ça vit dans Notion."),
 ("R", 2, "Deuxième couche : le harnais. Comment on travaille. Les agents, les skills, les règles. Ça vit dans un repo GitHub privé, qu'on appelle brain."),
 ("R", 3, "Troisième couche : l'exécution. C'est l'IA qui fait le travail. Aujourd'hui Claude Code, sur le Mac, dans le cloud, ou pilotée depuis l'iPad. Demain peut-être ChatGPT, ou un Mac mini."),
 ("R", 4, "Et à côté, les fichiers lourds, les decks, les vidéos : ils restent dans les Drive."),
 ("V", 4, "Aurélien l'a résumé d'une formule : Notion, c'est la base de connaissances, GitHub, c'est la base d'action."),
 ("R", 5, "C'est parfait. Et la clé, c'est que chaque couche est remplaçable. Si demain il change d'IA, il garde Notion et GitHub tels quels. Les formats sont ouverts : le fichier agents point M D, les skills au format skill point M D, et le protocole M C P pour les connecteurs. ChatGPT, Codex ou Gemini les comprennent aussi."),
])

# 3 ─ Notion structure
slide("Chapitre 3", "Notion : intégrer, pas un cerveau à part", """
<div class="tree">
<div data-s="1"><b>🏠 Home</b>               <i>cockpit : aujourd'hui, inbox, filtre pro / perso</i></div>
<div data-s="2"><b>⚙️ System</b>             <i>réservé à l'IA</i>
   ├─ About me             <i>profil, moins d'une page</i>
   ├─ Memories             <i>les faits, un par ligne</i>
   ├─ Session Log          <i>une ligne par session</i>
   └─ Brain Inbox          <i>les façons de faire à améliorer</i></div>
<div data-s="3"><b>📋 Tasks</b>              <i>une seule base, tous domaines</i>
<b>📁 Projects</b>           <i>le registre de tous les projets</i>
<b>🛠️ Build Roadmap</b>      <i>fusion des 3 roadmaps qui avaient divergé</i></div>
<div data-s="4"><b>── Domains ──</b>        <i>même modèle pour chacun</i>
   Work · Expeditions · Sport · Content
   Admin &amp; Finance · Career · Learning · Life</div>
<div data-s="5"><b>🗄️ Archive</b>            <i>Sprinklr, vieilles pages</i></div>
</div>
<div class="note" data-s="6">Nouveau domaine = dupliquer le modèle + une option « Domain » + une ligne de routage</div>
""", [
 ("V", 0, "Zoomons sur Notion. Aurélien se demandait s'il fallait un cerveau séparé, une sorte de cloud brain à part."),
 ("R", 0, "Et la réponse, c'est non. Un cerveau à part deviendrait une deuxième vérité, jamais à jour. On intègre plutôt dans son Notion existant, en le restructurant."),
 ("R", 1, "En haut, une page Home : le cockpit. Les tâches du jour, l'inbox, avec un filtre pro ou perso."),
 ("R", 2, "Ensuite une petite section System, réservée à l'IA : son profil, la base de mémoires, un journal des sessions, et la Brain Inbox, dont on reparlera."),
 ("R", 3, "Puis trois bases transverses. Tasks, une seule base pour toutes les tâches. Projects, le registre de tous les projets. Et Build Roadmap, qui fusionne les trois roadmaps qu'il avait recopiées pour Camp de Base, Element et l'app d'espagnol, et qui avaient divergé."),
 ("R", 4, "Ensuite, une page par domaine : Work, Expeditions, Sport, Content, Admin et Finance, Career, Learning, Life. Chacun est créé depuis le même modèle."),
 ("R", 5, "Et enfin une archive, pour Sprinklr et les vieilles pages."),
 ("V", 6, "Et ajouter un domaine plus tard, la finance par exemple ?"),
 ("R", 6, "Trois gestes. Dupliquer le modèle de page, ajouter une option dans la liste des domaines, et ajouter une ligne dans le fichier de règles. Rien d'autre ne casse."),
])

# 4 ─ Context card & tokens
slide("Chapitre 4", "La carte de contexte, et l'économie de tokens", """
<div class="two">
  <div class="card mono" data-s="1">
<b>Sport · carte de contexte</b>
<i>moins de 60 lignes</i>

Objectif · 3 buts du moment
Faits clés : seuil cardio ~170 en course,
  record semi 1 h 33, pas de capteur de puissance vélo
Règles : Element ne va jamais dans le pro
Où sont les choses : bases, repos, dossiers
Projets actifs → vue Projects
Tâches ouvertes → vue Tasks
  </div>
  <div class="col">
    <div class="kpi" data-s="2"><b>~8–10 k</b><span>tokens au démarrage d'une session : règles + profil + carte du domaine</span></div>
    <div class="kpi warn" data-s="3"><b>13</b><span>requêtes ont suffi à épuiser le quota du plan gratuit de Notion → lire par vues et pages courtes</span></div>
  </div>
</div>
""", [
 ("V", 0, "Tu parles souvent de carte de contexte. C'est quoi exactement ?"),
 ("R", 1, "C'est une page courte, moins de soixante lignes, en tête de chaque domaine. L'objectif du domaine, les faits clés, les règles, et où se trouvent les choses. Par exemple pour le sport : son seuil cardiaque, son record sur semi-marathon, et le fait qu'il n'a pas de capteur de puissance sur le vélo."),
 ("R", 2, "C'est la seule chose qu'une session charge par défaut, avec le profil et les règles. Trois petites pages au démarrage, au lieu de tout le Notion. C'est ça qui économise les tokens. On vise un démarrage autour de huit à dix mille tokens, et on va le mesurer."),
 ("R", 3, "Il y a aussi une contrainte : le plan gratuit de Notion limite les requêtes sur les bases. Pendant l'audit, treize appels ont suffi à épuiser le quota. Donc les agents lisent par vues enregistrées et par pages courtes, et on garde peu de bases, mais larges."),
])

# 5 ─ GitHub repo
slide("Chapitre 5", "GitHub : la base d'action", """
<div class="tree">
<b>ac-ua/brain</b>   <i>repo privé</i>
<div data-s="1">├─ AGENTS.md        <i>la constitution : règles dures + table de routage</i>
├─ CLAUDE.md        <i>une ligne qui pointe vers AGENTS.md</i></div><div data-s="2">├─ agents/          <i>une fiche par compétence</i>
│    chief-of-staff · builder · content-studio</div><div data-s="3">├─ skills/          <i>les savoir-faire réutilisables</i>
│    build-webapp (playbook offres gratuites) · config-guide
│    project-kickoff · session-close · sponsor-outreach…</div><div data-s="4">├─ domains/         <i>comment chaque compétence s'applique au domaine</i>
├─ templates/       <i>démarrer un projet toujours pareil</i></div><div data-s="5">└─ backups/         <i>export Notion hebdo (script, sans IA) · plugin UA mensuel</i></div>
</div>
<div class="note" data-s="6">Mac pro : lit et clone ✓ · écrit ✗ (bloqué par le réseau) → les modifs passent par le cloud ou l'iPad</div>
""", [
 ("V", 0, "Passons à GitHub. Qu'est-ce qu'il y a dans le repo brain ?"),
 ("R", 1, "À la racine, le fichier agents point M D. C'est la constitution : les règles dures, et une table de routage qui dit, pour chaque domaine, quoi lire. Le fichier claude point M D contient juste une ligne qui pointe vers lui."),
 ("R", 2, "Ensuite un dossier agents, avec une fiche par compétence."),
 ("R", 3, "Un dossier skills : les savoir-faire réutilisables. Par exemple build webapp, avec son playbook des offres gratuites Cloudflare, Supabase et GitHub, qui traîne aujourd'hui dans ses Téléchargements. Ou le guide de configuration, ou les trois skills de prospection sponsors qui existent déjà."),
 ("R", 4, "Un dossier domains, avec un petit fichier par domaine qui dit comment chaque compétence s'y applique. Et des templates, pour démarrer un nouveau projet toujours de la même façon."),
 ("R", 5, "Enfin, des sauvegardes : un export de Notion chaque semaine par un simple script, sans IA, et la copie mensuelle du plugin UnifyApps."),
 ("V", 6, "Et sur le Mac pro, qui ne peut pas écrire sur GitHub, comment il récupère tout ça ?"),
 ("R", 6, "Il peut lire. Donc il clone le repo, ou installe les skills comme un plugin. Les modifications du harnais, elles, passent par une session cloud ou par l'iPad. On y revient tout à l'heure."),
])

# 6 ─ Matrix
slide("Chapitre 6", "Compétences × domaines", """
<div class="matrix">
<table>
<tr data-on="2"><th></th><th>Work</th><th>Expeditions</th><th>Sport</th><th>Content</th><th>Admin</th><th>Career</th><th>Learning</th></tr>
<tr><th>Chief of Staff</th><td>agenda pro</td><td>échéances</td><td>semaine</td><td>calendrier</td><td>visa, impôts</td><td>relances</td><td></td></tr>
<tr><th>Builder</th><td>plateforme UA</td><td data-on="3">Camp de Base</td><td data-on="3">Element Logbook</td><td>site perso</td><td></td><td></td><td data-on="3">app espagnol</td></tr>
<tr><th>Content Studio</th><td>vidéos démo</td><td>films d'expé</td><td>clips</td><td>shorts</td><td></td><td></td><td></td></tr>
<tr data-dim="4"><th>Researcher</th><td>comptes</td><td>labos</td><td>science</td><td>tendances</td><td>règles</td><td>entreprises</td><td></td></tr>
<tr data-dim="4"><th>Analyst</th><td>prévisions</td><td>budget</td><td>Garmin</td><td>stats</td><td>budget</td><td></td><td>progrès</td></tr>
<tr data-dim="4"><th>Outreach</th><td></td><td>sponsors</td><td></td><td>marques</td><td></td><td>réseau</td><td></td></tr>
</table>
</div>
<div class="note" data-s="4">Pour démarrer : 3 agents, construits à partir de ce qu'on sait déjà faire</div>
""", [
 ("V", 0, "Aurélien avait une intuition : un tableau à deux entrées."),
 ("R", 1, "Oui, et c'est le cœur du modèle. Sur les lignes, les compétences : le Chief of Staff qui orchestre l'agenda, les mails et les tâches, le Builder qui construit les applis, le Content Studio pour la vidéo et les posts, et plus tard un Researcher, un Analyst, l'Outreach."),
 ("R", 2, "Sur les colonnes, les domaines."),
 ("R", 3, "Une case, c'est une compétence appliquée à un domaine. Le Builder dans le domaine Sport, c'est Element Logbook. Le même Builder dans Expeditions, c'est Camp de Base. Et c'est toujours le même playbook, la même roadmap, le même guide de configuration. Les bonnes pratiques sont écrites une fois, et elles s'appliquent partout."),
 ("R", 4, "Pour démarrer, seulement trois agents : Chief of Staff, Builder et Content Studio. Et on les construit à partir de ce qu'on sait déjà faire, pas à partir de rien."),
 ("V", 4, "Pourquoi pas un agent par domaine, comme une vraie entreprise ?"),
 ("R", 4, "Parce qu'un domaine, c'est du contexte, pas un savoir-faire. Et un sous-agent consomme nettement plus de tokens qu'une skill chargée dans la session. Donc on travaille dans une session par domaine qui charge des skills, et on n'appelle un sous-agent que pour un travail lourd et isolé, comme indexer des rushes."),
])

# 7 ─ Session lifecycle
slide("Chapitre 7", "Une session, du début à la fin", """
<div class="flow">
  <div class="step" data-s="1"><em>1 · GitHub</em><strong>Lire les règles</strong><span>AGENTS.md</span></div>
  <div class="arrow" data-s="2">→</div>
  <div class="step" data-s="2"><em>2 · Notion</em><strong>Profil + carte</strong><span>du domaine</span></div>
  <div class="arrow" data-s="3">→</div>
  <div class="step" data-s="3"><em>3 · Notion</em><strong>État du projet</strong><span>fiche, roadmap, tâches</span></div>
  <div class="arrow" data-s="4">→</div>
  <div class="step" data-s="4"><em>4 · Travail</em><strong>Skills utiles</strong><span>seulement</span></div>
  <div class="arrow" data-s="5">→</div>
  <div class="step hot" data-s="5"><em>5 · Notion</em><strong>Écrire ce qui a changé</strong><span>mémoires, tâches, roadmap, journal</span></div>
</div>
<div class="note" data-s="6">La mémoire locale de Claude n'est qu'un brouillon : rien d'important ne vit seulement sur un ordinateur</div>
""", [
 ("V", 0, "Concrètement, à quoi ressemble une session ?"),
 ("R", 1, "Elle commence par lire le fichier de règles dans GitHub."),
 ("R", 2, "Puis le profil d'Aurélien et la carte du domaine, dans Notion."),
 ("R", 3, "Puis l'état du projet : sa fiche, sa roadmap, les tâches ouvertes."),
 ("R", 4, "Ensuite elle travaille, en chargeant seulement les skills utiles."),
 ("R", 5, "Et à la fin, une skill de clôture écrit ce qui a changé : les nouvelles mémoires, les tâches, la ligne de roadmap, et une ligne dans le journal des sessions."),
 ("V", 6, "Et la mémoire automatique de Claude, celle des dossiers locaux ?"),
 ("R", 6, "Elle reste un brouillon. Elle n'est partagée ni entre machines, ni avec le cloud. Tout ce qui compte est écrit dans Notion. Comme ça, si Aurélien perd son Mac, il reprend depuis l'iPad sans rien perdre."),
])

# 8 ─ Plasticity loop
slide("Chapitre 8", "Un brain qui apprend", """
<div class="loop">
  <div class="row" data-s="1"><div class="b">Session</div><div class="a">un fait →</div><div class="b k">Notion · Memories</div><div class="ex">« Pôle Sud décalé à novembre 2027 »</div></div>
  <div class="row" data-s="2"><div class="b">Session</div><div class="a">une façon de faire →</div><div class="b h">Brain Inbox</div><div class="ex">« toujours mettre à jour le guide à chaque version »</div></div>
  <div class="row" data-s="3"><div class="b">Learnings UnifyApps</div><div class="a">tous les 15 jours →</div><div class="b h">Brain Inbox</div><div class="ex">leçons génériques, sans nom de client</div></div>
  <div class="row" data-s="4"><div class="b h">Brain Inbox</div><div class="a">chaque semaine →</div><div class="b g">PR sur brain</div><div class="ex">Aurélien valide</div></div>
  <div class="row" data-s="5"><div class="b g">brain v0.x</div><div class="a"></div><div class="b">roadmap · changelog</div><div class="ex">rétro chaque mois</div></div>
</div>
""", [
 ("V", 0, "Aurélien insistait sur un point : le brain doit être plastique. Il doit s'améliorer avec le temps."),
 ("R", 1, "Pour ça, on distingue deux types d'apprentissages. Un fait, comme : l'expédition au pôle Sud est décalée à novembre deux mille vingt-sept, va directement dans Notion."),
 ("R", 2, "Une façon de faire, comme : toujours mettre à jour le guide de configuration à chaque version, va dans une Brain Inbox, une base Notion. N'importe quelle session peut y écrire, même depuis le Mac pro."),
 ("R", 3, "Toutes les deux semaines, une routine lit aussi les learnings côté UnifyApps, et en extrait les leçons génériques, sans nom de client."),
 ("R", 4, "Chaque semaine, une routine cloud transforme l'inbox en modifications des skills, sous forme de pull request qu'Aurélien valide."),
 ("R", 5, "Et le brain a sa propre roadmap, un numéro de version, un changelog, et une rétro chaque mois."),
 ("V", 5, "C'est la boucle des learnings UnifyApps, en fait."),
 ("R", 5, "Exactement. Il l'a déjà construite, et elle tourne. On la réutilise pour le perso."),
])

# 9 ─ Files
slide("Chapitre 9", "Les fichiers : entrées et sorties", """
<div class="files">
  <div class="fcol" data-s="1"><em>Pro</em><div class="b">Drive UnifyApps</div><span>lecture ✓ · écriture ✓</span></div>
  <div class="fmid" data-s="3"><em>Session</em><div class="b">dossier de travail</div><span>cache jetable : entrées → sorties</span></div>
  <div class="fcol" data-s="2"><em>Perso</em><div class="b">Drive perso</div><span>lecture ✓ · écriture ✗ depuis le Mac pro</span>
    <div class="outs" data-s="4"><div class="b k">Notion</div><div class="b k">Artifacts</div><div class="b k">GitHub via cloud</div></div></div>
</div>
<div class="oneway" data-s="5"><span class="no">Perso → Pro : jamais</span><span class="yes">Pro → Perso : leçons génériques seulement</span></div>
""", [
 ("V", 0, "Et les fichiers ? Les decks qu'il télécharge, ceux qu'on produit ?"),
 ("R", 1, "Règle simple : le Drive est la source, le disque local n'est qu'un cache jetable. Côté pro, on lit et on écrit dans le Drive UnifyApps, via le connecteur."),
 ("R", 2, "Côté perso, depuis le Mac pro, on peut lire le Drive perso, mais pas y écrire."),
 ("R", 3, "Donc pendant une session, les fichiers transitent par un dossier de travail temporaire."),
 ("R", 4, "Et les sorties perso vont dans Notion, dans un artifact Claude, ou dans GitHub via une session cloud. Les artifacts, d'ailleurs, sont liés à son compte, pas à son ordinateur : ils survivent si le Mac casse."),
 ("R", 5, "Enfin, la règle de confidentialité est à sens unique. Rien du perso ne part vers le pro. Dans l'autre sens, seules les leçons génériques passent."),
 ("V", 5, "Et le Drive pro, il est rangé ?"),
 ("R", 5, "Pas vraiment : environ soixante-treize fichiers en vrac à la racine, des doublons, des versions dans les noms de fichiers. On propose un dossier par client, toujours avec les mêmes sous-dossiers. Mais on le fera au moment où on touchera au domaine Work."),
])

# 10 ─ Where to run
slide("Chapitre 10", "Où lancer quoi", """
<div class="grid4">
  <div class="card" data-s="1"><em>Mac pro · local</em><ul><li class="y">navigateur, Chrome</li><li class="y">fichiers pro</li><li class="n">écrire sur GitHub perso</li></ul></div>
  <div class="card" data-s="2"><em>Cloud</em><ul><li class="y">code perso, harnais</li><li class="y">routines, Mac éteint</li><li class="y">même forfait Max</li><li class="n">pas de navigateur</li></ul></div>
  <div class="card" data-s="3"><em>iPad · Android</em><ul><li class="y">télécommande</li><li class="n">pas de Claude Code local</li></ul></div>
  <div class="card dash" data-s="4"><em>Mac mini · plus tard</em><ul><li class="y">clone le repo, et c'est parti</li><li class="y">vidéo, modèles locaux</li></ul></div>
</div>
""", [
 ("V", 0, "Où est-ce qu'on lance quoi ?"),
 ("R", 1, "Sur le Mac pro, en local : tout ce qui demande un navigateur ou des fichiers pro. C'est là que Claude peut naviguer sur le web et piloter Chrome."),
 ("R", 2, "Dans le cloud : le code perso, le harnais, et les routines planifiées, qui tournent même Mac éteint. C'est le même forfait Max, sans surcoût de machine. Par contre, pas de navigateur dans le cloud."),
 ("R", 3, "L'iPad et le téléphone ne font pas tourner Claude Code eux-mêmes. Ce sont des télécommandes, pour piloter les sessions du Mac ou du cloud."),
 ("R", 4, "Et un Mac mini, plus tard, deviendrait simplement une machine de plus. Comme tout l'état est dans Notion et GitHub, il n'y a rien à migrer : il clone le repo, et c'est parti."),
])

# 11 ─ Connectors
slide("Chapitre 11", "Connecteurs et outils", """
<div class="two">
  <div class="col">
    <div class="mail" data-s="1">Gmail pro · UnifyApps <span class="tag" data-s="2">Drive branché</span></div>
    <div class="mail" data-s="1">Gmail expédition · sponsors <span class="tag" data-s="2">Gmail branché</span></div>
    <div class="mail" data-s="1">Gmail carrière</div>
    <div class="mail" data-s="1">Hotmail perso <span class="tag" data-s="2">agenda branché</span></div>
  </div>
  <div class="col">
    <div class="kpi" data-s="3"><b>plus tard</b><span>un connecteur multi-comptes, open source, hébergé par toi</span></div>
    <div class="kpi warn" data-s="4"><b>OpenClaw</b><span>écarté : failles de sécurité en 2026, machine allumée en permanence</span></div>
    <div class="kpi" data-s="5"><b>Sport</b><span>Garmin → intervals.icu (gratuit) · connecteur Strava officiel avec l'abonnement</span></div>
  </div>
</div>
""", [
 ("V", 0, "Les connecteurs, maintenant. Aurélien a quatre boîtes mail."),
 ("R", 1, "Oui : le Gmail pro UnifyApps, le Gmail expédition pour les sponsors, le Gmail carrière, et la boîte Hotmail perso."),
 ("R", 2, "Aujourd'hui, les connecteurs de Claude ne gèrent qu'un compte par service. Le Gmail est branché sur la boîte expédition, l'agenda sur le compte perso, et le Drive sur le pro."),
 ("R", 3, "Pour tout voir dans un seul cockpit, il faudra un connecteur multi-comptes, open source, hébergé par lui. On garde la porte ouverte, mais ce n'est pas la priorité."),
 ("R", 4, "Et OpenClaw, dont il avait entendu parler ? On l'écarte pour l'instant. Il a eu de sérieux problèmes de sécurité en deux mille vingt-six, et il exige une machine allumée en permanence avec un accès complet. Pour une personne seule, des routines planifiées font le même travail d'orchestration."),
 ("R", 5, "Côté sport, on passe par intervals point i c u, une plateforme gratuite synchronisée avec Garmin, qui a une API. Et le connecteur officiel Strava quand il prendra l'abonnement."),
])

# 12 ─ Content
slide("Chapitre 12", "Le contenu et le montage", """
<div class="banner" data-s="1">Format court · TikTok + Instagram · plusieurs posts par semaine</div>
<div class="flow">
  <div class="step" data-s="2"><em>IA</em><strong>Indexer</strong><span>transcription, plans, tags → Notion</span></div>
  <div class="arrow" data-s="2">→</div>
  <div class="step" data-s="2"><em>IA</em><strong>Choisir + script</strong><span>les meilleurs moments</span></div>
  <div class="arrow" data-s="2">→</div>
  <div class="step" data-s="2"><em>IA</em><strong>Premier montage</strong><span>fichier timeline FCPXML</span></div>
  <div class="arrow" data-s="3">→</div>
  <div class="step hot" data-s="3"><em>Toi</em><strong>Retouches</strong><span>DaVinci Resolve, Mac ou iPad</span></div>
  <div class="arrow" data-s="3">→</div>
  <div class="step" data-s="3"><em>Toi</em><strong>Publier</strong><span>à la main, au début</span></div>
</div>
<div class="note warn" data-s="4">Calcul lourd (200 Go de rushes, voix, transcription) → l'argument principal pour un Mac mini</div>
""", [
 ("V", 0, "Parlons contenu. C'est un gros chantier."),
 ("R", 1, "L'objectif, c'est du format court, pour TikTok et Instagram, plusieurs fois par semaine, voire tous les jours sur TikTok. Avec environ deux cents gigas de rushes, il y a de quoi tenir longtemps. La stratégie elle-même sera le premier travail du Content Studio."),
 ("R", 2, "Pour le montage, on vise un modèle hybride. L'IA indexe les rushes : transcription, plans, tags, dans un catalogue Notion. Elle choisit les moments, écrit le script, et livre un premier montage sous forme de fichier timeline."),
 ("R", 3, "Aurélien ouvre ce fichier dans DaVinci Resolve, sur le Mac ou sur l'iPad, et fait ses retouches lui-même, sans avoir à nous les décrire. La version gratuite de Resolve n'a pas d'API, mais elle importe ces timelines. Resolve Studio, environ trois cents dollars, ouvrirait l'API plus tard."),
 ("R", 4, "Le vrai point d'attention, c'est la puissance de calcul. Indexer des centaines de gigas, faire tourner la transcription ou la voix clonée, ça demande une vraie machine. C'est l'argument principal pour un Mac mini."),
 ("V", 4, "Et la voix clonée, justement ?"),
 ("R", 4, "Uniquement quand il la demande, comme aujourd'hui. Le code pourra aller dans un repo privé séparé, les modèles se retéléchargent, et ses enregistrements de voix restent chez lui."),
])

# 13 ─ Rules
slide("Chapitre 13", "Les règles du jeu", """
<div class="rules">
  <div data-s="1"><span class="ic n">✕</span>Aucun envoi externe, aucune publication, aucun paiement sans toi</div>
  <div data-s="2"><span class="ic q">?</span>Toute suppression demande ton accord</div>
  <div data-s="3"><span class="ic y">✓</span>Brouillons, mises à jour Notion et commits : libres</div>
  <div data-s="4"><span class="ic k">⚿</span>Secrets dans le gestionnaire de mots de passe, jamais dans Notion, GitHub ou la mémoire</div>
  <div data-s="5"><span class="ic k">⇢</span>Confidentialité à sens unique : le perso ne va jamais vers le pro</div>
</div>
""", [
 ("V", 0, "Quelles sont les règles du jeu pour les agents ?"),
 ("R", 1, "Aucun envoi externe, aucune publication, aucun paiement sans Aurélien."),
 ("R", 2, "Toute suppression demande son accord."),
 ("R", 3, "Par contre, les brouillons, les mises à jour Notion et les commits sont libres. Ces règles pourront s'assouplir domaine par domaine, par exemple le jour où il voudra automatiser la prospection."),
 ("R", 4, "Les secrets vivent dans un gestionnaire de mots de passe, jamais dans Notion, dans GitHub ou dans la mémoire."),
 ("R", 5, "Et la confidentialité reste à sens unique : le perso ne va jamais vers le pro."),
])

# 14 ─ Migration
slide("Chapitre 14", "La migration, concrètement", """
<div class="timeline">
  <div class="ph" data-s="1"><em>Phase 0 · 1 heure</em><strong>Sécuriser</strong><span>FileVault et identifiants hors de Notion · copie des 55 mémoires · playbook à l'abri</span></div>
  <div class="ph" data-s="2"><em>Phase 1 · 1 journée</em><strong>Poser le squelette</strong><span>repo brain, 3 agents, skills de base · System, Home et 3 bases dans Notion</span></div>
  <div class="ph" data-s="3"><em>Test</em><strong>Exercice « Mac perdu »</strong><span>reprendre une vraie tâche depuis l'iPad et le cloud uniquement</span></div>
  <div class="ph hot" data-s="4"><em>Au fil de l'eau</em><strong>Chaque domaine migre quand on y travaille</strong><span>ex. prochaine session Camp de Base → vieilles mémoires rassemblées, carte Expeditions écrite, roadmap déplacée, domaine coché</span></div>
  <div class="ph" data-s="5"><em>Ensuite</em><strong>Allumer les routines</strong><span>brief du matin · maintenance hebdo · learnings pro · sauvegardes</span></div>
</div>
""", [
 ("V", 0, "Dernier point : la migration. Aurélien n'avait pas bien compris le principe du au fil de l'eau."),
 ("R", 1, "On commence par une heure de sécurisation : la clé FileVault et les identifiants sortis de Notion, une copie des cinquante-cinq mémoires locales dans Notion pour ne rien perdre, et le playbook mis à l'abri."),
 ("R", 2, "Ensuite, une journée pour poser le squelette : le repo brain, les trois agents, les skills de base, et dans Notion la section System, la page Home et les trois bases."),
 ("R", 3, "Puis un test grandeur nature : on reprend une vraie tâche uniquement depuis l'iPad et le cloud, comme si le Mac était perdu."),
 ("R", 4, "Et après, au fil de l'eau. Ça veut dire qu'on ne migre pas tout d'un coup. La prochaine fois qu'Aurélien ouvre une session sur Camp de Base, les premières minutes servent à migrer le domaine Expeditions : on rassemble les vieilles mémoires du sujet, on écrit la carte de contexte, on déplace la roadmap dans la base commune, et on coche le domaine dans la roadmap du brain. Les domaines qu'il ne touche pas restent tels quels, jusqu'au jour où il y travaille."),
 ("R", 5, "Et une fois le squelette stable, on allume les routines : le brief du matin, la maintenance hebdomadaire, les learnings pro tous les quinze jours, et les sauvegardes."),
])

# 15 ─ Recap
slide("Pour finir", "Cinq phrases à retenir", """
<div class="recap">
  <div data-s="1"><b>1</b>Notion sait, GitHub sait faire, l'IA exécute.</div>
  <div data-s="2"><b>2</b>Une compétence s'écrit une fois et s'applique à tous les domaines.</div>
  <div data-s="3"><b>3</b>Chaque session lit peu au début, et écrit ce qui a changé à la fin.</div>
  <div data-s="4"><b>4</b>Les façons de faire passent par la Brain Inbox : le brain s'améliore chaque semaine.</div>
  <div data-s="5"><b>5</b>Rien d'important ne vit seulement sur un ordinateur.</div>
</div>
""", [
 ("V", 0, "Pour conclure, Rémy, les cinq phrases à retenir ?"),
 ("R", 1, "Un : Notion sait, GitHub sait faire, l'IA exécute."),
 ("R", 2, "Deux : une compétence s'écrit une fois, et s'applique à tous les domaines."),
 ("R", 3, "Trois : chaque session lit peu au début, et écrit ce qui a changé à la fin."),
 ("R", 4, "Quatre : les façons de faire passent par la Brain Inbox, et le brain s'améliore chaque semaine."),
 ("R", 5, "Cinq : rien d'important ne vit seulement sur un ordinateur."),
 ("V", 5, "Merci Rémy. Et Aurélien, la suite, c'est la phase zéro. À très vite."),
])
