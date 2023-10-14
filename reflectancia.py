

import matplotlib.pyplot as plt
from spectral_io import  *
import spectral
import numpy as np

# Ruta al archivo .hdr y .bin
hdr_file = 'avocado_day_01_01_back.hdr'
bin_file = 'avocado_day_01_01_back.bin'

# # Cargar el archivo .hdr
# header = spectral.envi.read_envi_header(hdr_file)
#
# # Obtener información importante del encabezado
# num_bands = header['bands']
# rows = header['lines']
# cols = header['samples']
# # Convertir a enteros
# num_bands = int(num_bands)
# rows = int(rows)
# cols = int(cols)
#
# print('Número de bandas:', num_bands)
# print('Filas:', rows)
# print('Columnas:', cols)
#
# # Cargar los datos de reflectancia del archivo .bin
# print('Intentando cargar', num_bands, 'bandas,', rows, 'filas y', cols, 'columnas.')
#
# # Cargar los datos de reflectancia del archivo .bin
# reflectance_data = np.fromfile(bin_file, dtype=np.float32, count=-1)
# reflectance_data = reflectance_data.reshape(num_bands, rows, cols)
#
# # Supongamos que también tienes información sobre las longitudes de onda
# # Si tienes esta información, cárgala desde donde la tengas disponible
# # wavelengths = ... # Puedes obtenerla del header o cargarla de otro lugar
#
# # Graficar la reflectancia de una banda específica
# band_to_plot = 200  # Cambia esto a la banda que desees graficar
# reflectancia_banda = reflectance_data[band_to_plot]
# wavelength_banda = NIR_BANDS[band_to_plot]

# Usar las longitudes de onda NIR_BANDS correspondientes a cada banda
wavelengths = np.array(NIR_BANDS)

# # Tomar solo un punto de las reflectancias (por ejemplo, el primer punto)
# reflectancia_banda = np.mean( reflectance_data[:, 0, 0])
#
# # Graficar
# import matplotlib.pyplot as plt
# plt.plot(wavelengths, reflectancia_banda)
# plt.xlabel('$\lambda$ (nm)')
# plt.ylabel('Reflectancia')
# plt.title(f'Firma espectral')
# plt.show()
#---------------------------------------------------
# Cargar los datos de la imagen hiperespectral
img = spectral.envi.open(hdr_file, bin_file)
data = img.load()


# Selecciona un píxel (en este caso, el píxel en el centro de la imagen)
x, y = data.shape[0] // 2, data.shape[1] // 2
spectrum = data[x, y, :].flatten()

# # Crea un arreglo de longitudes de onda para el eje x
# wavelengths = img.metadata['wavelength']
plt.figure(figsize=(10, 6))
plt.plot(wavelengths, spectrum, color='b', label='Firma Espectral')
plt.xlabel('Longitud de onda (nm)')
plt.ylabel('Reflectancia')
plt.title('Firma Espectral de un Píxel')
plt.legend()
plt.grid()
plt.show()
