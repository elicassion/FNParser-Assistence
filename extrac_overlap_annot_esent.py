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
SENT_ROOT_DIR = "G:/FNSentences/15/sentences_15/"

#sent.frame.elements file
sentFrameElements = openFileAndTransToList(SENT_ROOT_DIR + "sent.frame.elements")

#sent.all.lemma.tags file
sentAllLemmaTags = openFileAndTransToList(SENT_ROOT_DIR + "sent.all.lemma.tags")

#sent file
sents = openFileAndTransToList(SENT_ROOT_DIR + "sent")

#des file
DES_ROOT_DIR = "G:/FNSentences/15/overlap/esent/"
desSentFile = codecs.open(DES_ROOT_DIR + "sent", "w")
desSentFrameElementsFile = codecs.open(DES_ROOT_DIR + "sent.frame.elements", "w")
desSentAllLemmaTagsFile = codecs.open(DES_ROOT_DIR + "sent.all.lemma.tags", "w")
desSents = []
desSentFrameElements = []
desSentAllLemmaTags = []


#begin extrac by check sent.frame.elements

#count
count = 0
for stidx in range(0, len(sentFrameElements)):
	elementLine = sentFrameElements[stidx]
	tokens = elementLine.split("\t")
	frame = tokens[3]
	if frame in overlapFrames:
		tokens[7] = str(count)
		desSents.append(sents[stidx])
		desSentFrameElements.append("\t".join(tokens))
		desSentAllLemmaTags.append(sentAllLemmaTags[stidx])
		print count
		count += 1

#writeFile
desSentFile.write("\n".join(desSents))
desSentFrameElementsFile.write("\n".join(desSentFrameElements))
desSentAllLemmaTagsFile.write("\n".join(desSentAllLemmaTags))
desSentFile.close()
desSentFrameElementsFile.close()
desSentAllLemmaTagsFile.close()

