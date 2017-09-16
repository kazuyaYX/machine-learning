import lda
import numpy as np
import jieba
import codecs
import pandas
import matplotlib.pyplot as plt
from wordcloud import WordCloud

file = codecs.open('data/红楼梦.txt', 'r', 'utf-8')
content = file.read()
file.close()

jieba.load_userdict('data/红楼梦词库.txt')

segments = []
segs = jieba.cut(content)
for seg in segs:
    if len(seg) > 1:
        segments.append(seg)
segmentDF = pandas.DataFrame({'segment': segments})

stopwords = pandas.read_csv(
    'data/中文停用词库.txt',
    encoding='utf8',
    index_col=False,
    names=['stopword'],
    # quoting=3,
    sep='\r\n'
)
segmentDF = segmentDF[~segmentDF.segment.isin(stopwords.stopword)]

wyStopWords =pandas.Series([
  # 42个文言虚词
  '之', '其', '或', '亦', '方', '于', '即', '皆', '因', '仍', '故',
  '尚', '呢', '了', '的', '着', '一', '不', '乃', '呀', '吗', '咧',
  '啊', '把', '让', '向', '往', '是', '在', '越', '再', '更', '比',
  '很', '偏', '别', '好', '可', '便', '就', '但', '儿',
  #高频副词
  '又', '也', '都','要',
  #高频代词
  '这', '那', '你', '我', '他',
  #高频动词
  '来', '去', '道', '笑', '说',
  #空格
  ' ', '', '\r\n'
])
# print(wyStopWords)

segmentDF = segmentDF[~segmentDF.segment.isin(wyStopWords)]
segCount = segmentDF.segment.value_counts()

wcloud = WordCloud(
    font_path='C:/Windows/Fonts/msyh.ttc',
    background_color='black'
)
wcloud = wcloud.fit_words(segCount.head(1000))

plt.imshow(wcloud)
plt.axis('off')
plt.show()