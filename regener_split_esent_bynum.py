import xmltodict
import codecs
import os
import json
import re
import sys
import random
import datetime
import collections
reload(sys)
sys.setdefaultencoding('utf8')
def openFileAndTransToList(filename):
	f = codecs.open(filename, "r")
	l = [i.strip() for i in f]
	f.close()
	return l

ROOT_DIR = "G:/FNSentences/15/overlap/esent/"

#src files
srcSents = openFileAndTransToList(ROOT_DIR + "sent")
srcSentFrameElements = openFileAndTransToList(ROOT_DIR + "sent.frame.elements")
srcSentAllLemmaTags = openFileAndTransToList(ROOT_DIR + "sent.all.lemma.tags")

#train file
# TRAIN_ROOT_DIR = ROOT_DIR + "train/"
# trainSentFile = codecs.open(TRAIN_ROOT_DIR + "sent.train", "w")
# trainSentFrameElementsFile = codecs.open(TRAIN_ROOT_DIR + "sent.train.frame.elements", "w")
# trainSentAllLemmaTagsFile = codecs.open(TRAIN_ROOT_DIR + "sent.train.all.lemma.tags", "w")
# trainSentNums = openFileAndTransToList(TRAIN_ROOT_DIR + "sent.train.nums")
# trainSents = []
# trainSentFrameElements = []
# trainSentAllLemmaTags = []


#test file
TEST_ROOT_DIR = ROOT_DIR + "test/"
testSentFile = codecs.open(TEST_ROOT_DIR + "sent.test", "w")
testSentFrameElementsFile = codecs.open(TEST_ROOT_DIR + "sent.test.frame.elements", "w")
testSentAllLemmaTagsFile = codecs.open(TEST_ROOT_DIR + "sent.test.all.lemma.tags", "w")
testSentNums = openFileAndTransToList(TEST_ROOT_DIR + "sent.test.nums")
testSents = []
testSentFrameElements = []
testSentAllLemmaTags = []

# count = 0
# for i in trainSentNums:
# 	stidx = int(i)
# 	trainSents.append(srcSents[stidx])
# 	line = srcSentFrameElements[stidx]
# 	tokens = line.split("\t")
# 	tokens[7] = str(count)
# 	trainSentFrameElements.append("\t".join(tokens))
# 	trainSentAllLemmaTags.append(srcSentAllLemmaTags[stidx])
# 	count += 1

count = 0
for i in testSentNums:
	stidx = int(i)
	testSents.append(srcSents[stidx])
	line = srcSentFrameElements[stidx]
	tokens = line.split("\t")
	tokens[7] = str(count)
	testSentFrameElements.append("\t".join(tokens))
	testSentAllLemmaTags.append(srcSentAllLemmaTags[stidx])
	count += 1

# trainSentFile.write("\n".join(trainSents))
# trainSentFrameElementsFile.write("\n".join(trainSentFrameElements))
# trainSentAllLemmaTagsFile.write("\n".join(trainSentAllLemmaTags))
# trainSentFile.close()
# trainSentFrameElementsFile.close()
# trainSentAllLemmaTagsFile.close()

testSentFile.write("\n".join(testSents))
testSentFrameElementsFile.write("\n".join(testSentFrameElements))
testSentAllLemmaTagsFile.write("\n".join(testSentAllLemmaTags))
testSentFile.close()
testSentFrameElementsFile.close()
testSentAllLemmaTagsFile.close()