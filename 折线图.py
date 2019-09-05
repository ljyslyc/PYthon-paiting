import sys
sys.path.append('C:\Python34\Lib\site-packages')
import matplotlib.pyplot as plt
import tushare as ts
import numpy as np
import pandas as pd

data = np.array([964,991,1462.46,1369.61,1384.89,1341.78,1291.33,1053.43,1012.82])
x = range(len(data))
x_date = [datestr2num(i) for i in data.index]
plt.style.use('ggplot')
plt.figure(figsize=(10,5))
plt.title("上证50指数历史最高价、收盘价走势折线图")
plt.xlabel("时间")
plt.xticks(rotation=45)
plt.ylabel("指数")
plt.plot_date(x_date,data['close'],'-',label="收盘价")
plt.plot_date(x_date,data['high'],'-',label="最高价")
plt.legend()
plt.grid(True)