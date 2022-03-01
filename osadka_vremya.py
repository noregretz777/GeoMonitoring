# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt, mpld3
import numpy as np
import pandas as pd
import os 


data = pd.read_csv('try_1.csv', delimiter=';')

col_mark = len(data.columns)-2

print(col_mark)

for i in range(0,col_mark):
	plt.plot(data['aa'],data[f'aa{str(i)}'], label = f'M{str(i+1)}', mec='w', mew=5, ms=20)
	
plt.xlabel('Дата')

plt.ylabel('Осадка,мм')

plt.title("Simple Plot")

plt.legend()

plt.show()
#mpld3.show()