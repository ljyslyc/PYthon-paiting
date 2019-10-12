Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part 8 Create Scatter plot with pyecharts
>>> from pyecharts import EffectScatter
>>> es = EffectScatter()
>>> es.add("pin",[20],[20],symbol_size=20,effect_scale=3.5,effect_period=3,symbol="pin")
<pyecharts.charts.effectscatter.EffectScatter object at 0x00988F50>
>>> es.add("rect",[30],[30],symbol_size=12,effect_scale=4.5,effect_period=4,symbol="rect")
<pyecharts.charts.effectscatter.EffectScatter object at 0x00988F50>
>>> es.add("roundRect",[40],[40],symbol_size=30,effect_scale=5.5,effect_period=5,symbol="roundRect")
<pyecharts.charts.effectscatter.EffectScatter object at 0x00988F50>
>>> es.add("diamond_sample",[50],[50],symbol_size=10,effect_scale=6.5,effect_brushtype='fill',symbol="diamond")
<pyecharts.charts.effectscatter.EffectScatter object at 0x00988F50>
>>> es.add("arrow",[60],[60],symbol_size=16,effect_scale=5.5,effect_period=3,symbol="arrow")
<pyecharts.charts.effectscatter.EffectScatter object at 0x00988F50>
>>> es.add("triangle",[70],[70],symbol_size=12,effect_scale=4.5,effect_period=3,symbol="triangle")
<pyecharts.charts.effectscatter.EffectScatter object at 0x00988F50>
>>> es.render()
>>> 
