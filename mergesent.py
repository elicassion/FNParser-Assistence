import xmltodict
import codecs
import os
import json
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
suf = "G:/FNSentences/sentences_15/sentences_15_p"
end = ".txt"
des = "G:/FNSentences/sentences_15/sentences_15.txt"
desf = codecs.open(des, "w")
for i in range(1, 6):
	print i
	f = codecs.open(suf+str(i)+end, "r")
	string = f.read()
	desf.write(string)
desf.close()

