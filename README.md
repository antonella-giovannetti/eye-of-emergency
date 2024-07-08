# eye-of-emergency

## Présentation du projet :
Ce projet a pour but de nous initié aux **Natural Language Processing (NLP)** et de nous faire découvrir les différentes méthodes de traitement de texte.   
Pour cela, nous avons utilisé deux jeux de tweets en anglais : un jeu de tweets d'entrainement et un jeu de tweets de test.   
Les jeux de données se présentent sous forme de fichiers csv avec :
- une colonne `id` : l'identifiant unique du tweet,
- une colonne `text` : le contenu du tweet,
- une colonne `location` : la localisation de l'utilisateur ayant posté le tweet,
- une colonne `keyword` : le mot-clé associé au tweet.

Le jeu d'entraiement contient également :
- une colonne `target` : la cible du tweet (0 pour un tweet normal et 1 pour un tweet signalant une catastrophe).

## Veille sur le traitement du langage 

### Text mining (exploration de texte)
Le text mining consiste à examiner de grandes collections de documents pour découvrir de nouvelles informations ou aider à répondre à des questions de recherche spécifiques. 

L'exploration de texte permet d'identifier des faits, des relations et des affirmations qui, autrement, resteraient enfouis dans la masse de données textuelles volumineuses. Une fois extraites, ces informations sont converties en une forme structurée qui peut être analysée plus en détail ou présentée directement à l'aide de tableaux HTML groupés, de cartes mentales, de graphiques, etc. L'exploration de texte utilise diverses méthodologies pour traiter le texte, l'une des plus importantes étant le traitement du langage naturel (NLP) . 

### Natural language processing NLP (traitement du langage naturel)
Le traitement du langage naturel est l'application de techniques informatiques à l'analyse et à la synthèse du langage naturel et de la parole, il aide les machines à "lire" des informations textuelles en simulant la capacité humaine à comprendre, interpréter et générer du langage. Il vise à combler le fossé des communications entre les humains et les ordinateurs en facilitant une interface en langage naturel. L'aspect clé du NLP est la compréhension du langage naturel, qui décrit la capacité d'un système à "lire" ou "écouter", à reconnaître et à généraliser les significations contextuelles intégrées dans diverses expressions textuelles. Un autre aspect clé et populaire du NLP est la génération de langage naturel, qui vise à générer des représentations linguistiques significatives pour "répondre" à l'humain. Les applications populaires rendues possibles par le NLP comprennent les chatbots, les systèmes de questions-réponses, les outils de résumé, les services de traduction automatique, les assistants vocaux, etc

La différence entre l’exploration de texte et le NLP ? Ils ne sont pas identiques mais étroitement liés. On peut avoir du NLP sans text mining, mais il serait difficile de faire du text mining sans NLP.

### Les sous domaines du NLP et techniques différentes
#### L'analyse des sentiments
L'analyse des sentiments, également connue sous le nom d'exploration d'opinions, est un sous-domaine du traitement du langage naturel qui consiste à déterminer et à se concentrer sur les données émotionnelles dans un texte d'information. Il peut s'agir d'une évaluation, d'une appréciation ou d'une inclination à propos d'un point ou d'un élément spécifique. Voici les principaux types d'analyse des sentiments :

- **Analyse fine des sentiments** : elle va au-delà des simples évaluations positives, négatives ou neutres. Elle implique des évaluations très spécifiques, comme une note de 5 étoiles, par exemple.
- **Détection d'émotions** : Cela vise à détecter des émotions comme le bonheur, la frustration, la colère, la tristesse, etc. Le plus grand défi ici est de pouvoir identifier avec précision ces émotions dans le texte.
- **Analyse des sentiments basée sur les aspects** : elle est généralement utilisée pour comprendre des aspects spécifiques d'un produit ou d'un service donné. Par exemple, dans un avis du type « L'autonomie de la batterie de ce téléphone est excellente, mais l'écran n'est pas très clair », le sentiment envers l'autonomie de la batterie est positif, mais il est négatif envers l'écran.
- **Analyse des sentiments multilingues** : cela peut être particulièrement difficile car le même mot peut transmettre des sentiments différents dans différentes langues.
- **Analyse d'intention** : Cette étape permet de comprendre l'intention de l'utilisateur derrière une certaine déclaration. Par exemple, une déclaration telle que « J'aurais besoin d'une voiture » peut indiquer une intention d'achat.

L'analyse des sentiments à l'aide du NLP est une tâche complexe en raison du caractère inné du langage humain. La moquerie, par exemple, est particulièrement difficile à identifier. Par conséquent, la précision de l'analyse des sentiments dépend généralement de la complexité de la tâche et de la capacité du système à tirer parti d'un grand nombre d'informations.

#### La reconaissance d'entités nommées (NER)
La reconnaissance d'entités nommées est une méthode de traitement du langage naturel qui extrait des informations d'un texte. La NER consiste à détecter et à catégoriser des informations importantes dans un texte, appelées entités nommées. Les entités nommées font référence aux sujets clés d'un texte, tels que les noms, les lieux, les entreprises, les événements et les produits, ainsi que les thèmes, les sujets, les heures, les valeurs monétaires et les pourcentages. Il est particulièrement utile pour extraire rapidement des informations clés à partir de grandes quantités de données, car il automatise le processus d'extraction.

Le NER fournit aux organisations des informations essentielles sur leurs clients, leurs produits, la concurrence et les tendances du marché.

Par exemple, les entreprises l'utilisent pour détecter quand elles sont mentionnées dans des publications. Les prestataires de soins de santé l'utilisent pour extraire des informations médicales clés des dossiers des patients.

#### Le marquage POS (Parties Of Speech)
Le marquage de parties de la parole est une activité linguistique de traitement du langage naturel dans laquelle chaque mot d'un document se voit attribuer une partie particulière du discours (adverbe, adjectif, verbe, etc.) ou une catégorie grammaticale. Grâce à l'ajout d'une couche d'informations syntaxiques et sémantiques aux mots, cette procédure facilite la compréhension de la structure et du sens de la phrase.

Dans les applications NLP, le marquage POS est utile pour la traduction automatique, la reconnaissance d'entités nommées et l'extraction d'informations, entre autres. Cela fonctionne également bien pour dissiper l’ambiguïté de termes ayant de nombreuses significations et révéler la structure grammaticale d’une phrase.

**Exemple d'étiquetage POS**

Considérons la phrase : « Le rapide renard brun saute par-dessus le chien paresseux. »

Après avoir effectué le marquage POS :

"Le" est étiqueté comme déterminant (DT)
"rapide" est étiqueté comme adjectif (JJ)
"marron" est étiqueté comme adjectif (JJ)
"renard" est étiqueté comme nom (NN)
« sauter » est étiqueté comme verbe (VBZ)
« plus » est étiqueté comme préposition (IN)
"le" est étiqueté comme déterminant (DT)
"paresseux" est étiqueté comme adjectif (JJ)
"chien" est étiqueté comme nom (NN)

En offrant un aperçu de la structure grammaticale, ce balisage aide les machines à comprendre non seulement les mots individuels, mais également les liens entre eux au sein d'une phrase. Pour de nombreuses applications PNL , comme le résumé de texte, l’analyse des sentiments et la traduction automatique, ce type de données est essentiel.

### Exemples d'applications concrètes du NLP 
Le NLP trouve des applications variées dans notre vie quotidienne et dans le monde des affaires :

- **Relation client** : Les technologies de traitement du langage naturel sont utilisées pour automatiser la gestion des interactions clients. Elles permettent de recevoir, classifier, distribuer et analyser les messages des utilisateurs, tels que les emails, les tweets, les SMS, et divers documents. De plus, la transcription automatique de l'audio ou la prise de notes lors de conversations ou de réunions sont désormais largement disponibles. Grâce au NLP, les gains de productivité dans la gestion de la relation client sont considérables, transformant ainsi les méthodes et les outils de la Gestion de la Relation Client (GRC).
- **Chatbots** : Les chatbots modernes, tels que ChatGPT, utilisent les technologies de NLP pour interagir de manière conversationnelle avec les utilisateurs, que ce soit sur le web ou sur mobile. Ces applications répondent aux demandes des utilisateurs en mode conversationnel, offrant ainsi une expérience utilisateur plus interactive et personnalisée.
- **Classification de texte** : La classification de texte consiste à identifier des caractéristiques spécifiques dans un texte donné. Les classificateurs de texte sont employés pour mettre en ordre, structurer et catégoriser d'importants volumes de contenus textuels non structurés. Par exemple, ils peuvent être utilisés pour trier des articles de presse dans des catégories spécifiques ou pour classer des commentaires de clients en fonction de leur sentiment.
- **Correction automatique** : La correction automatique est devenue courante dans la plupart des éditeurs de texte (vous l'utilisez tout les jours). Les outils de correction orthographique proposent des suggestions de corrections en temps réel pendant la rédaction, améliorant ainsi la qualité et l'exactitude du texte final.
- **Traduction automatique** : Le développement d'algorithmes de traduction automatique a bouleversé la gestion des langues. Cette fonctionnalité est désormais largement disponible pour des centaines de langues, permettant aux utilisateurs de communiquer et d'accéder à l'information dans différentes langues sans effort.
- **Extraction des données après un OCR** : Le NLP facilite l'extraction automatique des principales informations à partir de documents tels que les reçus, les factures, les chèques et les fiches produits. Les données extraites sont ensuite stockées dans un format adapté aux traitements et au stockage ultérieur, simplifiant ainsi la gestion de l'information.
- **Résumé automatique** : Les technologies de NLP sont également exploitées pour générer des résumés concis de documents texte plus longs. Cette fonctionnalité est très utile pour les outils de veille et de recherche documentaire, permettant aux utilisateurs de gagner du temps en obtenant des informations essentielles rapidement.

### Les stop-word 
Les mots vides sont des mots courants dans une langue qui sont souvent filtrés lors des tâches de NLP car ils sont considérés comme ayant peu de sens ou contribuant peu à la compréhension globale d'un texte. Les exemples incluent « le », « est », « et », « dans », etc.

Les mots vides sont supprimés en NLP pour se concentrer sur les mots les plus significatifs et informatifs d'un texte. Ceci est souvent fait pour réduire le bruit, améliorer l'efficacité du traitement et mettre en évidence les mots-clés qui portent le sens essentiel du texte.

### Les caractères spéciaux et la ponctuation 
Les caractères spéciaux et la ponctuation peuvent compliquer la lecture des mots. Ils peuvent perturber les machines qui tentent de comprendre les mots ou d'en déterminer le sens. Nous les supprimons donc pour que les machines comprennent mieux les mots et puissent faire leur travail, comme comprendre le sens des mots ou découvrir ce que les gens ressentent à l'écrit. 

Voici quelques exemples de caractères spéciaux et de ponctuation qui sont souvent supprimés :
| # ‘«  , .% & ^*! @ ( ) _ = – [ ]$ > \ { } ` ~; : / ? <

### La tokenisation et les N-gram
La tokenisation, dans le domaine du traitement du langage naturel (NLP) et de l'apprentissage automatique , fait référence au processus de conversion d'une séquence de texte en parties plus petites, appelées tokens. Ces tokens peuvent être aussi petits que des caractères ou aussi longs que des mots. La principale raison pour laquelle ce processus est important est qu'il aide les machines à comprendre le langage humain en le décomposant en éléments de la taille d'une bouchée, plus faciles à analyser.

L'objectif principal de la tokenisation est de représenter un texte de manière à ce qu'il soit significatif pour les machines sans perdre son contexte. En convertissant le texte en tokens, les algorithmes peuvent plus facilement identifier des modèles. Cette reconnaissance de modèles est cruciale car elle permet aux machines de comprendre et de répondre aux entrées humaines. Par exemple, lorsqu'une machine rencontre le mot « running », elle ne le voit pas comme une entité singulière mais plutôt comme une combinaison de tokens qu'elle peut analyser et dont elle peut tirer un sens.

Les méthodes de tokenisation varient en fonction de la granularité de la décomposition du texte et des exigences spécifiques de la tâche à accomplir. Ces méthodes peuvent aller de la dissection du texte en mots individuels à leur décomposition en caractères ou même en unités plus petites. Voici un aperçu plus détaillé des différents types :

- **Tokenisation des mots** : Cette méthode décompose le texte en mots individuels. C'est l'approche la plus courante et elle est particulièrement efficace pour les langues avec des limites de mots claires comme l'anglais.
- **Tokenisation des caractères** : Dans ce cas, le texte est segmenté en caractères individuels. Cette méthode est utile pour les langues qui ne disposent pas de limites de mots claires ou pour les tâches qui nécessitent une analyse granulaire, comme la correction orthographique.
- **Tokenisation de sous-mots** : En trouvant un équilibre entre la tokenisation de mots et de caractères, cette méthode divise le texte en unités qui peuvent être plus grandes qu'un seul caractère mais plus petites qu'un mot complet. Par exemple, les « chatbots » peuvent être tokenisés en « chat » et « bots ». Cette approche est particulièrement utile pour les langues qui forment un sens en combinant des unités plus petites ou lorsqu'il s'agit de mots hors vocabulaire dans les tâches de PNL.


Un N-gram est une séquence contiguë de n éléments provenant d'un échantillon donné de texte ou de discours. Ces éléments peuvent être des mots, des lettres, des syllabes ou des phonèmes, selon le niveau de granularité que nous souhaitons utiliser. Un modèle N-gram est un modèle statistique du langage qui utilise une séquence de n éléments pour prédire la probabilité de l'élément suivant de la séquence.

La valeur de n détermine le nombre de token dans un N-gram. Les valeurs courantes de n dans les tâches de NLP vont de 1 à 5, bien que n'importe quelle valeur entière de n puisse être utilisée. Les N-gram avec des valeurs de n plus grandes sont souvent appelés « N-gram d'ordre supérieur ».

Les N-gram sont un élément essentiel de nombreuses tâches de PNL. Ils sont utilisés pour modéliser la distribution de probabilité d'une séquence donnée et peuvent être utilisés pour faire des prédictions sur le prochain jeton d'une séquence. Par exemple, dans une tâche de modélisation du langage, un modèle n-gramme peut être utilisé pour prédire le mot suivant dans une phrase, compte tenu des n-1 mots précédents.

De plus, les N-gram peuvent également être utilisés pour extraire des caractéristiques de données textuelles afin de les utiliser dans d'autres tâches de traitement du langage naturel, telles que la classification de texte et l'analyse des sentiments. En capturant la cooccurrence de token dans une séquence, les N-gram peuvent capturer des informations contextuelles importantes qui peuvent ne pas être capturées par des token individuels.

### Stemming et lemmatization 
La lemmatisation et la stemming sont des techniques de normalisation de texte dans le domaine du traitement du langage naturel qui sont utilisées pour préparer le texte, les mots et les documents en vue d'un traitement ultérieur.

Le stemming consiste principalement à supprimer les affixes des mots, ce qui peut aboutir à un mot invalide dans le dictionnaire. Par exemple, après l'étape de stemming, les mots « requiring », « required » et « requirement » seront réduits à « require ».

La lemmatisation utilise le vocabulaire et l'analyse morphologique pour supprimer les affixes des mots. Par exemple, "building has floors" se réduit à "build have floor" après lemmatisation.

Comparaison des deux approches :

- La lemmatisation utilise le vocabulaire et l'analyse morphologique, tandis que le stemming utilise des règles heuristiques simples
- La lemmatisation renvoie les formes des mots qu'on trouve dans le dictionnaire, alors que le stemming peut aboutir à des mots invalides.

### Méthode de transformation de texte en vecteur
L’un des problèmes de la modélisation de texte est qu’elle est confuse, et les techniques comme les algorithmes d’apprentissage automatique préfèrent des entrées et des sorties de longueur fixe bien définies.

Les algorithmes d'apprentissage automatique ne peuvent pas travailler directement avec le texte brut ; le texte doit être converti en nombres. Plus précisément, en vecteurs de nombres.
Les méthodes populaires et simples d’extraction de caractéristiques avec des données textuelles actuellement utilisées sont :

- Bag of Words
- TF-IDF

#### Bag of Words (BoW)
Bag of Words (BoW) est un algorithme qui compte le nombre de fois qu'un mot apparaît dans un document. C'est un décompte. Ce décompte de mots nous permet de comparer des documents et d'évaluer leurs similitudes pour des applications telles que la recherche, la classification de documents et la modélisation de sujets. BoW est également une méthode de préparation de texte pour la saisie dans un réseau d'apprentissage profond.

BoW répertorie les mots associés à leur nombre de mots par document. Dans le tableau où sont stockés les mots et les documents qui deviennent effectivement des vecteurs, chaque ligne est un mot, chaque colonne est un document et chaque cellule est un nombre de mots. Chacun des documents du corpus est représenté par des colonnes de longueur égale. Il s'agit de vecteurs de nombre de mots, une sortie dépouillée de son contexte.

#### TF-IDF
La méthode TF-IDF ( Term-frequency-inverse document frequency ) est une autre façon d'évaluer le sujet d'un article en fonction des mots qu'il contient. Avec la méthode TF-IDF, les mots sont pondérés : la méthode TF-IDF mesure la pertinence et non la fréquence. Autrement dit, le nombre de mots est remplacé par les scores TF-IDF sur l'ensemble des données.

Premièrement, la méthode TF-IDF mesure le nombre de fois que des mots apparaissent dans un document donné (c'est ce qu'on appelle la « fréquence des termes »). Mais comme des mots tels que « et » ou « le » apparaissent fréquemment dans tous les documents, ils doivent être systématiquement écartés. C'est la partie de la fréquence inverse des documents. Plus un mot apparaît dans de nombreux documents, moins ce mot est précieux en tant que signal permettant de différencier un document donné. L'objectif est de ne conserver que les mots fréquents ET distinctifs comme marqueurs. La pertinence TF-IDF de chaque mot est un format de données normalisé qui s'ajoute également à un.


**sources :** 
- https://www.linguamatics.com/guides/what-text-mining-healthcare-nlp-and-llms
- https://relativeinsight.com/text-mining-vs-nlp/#h-wait-so-are-nlp-and-text-mining-the-same
- https://www.analyticsvidhya.com/blog/2021/06/nlp-sentiment-analysis/
- https://www.techtarget.com/whatis/definition/named-entity-recognition-NER
- https://www.geeksforgeeks.org/nlp-part-of-speech-default-tagging/
- https://www.justai.co/articles-de-blog/le-traitement-du-langage-naturel
- https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
- https://geekflare.com/fr/nlp-text-cleaning-and-preprocessing/
- https://medium.com/@pankajchandravanshi/nlp-unlocked-n-grams-006-ceab1bc56bf4
- https://www.datacamp.com/blog/what-is-tokenization
- https://fr.mathworks.com/discovery/lemmatization.html
- https://fr.mathworks.com/discovery/stemming.html
- https://medium.com/analytics-vidhya/fundamentals-of-bag-of-words-and-tf-idf-9846d301ff22
- https://wiki.pathmind.com/bagofwords-tf-idf