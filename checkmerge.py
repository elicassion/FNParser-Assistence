import xmltodict
import codecs
import os
import json
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
src = "G:/FNSentences/sentencesAll_v2_RIGHT_p1.json"
f = codecs.open(src, "r")
dic = json.loads(f.read())
print len(dic.items())