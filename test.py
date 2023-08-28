"""
Script para validar la consistencia de las imágenes hiperespectrales.

"""

# Librerías y módulos necesarios
from hsi import HSI

# Archivos de imagen hiperespectral
hdr_file = "avocado_day_01_01_back.hdr"
bin_file = "avocado_day_01_01_back.bin"

hdr_file2 = 'NIR/day_07/avocado_day_07_04_back.hdr'
bin_file2 = 'NIR/day_07/avocado_day_07_04_back.bin'

# Crea una instancia de la clase HSI
img_hsi = HSI(hdr_file, bin_file)
#image_hsi = HSI(hdr_file2, bin_file2)

# Muestra la banda n con el mapa de colores 'viridis'
#img_hsi.show_band(100)
img_hsi.show_band(200)

# Muestra el hipercubo en 3D
img_hsi.show_3d_hypercube()

# # Exporta la banda 200 como archivo 'avocado_day_07_04_back_banda_200.svg'
# image_hsi.export_band(200, 'avocado_day_07_04_back_banda_200.svg')

