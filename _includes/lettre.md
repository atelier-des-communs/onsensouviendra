{% if page.genre == "M" %}
	{% assign prefixe = "monsieur " %}
	{% assign pref = "Mr " %}
	{% assign hommeFemme = "un homme " %}
{% else %}
	{% assign prefixe = "madame " %}
	{% assign pref = "Mme " %}
	{% assign hommeFemme = "une femme " %}
{% endif %}

{{ prefixe | capitalize }} {{ page.nom }},

Vous avez signé, le 11 mai 2016, une motion de censure de gauche contre le gouvernement, en réponse au 49-3 déployé pour faire passer en force la loi travail, sans amendement.

L'utilisation du 49-3 dans ces conditions est un détournement inadmissible de la constitution, un piétinement intolérable de notre démocratie, et la trahison ultime d'un éxécutif qui n'a eu de cesse, depuis 2012, de renier ses engagements électoraux et de servir les intérêts des plus riches au détriment du bien commun.

Ce 49-3 s'assoie sur :

* Un rejet populaire sans précédent : Une [pétition signée par 1.3 million de Français](https://www.change.org/p/loi-travail-non-merci-myriamelkhomri-loitravailnonmerci), des [*Nuit Debout*](https://nuitdebout.fr/) dans toutes les villes de France, [un rejet de cette loi par 3 français sur 4](http://www.20minutes.fr/societe/1839395-20160504-loi-travail-trois-francais-quatre-opposes-selon-sondage)
* Le débat parlementaire, émanation de la démocratie représentative
* Une opposition grandissante au sein même de la majorité

{% if page['censure-1'] == "1" %}

En votant la censure déposée par la droite, vous avez été fidèle à vos engagements et avez agi, au délà d'une simple posture désincarnée, dans le sens de la volonté populaire.

Nous savons combien le texte accompagnant la motion de droite est éloigné de vos convictions. Aucun électeur de gauche ne s'y trompe : Vos motivations sont diamétralement opposées à celles de la motion de droite. Vous avez su dépasser cette apparente contradiction et choisir l'acte plutôt que la posture, dans le sens de l'intéret général : Ce courage vous honore.

Nous vous demandons de réitérer la censure du gouvernement au deuxième passage de cette loi devant l'assemblée nationale. Si une motion de gauche venait à voir le jour, nous vous demandons de voter les deux motions. Il y a de fortes chances que la droite ne vote pas la motion de gauche et vice versa : Les français sont fatigués de ces guerres de chapelles. Il est impératif de tout mettre en oeuvre pour dissoudre ce gouvernement et bloquer la loi travail.

Nous vous invitons aussi à faire tout votre possible pour rallier tous les députés de gauche à cette cause, et les persuader de voter la censure, qu'elle vienne de droite au de gauche, éventuellement contre leur propre parti. Ils se montreront ainsi fidèles à l'idée de la gauche : la défense des travailleurs, plutôt qu'à une étiquette. 

{% else %}

En refusant de voter la motion déposée par la droite, vous n'avez pas été au bout de vos convictions et avez préféré la posture à l'acte.

Nous savons combien le texte accompagnant la motion de droite est éloigné de vos convictions. Aucun électeur de gauche ne s'y trompe : Vos motivations sont diamétralement opposées à celles de la motion de droite.

Ce texte n'a aucune valeur légale, n'engage en rien et n'a aucun impact sur l'effet de la censure. La censure de droite ou de gauche aura exactement le même effet : Dissolution du gouvernement Valls, et blocage de la loi travail. François Hollande nommera un nouveau premier ministre qui formera un nouveau gouvernement. La droite ne viendra pas au pouvoir. François Hollande n'a aucune raison d'y ajouter une dissolution de l'assemblée.  

Vous pouvez, [comme Philippe Noguès](http://pnogues.fr/2016/05/12/pourquoi-jai-vote-la-censure/), faire une déclaration publique, expliquant les raisons de votre vote, vous désolidarisant ainsi, sans équivoque possible, du texte de la motion de droite.

Devons nous vous rappelez que, pour faire barrage au FN, vos électeurs n'ont pas hésité, à plusieurs reprises, à suivre vos instructions et voter pour des hommes de droite : Jacques Chirac, Xavier Bertrand, Christian Estrosi, ...

C'est pourquoi, nous vous exhortons solennellement à voter la prochaine motion de censure, au deuxième passage de la loi travail devant l'assemblée.

Si une motion de gauche venait à voir le jour, nous vous demandons également de voter les deux motions. Il y a de fortes chances que la droite ne vote pas la motion de gauche et vice versa : Les français sont fatigués de ces guerres de chapelles. Il est impératif de tout mettre en oeuvre pour dissoudre ce gouvernement et bloquer la loi travail.

{% if page['parti'] == "Parti socialiste" %}

Vous craignez sans doute une sanction de votre parti en cas de vote de la censure, allant jusqu'à l'exlusion.

Si vous êtes {{hommeFemme}} de gauche, vous n'avez pas à craindre une éviction. Plus aucun électeur de gauche n'est prêt à voter pour le PS légitimiste : celui qui embrasse l'imposture du mandat de François Hollande. vous traineriez l'étiquette PS comme un boulet pour les prochaines élections. Le vote de la censure vous apportera au contraire le crédit d'{{hommeFemme}} intègre, joignant l'acte à la parole.

Soyez fidèle à vos convictions, plutôt qu'à l'étiquette d'un parti qui les renie.

{% endif %}

{% endif %}

Quel que soit votre choix, ce site fera office de pense bête citoyen, en archivant les votes sur les motions de censure. Les électeurs s'en souviendront.

Sincères salutations,

Des citoyens français.   


