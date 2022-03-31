from wordcloud import WordCloud

text = WordCloud.__doc__
wc = WordCloud(width=480, height=320)
wc.generate(text)
wc.to_file('test.png')
