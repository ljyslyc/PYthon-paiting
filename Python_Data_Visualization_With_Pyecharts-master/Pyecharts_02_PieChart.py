Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part 2 Draw Pie Chart with Pyecharts
>>> from pyecharts import Pie
>>> from pyecharts_snapshot.main import make_a_snapshot #for creating output in forms of PNG and PDF
>>> attr=["V40","V60","V90","S90","S60","XC40","XC60","XC90","Polestar1"]
>>> v1=[500,200,360,1000,750,300,1200,1800,100]
>>> pie=Pie("MSales")
>>> pie.add("",attr,v1,is_label_show=True)
<pyecharts.charts.pie.Pie object at 0x03178F50>
>>> pie.render()
>>> make_a_snapshot('render.html', 'snapshot.png') # output png
phantomjs version: 2.1.1

Generating file ...
File saved in C:\Users\LylionCj\AppData\Local\Programs\Python\Python36-32\snapshot.png
>>> make_a_snapshot('render.html', 'snapshot.pdf') # output PDF
phantomjs version: 2.1.1

Generating file ...
File saved in C:\Users\LylionCj\AppData\Local\Programs\Python\Python36-32\snapshot.pdf
>>> 
