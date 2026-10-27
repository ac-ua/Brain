# Le Brain : comment fonctionne ton workspace

**Vivienne** — Bonjour et bienvenue. Aujourd'hui, on décortique le nouveau workspace d'Aurélien, celui qu'on a appelé le brain. L'objectif : qu'à la fin de cet épisode, il comprenne exactement comment tout fonctionne, et pourquoi.

**Rémy** — Et c'est important, parce que ce workspace va servir de base à tout ce qu'il va faire avec l'IA dans les prochains mois. Les expéditions, le sport, le contenu, le travail chez UnifyApps, l'administratif. Tout.


## Chapitre 1 — Le point de départ

**Vivienne** — Commençons par le constat. Rémy, c'était quoi, la situation de départ ?

**Rémy** — Une soixantaine de sessions Claude, dont la moitié ne sont rangées dans aucun groupe.

**Rémy** — Ensuite, la mémoire. Cinquante-cinq petits fichiers de mémoire, répartis dans vingt-trois dossiers, la plupart temporaires. Si on supprime la session, ou si on perd le Mac, tout part avec.

**Rémy** — Et à l'inverse, dans Notion, la base de mémoires ne contient qu'une seule ligne.

**Rémy** — Ajoute à ça deux Drive, un pro et un perso, quatre boîtes mail, et un Mac pro qui peut lire le GitHub perso, mais pas y écrire. On l'a testé aujourd'hui : l'envoi est bloqué par le réseau de l'entreprise.

**Rémy** — Et l'audit a trouvé une clé de récupération FileVault en clair dans une page Notion. Ça, c'est à corriger tout de suite, indépendamment du reste.

**Vivienne** — Donc le problème, ce n'est pas le manque d'outils. C'est que rien n'a de place attitrée.

**Rémy** — Exactement. Tout le reste de l'épisode, c'est la réponse à ça.


## Chapitre 2 — L'idée centrale : trois couches

**Vivienne** — Alors, l'idée centrale ?

**Rémy** — Séparer trois choses. Première couche : le savoir et l'état. Qui est Aurélien, où en est chaque projet, quelles sont les tâches. Ça vit dans Notion.

**Rémy** — Deuxième couche : le harnais. Comment on travaille. Les agents, les skills, les règles. Ça vit dans un repo GitHub privé, qu'on appelle brain.

**Rémy** — Troisième couche : l'exécution. C'est l'IA qui fait le travail. Aujourd'hui Claude Code, sur le Mac, dans le cloud, ou pilotée depuis l'iPad. Demain peut-être ChatGPT, ou un Mac mini.

**Rémy** — Et à côté, les fichiers lourds, les decks, les vidéos : ils restent dans les Drive.

**Vivienne** — Aurélien l'a résumé d'une formule : Notion, c'est la base de connaissances, GitHub, c'est la base d'action.

**Rémy** — C'est parfait. Et la clé, c'est que chaque couche est remplaçable. Si demain il change d'IA, il garde Notion et GitHub tels quels. Les formats sont ouverts : le fichier agents point M D, les skills au format skill point M D, et le protocole M C P pour les connecteurs. ChatGPT, Codex ou Gemini les comprennent aussi.


## Chapitre 3 — Notion : intégrer, pas un cerveau à part

**Vivienne** — Zoomons sur Notion. Aurélien se demandait s'il fallait un cerveau séparé, une sorte de cloud brain à part.

**Rémy** — Et la réponse, c'est non. Un cerveau à part deviendrait une deuxième vérité, jamais à jour. On intègre plutôt dans son Notion existant, en le restructurant.

**Rémy** — En haut, une page Home : le cockpit. Les tâches du jour, l'inbox, avec un filtre pro ou perso.

**Rémy** — Ensuite une petite section System, réservée à l'IA : son profil, la base de mémoires, un journal des sessions, et la Brain Inbox, dont on reparlera.

**Rémy** — Puis trois bases transverses. Tasks, une seule base pour toutes les tâches. Projects, le registre de tous les projets. Et Build Roadmap, qui fusionne les trois roadmaps qu'il avait recopiées pour Camp de Base, Element et l'app d'espagnol, et qui avaient divergé.

**Rémy** — Ensuite, une page par domaine : Work, Expeditions, Sport, Content, Admin et Finance, Career, Learning, Life. Chacun est créé depuis le même modèle.

**Rémy** — Et enfin une archive, pour Sprinklr et les vieilles pages.

**Vivienne** — Et ajouter un domaine plus tard, la finance par exemple ?

**Rémy** — Trois gestes. Dupliquer le modèle de page, ajouter une option dans la liste des domaines, et ajouter une ligne dans le fichier de règles. Rien d'autre ne casse.


## Chapitre 4 — La carte de contexte, et l'économie de tokens

**Vivienne** — Tu parles souvent de carte de contexte. C'est quoi exactement ?

**Rémy** — C'est une page courte, moins de soixante lignes, en tête de chaque domaine. L'objectif du domaine, les faits clés, les règles, et où se trouvent les choses. Par exemple pour le sport : son seuil cardiaque, son record sur semi-marathon, et le fait qu'il n'a pas de capteur de puissance sur le vélo.

**Rémy** — C'est la seule chose qu'une session charge par défaut, avec le profil et les règles. Trois petites pages au démarrage, au lieu de tout le Notion. C'est ça qui économise les tokens. On vise un démarrage autour de huit à dix mille tokens, et on va le mesurer.

**Rémy** — Il y a aussi une contrainte : le plan gratuit de Notion limite les requêtes sur les bases. Pendant l'audit, treize appels ont suffi à épuiser le quota. Donc les agents lisent par vues enregistrées et par pages courtes, et on garde peu de bases, mais larges.


## Chapitre 5 — GitHub : la base d'action

**Vivienne** — Passons à GitHub. Qu'est-ce qu'il y a dans le repo brain ?

**Rémy** — À la racine, le fichier agents point M D. C'est la constitution : les règles dures, et une table de routage qui dit, pour chaque domaine, quoi lire. Le fichier claude point M D contient juste une ligne qui pointe vers lui.

**Rémy** — Ensuite un dossier agents, avec une fiche par compétence.

**Rémy** — Un dossier skills : les savoir-faire réutilisables. Par exemple build webapp, avec son playbook des offres gratuites Cloudflare, Supabase et GitHub, qui traîne aujourd'hui dans ses Téléchargements. Ou le guide de configuration, ou les trois skills de prospection sponsors qui existent déjà.

**Rémy** — Un dossier domains, avec un petit fichier par domaine qui dit comment chaque compétence s'y applique. Et des templates, pour démarrer un nouveau projet toujours de la même façon.

**Rémy** — Enfin, des sauvegardes : un export de Notion chaque semaine par un simple script, sans IA, et la copie mensuelle du plugin UnifyApps.

**Vivienne** — Et sur le Mac pro, qui ne peut pas écrire sur GitHub, comment il récupère tout ça ?

**Rémy** — Il peut lire. Donc il clone le repo, ou installe les skills comme un plugin. Les modifications du harnais, elles, passent par une session cloud ou par l'iPad. On y revient tout à l'heure.


## Chapitre 6 — Compétences × domaines

**Vivienne** — Aurélien avait une intuition : un tableau à deux entrées.

**Rémy** — Oui, et c'est le cœur du modèle. Sur les lignes, les compétences : le Chief of Staff qui orchestre l'agenda, les mails et les tâches, le Builder qui construit les applis, le Content Studio pour la vidéo et les posts, et plus tard un Researcher, un Analyst, l'Outreach.

**Rémy** — Sur les colonnes, les domaines.

**Rémy** — Une case, c'est une compétence appliquée à un domaine. Le Builder dans le domaine Sport, c'est Element Logbook. Le même Builder dans Expeditions, c'est Camp de Base. Et c'est toujours le même playbook, la même roadmap, le même guide de configuration. Les bonnes pratiques sont écrites une fois, et elles s'appliquent partout.

**Rémy** — Pour démarrer, seulement trois agents : Chief of Staff, Builder et Content Studio. Et on les construit à partir de ce qu'on sait déjà faire, pas à partir de rien.

**Vivienne** — Pourquoi pas un agent par domaine, comme une vraie entreprise ?

**Rémy** — Parce qu'un domaine, c'est du contexte, pas un savoir-faire. Et un sous-agent consomme nettement plus de tokens qu'une skill chargée dans la session. Donc on travaille dans une session par domaine qui charge des skills, et on n'appelle un sous-agent que pour un travail lourd et isolé, comme indexer des rushes.


## Chapitre 7 — Une session, du début à la fin

**Vivienne** — Concrètement, à quoi ressemble une session ?

**Rémy** — Elle commence par lire le fichier de règles dans GitHub.

**Rémy** — Puis le profil d'Aurélien et la carte du domaine, dans Notion.

**Rémy** — Puis l'état du projet : sa fiche, sa roadmap, les tâches ouvertes.

**Rémy** — Ensuite elle travaille, en chargeant seulement les skills utiles.

**Rémy** — Et à la fin, une skill de clôture écrit ce qui a changé : les nouvelles mémoires, les tâches, la ligne de roadmap, et une ligne dans le journal des sessions.

**Vivienne** — Et la mémoire automatique de Claude, celle des dossiers locaux ?

**Rémy** — Elle reste un brouillon. Elle n'est partagée ni entre machines, ni avec le cloud. Tout ce qui compte est écrit dans Notion. Comme ça, si Aurélien perd son Mac, il reprend depuis l'iPad sans rien perdre.


## Chapitre 8 — Un brain qui apprend

**Vivienne** — Aurélien insistait sur un point : le brain doit être plastique. Il doit s'améliorer avec le temps.

**Rémy** — Pour ça, on distingue deux types d'apprentissages. Un fait, comme : l'expédition au pôle Sud est décalée à novembre deux mille vingt-sept, va directement dans Notion.

**Rémy** — Une façon de faire, comme : toujours mettre à jour le guide de configuration à chaque version, va dans une Brain Inbox, une base Notion. N'importe quelle session peut y écrire, même depuis le Mac pro.

**Rémy** — Toutes les deux semaines, une routine lit aussi les learnings côté UnifyApps, et en extrait les leçons génériques, sans nom de client.

**Rémy** — Chaque semaine, une routine cloud transforme l'inbox en modifications des skills, sous forme de pull request qu'Aurélien valide.

**Rémy** — Et le brain a sa propre roadmap, un numéro de version, un changelog, et une rétro chaque mois.

**Vivienne** — C'est la boucle des learnings UnifyApps, en fait.

**Rémy** — Exactement. Il l'a déjà construite, et elle tourne. On la réutilise pour le perso.


## Chapitre 9 — Les fichiers : entrées et sorties

**Vivienne** — Et les fichiers ? Les decks qu'il télécharge, ceux qu'on produit ?

**Rémy** — Règle simple : le Drive est la source, le disque local n'est qu'un cache jetable. Côté pro, on lit et on écrit dans le Drive UnifyApps, via le connecteur.

**Rémy** — Côté perso, depuis le Mac pro, on peut lire le Drive perso, mais pas y écrire.

**Rémy** — Donc pendant une session, les fichiers transitent par un dossier de travail temporaire.

**Rémy** — Et les sorties perso vont dans Notion, dans un artifact Claude, ou dans GitHub via une session cloud. Les artifacts, d'ailleurs, sont liés à son compte, pas à son ordinateur : ils survivent si le Mac casse.

**Rémy** — Enfin, la règle de confidentialité est à sens unique. Rien du perso ne part vers le pro. Dans l'autre sens, seules les leçons génériques passent.

**Vivienne** — Et le Drive pro, il est rangé ?

**Rémy** — Pas vraiment : environ soixante-treize fichiers en vrac à la racine, des doublons, des versions dans les noms de fichiers. On propose un dossier par client, toujours avec les mêmes sous-dossiers. Mais on le fera au moment où on touchera au domaine Work.


## Chapitre 10 — Où lancer quoi

**Vivienne** — Où est-ce qu'on lance quoi ?

**Rémy** — Sur le Mac pro, en local : tout ce qui demande un navigateur ou des fichiers pro. C'est là que Claude peut naviguer sur le web et piloter Chrome.

**Rémy** — Dans le cloud : le code perso, le harnais, et les routines planifiées, qui tournent même Mac éteint. C'est le même forfait Max, sans surcoût de machine. Par contre, pas de navigateur dans le cloud.

**Rémy** — L'iPad et le téléphone ne font pas tourner Claude Code eux-mêmes. Ce sont des télécommandes, pour piloter les sessions du Mac ou du cloud.

**Rémy** — Et un Mac mini, plus tard, deviendrait simplement une machine de plus. Comme tout l'état est dans Notion et GitHub, il n'y a rien à migrer : il clone le repo, et c'est parti.


## Chapitre 11 — Connecteurs et outils

**Vivienne** — Les connecteurs, maintenant. Aurélien a quatre boîtes mail.

**Rémy** — Oui : le Gmail pro UnifyApps, le Gmail expédition pour les sponsors, le Gmail carrière, et la boîte Hotmail perso.

**Rémy** — Aujourd'hui, les connecteurs de Claude ne gèrent qu'un compte par service. Le Gmail est branché sur la boîte expédition, l'agenda sur le compte perso, et le Drive sur le pro.

**Rémy** — Pour tout voir dans un seul cockpit, il faudra un connecteur multi-comptes, open source, hébergé par lui. On garde la porte ouverte, mais ce n'est pas la priorité.

**Rémy** — Et OpenClaw, dont il avait entendu parler ? On l'écarte pour l'instant. Il a eu de sérieux problèmes de sécurité en deux mille vingt-six, et il exige une machine allumée en permanence avec un accès complet. Pour une personne seule, des routines planifiées font le même travail d'orchestration.

**Rémy** — Côté sport, on passe par intervals point i c u, une plateforme gratuite synchronisée avec Garmin, qui a une API. Et le connecteur officiel Strava quand il prendra l'abonnement.


## Chapitre 12 — Le contenu et le montage

**Vivienne** — Parlons contenu. C'est un gros chantier.

**Rémy** — L'objectif, c'est du format court, pour TikTok et Instagram, plusieurs fois par semaine, voire tous les jours sur TikTok. Avec environ deux cents gigas de rushes, il y a de quoi tenir longtemps. La stratégie elle-même sera le premier travail du Content Studio.

**Rémy** — Pour le montage, on vise un modèle hybride. L'IA indexe les rushes : transcription, plans, tags, dans un catalogue Notion. Elle choisit les moments, écrit le script, et livre un premier montage sous forme de fichier timeline.

**Rémy** — Aurélien ouvre ce fichier dans DaVinci Resolve, sur le Mac ou sur l'iPad, et fait ses retouches lui-même, sans avoir à nous les décrire. La version gratuite de Resolve n'a pas d'API, mais elle importe ces timelines. Resolve Studio, environ trois cents dollars, ouvrirait l'API plus tard.

**Rémy** — Le vrai point d'attention, c'est la puissance de calcul. Indexer des centaines de gigas, faire tourner la transcription ou la voix clonée, ça demande une vraie machine. C'est l'argument principal pour un Mac mini.

**Vivienne** — Et la voix clonée, justement ?

**Rémy** — Uniquement quand il la demande, comme aujourd'hui. Le code pourra aller dans un repo privé séparé, les modèles se retéléchargent, et ses enregistrements de voix restent chez lui.


## Chapitre 13 — Les règles du jeu

**Vivienne** — Quelles sont les règles du jeu pour les agents ?

**Rémy** — Aucun envoi externe, aucune publication, aucun paiement sans Aurélien.

**Rémy** — Toute suppression demande son accord.

**Rémy** — Par contre, les brouillons, les mises à jour Notion et les commits sont libres. Ces règles pourront s'assouplir domaine par domaine, par exemple le jour où il voudra automatiser la prospection.

**Rémy** — Les secrets vivent dans un gestionnaire de mots de passe, jamais dans Notion, dans GitHub ou dans la mémoire.

**Rémy** — Et la confidentialité reste à sens unique : le perso ne va jamais vers le pro.


## Chapitre 14 — La migration, concrètement

**Vivienne** — Dernier point : la migration. Aurélien n'avait pas bien compris le principe du au fil de l'eau.

**Rémy** — On commence par une heure de sécurisation : la clé FileVault et les identifiants sortis de Notion, une copie des cinquante-cinq mémoires locales dans Notion pour ne rien perdre, et le playbook mis à l'abri.

**Rémy** — Ensuite, une journée pour poser le squelette : le repo brain, les trois agents, les skills de base, et dans Notion la section System, la page Home et les trois bases.

**Rémy** — Puis un test grandeur nature : on reprend une vraie tâche uniquement depuis l'iPad et le cloud, comme si le Mac était perdu.

**Rémy** — Et après, au fil de l'eau. Ça veut dire qu'on ne migre pas tout d'un coup. La prochaine fois qu'Aurélien ouvre une session sur Camp de Base, les premières minutes servent à migrer le domaine Expeditions : on rassemble les vieilles mémoires du sujet, on écrit la carte de contexte, on déplace la roadmap dans la base commune, et on coche le domaine dans la roadmap du brain. Les domaines qu'il ne touche pas restent tels quels, jusqu'au jour où il y travaille.

**Rémy** — Et une fois le squelette stable, on allume les routines : le brief du matin, la maintenance hebdomadaire, les learnings pro tous les quinze jours, et les sauvegardes.


## Pour finir — Cinq phrases à retenir

**Vivienne** — Pour conclure, Rémy, les cinq phrases à retenir ?

**Rémy** — Un : Notion sait, GitHub sait faire, l'IA exécute.

**Rémy** — Deux : une compétence s'écrit une fois, et s'applique à tous les domaines.

**Rémy** — Trois : chaque session lit peu au début, et écrit ce qui a changé à la fin.

**Rémy** — Quatre : les façons de faire passent par la Brain Inbox, et le brain s'améliore chaque semaine.

**Rémy** — Cinq : rien d'important ne vit seulement sur un ordinateur.

**Vivienne** — Merci Rémy. Et Aurélien, la suite, c'est la phase zéro. À très vite.
