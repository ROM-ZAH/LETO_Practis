import random
import csv
import math 
import matplotlib.pyplot as plt

def gen_str31():
    X = []
    Y = []
    
    file = open("Alg_str31_1.csv", "w+")
    file.write("vu,x,y\n")
    
    r_min = 10
    r_max = 20
    R_min = 80
    R_max = 120
    r_pu = 50
    R_pu = 100
    
    X.append(0)
    Y.append(0)
    
    #Размещение взвода управления огнем
    X.append(0)
    Y.append(0)
    file.write("FIREU," + str(X[1]) + "," + str(Y[1]) + "\n")
    X.append(X[1] + random.uniform(r_min, r_max))
    Y.append(Y[1] + random.uniform(r_min, r_max))
    file.write("FIREU," + str(X[2]) + "," + str(Y[2]) + "\n")
    X.append(X[1] + random.uniform(r_min / 6, r_max / 6))
    Y.append(Y[1] + random.uniform(r_min, r_max))
    file.write("FIREU," + str(X[3]) + "," + str(Y[3]) + "\n")
    X.append(X[1] - random.uniform(r_min, r_max))
    Y.append(Y[1] + random.uniform(r_min, r_max))
    file.write("FIREU," + str(X[4]) + "," + str(Y[4]) + "\n")
    
    #Размещение огневых секций
    X.append(X[1] + math.sqrt(2) * random.uniform(R_min, R_max))
    Y.append(Y[1] - math.sqrt(2) * random.uniform(R_min, R_max))
    file.write("FIRES," + str(X[5]) + "," + str(Y[5]) + "\n")
    X.append(X[5] + math.sqrt(2) * random.uniform(r_pu, R_pu))
    Y.append(Y[5] + math.sqrt(2) * random.uniform(r_pu, R_pu))
    file.write("FIRES," + str(X[6]) + "," + str(Y[6]) + "\n")
    X.append(X[6] + math.sqrt(2) * random.uniform(R_min, R_max))
    Y.append(Y[6] + math.sqrt(2) * random.uniform(R_min, R_max))
    file.write("FIRES," + str(X[7]) + "," + str(Y[7]) + "\n")
    X.append(X[7] + math.sqrt(2) * random.uniform(r_pu, R_pu))
    Y.append(Y[7] + math.sqrt(2) * random.uniform(r_pu, R_pu))
    file.write("FIRES," + str(X[8]) + "," + str(Y[8]) + "\n")
    X.append(X[8] + random.uniform(r_min, r_max))
    Y.append(Y[8] + math.sqrt(2) * random.uniform(R_min, R_max))
    file.write("FIRES," + str(X[9]) + "," + str(Y[9]) + "\n")
    X.append(X[9] - math.sqrt(2) * random.uniform(r_pu, R_pu))
    Y.append(Y[9] + math.sqrt(2) * random.uniform(r_pu, R_pu))
    file.write("FIRES," + str(X[10]) + "," + str(Y[10]) + "\n")
    X.append(X[10] - math.sqrt(2) * random.uniform(R_min, R_max))
    Y.append(Y[10] + math.sqrt(2) * random.uniform(R_min, R_max))
    file.write("FIRES," + str(X[11]) + "," + str(Y[11]) + "\n")
    X.append(X[11] - math.sqrt(2) * random.uniform(r_pu, R_pu))
    Y.append(Y[11] + math.sqrt(2) * random.uniform(r_pu, R_pu))
    file.write("FIRES," + str(X[12]) + "," + str(Y[12]) + "\n")
    
    #Размещение взвода обслуживания
    X.append(X[1] + random.uniform(r_min, r_max))
    Y.append(Y[1] - random.uniform(R_min, R_max))
    file.write("vzvodOBSL," + str(X[13]) + "," + str(Y[13]) + "\n")
    X.append(X[13] - random.uniform(r_min, r_max))
    Y.append(Y[13] + random.uniform(r_min, r_max))
    file.write("vzvodOBSL," + str(X[14]) + "," + str(Y[14]) + "\n")
    X.append(X[14] - random.uniform(r_min, r_max))
    Y.append(Y[14] + random.uniform(r_min, r_max))
    file.write("vzvodOBSL," + str(X[15]) + "," + str(Y[15]) + "\n")
    X.append(X[15] + random.uniform(r_min, r_max))
    Y.append(Y[15] + random.uniform(r_min, r_max))
    file.write("vzvodOBSL," + str(X[16]) + "," + str(Y[16]) + "\n")
    X.append(X[16] - random.uniform(r_min, r_max))
    Y.append(Y[16] + random.uniform(r_min, r_max))
    file.write("vzvodOBSL," + str(X[17]) + "," + str(Y[17]) + "\n")
    X.append(X[13] - random.uniform(r_min, r_max))
    Y.append(Y[13] + random.uniform(r_min, r_max))
    file.write("vzvodOBSL," + str(X[18]) + "," + str(Y[18]) + "\n")
    X.append(X[18] - random.uniform(r_min, r_max))
    Y.append(Y[18] + random.uniform(r_min, r_max))
    file.write("vzvodOBSL," + str(X[19]) + "," + str(Y[19]) + "\n")


def draw_gen_str31():
    x1 = []
    y1 = []

    x2 = []
    y2 = []

    x3 = []
    y3 = []

    with open('Alg_str31_1.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['vu'] == 'FIREU':
                x1.append(float(row['x']))
                y1.append(float(row['y']))
            elif row['vu'] == 'FIRES':
                x2.append(float(row['x']))
                y2.append(float(row['y']))
            elif row['vu'] == 'vzvodOBSL':
                x3.append(float(row['x']))
                y3.append(float(row['y']))
    fig, ax = plt.subplots()
    
    ax.scatter(x1, y1, label='FIREU')
    ax.scatter(x2, y2, label='FIRES') 
    ax.scatter(x3, y3, label='vzvodOBSL')
    x = []
    y = []
    num = 25
    for i in range(-num,num):
        y.append(i*i)
        x.append(i)
    
   
    ax.plot(x, y, label='cos(x)')
    ax.set_title('Гармонические функции')
    ax.set_xlabel('x')  # Add an x-label to the axes.
    ax.set_ylabel('y') 
    ax.legend()

    ax.legend()    
    plt.show()

gen_str31()
draw_gen_str31()
