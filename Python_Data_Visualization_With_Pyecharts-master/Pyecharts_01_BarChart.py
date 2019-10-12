import numpy
import pyecharts
from pyecharts.charts import Bar
from pyecharts_snapshot.main import make_a_snapshot #for creating output in forms of PNG and PDF
attr=["V40","V60","V90","S90","S60","XC40","XC60","XC90","Polestar1"]
v1=[500,200,360,1000,750,300,600,900,100]
v2=[300,400,160,400,1250,100,1000,1800,200]
bar=Bar({"width":"900px"})
bar.add("Dealer A",attr,v1,is_stack=True)
bar.add("Dealer B",attr,v2,is_stack=True)
bar.render()  # output html file in default file path where python lives in
make_a_snapshot('render.html', 'snapshot.png') # output png
make_a_snapshot('render.html', 'snapshot.pdf') # output PDF

