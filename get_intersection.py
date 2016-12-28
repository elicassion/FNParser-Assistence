import xmltodict
import codecs
import os
import json
import re
import sys
import random
import datetime
import collections
import pylab
reload(sys)
sys.setdefaultencoding('utf8')
f1Name = "G:/FNSentences/15/sentences_15/sent.frames"
f2Name = "G:/FNSentences/15/fulltext_15/sent.frames"
desFileName = "G:/FNSentences/15/overlap/sent.frames"
f1 = codecs.open(f1Name, "r")
f2 = codecs.open(f2Name, "r")
des = codecs.open(desFileName, "w")
l1 = [i.strip() for i in f1]
l2 = [i.strip() for i in f2]
s1 = set(l1)
s2 = set(l2)
set_inter = s1 & s2
for i in set_inter:
	des.write(i+"\n")