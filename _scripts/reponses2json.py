import simplejson as json
import sys
import codecs
import os

ROOT = '_data/reponses_md'


reponses = {}
for fn in os.listdir(ROOT):
    filename = ROOT + '/' + fn
    id = fn.replace(".md", "")
    if os.path.isfile(filename) :
        with codecs.open(filename, 'r', encoding='utf-8') as f :
            reponses[id] = f.read()

json.dump(reponses, sys.stdout)

        

