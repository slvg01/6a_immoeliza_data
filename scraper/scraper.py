
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

variable_dict = {'ID':["div","class", "classified__header--immoweb-code"],
                 'Price': ["span", "class", "sr-only"]}

urls = ['https://www.immoweb.be/en/classified/apartment/for-sale/gavere/9890/11118082', 'https://www.immoweb.be/en/classified/apartment/for-sale/gavere/9890/11118079', 'https://www.immoweb.be/en/classified/apartment/for-sale/gavere/9890/11118089', 'https://www.immoweb.be/en/classified/apartment/for-sale/gavere/9890/11118087', 'https://www.immoweb.be/en/classified/apartment/for-sale/gavere/9890/11118088', 'https://www.immoweb.be/en/classified/apartment/for-sale/gavere/9890/11118086', 'https://www.immoweb.be/en/classified/apartment/for-sale/gavere/9890/11118083', 'https://www.immoweb.be/en/classified/apartment/for-sale/gavere/9890/11118080', 'https://www.immoweb.be/en/classified/apartment/for-sale/gavere/9890/11118076', 'https://www.immoweb.be/en/classified/apartment/for-sale/seraing/4101/11120131', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/libin/6890/11120115', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/gent-zwijnaarde/9052/11120020', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/gent/9000/11120015', 'https://www.immoweb.be/en/classified/apartment-block/for-sale/forest/1190/11120343', 'https://www.immoweb.be/en/classified/flat-studio/for-sale/schaerbeek/1030/11119856', 'https://www.immoweb.be/en/classified/flat-studio/for-sale/schaerbeek/1030/11119855', 'https://www.immoweb.be/en/classified/house/for-sale/ronse/9600/11119431', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/gent/9000/11119406', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/oudenaarde/9700/11119386', 'https://www.immoweb.be/en/classified/apartment/for-sale/gent/9000/11119422', 'https://www.immoweb.be/en/classified/house/for-sale/gent/9000/11119421', 'https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/nazareth/9810/11119374', 'https://www.immoweb.be/en/classified/house/for-sale/vilvoorde/1800/11119955', 'https://www.immoweb.be/en/classified/apartment/for-sale/anderlecht/1070/11115396', 'https://www.immoweb.be/en/classified/house/for-sale/seraing/4100/11016538', 'https://www.immoweb.be/en/classified/house/for-sale/liege/4032/11118577', 'https://www.immoweb.be/en/classified/apartment/for-sale/liege/4020/11118578', 'https://www.immoweb.be/en/classified/apartment/for-sale/mons/7000/11118180', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/gavere/9890/11118092', 
'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/gavere/9890/11118061', 'https://www.immoweb.be/en/classified/house/for-sale/gent/9000/11121136', 'https://www.immoweb.be/en/classified/house/for-sale/beersel/1650/11121127', 'https://www.immoweb.be/en/classified/house/for-sale/alsemberg/1652/11121126', 'https://www.immoweb.be/en/classified/villa/for-sale/brecht/2960/11121125', 'https://www.immoweb.be/en/classified/house/for-sale/grobbendonk/2280/11121124', 'https://www.immoweb.be/en/classified/villa/for-sale/brasschaat/2930/11121123', 'https://www.immoweb.be/en/classified/house/for-sale/brecht/2960/11121122', 'https://www.immoweb.be/en/classified/house/for-sale/schilde/2970/11121121', 'https://www.immoweb.be/en/classified/house/for-sale/brasschaat/2930/11121120', 'https://www.immoweb.be/en/classified/house/for-sale/sint-job-in-%27t-goor/2960/11121119', 'https://www.immoweb.be/en/classified/penthouse/for-sale/brasschaat/2930/11121118', 'https://www.immoweb.be/en/classified/apartment/for-sale/brasschaat/2930/11121117', 'https://www.immoweb.be/en/classified/service-flat/for-sale/brasschaat/2930/11121116', 'https://www.immoweb.be/en/classified/mixed-use-building/for-sale/lille/2275/11121115', 'https://www.immoweb.be/en/classified/house/for-sale/schilde/2970/11121114', 'https://www.immoweb.be/en/classified/penthouse/for-sale/brasschaat/2930/11121113', 'https://www.immoweb.be/en/classified/house/for-sale/hallaar/2220/11121107', 'https://www.immoweb.be/en/classified/apartment/for-sale/merksem/2170/11121105', 'https://www.immoweb.be/en/classified/apartment/for-sale/hoboken/2660/11121104', 'https://www.immoweb.be/en/classified/house/for-sale/deurne/2100/11121102', 'https://www.immoweb.be/en/classified/house/for-sale/balegem/9860/11121096', 'https://www.immoweb.be/en/classified/apartment/for-sale/gent/9000/11121091', 'https://www.immoweb.be/en/classified/apartment/for-sale/gent/9000/11121087', 'https://www.immoweb.be/en/classified/house/for-sale/sint-niklaas/9100/11121086', 'https://www.immoweb.be/en/classified/house/for-sale/diest/3293/10903959', 'https://www.immoweb.be/en/classified/apartment-block/for-sale/schaerbeek/1030/11121085', 'https://www.immoweb.be/en/classified/apartment/for-sale/oostende/8400/11121081', 'https://www.immoweb.be/en/classified/mansion/for-sale/tournai/7500/11121079', 'https://www.immoweb.be/en/classified/house/for-sale/wolvertem/1861/11121076', 'https://www.immoweb.be/en/classified/house/for-sale/fl%C3%A9malle-grande/4400/11121065', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/gent/9040/11118009', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/wetteren/9230/11118039', 'https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/gent-mariakerke/9030/11118053', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/jette/1090/11119069', 'https://www.immoweb.be/en/classified/villa/for-sale/woluwe-saint-lambert/1200/11118328', 'https://www.immoweb.be/en/classified/apartment/for-sale/anderlecht/1070/11112291', 'https://www.immoweb.be/en/classified/apartment/for-sale/leuven/3000/11113388', 'https://www.immoweb.be/en/classified/apartment/for-sale/leuven/3000/11113353', 'https://www.immoweb.be/en/classified/apartment/for-sale/ixelles/1050/11111910', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/gent/9040/11115089', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/arlon/6700/11117182', 'https://www.immoweb.be/en/classified/apartment/for-sale/molenbeek-saint-jean/1080/11115297', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/forest/1190/11115447', 'https://www.immoweb.be/en/classified/apartment/for-sale/blankenberge/8370/11117389', 'https://www.immoweb.be/en/classified/apartment/for-sale/brussels-city/1000/11116006', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/gentbrugge/9050/11117092', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/deinze/9800/11117307', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/herenthout/2270/11116899', 'https://www.immoweb.be/en/classified/apartment/for-sale/antwerpen/2018/11115967', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/berlaar/2590/11116504', 'https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/dessel/2480/11117598', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/astene/9800/11117309', 'https://www.immoweb.be/en/classified/apartment/for-sale/gent/9000/11115063', 'https://www.immoweb.be/en/classified/apartment/for-sale/gent/9000/11115052', 'https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/malonne/5020/11116000', 'https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/deinze-astene/9800/11115064', 'https://www.immoweb.be/en/classified/apartment/for-sale/etterbeek/1040/11115039', 'https://www.immoweb.be/en/classified/apartment/for-sale/gent/9000/11116035', 'https://www.immoweb.be/en/classified/villa/for-sale/berloz/4257/11115196', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/braine-lalleud/1420/11115129', 'https://www.immoweb.be/en/classified/apartment/for-sale/andenne/5300/11121064', 'https://www.immoweb.be/en/classified/apartment/for-sale/li%C3%A8ge/4000/11121063', 'https://www.immoweb.be/en/classified/apartment/for-sale/braine-le-comte/7090/11121062', 'https://www.immoweb.be/en/classified/house/for-sale/ahin/4500/11121061', 'https://www.immoweb.be/en/classified/country-cottage/for-sale/deurle/9831/11121057', 'https://www.immoweb.be/en/classified/house/for-sale/deurle/9831/11121056', 'https://www.immoweb.be/en/classified/duplex/for-sale/antwerpen/2000/11121054', 'https://www.immoweb.be/en/classified/house/for-sale/herstal/4040/11121053', 'https://www.immoweb.be/en/classified/house/for-sale/overijse/3090/11121052', 'https://www.immoweb.be/en/classified/house/for-sale/hooglede/8830/11121051', 'https://www.immoweb.be/en/classified/apartment/for-sale/hooglede/8830/11121050', 'https://www.immoweb.be/en/classified/apartment/for-sale/hooglede/8830/11121049', 'https://www.immoweb.be/en/classified/house/for-sale/hooglede/8830/11121048', 'https://www.immoweb.be/en/classified/apartment/for-sale/hooglede/8830/11121047', 'https://www.immoweb.be/en/classified/house/for-sale/tamines/5060/11094653', 'https://www.immoweb.be/en/classified/house/for-sale/braine-le-ch%C3%82teau/1440/11121042', 'https://www.immoweb.be/en/classified/house/for-sale/bouge/5004/11121041', 'https://www.immoweb.be/en/classified/house/for-sale/gougnies/6280/11121040', 'https://www.immoweb.be/en/classified/apartment-block/for-sale/namur/5000/11121038', 'https://www.immoweb.be/en/classified/apartment/for-sale/andenne/5300/11121037', 'https://www.immoweb.be/en/classified/apartment/for-sale/bouge/5004/11121034', 'https://www.immoweb.be/en/classified/villa/for-sale/grimbergen/1850/10753582', 'https://www.immoweb.be/en/classified/apartment/for-sale/eghez%C3%A9e/5310/11121033', 'https://www.immoweb.be/en/classified/apartment/for-sale/brussels%20city/1000/11121032', 'https://www.immoweb.be/en/classified/apartment/for-sale/ixelles/1050/11121030', 'https://www.immoweb.be/en/classified/apartment/for-sale/brussels%20city/1000/11121026', 'https://www.immoweb.be/en/classified/apartment/for-sale/brussels%20city/1000/11121025', 'https://www.immoweb.be/en/classified/apartment/for-sale/brussels%20city/1000/11121023', 'https://www.immoweb.be/en/classified/apartment/for-sale/brussels%20city/1000/11121022', 'https://www.immoweb.be/en/classified/apartment/for-sale/brussels%20city/1000/11121021', 'https://www.immoweb.be/en/classified/house/for-sale/steenokkerzeel/1820/11117067', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/merelbeke/9820/11117128', 'https://www.immoweb.be/en/classified/house/for-sale/gent/9030/11117013', 'https://www.immoweb.be/en/classified/apartment/for-sale/gent/9000/11117845', 'https://www.immoweb.be/en/classified/apartment/for-sale/gent/9000/11120014', 'https://www.immoweb.be/en/classified/apartment/for-sale/bruxelles/1000/11109502', 'https://www.immoweb.be/en/classified/penthouse/for-sale/bruxelles/1000/11109514', 'https://www.immoweb.be/en/classified/apartment/for-sale/bruxelles/1000/11109501', 'https://www.immoweb.be/en/classified/apartment/for-sale/bruxelles/1000/11109500', 'https://www.immoweb.be/en/classified/apartment/for-sale/ixelles/1050/11109851', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/seraing/4100/11113560', 'https://www.immoweb.be/en/classified/apartment/for-sale/bruxelles/1020/11111977', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/deinze/9800/11114513', 'https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/ronse/9600/11114416', 'https://www.immoweb.be/en/classified/bungalow/for-sale/herve-battice/4651/11112756', 'https://www.immoweb.be/en/classified/apartment/for-sale/arlon/6700/11113152', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/gent/9000/11114507', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/gent/9000/11114506', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/bruxelles/1000/11112295', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/marche-en-famenne/6900/11112698', 'https://www.immoweb.be/en/classified/apartment/for-sale/mortsel/2640/11113298', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/bachte-maria-leerne/9800/11114508', 
'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/gent/9000/11114505', 'https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/ronse/9600/11114411', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/evere/1140/11112306', 'https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/wielsbeke/8710/11114368', 'https://www.immoweb.be/en/classified/apartment/for-sale/blankenberge/8370/11113359', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/uccle/1180/11114062', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/rhode-saint-genese/1640/11112309', 'https://www.immoweb.be/en/classified/apartment/for-sale/nieuwpoort/8620/11114300', 'https://www.immoweb.be/en/classified/apartment/for-sale/brussels%20city/1000/11121020', 'https://www.immoweb.be/en/classified/house/for-sale/gr%C3%82ce-hollogne/4460/11121017', 'https://www.immoweb.be/en/classified/house/for-sale/engis/4480/11121016', 'https://www.immoweb.be/en/classified/house/for-sale/quaregnon/7390/11121015', 'https://www.immoweb.be/en/classified/house/for-sale/quaregnon/7390/11121014', 'https://www.immoweb.be/en/classified/house/for-sale/fallais/4260/11121011', 'https://www.immoweb.be/en/classified/house/for-sale/moustier/5190/10985424', 'https://www.immoweb.be/en/classified/apartment/for-sale/li%C3%A8ge/4000/11121010', 'https://www.immoweb.be/en/classified/house/for-sale/florennes/5620/11121009', 'https://www.immoweb.be/en/classified/house/for-sale/florennes/5620/11121008', 'https://www.immoweb.be/en/classified/apartment/for-sale/florennes/5620/11121007', 'https://www.immoweb.be/en/classified/apartment/for-sale/florennes/5620/11121006', 'https://www.immoweb.be/en/classified/house/for-sale/auvelais/5060/11121005', 'https://www.immoweb.be/en/classified/bungalow/for-sale/yvoir/5530/11121004', 'https://www.immoweb.be/en/classified/apartment/for-sale/tournai/7500/10979750', 'https://www.immoweb.be/en/classified/apartment/for-sale/borgerhout/2140/11120997', 'https://www.immoweb.be/en/classified/apartment/for-sale/tournai/7500/10628156', 'https://www.immoweb.be/en/classified/apartment/for-sale/anderlecht/1070/10943355', 'https://www.immoweb.be/en/classified/apartment/for-sale/molenbeek-saint-jean/1080/11120995', 'https://www.immoweb.be/en/classified/apartment/for-sale/ixelles/1050/11120990', 'https://www.immoweb.be/en/classified/loft/for-sale/bruxelles/1000/11120988', 'https://www.immoweb.be/en/classified/house/for-sale/tervuren/3080/11120983', 'https://www.immoweb.be/en/classified/house/for-sale/ellezelles/7890/11120982', 'https://www.immoweb.be/en/classified/house/for-sale/ellezelles/7890/11120981', 'https://www.immoweb.be/en/classified/apartment/for-sale/bruxelles%20ville/1000/11120980', 'https://www.immoweb.be/en/classified/house/for-sale/goesnes/5353/11120979', 'https://www.immoweb.be/en/classified/house/for-sale/noduwez/1350/11120977', 'https://www.immoweb.be/en/classified/penthouse/for-sale/woluwe-saint-lambert/1200/11120969', 'https://www.immoweb.be/en/classified/penthouse/for-sale/woluwe-saint-lambert/1200/11120968', 'https://www.immoweb.be/en/classified/flat-studio/for-sale/uccle/1180/11120966', 'https://www.immoweb.be/en/classified/apartment/for-sale/ixelles/1050/11112816', 'https://www.immoweb.be/en/classified/apartment/for-sale/turnhout/2300/11113788', 'https://www.immoweb.be/en/classified/apartment/for-sale/antwerp/2000/11112337', 'https://www.immoweb.be/en/classified/apartment/for-sale/ixelles/1050/11112962', 'https://www.immoweb.be/en/classified/house/for-sale/woluwe-saint-pierre/1150/11112019', 'https://www.immoweb.be/en/classified/apartment/for-sale/waimes/4950/11119440', 'https://www.immoweb.be/en/classified/apartment/for-sale/schaerbeek/1030/11120339', 'https://www.immoweb.be/en/classified/apartment/for-sale/schaerbeek/1030/11120338', 'https://www.immoweb.be/en/classified/apartment/for-sale/bruxelles/1000/11120340', 'https://www.immoweb.be/en/classified/apartment/for-sale/vorst/1190/11120570', 'https://www.immoweb.be/en/classified/apartment/for-sale/anderlecht/1070/11112284', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/eupen/4700/11109210', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/seraing/4100/11109402', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/leuze-en-hainaut/7900/11108685', 
'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/eupen/4700/11109183', 'https://www.immoweb.be/en/classified/house/for-sale/angleur/4031/11109640', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/saint-ghislain-tertre/7333/11108610', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/deinze/9800/11111498', 'https://www.immoweb.be/en/classified/apartment/for-sale/molenbeek-saint-jean/1080/11108350', 
'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/berchem-sainte-agathe/1082/11108296', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/forest/1190/11108316', 'https://www.immoweb.be/en/classified/flat-studio/for-sale/antwerpen/2018/11110852', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/liege/4000/11109248', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/namur/5000/11108746', 'https://www.immoweb.be/en/classified/house/for-sale/flemalle/4400/11109457', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/namur-saint-servais/5002/11108956', 'https://www.immoweb.be/en/classified/apartment/for-sale/antwerp/2170/11111476', 'https://www.immoweb.be/en/classified/apartment/for-sale/nivelles/1400/11111123', 'https://www.immoweb.be/en/classified/apartment/for-sale/molenbeek-saint-jean/1080/11108349', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/namur/5001/11108883', 'https://www.immoweb.be/en/classified/ground-floor/for-sale/antwerpen%202/2020/11120965', 'https://www.immoweb.be/en/classified/house/for-sale/mons-lez-li%C3%88ge/4400/11120950', 'https://www.immoweb.be/en/classified/house/for-sale/mol/2400/11120949', 'https://www.immoweb.be/en/classified/other-property/for-sale/manage/7170/11120947', 'https://www.immoweb.be/en/classified/apartment/for-sale/brasschaat/2930/11112352', 'https://www.immoweb.be/en/classified/house/for-sale/brecht/2960/11120941', 'https://www.immoweb.be/en/classified/duplex/for-sale/knokke-heist/8300/11120939', 'https://www.immoweb.be/en/classified/service-flat/for-sale/leuven/3001/10509356', 'https://www.immoweb.be/en/classified/apartment/for-sale/wilrijk/2610/11120937', 'https://www.immoweb.be/en/classified/other-property/for-sale/manage/7170/11120933', 'https://www.immoweb.be/en/classified/apartment/for-sale/neder-over-heembeek%20%28bru.%29/1120/11120932', 'https://www.immoweb.be/en/classified/apartment/for-sale/neder-over-heembeek%20%28bru.%29/1120/11120931', 'https://www.immoweb.be/en/classified/house/for-sale/zottegem/9620/11120930', 'https://www.immoweb.be/en/classified/house/for-sale/herzele/9550/11120929', 'https://www.immoweb.be/en/classified/apartment/for-sale/wilrijk/2610/11120927', 'https://www.immoweb.be/en/classified/apartment-block/for-sale/saint-nicolas/4420/11120926', 'https://www.immoweb.be/en/classified/house/for-sale/charleroi%20couillet/6010/11120925', 'https://www.immoweb.be/en/classified/house/for-sale/loncin/4431/11120921', 'https://www.immoweb.be/en/classified/house/for-sale/brugge/8000/11120920', 'https://www.immoweb.be/en/classified/other-property/for-sale/manage/7170/11120919', 'https://www.immoweb.be/en/classified/apartment/for-sale/aalst/9300/11120918', 'https://www.immoweb.be/en/classified/house/for-sale/herstal/4040/11120916', 'https://www.immoweb.be/en/classified/house/for-sale/oupeye/4680/11120915', 'https://www.immoweb.be/en/classified/apartment/for-sale/uccle/1180/11120914', 'https://www.immoweb.be/en/classified/apartment/for-sale/uccle/1180/11120910', 'https://www.immoweb.be/en/classified/house/for-sale/sint-katherina-lombeek/1742/11120904', 'https://www.immoweb.be/en/classified/house/for-sale/geraardsbergen/9500/11120902', 'https://www.immoweb.be/en/classified/house/for-sale/rebecq/1430/11120901', 'https://www.immoweb.be/en/classified/house/for-sale/menen/8930/11120900', 'https://www.immoweb.be/en/classified/duplex/for-sale/temse/9140/11120898', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/wetteren/9230/11111496', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/molenbeek-saint-jean/1080/11108310', 'https://www.immoweb.be/en/classified/house/for-sale/frasnes-lez-anvaing/7910/11108431', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/chaudfontaine-beaufays/4052/11109147', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/asse/1730/11108274', 'https://www.immoweb.be/en/classified/loft/for-sale/verviers/4800/11108048', 'https://www.immoweb.be/en/classified/house/for-sale/branst/2880/11110540', 'https://www.immoweb.be/en/classified/house/for-sale/rendeux-bas/6987/11110608', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/zingem/9750/11111499', 'https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/eupen/4700/11109169', 'https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/marche-en-famenne/6900/11110975', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/ixelles/1050/11108547', 'https://www.immoweb.be/en/classified/house/for-sale/faimes/4317/11109944', 'https://www.immoweb.be/en/classified/villa/for-sale/saint-nicolas/4420/11108186', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/uccle/1180/11108024', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/bruxelles/1000/11108330', 'https://www.immoweb.be/en/classified/apartment/for-sale/gent/9000/11107989', 'https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/gent/9000/11111495', 'https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/zwijnaarde/9052/11111494', 'https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/bruxelles/1130/11108302', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/evere/1140/11108288', 'https://www.immoweb.be/en/classified/apartment/for-sale/ixelles/1050/11108239', 'https://www.immoweb.be/en/classified/house/for-sale/forest/1190/11108236', 'https://www.immoweb.be/en/classified/apartment/for-sale/ixelles/1050/11108238', 'https://www.immoweb.be/en/classified/villa/for-sale/braine-lalleud/1420/11108183', 'https://www.immoweb.be/en/classified/villa/for-sale/rhode-saint-genese/1640/11108184', 'https://www.immoweb.be/en/classified/apartment/for-sale/gavere/9890/11118075', 'https://www.immoweb.be/en/classified/apartment/for-sale/anderlecht/1070/11119478', 'https://www.immoweb.be/en/classified/apartment/for-sale/ixelles/1050/11119851', 'https://www.immoweb.be/en/classified/new-real-estate-project-apartments/for-sale/berchem-sainte-agathe/1082/11104562', 'https://www.immoweb.be/en/classified/apartment/for-sale/heist-aan-zee/8301/11120894', 'https://www.immoweb.be/en/classified/house/for-sale/gent/9000/11120893', 'https://www.immoweb.be/en/classified/ground-floor/for-sale/bruxelles/1020/10921911', 'https://www.immoweb.be/en/classified/apartment/for-sale/westkerke/8460/11120890', 'https://www.immoweb.be/en/classified/ground-floor/for-sale/sint-niklaas/9100/11033437', 'https://www.immoweb.be/en/classified/house/for-sale/asse/1730/11120889', 'https://www.immoweb.be/en/classified/house/for-sale/borgloon/3840/11120888', 'https://www.immoweb.be/en/classified/villa/for-sale/maasmechelen/3630/11120887', 'https://www.immoweb.be/en/classified/house/for-sale/tongeren/3700/11120886', 'https://www.immoweb.be/en/classified/apartment/for-sale/schoten/2900/11120884', 'https://www.immoweb.be/en/classified/apartment/for-sale/schoten/2900/11120883', 'https://www.immoweb.be/en/classified/house/for-sale/peutie/1800/11120882', 'https://www.immoweb.be/en/classified/house/for-sale/ieper/8900/11120881', 'https://www.immoweb.be/en/classified/apartment/for-sale/molenbeek-saint-jean/1080/11120880', 'https://www.immoweb.be/en/classified/house/for-sale/torhout/8820/11120878', 'https://www.immoweb.be/en/classified/house/for-sale/ichtegem/8480/11120876', 'https://www.immoweb.be/en/classified/house/for-sale/p%C3%89ruwelz/7600/11120873', 'https://www.immoweb.be/en/classified/town-house/for-sale/la%20louvi%C3%88re/7100/11120872', 'https://www.immoweb.be/en/classified/apartment/for-sale/nivelles/1400/11120871', 'https://www.immoweb.be/en/classified/apartment/for-sale/evergem/9940/11120868', 'https://www.immoweb.be/en/classified/duplex/for-sale/wichelen/9260/11120867', 'https://www.immoweb.be/en/classified/house/for-sale/lokeren/9160/11120866', 'https://www.immoweb.be/en/classified/house/for-sale/lochristi/9080/11120864', 'https://www.immoweb.be/en/classified/house/for-sale/ichtegem/8480/11120858', 'https://www.immoweb.be/en/classified/house/for-sale/aalbeke/8511/11120857', 'https://www.immoweb.be/en/classified/house/for-sale/merksplas/2330/11120855', 'https://www.immoweb.be/en/classified/house/for-sale/ledeberg/9050/11120853', 'https://www.immoweb.be/en/classified/house/for-sale/gent/9000/10950521', 'https://www.immoweb.be/en/classified/apartment/for-sale/wommelgem/2160/11120851', 'https://www.immoweb.be/en/classified/house/for-sale/li%C3%A8ge/4000/11120850']



class Immoweb_Scraper:
    """
    A class for scraping data from the Immoweb website.
    """

    def __init__(self, variable_dict) -> None:
        """
        Initialize the Immoweb_Scraper object.

        Args:
        - variable_dict (dict): A dictionary containing variable names as keys and
                                corresponding CSS selectors as values.
        - urls (list): A list of URLs to scrape.
        """
        self.variable_dict = variable_dict
        self.base_urls_list = []
        self.immoweb_urls_list = []
        self.element_list = ["Construction year","Price","Bedrooms","Living area","Kitchen type","Furnished","Terrace surface", "Surface of the plot","Garden surface","Number of frontages","Swimming pool","Building condition"]
        self.data_set = []
        self.dataset_df = pd.DataFrame()
        self.soups = []


        
    def get_base_urls(self):
        """
            Get the list of base URLs after applying the filter 
            as Life Annuity as False. Go through mupltiple pages 
            to get the list of all base URLs which will allow  
            fetching 10000 URLs of House or Appartment for sale.
        """
        for i in range(1,2):
            base_url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isALifeAnnuitySale=false&page={i}&orderBy=relevance"
            self.base_urls_list.append(base_url)
        print('Base URLs generated!')
        return(self.base_urls_list)    
    

        
    def get_immoweb_urls(self):
        """
            Gets the list of Immoweb URLs from each page of base URLs
        """
        self.base_urls_list = self.get_base_urls()
        counter = 0
        for each_url in self.base_urls_list:
            url_content = requests.get(each_url).content
            soup = BeautifulSoup(url_content, "html.parser")
            for tag in soup.find_all("a", attrs={"class" : "card__title-link"}):
                immoweb_url = tag.get("href")
                if "www.immoweb.be" in immoweb_url and counter < 10:
                    self.immoweb_urls_list.append(immoweb_url)
                    counter += 1
        print('Immoweb URLs generated!', len(self.immoweb_urls_list))
        return(self.immoweb_urls_list)
    


    def request_urls(self):
        """
        Request URLs and parse HTML content.

        Sends HTTP requests to the provided URLs, parses the HTML content,
        and stores the parsed soup objects.
        """
        self.immoweb_urls_list = self.get_immoweb_urls()
        for url in self.immoweb_urls_list:
            url_content = requests.get(url)
            if url_content.status_code == 200:
                self.soups.append(BeautifulSoup(url_content.content, "html.parser"))
            else:
                continue
        print(len(self.soups))
        return self.soups
    
       
    def scrape_table_dataset(self):
        """  
            Get the 1st part of the parameters from URLs extracting
            and the 2nd part of the parameters from page scraping
        """
        
        self.immoweb_urls_list = self.get_immoweb_urls()
        for each_url in self.immoweb_urls_list:
            data_dict = {}
            data_dict["url"] = each_url
            data_dict["Property ID"] = each_url.split('/')[-1]
            data_dict["Locality name"] = each_url.split('/')[-3]
            data_dict["Postal code"] = each_url.split('/')[-2]
            data_dict["Subtype of property"] = each_url.split('/')[-5]
            url_content = requests.get(each_url).content
            soup = BeautifulSoup(url_content, "html.parser")
            #print(each_url)
            for tag in soup.find_all("tr", attrs={"class" : "classified-table__row"}):
                for tag1 in tag.find_all("th", attrs={"class" : "classified-table__header"}):
                    if tag1.string is not None:                
                        #print(tag1.string.strip())
                        for element in self.element_list:
                            if element == tag1.string.strip():
                                tag_text = str(tag.td).strip().replace("\n","").replace(" ","")
                                #print(tag_text)
                                start_loc = tag_text.find('>')
                                end_loc = tag_text.find('<',tag_text.find('<')+1)
                                table_data = tag_text[start_loc+1:end_loc]
                                #print(element + ' : '+ table_data)
                                data_dict[element] = table_data
            #print(data_dict)
            self.data_set.append(data_dict)
        return(self.data_set)


    def to_DataFrame (self) :
        """ allow to convert the data_set list of dict in a DataFrame """
        self.data_set_df = pd.DataFrame(self.data_set)
        print(self.data_set_df.head(3))
        return self.data_set_df     
         


    def to_csv (self):
        """ allow to convert the data_set DataFrame in CSV """
        data_set = self.data_set_df.to_csv ('data_set.csv', index= False)
        return data_set


        

# Example usage and testing:
immoscrap = Immoweb_Scraper(variable_dict)
immoscrap.get_immoweb_urls()
immoscrap.request_urls()
immoscrap.scrape_table_dataset()
immoscrap.to_DataFrame()
immoscrap.to_csv()


"""

def save_csv(self):
    
        Save scraped data dictionary to a CSV file.

        Save the scraped data dictionary to a CSV file where each key-value
        pair is written as a row with the key in the first column and the
        value in the second column.
    
        with open('immo_dict.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in self.data_set.items():
                writer.writerow([key, value])
   

def URL_extractor(self, url):
        
        Extract data from URLs.

        Extract relevant data (IDs, Postal_codes, Locality_names, Subtypes)
        from the provided URLs.

        Args:
        - url (str): The URL from which data needs to be extracted.

        Returns:
        - dict: A dictionary containing extracted data.
        
        splits = url.split('/')
        IDs = splits[-1]
        Postal_code = splits[-2]
        Locality_name = splits[-3].capitalize()
        Subtype = splits[-5]

        # Return the extracted data as a dictionary
        return {'ID': IDs, 'Postal_code': Postal_code, 'Locality_name': Locality_name, 'Subtype': Subtype}
        
        
 
    def extract_urls(self):
        
        Extract data from URLs and save to a CSV file.

        Extract relevant data (IDs, Postal_codes, Locality_names, Subtypes)
        from the provided URLs, save the data to a dictionary, and then write
        the dictionary to a CSV file.
        
        url_dict = {}

        IDs = []
        Postal_codes = []
        Locality_names = []
        Subtypes = []

        for url in self.urls:
            extracted_data = self.URL_extractor(url)
            IDs.append(extracted_data['ID'])
            Postal_codes.append(extracted_data['Postal_code'])
            Locality_names.append(extracted_data['Locality_name'])
            Subtypes.append(extracted_data['Subtype'])

        url_dict['IDs'] = IDs
        url_dict['Postal_codes'] = Postal_codes
        url_dict['Locality_names'] = Locality_names
        url_dict['Subtypes'] = Subtypes

        with open('url_dict.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in url_dict.items():
                writer.writerow([key, value])

        return url_dict
    
        

# Example usage and testing:
immoscrap = Immoweb_Scraper(variable_dict)
immoscrap.get_immoweb_urls()
immoscrap.request_urls()
#immoscrap.scrape_vars()
#immoscrap.to_dict()
#immoscrap.save_csv()
#immoscrap.get_elements_value()
scraped_data = immoscrap.scrape_table_dataset()
print(scraped_data)
# immoscrap.extract_urls()