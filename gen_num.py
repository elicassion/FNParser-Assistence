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
annotNumsFile = codecs.open("G:/FNSentences/15/sentences_15/sent.nums.pure", "w")
trainPureFile = codecs.open("G:/FNSentences/split_train_test_1/sent.train.nums.pure", "r")
testPureFile = codecs.open("G:/FNSentences/split_train_test_1/sent.test.nums.pure", "r")
numl = []
for i in trainPureFile:
	numl.append(int(i.strip()))
for i in testPureFile:
	numl.append(int(i.strip()))
numl.sort()
for i in numl:
	annotNumsFile.write(str(i)+"\n")