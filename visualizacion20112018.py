# visualización sismos Colombia. Iván Ferreira (2019)

import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from mpl_toolkits.mplot3d import axes3d  # noqa: F401 unused import
import numpy as np
import pandas as pd
import matplotlib.cm as cm


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


hora = str(horas[2])
hora = hora.replace(':','-',1)
fecha = str(fechas[2])
#prueba del formato de fecha con hora y minutos

print(fecha[:10]+'h'+hora[:5])





# Fixing random state for reproducibility

fig = plt.figure(figsize=(12,9))
ax = fig.add_subplot(111, projection='3d')
# proj_ax = plt.figure().add_axes([0, 0, 1, 1], projection=ccrs.Mercator())

c_lons = lons - lons.min()
c_lats = lats - lats.min()



prof = 0


# Se ubican las ciudades

ax.scatter(c_lons, c_lats, -deps,'r*', c=mags/10, cmap='jet', s=mags*3,label ="Sismos")

xx, yy = np.meshgrid(range(2), range(2)) # se crea la red que genera el plano
xx, yy = xx/2, yy/2
z = np.zeros((2,2))
a = 0
z= np.array([[ a,  a],[a, a]]) # plano en cero, se crea variable a para controlar su ubicación
ax.plot_surface(xx, yy, z,alpha=0.2)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Profundidad')
ax.set_title("Sismos Colombia 2011-2018\n (MW>3.5)\n")

plt.legend()
plt.show()
