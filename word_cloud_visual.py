from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

d=path.dirname(__file__)
font_path='C:\WINDOWS\Fonts\simhei.ttf'
def cloud_visual(file):
    text=open('./{}/{}word_filtered.txt'.format(file,file),encoding='utf-8').read()

    wc=WordCloud(font_path=font_path,background_color="white",max_words=200,
    max_font_size=200,random_state=42,width=1000,height=860,margin=2)

    wc.generate(text)

    plt.figure()
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.show()

    wc.to_file(path.join(d,'./{}/wordcloud.jpg'.format(file)))
if __name__=='__main__':
    cloud_visual('巴赫穆特')
