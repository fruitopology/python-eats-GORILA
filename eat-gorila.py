import urllib2
from datetime import datetime

"""
This is an example url for an image from GORILA.  The other resolution that exists is 660, so if you want those you would replace "r=1294" with "r=660"
http://cefael.efa.gr/apps/library/services/images/?f=EtCret_21-1_1976_062.jpg&p=jpg%2F150%2FEtCret%2FEtCret_21-1_1976%2FEtCret_21-1_1976_VolumeBroche&r=1294

If you want to browse on the web, check out:
http://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&ce=7mbmdl9o5agdeq6cu7n2stcntl608imp&sp=313
"""

# number of pages in each section
preliminary = 36
text = 334
final = 2

# 1-indexed
for i in range(1, preliminary + text + final + 1):
	imageurl = 'http://cefael.efa.gr/apps/library/services/images/?f=EtCret_21-1_1976_%03d' % (i) +'.jpg&p=jpg%2F150%2FEtCret%2FEtCret_21-1_1976%2FEtCret_21-1_1976_VolumeBroche&r=1294'
	print imageurl
	u = urllib2.urlopen(imageurl)
	# if you don't want preliminary or finale pages, one can easily use this logic to not download those pages.
	if i > text + preliminary:
		suffix = 'final'
	elif i > preliminary:
		suffix = 'text'
	else:
		suffix = 'preliminary'

	localfile = open('gorila%03d_%s.jpg' % (i, suffix), 'w')
	localfile.write(u.read())
	localfile.close()

print "done at %s" % datetime.now()

