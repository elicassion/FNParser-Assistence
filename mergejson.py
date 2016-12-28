import xmltodict
import codecs
import os
import json
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
suf = "G:/FNSentences/sentencesAll_v2_RIGHT_p"
end = ".json"
des = "G:/FNSentences/sentencesAll_v2_RIGHT.json"
desf = codecs.open(des, "w")
desf.write("{")
for i in range(1, 7):
	print i
	f = codecs.open(suf+str(i)+end, "r")
	string = f.read()
	print string[0], string[-1], string[-2], string[-3]
	desf.write(string[1:-2])
	if i < 6:
		desf.write(",\n")
desf.write("\n}")
desf.close()
src = "G:/FNSentences/sentencesAll_v2_RIGHT.json"
f = codecs.open(src, "r")
dic = json.loads(f.read())
print len(dic.items())
