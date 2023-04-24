#########################################################
#    precisa instalar essas duas bibliotecas
#    pip install geopy
#    conda install -c anaconda basemap
########################################################
import os
os.environ["PROJ_LIB"] = "C:\\Users\\Dell\\Anaconda3\\Library\\share"; #fixr
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as fig
import numpy as np
# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
map = Basemap(projection='ortho', lat_0=-20, lon_0=-50,
              resolution='l', area_thresh=1000.0)
 
map.drawcoastlines()
map.drawcountries() 
map.drawmapboundary()
fig.show()

long, lat = map(*zip(*[(-51.22, -30.02),(-46.38,-23.96)]))

map.plot(long, lat, marker='o', markersize=6, markerfacecolor='red', linewidth=0)


