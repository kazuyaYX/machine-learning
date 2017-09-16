import lda
import numpy as np
import jieba
import codecs
import pandas

segments = ['a', 'b', 'v', 'a']
stopwords = ['b']
segmentDF = pandas.DataFrame({'segment': segments})
segmentDF = segmentDF[~segmentDF.segment.isin(stopwords)]
# print(segmentDF)
print(segmentDF.segment.value_counts().head(1))