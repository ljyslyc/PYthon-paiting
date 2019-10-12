Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part 14 Create Heatmap with Pyecharts
>>> from pyecharts import HeatMap
>>> import random
>>> x_axis=["12a","1a","2a","3a","4a","5a","6a","7a","8a","9a","10a","11a","12p","1p","2p","3p","4p","5p","6p","7p","8p","9p","10p","11p",]
>>> y_axis=["Saturday","Friday","Thursday","Wednesday","Tuesday","Monday","Sunday"]
>>> data=[[i,j,random.randint(0,50)] for i in range(24) for j in range(7)]
>>> heatmap=HeatMap()
>>> heatmap.add("Rectangular Coordinate Heatmap",x_axis,y_axis,data,is_visualmap=True,visual_text_color="#000",visual_orient="horizontal")
<pyecharts.charts.heatmap.HeatMap object at 0x038C1A50>
>>> heatmap.render()
>>> 
