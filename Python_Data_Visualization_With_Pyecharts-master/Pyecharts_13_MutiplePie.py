Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part 13 Create Mutiple Pie with Pyecharts
>>> from pyecharts import Pie
>>> pie =Pie('GoodFilmRate', "Data from DouBan", title_pos='center')
>>> pie.add("", ["dram", ""], [25, 75], center=[10, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, )
<pyecharts.charts.pie.Pie object at 0x03677930>
>>> pie.add("", ["Fantnsy", ""], [24, 76], center=[30, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, legend_pos='left')
<pyecharts.charts.pie.Pie object at 0x03677930>
>>> pie.add("", ["Love", ""], [14, 86], center=[50, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
<pyecharts.charts.pie.Pie object at 0x03677930>
>>> pie.add("", ["Thriller", ""], [11, 89], center=[70, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
<pyecharts.charts.pie.Pie object at 0x03677930>
>>> pie.add("", ["Adventurer", ""], [27, 73], center=[90, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
<pyecharts.charts.pie.Pie object at 0x03677930>
>>> pie.add("", ["Action", ""], [15, 85], center=[10, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
<pyecharts.charts.pie.Pie object at 0x03677930>
>>> pie.add("", ["Comedy", ""], [54, 46], center=[30, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
<pyecharts.charts.pie.Pie object at 0x03677930>
>>> pie.add("", ["Fiction", ""], [26, 74], center=[50, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
<pyecharts.charts.pie.Pie object at 0x03677930>
>>> pie.add("", ["War", ""], [25, 75], center=[70, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
<pyecharts.charts.pie.Pie object at 0x03677930>
>>> pie.add("", ["Crime", ""], [28, 72], center=[90, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, is_legend_show=True, legend_top="center")
<pyecharts.charts.pie.Pie object at 0x03677930>
>>> pie.render()
>>> 
