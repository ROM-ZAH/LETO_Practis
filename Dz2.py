import csv
import matplotlib.pyplot as plt

x1 = []
y1 = []

x2 = []
y2 = []
    
with open('dz2.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Period'] == '2010' and row['Sex'] == 'Male':
            x1.append(int(row['Age']))
            y1.append(int(row['Count']))
       
    num = 25
    for i in range(-num,num):
        y2.append(i*i)
        x2.append(i)

fig = plt.figure(figsize=(10, 10))         
ax = plt.subplot(2, 1, 1)
ax.plot(x2, y2, label='X * X')
ax.set_title('Гармонические функции')
ax.set_xlabel('x')  # Add an x-label to the axes.
ax.set_ylabel('y') 
ax1 = plt.subplot(2, 1, 2)
ax1.plot(x1, y1, label='deth')
ax1.set_title('Количество смертей в 2010 по годам(мужчины)')
ax1.set_xlabel('Age')  # Add an x-label to the axes.
ax1.set_ylabel('Count') 
ax1.legend()
plt.show()