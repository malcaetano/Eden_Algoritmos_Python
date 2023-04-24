import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pants
import math

from mpl_toolkits.basemap import Basemap

fig=plt.figure(figsize=(12, 8) )
ax=fig.add_axes([0.1,0.1,0.8,0.8])

m = Basemap(llcrnrlon=-90.,llcrnrlat=-40.,urcrnrlon=-20.,urcrnrlat=5.,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            lat_0=-20,lon_0=-15,lat_ts=-20)

# nylat, nylon are lat/lon of New York
nylat = -1.4; nylon = -48
# lonlat, lonlon are lat/lon of London.
lonlat = -23; lonlon = -46
# draw great circle route between NY and London
m.drawgreatcircle(nylon,nylat,lonlon,lonlat,linewidth=2,color='b')
m.drawcoastlines()
m.fillcontinents(color='tan',lake_color='lightblue')
m.drawmapboundary(fill_color='lightblue')
# draw parallels
m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
# draw meridians
m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])


# When you use regular matplotlib commands, you need to get the mapping from the
# map projection to x,y that matplotlib uses. This is accomplished using the Basemap object,
# here which is assigned to be m()
x, y = m(lonlon, lonlat)  
plt.text(x, y, 'London',fontsize=12,fontweight='bold', ha='left',va='top',color='k')

x, y = m(nylon, nylat)  
plt.text(x, y, 'New York',fontsize=12,fontweight='bold',ha='left',va='top',color='k')

ax.set_title('Great Circle from New York to London');
