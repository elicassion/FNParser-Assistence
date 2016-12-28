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
def find_all_index(l):
	res = []
	mark_blank = False
	for i in range(0, len(l)):
		if l[i] == ' ' and not mark_blank:
			res.append(i)
			mark_blank = True
		else:
			mark_blank = False
	return res

def getTargetLoc(start, end, blankLoc):
	st_token_num = -1
	ed_token_num = -1
	for i in range(len(blankLoc)):
		if start < blankLoc[i]:
			st_token_num = i
			break
	for i in range(len(blankLoc)):
		if end < blankLoc[i]:
			ed_token_num = i
			break
	if st_token_num == -1:
		st_token_num = len(blankLoc)
	if ed_token_num == -1:
		ed_token_num = len(blankLoc)
	resString = "_".join([str(i) for i in range(st_token_num, ed_token_num+1)])
	return resString

def getFELoc(start, end, blankLoc):
	st_token_num = -1
	ed_token_num = -1
	for i in range(len(blankLoc)):
		if start < blankLoc[i]:
			st_token_num = i
			break
	for i in range(len(blankLoc)):
		if end < blankLoc[i]:
			ed_token_num = i
			break
	if st_token_num == -1:
		st_token_num = len(blankLoc)
	if ed_token_num == -1:
		ed_token_num = len(blankLoc)
	if st_token_num == ed_token_num:
		resString = str(st_token_num)
	else:
		resString = str(st_token_num)+":"+str(ed_token_num)
	return resString

rightFileName = "G:/FNSentences/15/sentences_15/sentences_15_p"
inputFileName = "G:/FNSentences/15/sentences_15/sent.nums"
feoutputFileName = "G:/FNSentences/15/sentences_15/sent.frame.elements"
frameoutputFileName = "G:/FNSentences/15/sentences_15/sent.frames"
unAnnotoutputFileName = "G:/FNSentences/15/sentences_15/sent.unannot.nums"
sentFileName = "G:/FNSentences/15/sentences_15/sent"
feoutputFile = codecs.open(feoutputFileName, "w")
inputNumFile = codecs.open(inputFileName, "r")
sentFile = codecs.open(sentFileName, "w")
numLimits = [0, 28432, 56562, 76606, 102338, 122952]
rightjsonFileName = rightFileName+str(1)+".json"
jsonFile = codecs.open(rightjsonFileName, "r")
rightDict = json.loads(jsonFile.read())
cur_limit = 1
sent_num = 0
allFrames = []
unAnnotNums = []
for num in inputNumFile:
	flag = True
	print sent_num
	num = num.strip()
	int_num = int(num)
	if int_num > numLimits[cur_limit]:
		cur_limit += 1
		rightjsonFileName = rightFileName+str(cur_limit)+".json"
		jsonFile.close()
		jsonFile = codecs.open(rightjsonFileName, "r")
		rightDict = json.loads(jsonFile.read())
	if not rightDict.has_key(num):
		unAnnotNums.append(num)
		continue
	sentDict = rightDict[num]
	sentText = sentDict["text"]
	blankLoc = find_all_index(sentText)
	layers = sentDict["layer"]
	for item in layers:
		if item["@name"] == "Target":
			if not item.has_key("label"):
				flag = False
				break
			if type(item["label"]) == type(blankLoc):
				flag = False
				break
			tstart = int(item["label"]["@start"])
			tend = int(item["label"]["@end"])
			target = sentText[tstart:tend+1]
		elif item["@name"] == "FE":
			if not item.has_key("label"):
				flag = False
				break
			fes = item["label"]
		elif item["@name"] == "Noun":
			targetpos = ".n"
		elif item["@name"] == "Verb":
			targetpos = ".v"
		elif item["@name"] == "Adj":
			targetpos = ".a"
		elif item["@name"] == "Adv":
			targetpos = ".adv"
		elif item["@name"] == "Prep":
			targetpos = ".prep"
	if not flag:
		unAnnotNums.append(num)
		continue
	rank = "0"
	score = "20.000"
	#tokensnum
	frame = sentDict["frame"]
	targetpluspos = target.lower()+targetpos
	targetloc = getTargetLoc(tstart, tend, blankLoc)
	#target=target
	sentNum = str(sent_num)
	fesList = []
	fesString = ""
	if type(fes) == type(fesList):
		for fe in fes:
			#print fe
			if not fe.has_key("@start"):
				continue
			festart = int(fe["@start"])
			feend = int(fe["@end"])
			fesList.append(fe["@name"] + '\t' + getFELoc(festart, feend, blankLoc))
	else:
		if fes.has_key("@start"):
			festart = int(fes["@start"])
			feend = int(fes["@end"])
			fesList.append(fes["@name"] + '\t' + getFELoc(festart, feend, blankLoc))
	tokensnum = str(len(fesList)+1)
	fesString = "\t".join(fesList)
	infoString = "\t".join([rank, score, tokensnum, frame, targetpluspos, targetloc, target, sentNum, fesString])
	feoutputFile.write(infoString+"\n")
	sentFile.write(sentText+"\n")

	sent_num += 1
	if frame not in allFrames:
		allFrames.append(frame)
	# break
feoutputFile.close()
sentFile.close()

frameoutputFile = codecs.open(frameoutputFileName, "w")
for item in allFrames:
	frameoutputFile.write(item+"\n")
frameoutputFile.close()

unAnnotoutputFile = codecs.open(unAnnotoutputFileName, "w")
for item in unAnnotNums:
	unAnnotoutputFile.write(item+"\n")
unAnnotoutputFile.close()

