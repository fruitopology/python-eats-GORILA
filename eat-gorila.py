#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import urllib2
from datetime import datetime

"""
Thanks to Cefael and the French School of Athens for making their contents available to anyone for personal use.

This is an example url for an image from GORILA.  The other resolution that exists is 660, so if you want those you would replace "r=1294" with "r=660"
http://cefael.efa.gr/apps/library/services/images/?f=EtCret_21-1_1976_062.jpg&p=jpg%2F150%2FEtCret%2FEtCret_21-1_1976%2FEtCret_21-1_1976_VolumeBroche&r=1294

If you want to browse on the web, check out:
http://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&ce=7mbmdl9o5agdeq6cu7n2stcntl608imp&sp=313

Page for 5 volumes available: http://cefael.efa.gr/result.php?section_title=Recueil+des+inscriptions+en+Lin%C3%A9aire+A&site_id=1&actionID=simple&operator=AND
(with links to browse)

Volume 1: Recueil des inscriptions en Linéaire A. 1. Tablettes éditées avant 1970.
		Collection of inscriptions in Linear A. 1. Shelves published before 1970.
http://cefael.efa.gr/apps/library/services/images/?f=EtCret_21-1_1976_001.jpg&p=jpg%2F150%2FEtCret%2FEtCret_21-1_1976%2FEtCret_21-1_1976_VolumeBroche&r=1294

# number of pages in each section of Volume 1
preliminary = 36
text = 334
final = 2

Volume 2: Recueil des inscriptions en Linéaire A. 2. Nodules, scellés et rondelles édités avant 1970.
	Collection of inscriptions in Linear A. 2. Nodules, seals and washers published before 1970.
http://cefael.efa.gr/apps/library/services/images/?f=EtCret_21-2_1979_005.jpg&p=jpg%2F150%2FEtCret%2FEtCret_21-2_1979%2FEtCret_21-2_1979_VolumeBroche&r=1294

Volume 3: Recueil des inscriptions en Linéaire A. 3. Tablettes, nodules et rondelles édités entre 1975 et 1976.
		Collection of inscriptions in Linear A. 3. Tablets, nodules and washers published between 1975 and 1976.
http://cefael.efa.gr/apps/library/services/images/?f=EtCret_21-3_1976_005.jpg&p=jpg%2F150%2FEtCret%2FEtCret_21-3_1976%2FEtCret_21-3_1976_VolumeBroche&r=1299

Volume 4: Recueil des inscriptions en Linéaire A. 4. Autres documents.
		Collection of inscriptions in Linear A. 4. Other documents.
http://cefael.efa.gr/apps/library/services/images/?f=EtCret_21-4_1982_004.jpg&p=jpg%2F150%2FEtCret%2FEtCret_21-4_1982%2FEtCret_21-4_1982_VolumeBroche&r=1299

Volume 5: Recueil des inscriptions en Linéaire A. 5. Addenda, corrigenda, concordances, index et planches des signes.
		Handbook of Linear A. inscriptions 5. Addenda, corrigenda, concordances, indexes and signs boards.
http://cefael.efa.gr/apps/library/services/images/?f=EtCret_21-5_1985_005.jpg&p=jpg%2F150%2FEtCret%2FEtCret_21-5_1985%2FEtCret_21-5_1985_VolumeBroche&r=1299
"""

# The start/end numbers might be off.
volumes = [
	{'url':'http://cefael.efa.gr/apps/library/services/images/?f=EtCret_21-1_1976_{0:{fill}3}.jpg&p=jpg%2F150%2FEtCret%2FEtCret_21-1_1976%2FEtCret_21-1_1976_VolumeBroche&r=1294',
		'start':1,
		'end': 372,
		'index': 1},
	{'url':'http://cefael.efa.gr/apps/library/services/images/?f=EtCret_21-2_1979_{0:{fill}3}.jpg&p=jpg%2F150%2FEtCret%2FEtCret_21-2_1979%2FEtCret_21-2_1979_VolumeBroche&r=1294',
		'start':5,
		'end': 162,
		'index': 2},
	{'url':'http://cefael.efa.gr/apps/library/services/images/?f=EtCret_21-3_1976_{0:{fill}3}.jpg&p=jpg%2F150%2FEtCret%2FEtCret_21-3_1976%2FEtCret_21-3_1976_VolumeBroche&r=1299',
		'start':5,
		'end': 236,
		'index': 3},
	{'url':'http://cefael.efa.gr/apps/library/services/images/?f=EtCret_21-4_1982_{0:{fill}3}.jpg&p=jpg%2F150%2FEtCret%2FEtCret_21-4_1982%2FEtCret_21-4_1982_VolumeBroche&r=1299',
		'start': 4,
		'end': 222,
		'index': 4},
	{'url':'http://cefael.efa.gr/apps/library/services/images/?f=EtCret_21-5_1985_{0:{fill}3}.jpg&p=jpg%2F150%2FEtCret%2FEtCret_21-5_1985%2FEtCret_21-5_1985_VolumeBroche&r=1299',
		'start':5,
		'end': 524,
		'index': 5},
]

for v in volumes:
	os.mkdir(os.path.join(os.getcwd(), 'gorila_volume%d' % (v['index'])))
	for i in range(v['start'], v['end'] + 1):
		imageurl = v['url'].format(i, fill='0', align='right')
		print imageurl
		u = urllib2.urlopen(imageurl)
		localfile = open(os.path.join(os.getcwd(), 'gorila_volume%d' % (v['index']), 'image%03d.jpg' % (i)), 'w')
		localfile.write(u.read())
		localfile.close()

print "done at %s" % datetime.now()



