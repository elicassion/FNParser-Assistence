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
allSentFileName = 'G:/FNSentences/15/sentences_15/sentences_15.txt'
allSentFile = codecs.open(allSentFileName, "r")
allSent = []
for line in allSentFile:
	allSent.append(line.replace("\n", ""))

# testSentFileName = 'G:/FNSentences/split_train_test_1/sent.test'
# trainSentFileName = 'G:/FNSentences/split_train_test_1/sent.train'
testSentNumFileName = 'G:/FNSentences/split_train_test_1/sent.test.nums'
trainSentNumFileName = 'G:/FNSentences/split_train_test_1/sent.train.nums'
l = [i for i in range(0, 122953)]
nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
random.seed(nowTime)


sent_train_nums = random.sample(l, 86067)
sent_train_nums.sort()
trainSentNumFile = codecs.open(trainSentNumFileName, "w")
# trainSentFile = codecs.open(trainSentFileName, "w")
for i in sent_train_nums:
	trainSentNumFile.write(str(i)+'\n')
	# trainSentFile.write(allSent[i]+'\n')
# trainSentFile.close()
trainSentNumFile.close()


sent_test_nums = list(set(l).difference(set(sent_train_nums)))
sent_test_nums.sort()
testSentNumFile = codecs.open(testSentNumFileName, "w")
# testSentFile = codecs.open(testSentFileName, "w")
for i in sent_test_nums:
	testSentNumFile.write(str(i)+'\n')
	# testSentFile.write(allSent[i]+'\n')
# testSentFile.close()
testSentNumFile.close()


