import xmltodict
import codecs
import os
import json
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
desFileName = 'G:/FNSentences/sentencesAll.txt'
desFile = codecs.open(desFileName, "w")
srcDir = 'D:/SJTU/SpeechLab/FrameNet/FrameNetData/fndata-1.6/lu'
i = 0
sentenceNumber = 0
for parent, dirnames, filenames in os.walk(srcDir):
    for filename in filenames:
        if '.xml' not in filename:
            continue
        i += 1
        if i > 1000:
            break
        file = codecs.open(os.path.join(srcDir, filename), "r")
        fileStr = file.read()
        file.close()
        dic = xmltodict.parse(fileStr)
        lu = dic['lexUnit']
        try:
            for subCorpus in lu['subCorpus']:
                for sentence in subCorpus['sentence']:
                    desFile.write(sentence['text']+'\n')
                    sentenceNumber += 1
        except TypeError: continue
        except KeyError : continue
desFile.close()
print "Sentence Number: ", sentenceNumber



