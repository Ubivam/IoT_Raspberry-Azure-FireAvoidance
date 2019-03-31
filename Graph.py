import matplotlib              # plotting library
import matplotlib.mlab as mlab # matlab compatibility functions
from matplotlib.backends import backend_agg as agg # raster backend
import pandas       # data analysis library
import numpy        # numerical routines

table = pandas.read_table("../example_data/column_data.txt", 
                          sep=' ', header=None, 
                          names=["x", "y", "z", "w"])
fig = matplotlib.figure.Figure() # create the figure
agg.FigureCanvasAgg(fig)         # attach the rasterizer
ax = fig.add_subplot(1, 1, 1)    # make axes to plot on
ax.plot(table.x, table.y, '-', color='k', linewidth=2, label="Series 1")
ax.plot(table.x, table.z, '--', color='r', linewidth=2, label="Series 2")
ax.plot(table.x, table.w, '-', color=[0.75]*3, linewidth=3, label="Series 3")
ax.set_xticks(numpy.arange(0, 10, 1))
ax.set_yticks(numpy.arange(0,1,0.1))
ax.legend(loc=4)
ax.grid()

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Line Plot of Column Data")

fig.savefig("line_plot.png")
