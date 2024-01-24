import matplotlib as plt
import matplotlib.pyplot as plt
x = ["A", "B", "C", "D"]
x1 = [0.8, 1.8, 2.8, 3.8, 4.8]
x2 = [1.2, 2.2, 3.2, 4.2, 5.2]
y1 = [3, 8, 1, 10, 11]
y2 = [6, 1, 4, 13, 5]
plt.bar(x1,y1,label='Año 2022',width=0.35)
plt.bar(x2,y2,label='Año 2023',width=0.35)
plt.legend()
plt.grid()
plt.show()