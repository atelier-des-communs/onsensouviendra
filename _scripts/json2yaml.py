import simplejson as json
import yaml
import sys
import unicodecsv as csv
from collections import OrderedDict, defaultdict
import re

from unicodedata import normalize
import codecs

PUNCT_REGEXP = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.:]+')
DATA_FILES_PATTERN = "_data/%s.csv"

def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    result = []

    for word in PUNCT_REGEXP.split(text.lower()):
    	word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))

# Add flag from list of deputes
def jointFlag(key, deputesMap) :
	noms  = tuple(codecs.open(DATA_FILES_PATTERN % (key), encoding='utf-8'))
	for nom in noms :
		id = slugify(nom.strip())
		if not  deputesMap.has_key(id) :
			raise "Depute non trouve : %s" % (id)
		else :
			deputesMap[id][key] = "1"

# Transform list of deputes to list by id
# The Dict is ordered, by surname
def toDictById(deputes) :
	deputes.sort(key=lambda depute : depute["id"].split('-')[1])
	return OrderedDict((depute["id"], depute) for depute in deputes)	

# Cleanup data
def cleanup(deputesMap) :
	for depute in deputesMap.values() :
		# Remove '.' from nom
		nom = depute['nom']
		depute['nom'] = nom.replace(".", " ").strip()

		# Split emails in several fields
		emails = depute["emails"]
		if len(emails) > 0 :
			depute["email_1"] = emails[0]
		if len(emails) > 1 :
			depute["email_2"] = emails[1]
		del depute["emails"]

# Dump to CSV
def toCSV(deputesMap) :
	KEYS = ["id", "nom", "parti", "groupe", "departement", "email_1", "email_2", "site", "motion-gauche", "censure-1"]
	writer = csv.writer(sys.stdout, delimiter=';')
	writer.writerow(KEYS) 
	for depute in deputesMap.values() :
		row = []
		for key in KEYS :
			if key in depute :
				row.append(depute[key])
			else :
				row.append("")
		writer.writerow(row)

def filterMotionGauche(deputesMap) :
	return OrderedDict((id, depute) for id, depute in deputesMap.iteritems() if 'motion-gauche' in depute)

def toYAML(deputesMap):
	yaml.safe_dump(deputesMap.values(), sys.stdout, allow_unicode=True)


# ------------------
# Main
# ------------------

deputes = json.load(sys.stdin)
deputesMap = toDictById(deputes)

# Jointure with other data flags in other files
jointFlag("motion-gauche", deputesMap)
jointFlag("censure-1", deputesMap)

deputesMap = filterMotionGauche(deputesMap)

cleanup(deputesMap)
toYAML(deputesMap)

