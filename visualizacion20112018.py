from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import itertools
import numpy as np
import matplotlib.cm as cm
import pandas as pd


# importo las tablas de excel donde estan los sismos del servicio geológico

sismos = pd.read_excel('reporte763.xlsx')
# Selecciono los datos a usar de latitud, longitud, profundidad, magnitud
# tanto los picados por mi (ms) como los picados por el servicio (ss)

lats = np.asarray(sismos['LATITUD (grados)'])
lons = np.asarray(sismos['LONGITUD (grados)'])
deps = np.asarray(sismos['PROFUNDIDAD (Km)'])
mags = np.asarray(sismos['MAGNITUD Mw'])

fechas = np.asarray(sismos['FECHA'])
horas = np.asarray(sismos['HORA_UTC'])






fig = plt.figure()
ax = Axes3D(fig, xlim=[-80, -65], ylim=[-5, 15])
ax.set_zlim(bottom=-300)


target_projection = ccrs.PlateCarree()

feature = cartopy.feature.COASTLINE
geoms = feature.geometries()

geoms = [target_projection.project_geometry(geom, feature.crs)
         for geom in geoms]

paths = list(itertools.chain.from_iterable(geos_to_path(geom) for geom in geoms))


segments = []
for path in paths:
    vertices = [vertex for vertex, _ in path.iter_segments()]
    vertices = np.asarray(vertices)
    segments.append(vertices)

lc = LineCollection(segments, color='green')


ax.add_collection3d(lc)

s = lambda x : ((x-x.min())/float(x.max()-x.min()))*50



# ax.scatter(lons,lats, -deps, s=s(mags), c=mags, cmap=cm.rainbow, label ="Sismos")
img =  ax.scatter(lons,lats, -deps, s=s(mags), c=mags, cmap=cm.rainbow, label ="Sismos")

fig.colorbar(img)
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
ax.set_zlabel('Profundidad')
ax.scatter(-73.1023,6.7557,1.3,marker='*',c='black', s=400)
ax.scatter(-73.1023,6.7557, 1.3,marker='*',c='red', s=200, label='Los Santos')

ax.scatter(-74.1029,4.7154,2.6, marker='*',c='black', s=400)
ax.scatter(-74.1029,4.7154,2.6,marker='*',c='yellow', s=200, label='Bogota')

ax.scatter(-76.6498,5.6956,marker='*',c='black', s=400) 
ax.scatter(-76.6498,5.6956,marker='*',c='blue', s=200, label='Quibdo')


 
plt.legend()
plt.savefig('fig_NablaBsing.pdf', bbox_inches='tight')
plt.show()
