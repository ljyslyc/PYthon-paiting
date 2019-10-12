Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part 7 Create Polar Coordinates with Pyecharts
>>> from pyecharts import Polar
>>> radius=['Mon','Tus','Wen','Thu','Fri','Sat','Sun']
>>> polar=Polar("Polar Coordinate",width=1200,height=600)
>>> polar.add("XC90",[100,200,300,200,400,500],radius_data=radius,type="barRadius",is_stack=True)
<pyecharts.charts.polar.Polar object at 0x0366D5B0>
>>> polar.add("XC60",[200,100,400,150,300,600],radius_data=radius,type="barRadius",is_stack=True)
<pyecharts.charts.polar.Polar object at 0x0366D5B0>
>>> polar.add("S60",[150,50,300,250,200,500],radius_data=radius,type="barRadius",is_stack=True)
<pyecharts.charts.polar.Polar object at 0x0366D5B0>
>>> polar.add("S90",[120,180,200,350,400,1000],radius_data=radius,type="barRadius",is_stack=True)
<pyecharts.charts.polar.Polar object at 0x0366D5B0>
>>> polar.add("xc40",[250,280,100,150,600,1200],radius_data=radius,type="barRadius",is_stack=True)
<pyecharts.charts.polar.Polar object at 0x0366D5B0>
>>> polar.add("V40",[50,80,200,150,60,120],radius_data=radius,type="barRadius",is_stack=True)
<pyecharts.charts.polar.Polar object at 0x0366D5B0>
>>> polar.add("V60",[130,180,260,150,360,700],radius_data=radius,type="barRadius",is_stack=True)
<pyecharts.charts.polar.Polar object at 0x0366D5B0>
>>> polar.add("PoleStar1",[50,80,20,150,160,220],radius_data=radius,type="barRadius",is_stack=True)
<pyecharts.charts.polar.Polar object at 0x0366D5B0>
>>> polar.render()
>>> 
