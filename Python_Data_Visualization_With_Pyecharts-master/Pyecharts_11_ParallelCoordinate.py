Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part 11 Create Parallel Coordinate with Pyecharts
>>> from pyecharts import Parallel
>>> c_schema=[ {"dim": 0, "name": "data"}, {"dim": 1, "name": "AQI"}, {"dim": 2, "name": "PM2.5"}, {"dim": 3, "name": "PM10"}, {"dim": 4, "name": "CO"}, {"dim": 5, "name": "NO2"}, {"dim": 6, "name": "CO2"}, {"dim": 7, "name": "level", "type": "category", "data": ['Great', 'Good', 'MildPollution', 'Medium', 'Heavy', 'TerriblePollution']}]
>>> data = [ [1, 91, 45, 125, 0.82, 34, 23, "Good"],[2, 65, 27, 78, 0.86, 45, 29, "Good"],[3, 83, 60, 84, 1.09, 73, 27, "Good"], [4, 109, 81, 121, 1.28, 68, 51, "MildPollution"], [5, 106, 77, 114, 1.07, 55, 51, "MildPollution"], [6, 109, 81, 121, 1.28, 68, 51, "MildPollution"], [7, 106, 77, 114, 1.07, 55, 51, "MildPollution"], [8, 89, 65, 78, 0.86, 51, 26, "Good"], [9, 53, 33, 47, 0.64, 50, 17, "Good"], [10, 80, 55, 80, 1.01, 75, 24, "Good"], [11, 117, 81, 124, 1.03, 45, 24, "MildPollution"], [12, 99, 71, 142, 1.1, 62, 42, "Good"], [13, 95, 69, 130, 1.28, 74, 50, "Good"], [14, 116, 87, 131, 1.47, 84, 40, "MildPollution"]]
>>> parallel=Parallel("ParallelCoordinate-AirQulity Analysis")
>>> parallel.config(c_schema = c_schema)
<pyecharts.charts.parallel.Parallel object at 0x036619F0>
>>> parallel.add("parallel",data)
<pyecharts.charts.parallel.Parallel object at 0x036619F0>
>>> parallel.render()
>>> 
