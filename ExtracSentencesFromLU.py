import xmltodict
import codecs
import os
import json
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
desFileNameSuf = 'G:/FNSentences/15/sentences_15/sentences_15_p'
rightAnswerFileNameSuf = 'G:/FNSentences/15/sentences_15/sentences_15_p'
srcDir = 'D:/SJTU/SpeechLab/FrameNet/FrameNetData/fndata-1.5/lu'
sentenceNumber = 0
rg=[-1, 4000, 6000, 8000, 10000, 12000, 14000]
for loop in range(1, 6):
	rightDict = {}
	desFileName = desFileNameSuf+str(loop)+'.txt'
	desFile = codecs.open(desFileName, "w")
	rightAnswerFileName = rightAnswerFileNameSuf+str(loop)+'.json'
	i = 0
	for parent, dirnames, filenames in os.walk(srcDir):
	    for filename in filenames:
	        if '.xml' not in filename:
	            continue
	        i += 1
	        if i <= rg[loop-1]:
	        	continue
	        if i > rg[loop]:
	            break
	        file = codecs.open(os.path.join(srcDir, filename), "r")
	        fileStr = file.read()
	        file.close()
	        dic = xmltodict.parse(fileStr)
	        lu = dic['lexUnit']
	        frame = lu['@frame']
	        try:
	            for subCorpus in lu['subCorpus']:
	            	try:
		                for sentence in subCorpus['sentence']:
		                    desFile.write(sentence['text']+'\n')
		                    sentenceNumber += 1
		                    annotationSet = sentence['annotationSet']
		                    for antset in annotationSet:
		                    	if antset['@status'] == 'MANUAL':
		                    		antset['text'] = sentence['text']
		                    		antset['frame'] = frame
		                    		rightDict[str(sentenceNumber-1)] = antset
		                    #if sentenceNumber >= 40000:
	                except TypeError: continue
	            	except KeyError : continue
	        except TypeError: continue
	        except KeyError : continue
	desFile.close()
	rightAnswerFile = codecs.open(rightAnswerFileName, "w")
	rightAnswerFile.write(json.dumps(rightDict, ensure_ascii = False, indent = 4, sort_keys=True))
	rightAnswerFile.close()
	print "Sentence Number: ", sentenceNumber


