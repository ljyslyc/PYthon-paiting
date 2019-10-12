Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part 5 Create Funnel with Pyecharts
>>> from pyecharts import Funnel
>>> attr=["potential","contact","interested","intention","engaged","negotiation","deal"]
>>> value=[140,120,100,80,60,40,20]
>>> funnel=Funnel("CBAF") # CBAF means customer behaviour analysis funnel
>>> funnel.add("CBAF",attr,value,is_label_show=True,label_pos="inside",label_text_color="#fff")
<pyecharts.charts.funnel.Funnel object at 0x03727910>
>>> funnel.render()
>>> 
