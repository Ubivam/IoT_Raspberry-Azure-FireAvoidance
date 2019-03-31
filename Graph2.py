import matplottheme as mpt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

x = []
y = []
flag=True
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
lastLengt=0;
def animate(i):
    with open('ivana_mi_te_volimo.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        j = 0
        for row in plots:
            if len(row)>1:
                temp = row[0].split(':')
                pom = int(temp[0]) * 3600 + int(temp[1]) * 60 + int(temp[2])
                x.append(pom)
                try:
                    y.append(float(row[1]))
                except:
                    y.append(26)
        ax1.clear()
        ax1.plot(x,y)
        f = open("ivana_mi_te_volimo.txt", "w").close()
        plt.xlabel('Time of The Day')
        plt.ylabel('Temperature')
        plt.title('Graph representing corelation between temeperature and time')
        mpt.set_theme('ggplot2', 'ggplot2')
ani= animation.FuncAnimation(fig,animate,interval=5000)
plt.show()
