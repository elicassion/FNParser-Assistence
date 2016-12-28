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
inName = "G:/FNSentences/split_train_test_1/sent.test.nums"
unAnnotNumsName = "G:/FNSentences/split_train_test_1/sent.test.unannot.nums"
outName = "G:/FNSentences/split_train_test_1/sent.test.nums.pure"
res = ""
inf = codecs.open(inName, "r")
ot = codecs.open(outName, "w")

unAnnotNums = []
unAnnotNumsFile = codecs.open(unAnnotNumsName, "r")
for line in unAnnotNumsFile:
	unAnnotNums.append(int(line.strip()))
unAnnotNumsFile.close()

ct = 0
for line in inf:
	if int(line.strip()) in unAnnotNums:
		continue
	ct += 1
	res += line


ot.write(res)
ot.close()