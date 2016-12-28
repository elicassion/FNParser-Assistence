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

#overlap frame info
overlapFrames = openFileAndTransToList("G:/FNSentences/15/overlap/sent.frames")

#root dir
ROOT_DIR = "G:/FNSentences/15/overlap/fulltext/"

#src file
srcSents = openFileAndTransToList(ROOT_DIR + "sent")
srcSentFrameElements = openFileAndTransToList(ROOT_DIR + "sent.frame.elements")
srcSentAllLemmaTags = openFileAndTransToList(ROOT_DIR + "sent.all.lemma.tags")

#train file
TRAIN_ROOT_DIR = ROOT_DIR + "train/"
trainSentFile = codecs.open(TRAIN_ROOT_DIR + "sent.train", "w")
trainSentFrameElementsFile = codecs.open(TRAIN_ROOT_DIR + "sent.train.frame.elements", "w")
trainSentAllLemmaTagsFile = codecs.open(TRAIN_ROOT_DIR + "sent.train.all.lemma.tags", "w")
trainSentNumFile = codecs.open(TRAIN_ROOT_DIR + "sent.train.nums", "w")
trainSentFramesFile = codecs.open(TRAIN_ROOT_DIR + "sent.train.frames", "w")
trainSents = []
trainSentFrameElements = []
trainSentAllLemmaTags = []
trainFrameDict = {}

#test file
TEST_ROOT_DIR = ROOT_DIR + "test/"
testSentFile = codecs.open(TEST_ROOT_DIR + "sent.test", "w")
testSentFrameElementsFile = codecs.open(TEST_ROOT_DIR + "sent.test.frame.elements", "w")
testSentAllLemmaTagsFile = codecs.open(TEST_ROOT_DIR + "sent.test.all.lemma.tags", "w")
testSentNumFile = codecs.open(TEST_ROOT_DIR + "sent.test.nums", "w")
testSentFramesFile = codecs.open(TEST_ROOT_DIR + "sent.test.frames", "w")
testSents = []
testSentFrameElements = []
testSentAllLemmaTags = []
testFrameDict = {}

allNumSet = set([i for i in range(0, 3678)])
trainNums = []
testNums = []
frameDict = {} # frame: [lines in frame.elements file]
frameElementsDict = {} # stidx(int):[line numbers(int) in frame.elements file]
for i in range(0, len(srcSentFrameElements)):
	tokens = srcSentFrameElements[i].split("\t")
	stidx = int(tokens[7])
	if frameElementsDict.has_key(stidx):
		frameElementsDict[stidx].append(i)
	else:
		frameElementsDict[stidx] = [i]


def extracFromNumber():
	
	trainSentNumFile.write("\n".join([str(i) for i in trainNums]))
	trainSentNumFile.close()
	count = 0
	for stidx in trainNums:
		# print "train: ", count
		lineNumbers = frameElementsDict[stidx]
		for lineNumber in lineNumbers:
			line = srcSentFrameElements[lineNumber]
			tokens = line.split("\t")
			tokens[7] = str(count)
			tokens[1] = str(100.000)
			frame = tokens[3]
			if trainFrameDict.has_key(frame):
				trainFrameDict[frame] += 1
			else:
				trainFrameDict[frame] = 1
			trainSentFrameElements.append("\t".join(tokens))
		trainSents.append(srcSents[stidx])
		trainSentAllLemmaTags.append(srcSentAllLemmaTags[stidx])
		count += 1

	trainNumSet = set(trainNums)
	testNumSet = allNumSet - trainNumSet
	testNums = [i for i in testNumSet]
	testNums.sort()
	testSentNumFile.write("\n".join([str(i) for i in testNums]))
	testSentNumFile.close()

	count = 0
	for stidx in testNums:
		# print "test: ", count
		lineNumbers = frameElementsDict[stidx]
		for lineNumber in lineNumbers:
			line = srcSentFrameElements[lineNumber]
			tokens = line.split("\t")
			tokens[7] = str(count)
			tokens[1] = str(100.000)
			frame = tokens[3]
			if testFrameDict.has_key(frame):
				testFrameDict[frame] += 1
			else:
				testFrameDict[frame] = 1
			testSentFrameElements.append("\t".join(tokens))
		testSents.append(srcSents[stidx])
		testSentAllLemmaTags.append(srcSentAllLemmaTags[stidx])
		count += 1
	
def writeFile():
	trainSentFile.write("\n".join(trainSents))
	trainSentFrameElementsFile.write("\n".join(trainSentFrameElements))
	trainSentAllLemmaTagsFile.write("\n".join(trainSentAllLemmaTags))
	trainSentFramesFile.write("\n".join([k+"\t"+str(v) for k, v in trainFrameDict.items()]))
	trainSentFile.close()
	trainSentFrameElementsFile.close()
	trainSentAllLemmaTagsFile.close()

	testSentFile.write("\n".join(testSents))
	testSentFrameElementsFile.write("\n".join(testSentFrameElements))
	testSentAllLemmaTagsFile.write("\n".join(testSentAllLemmaTags))
	testSentFramesFile.write("\n".join([k+"\t"+str(v) for k, v in testFrameDict.items()]))
	testSentFile.close()
	testSentFrameElementsFile.close()
	testSentAllLemmaTagsFile.close()


def generNums():
	remNumSet = allNumSet.copy()
	for line in srcSentFrameElements:
		tokens = line.split("\t")
		frame = tokens[3]
		if frameDict.has_key(frame):
			frameDict[frame].append(line)
		else:
			frameDict[frame] = [line]

	haspick = 0
	# print len(frameDict.items())
	for k, v in frameDict.items():
		pickline = v[random.choice([i for i in range(0, len(v))])]
		# print pickline
		tokens = pickline.split("\t")
		stidx = tokens[7]
		if int(stidx) not in trainNums:
			trainNums.append(int(stidx))
			remNumSet.remove(int(stidx))
			haspick += 1

	notpick = 2678 - haspick
	randomPickNums = random.sample([i for i in remNumSet], notpick)
	trainNums.extend(randomPickNums)
	trainNums.sort()

generNums()
extracFromNumber()
writeFile()


	