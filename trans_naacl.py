import xmltodict
import codecs
import os
import json
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
srcName = "D:/SJTU/SpeechLab/FrameNet/naacl2012/cv.train.sentences.frame.elements"
dstName = "D:/SJTU/SpeechLab/FrameNet/naacl2012/cv.train.sentences.frame.elements.trans"
src = codecs.open(srcName, "r")
dst = codecs.open(dstName, "w")
for line in src:
	dst.write("0\t20.000\t"+line)
src.close()
dst.close()
dst = codecs.open(dstName, "r")
for line in dst:
	if "\r" in line:
		print "ruok"
	break