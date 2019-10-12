Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part 3 Create Gauge with Pyecharts
>>> from pyecharts import Gauge
>>> gauge=Gauge("KPI Completion Rate Dashboard")
>>> gauge.add("KPI","CompletionRate",66.66)
<pyecharts.charts.gauge.Gauge object at 0x02D48F50>
>>> gauge.render()
>>> 
