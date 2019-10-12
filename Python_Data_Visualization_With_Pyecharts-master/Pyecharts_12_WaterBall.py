Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part 12 Create WaterBall with Pyecharts
>>> from pyecharts import Liquid
>>> lq=Liquid("WaterBall")
>>> lq.add("Liquid", [0.8, 0.5, 0.2], is_liquid_outline_show=False, is_liquid_animation=True)
<pyecharts.charts.liquid.Liquid object at 0x008C8F50>
>>> lq.render()
>>> 
