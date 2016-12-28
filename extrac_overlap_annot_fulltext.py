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

#annoted sent info root dir
SENT_ROOT_DIR = "G:/FNSentences/15/fulltext_15/"

#sent.frame.elements file
sentFrameElements = openFileAndTransToList(SENT_ROOT_DIR + "sent.frame.elements")

#sent.all.lemma.tags file
sentAllLemmaTags = openFileAndTransToList(SENT_ROOT_DIR + "sent.all.lemma.tags")

#sent file
sents = openFileAndTransToList(SENT_ROOT_DIR + "sent")

#des file
DES_ROOT_DIR = "G:/FNSentences/15/overlap/fulltext/"
desSentFile = codecs.open(DES_ROOT_DIR + "sent", "w")
desSentFrameElementsFile = codecs.open(DES_ROOT_DIR + "sent.frame.elements", "w")
desSentAllLemmaTagsFile = codecs.open(DES_ROOT_DIR + "sent.all.lemma.tags", "w")
desSents = []
desSentFrameElements = []
desSentAllLemmaTags = []


#begin extrac by check sent.frame.elements

#count
count = -1
sentIdxalreadyIn = []
for i in range(0, len(sentFrameElements)):
	elementLine = sentFrameElements[i]
	tokens = elementLine.split("\t")
	frame = tokens[3]
	stidx = tokens[7]
	if frame in overlapFrames:
		if not stidx in sentIdxalreadyIn:
			count += 1
			print count
			desSents.append(sents[int(stidx)])
			desSentAllLemmaTags.append(sentAllLemmaTags[int(stidx)])
			sentIdxalreadyIn.append(stidx)
		tokens[7] = str(count)
		desSentFrameElements.append("\t".join(tokens))

#writeFile
desSentFile.write("\n".join(desSents))
desSentFrameElementsFile.write("\n".join(desSentFrameElements))
desSentAllLemmaTagsFile.write("\n".join(desSentAllLemmaTags))
desSentFile.close()
desSentFrameElementsFile.close()
desSentAllLemmaTagsFile.close()

