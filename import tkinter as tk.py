import tkinter as tk 
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import pandas as pd
import os

csv = os.path.abspath('DATA.csv')

data = pd.read_csv(csv, delimiter=';')

x = data['a']
y = data['b']
s = -data['c']

su = 150

n = data.shape[0]

nn = round(s.max(),0)

nn = 12
lw = 1
ms = 1

root = tk.Tk() 



if su < abs(s.max()):
	label1 = tk.Label(text = "Деформации превышены остановите строительство!", font="Arial 20")
else: 
	label1 = tk.Label(text = f'Максимальная фактическая осадка, мм: {float(abs(s.max()))}\nВеличина деформаций до предельных значений, мм: {su-abs(s.max())}', font="Arial 20")

label1.pack()


figure = plt.Figure(figsize=(6,6), dpi=300)

axs = figure.add_subplot(111)

chart_type = FigureCanvasTkAgg(figure, root)

chart_type.get_tk_widget().pack()

levels = np.linspace(s.min(), s.max(), nn)

pc = axs.tricontourf(x, y, s, levels = 12, cmap='jet', alpha= 0.5, antialiased = True)

plt.colorbar(pc, ax = axs)
 
img = plt.imread("substrate.png")

axs.set_title('Деформация ростверка');

axs.imshow(img, extent=[x.min(), x.max(), y.min(), y.max()], alpha = 1)

root.mainloop()