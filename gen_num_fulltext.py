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
numsFile = codecs.open("G:/FNSentences/15/fulltext_15/sent.nums", "w")
for i in range(0,3690):
	numsFile.write(str(i)+"\n")