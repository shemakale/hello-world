import matplotlib.pyplot as plt
import numpy as np
np.random.seed(444)
rng = np.arange(50)
rnd = np.random.randint(0, 10, size=(3, rng.size)) #3 графика, поэтому 3
yrs = 1950 + rng #предварительная фигня для вида графиков

#plt.subplots() создает 2 объекта. 1й объект – это объект Figure,
# контейнер, содержащий один или несколько объектов Axes (графиков).
fig, ax = plt.subplots(figsize=(7, 4)) #figsize задает размер графика
#2й объект - ax является объектом AxesSubplot. Через него можно задавать атрибуты графика
#stackplot - задает ось x, данные для графика, labels - названия в легенде
ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
ax.set_title('Combined debt growth over time') #название всей диаграммы
ax.legend(loc='upper left') #параметры легенды (локация)
ax.set_ylabel('Total debt') #название оси y
ax.set_xlabel('years') #название оси x
ax.set_xlim(xmin=yrs[0], xmax=yrs[-1]) #задает пределы оси x
fig.tight_layout() #применяется к объекту Figure в целом для очистки пробелов
plt.show() #вывести график
