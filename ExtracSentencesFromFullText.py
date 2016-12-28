import xmltodict
import codecs
import os
import json
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
desFileName = 'G:/FNSentences/15/fulltext_15/fulltext_15.txt'
rightAnswerFileName = 'G:/FNSentences/15/fulltext_15/fulltext_15.json'
srcDir = 'D:/SJTU/SpeechLab/FrameNet/FrameNetData/fndata-1.5/fulltext'
sentenceNumber = 0
alltags = 0
rightDict = {}
desFile = codecs.open(desFileName, "w")
for parent, dirnames, filenames in os.walk(srcDir):
    for filename in filenames:
        if '.xml' not in filename:
            continue
        file = codecs.open(os.path.join(srcDir, filename), "r")
        fileStr = file.read()
        file.close()
        dic = xmltodict.parse(fileStr)
        sentences = dic['fullTextAnnotation']['sentence']
        for sentence in sentences:
			rtlist = []
			if not type(sentence['annotationSet']) == type([]):
				if sentence['annotationSet'] == 'MANUAL':
					rtlist.append(sentence[annotationSet])
					alltags += 1
			else:
				for antset in sentence['annotationSet']:
					if antset['@status'] == 'MANUAL':
						rtlist.append(antset)
						alltags += 1
			if len(rtlist) > 0:
				desFile.write(sentence['text']+'\n')
				sentenceNumber += 1
				print sentenceNumber
				sdict = {}
				sdict["text"] = sentence['text']
				sdict["frames"] = rtlist
				rightDict[str(sentenceNumber-1)] = sdict
desFile.close()
rightAnswerFile = codecs.open(rightAnswerFileName, "w")
rightAnswerFile.write(json.dumps(rightDict, ensure_ascii = False, indent = 4, sort_keys=True))
rightAnswerFile.close()
print "Sentence Number: ", sentenceNumber
print "All Tags: ", alltags


