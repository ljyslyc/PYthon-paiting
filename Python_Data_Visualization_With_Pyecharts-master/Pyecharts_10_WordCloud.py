import pyecharts
from pyecharts import WordCloud
name = ['Volvo Cars','Hofstra University','Yang Lei','Ryln Lei','BeiBei','Data Scince','Data Analyst','New York','Long Island','Sillicon Valley','American Dream','Thankful','Hard Working','Data Scientist','Polestar','Xc90','Garden City','Houston,Texas','Zarb','Business Analytics Master']
value=[1112,4380,6181,4055,5668,2366,1866,1366,1166,966,456,323,10100,355,306,266,399,199,216,202]
wordcould=WordCloud(width=1300,height=620)
wordcloud=WordCloud(width=1300,height=620)
wordcloud.add("",name,value,word_size_range=[20,100])
wordcloud.render()