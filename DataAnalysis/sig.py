# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma
mp.figure('Signal', facecolor='lightgray')
mp.title('Signal', fontsize=20)
mp.xlabel('Time', fontsize=14)
mp.ylabel('Signal', fontsize=14)
ax = mp.gca()
ax.set_ylim(-3, 3)
ax.set_xlim(0, 10)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 創建曲線對象
pl, = mp.plot([], [], c='orangered')
# 在曲線對象內部創建緩衝區，以容納曲線上點的橫坐標
pl.set_data([], [])


# 更新回調函數
def update(data):
    t, v = data
    # 獲取曲線上當前所有的點
    x, y = pl.get_data()
    # 追加新採集到的點
    x.append(t)
    y.append(v)
    # 獲取當前水平座標範圍
    x_min, x_max = ax.get_xlim()
    # 如果新點水平座標超過水平座標範圍
    if t >= x_max:
        # 重新設置水平座標範圍
        ax.set_xlim(t - (x_max - x_min), t)
        # 重新繪製座標軸
        ax.figure.canvas.draw()
    # 設置曲線上的點
    pl.set_data(x, y)


# 生成器函數
def generator():
    t = 0
    while True:
        v = np.sin(2 * np.pi * t) * np.exp(
            np.sin(0.2 * np.pi * t))
        yield t, v
        t += 0.05


# 啟動動畫
anim = ma.FuncAnimation(
    mp.gcf(), update, generator, interval=5)
mp.show()
