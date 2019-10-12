Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part 9 Create 3D Scatter Plot with pyecharts
>>> from pyecharts import Scatter3D
>>> import random
>>> data=[[random.randint(0,100),random.randint(0,100),random.randint(0,100)]for x in range(80)]
>>> range_color=['#313695','#4575b4','#74add1','#abd9e9','#e0f3f8','#ffffbf','#fee090','#fdae61','#f46d43','#d73027','#a50026']
>>> scatter3D=Scatter3D("",width=1200,height=600)
>>> scatter3D.add("",data,is_visualmap=True,visual_range_color=range_color)
>>> scatter3D.render()
>>> 
