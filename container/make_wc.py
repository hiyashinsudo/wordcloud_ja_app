import datetime
import MeCab
from wordcloud import WordCloud

mecab = MeCab.Tagger()

font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'

with open('document.txt') as f:
    text = f.read()

nodes = mecab.parseToNode(text)
s = []
while nodes:
    if nodes.feature[:2] == '名詞':
        s.append(nodes.surface)
    nodes = nodes.next
wc = WordCloud(width=480, height=320, background_color="white",
               stopwords={"もの","これ","ため","それ","ところ","よう"},
               font_path=font_path)
wc.generate(" ".join(s))
now = datetime.datetime.now()
wc.to_file('wc_%s.png'%(now))
