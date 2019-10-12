Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part 6 Create Radar with Pyecharts
>>> from pyecharts import Radar
>>> schema=[("Sales",6500),("Magagement",16000),("IT",30000),("CustomerService",38000),("R&D",52000),("Marketing",25000)]
>>> v1=[[4300,10000,28000,35000,50000,19000]]
>>> v2=[[5000,14000,28000,31000,42000,21000]]
>>> radar=Radar()
>>> radar.config(schema)
<pyecharts.charts.radar.Radar object at 0x038A7930>
>>> radar.add("budget",v1,is_splitline=True,is_axisline_show=True)
<pyecharts.charts.radar.Radar object at 0x038A7930>
>>> radar.add("spent",v2,label_color=["#4e79a7"],is_area_show=False)
<pyecharts.charts.radar.Radar object at 0x038A7930>
>>> radar.show_config()

{
    "title": [
        {
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "fontSize": 18
            },
            "subtextStyle": {
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "save as image"
            },
            "restore": {
                "show": true,
                "title": "restore"
            },
            "dataView": {
                "show": true,
                "title": "data view"
            }
        }
    },
    "series_id": 8035395,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "backgroundColor": "rgba(50,50,50,0.7)",
        "borderColor": "#333",
        "borderWidth": 0
    },
    "series": [
        {
            "type": "radar",
            "name": "budget",
            "data": [
                [
                    4300,
                    10000,
                    28000,
                    35000,
                    50000,
                    19000
                ]
            ],
            "symbol": "circle",
            "label": {
                "normal": {
                    "show": false,
                    "position": "top",
                    "textStyle": {
                        "fontSize": 12
                    }
                },
                "emphasis": {
                    "show": true,
                    "textStyle": {
                        "fontSize": 12
                    }
                }
            },
            "itemStyle": {
                "normal": {}
            },
            "lineStyle": {
                "normal": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "areaStyle": {
                "opacity": 0
            }
        },
        {
            "type": "radar",
            "name": "spent",
            "data": [
                [
                    5000,
                    14000,
                    28000,
                    31000,
                    42000,
                    21000
                ]
            ],
            "symbol": "circle",
            "label": {
                "normal": {
                    "show": false,
                    "position": "top",
                    "textStyle": {
                        "fontSize": 12
                    }
                },
                "emphasis": {
                    "show": true,
                    "textStyle": {
                        "fontSize": 12
                    }
                }
            },
            "itemStyle": {
                "normal": {}
            },
            "lineStyle": {
                "normal": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "areaStyle": {
                "opacity": 0
            }
        }
    ],
    "legend": [
        {
            "data": [
                "budget",
                "spent"
            ],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12
            }
        }
    ],
    "animation": true,
    "radar": {
        "indicator": [
            {
                "name": "Sales",
                "max": 6500
            },
            {
                "name": "Magagement",
                "max": 16000
            },
            {
                "name": "IT",
                "max": 30000
            },
            {
                "name": "CustomerService",
                "max": 38000
            },
            {
                "name": "R&D",
                "max": 52000
            },
            {
                "name": "Marketing",
                "max": 25000
            }
        ],
        "name": {
            "textStyle": {
                "color": "#333",
                "fontSize": 12
            }
        },
        "splitLine": {
            "show": true,
            "lineStyle": {
                "normal": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        },
        "splitArea": {
            "show": true,
            "areaStyle": {
                "opacity": 1
            }
        },
        "axisLine": {
            "show": true,
            "lineStyle": {
                "normal": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    },
    "color": [
        "#4e79a7",
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
}
>>> radar.render()
>>> 
