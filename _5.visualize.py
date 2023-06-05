from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

d=path.dirname(__file__)
font_path='C:\WINDOWS\Fonts\simhei.ttf'
text=open('无耻之徒_words.txt',encoding='utf-8').read()

wc=WordCloud(font_path=font_path,background_color="white",max_words=200,
max_font_size=200,random_state=42,width=1000,height=860,margin=2)

wc.generate(text)

plt.figure()
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()

wc.to_file(path.join(d,'wordcloud.jpg'))