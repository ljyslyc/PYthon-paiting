Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part 4 Create Dashboard with Pyecharts
>>> from pyecharts import Line,Pie,Grid
>>> attr=["Mon","Tus","Wen","Thur","Fri","Sat","Sun"]
>>> line=Line("LineChart",width=1200)
>>> line.add("WestSales",attr,[1000,1200,2500,900,800,600,1000],mark_point=["max","min"],mark_line=["average"])
<pyecharts.charts.line.Line object at 0x04059590>
>>> line.add("EastSales",attr,[1500,2300,4000,2000,1900,2000,3300],mark_point=["max","min"],mark_line=["average"])
<pyecharts.charts.line.Line object at 0x04059590>
>>> line.add("EastSales",attr,[1500,2300,4000,2000,1900,2000,3300],mark_point=["max","min"],mark_line=["average"],legend_pos="20%")
<pyecharts.charts.line.Line object at 0x04059590>
>>> # Create ModelSales pie chart
>>> attr=["V40","V60","V90","S90","S60","XC40","XC60","XC90","Polestar1"]
>>> v1=[500,200,360,1000,750,300,1200,1800,100]
>>> pie=Pie("MSalesPieChart",title_pos="55%")
>>> pie.add("",attr,v1,radius=[45,65],center=[65,50],legend_pos="80%",legend_orient="vertical")
<pyecharts.charts.pie.Pie object at 0x0479DE90>
>>> grid=Grid()
>>> grid.add(line,grid_right="55%")
<pyecharts.custom.grid.Grid object at 0x0479DE70>
>>> grid.add(pie,grid_left="60%")
<pyecharts.custom.grid.Grid object at 0x0479DE70>
>>> grid
<pyecharts.custom.grid.Grid object at 0x0479DE70>
>>> grid.render()
>>> 
