import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

fig = plt.figure()
fig.set_figheight(12)
fig.set_figwidth(16)

# Задание 1

ax_1 = fig.add_subplot(2, 3, 1)
plt.axis('off')

ax_1.set_title('Сесилия Пейн', fontfamily='century gothic', fontweight='bold', fontsize=15)
with cbook.get_sample_data('/Users/grvml/Downloads/image.png') as image_file:
    image = plt.imread(image_file)

ax_1.imshow(image)

# Задание 2

ax_2 = fig.add_subplot(2, 3, 2)
ax_2.grid()
ax_2.set_title('Стандартный график с заливкой', fontfamily='comic sans ms', fontstyle='oblique',
               fontsize=15, color=(0.8, 0.5, 0.1, 1), fontweight='normal')
plt.xticks(rotation=60)
plt.yticks(rotation=60)

with open("file_date.txt") as file:
    lines = file.readlines()
x = [int(i) for i in lines[0].split()]
y1 = [float(i) for i in lines[9].split()]

y2 = np.zeros(27)

ax_2.plot(x, y1)

ax_2.fill_between(x, y1, y2, where=(y1 <= y2), color='r', alpha=0.5)
ax_2.fill_between(x, y1, y2, where=(y1 >= y2), color='g', alpha=0.5)

ax_2.set_xlabel('Время', fontfamily='courier', fontsize=10)
ax_2.set_ylabel('Температура', fontfamily='courier', fontsize=10)

# Задание 3

ax_3 = fig.add_subplot(2, 3, 3)
ax_3.set_facecolor('floralwhite')
ax_3.grid()

with open ("fig8.txt") as file:
    lines = file.readlines()
x_3 = [int(i) for i in lines[16].split()]
y_3 = [int(i) for i in lines[17].split()]
x_3 = np.arange(x_3[0], x_3[1]+1)
ax_3.bar(x_3, y_3, color='g')
ax_3.set_title('Диаграмма с аннотацией')

ax_3.arrow(275, 15, -15, -1.5, width=0.3, color='#F95C5C')
ax_3.text(260, 14, 'Выпадающая точка', rotation=12, fontsize=12, fontfamily='times new roman',
          color=(0.5, 0.2, 0.3, 0.8), fontstyle='oblique', fontweight='bold')

# Задание 4

ax_4 = fig.add_subplot(2, 3, 4)
ax_4.grid()
ax_4.set_title('График с легендой')
plt.xticks(rotation=15)

x = np.linspace(-1, 1, 2000)
p = np.poly([-1.63, -0.44, 0.35, 1.9])

n = x * x * x * x
k = 0
for i in p:
    k = i * n + k
    n = n / x

y1 = np.sin(2 * x) ** 2 - np.cos(6 * x) ** 2
y2 = 0.3 * k

ax_4.plot(x, y1, label='sin(2x)^2 - cos(6x)^2', linestyle='--')
ax_4.plot(x, y2, label='0.3*p(x)')

l = ax_4.legend(fontsize=13, prop={'family': 'tahoma', 'style': 'italic', 'weight': 'bold'})
for text in l.get_texts():
    text.set_color("red")

# Задание 5

ax_5 = fig.add_subplot(2, 3, 5)
ax_5.set_title('Диаграмма рассеяния')
ax_5.grid(color='r', alpha=0.2)

x = np.random.rand(300)
y1 = np.random.normal(7, 3, size=300)
y2 = np.random.uniform(0, 10, size=300)
y3 = np.random.gamma(shape=0.8, scale=1.7, size=300)

ax_5.scatter(x, y1, c=(1, 0.7, 0), s=2)
ax_5.scatter(x + 1, y2, c='#1ed624', s=2)
ax_5.scatter(x + 2, y3, c='w', s=2)

ax_5.set_facecolor('black')

# Задание 6

ax_6 = fig.add_subplot(2, 3, 6)
ax_6.set_title('Фигуры Лиссажу')
t = np.linspace(0, 2 * np.pi, 500)

x = 4 * np.sin(3 * t + np.pi / 2)
y = 13 * np.sin(4 * t)

ax_6.plot(x, y, 'b', linewidth=0.5)
ax_6.grid(color='r', linewidth=0.5)
ax_6.fill(x, y, color=(0.75, 0, 0.75), fill=True, alpha=0.3)

fig.set_facecolor('#f5f5dc')

plt.show()
