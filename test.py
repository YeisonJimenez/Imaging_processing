"""
Script para validar la consistencia de las imágenes hiperespectrales.

"""

# Librerías y módulos necesarios
from hsi import HSI
from spectral_io import VIS_BANDS, VIS_COR_BANDS, NIR_BANDS

# Archivos de imagen hiperespectral
# NIR
hdr_avocado_nir_ripe = "nir/ripe/avocado_day_04_08_front.hdr"
bin_avocado_nir_ripe = "nir/ripe/avocado_day_04_08_front.bin"
hdr_avocado_nir_unripe = "nir/unripe/avocado_day_05_03_front.hdr"
bin_avocado_nir_unripe = "nir/unripe/avocado_day_05_03_front.bin"
hdr_avocado_nir_overripe = "nir/overripe/avocado_day_10_01_front.hdr"
bin_avocado_nir_overripe = "nir/overripe/avocado_day_10_01_front.bin"

hdr_kiwi_nir_ripe = 'nir/ripe/kiwi_day_01_28_back.hdr'  # Ripe
bin_kiwi_nir_ripe = 'nir/ripe/kiwi_day_01_28_back.bin'  # Ripe
hdr_kiwi_nir_unripe = 'nir/unripe/kiwi_day_05_26_front.hdr'  # Unripe
bin_kiwi_nir_unripe = 'nir/unripe/kiwi_day_05_26_front.bin'  # Unripe
hdr_kiwi_nir_overripe = 'nir/overripe/kiwi_day_04_22_front.hdr'  # Overripe
bin_kiwi_nir_overripe = 'nir/overripe/kiwi_day_04_22_front.bin'  # Overripe

# VIS
hdr_avocado_vis_ripe = 'vis/ripe/avocado_day_m4_01_29_front.hdr'
bin_avocado_vis_ripe = 'vis/ripe/avocado_day_m4_01_29_front.bin'
hdr_avocado_vis_unripe = 'vis/unripe/avocado_day_m4_03_02_front.hdr'
bin_avocado_vis_unripe = 'vis/unripe/avocado_day_m4_03_02_front.bin'
hdr_avocado_vis_overripe = 'vis/overripe/avocado_day_m4_06_05_back.hdr'
bin_avocado_vis_overripe = 'vis/overripe/avocado_day_m4_06_05_back.bin'

hdr_kiwi_vis_ripe = 'vis/ripe/kiwi_day_01_28_back.hdr'
bin_kiwi_vis_ripe = 'vis/ripe/kiwi_day_01_28_back.bin'
hdr_kiwi_vis_unripe = 'vis/unripe/kiwi_day_05_26_front.hdr'
bin_kiwi_vis_unripe = 'vis/unripe/kiwi_day_05_26_front.bin'
hdr_kiwi_vis_overripe = 'vis/overripe/kiwi_day_04_22_front.hdr'
bin_kiwi_vis_overripe = 'vis/overripe/kiwi_day_04_22_front.bin'

hdr_papaya_ripe = 'vis/ripe/papaya_day_m4_06_06_front.hdr'
bin_papaya_ripe = 'vis/ripe/papaya_day_m4_06_06_front.bin'
hdr_papaya_unripe = 'vis/unripe/papaya_day_m4_04_23_front.hdr'
bin_papaya_unripe = 'vis/unripe/papaya_day_m4_04_23_front.bin'
hdr_papaya_overripe = 'vis/overripe/papaya_day_m4_06_24_front.hdr'
bin_papaya_overripe = 'vis/overripe/papaya_day_m4_06_24_front.bin'
# hdr_kaki = 'kaki_day_4_m3_04_front.hdr'
# bin_kaki = 'kaki_day_4_m3_04_front.bin'
hdr_kaki = 'kaki_day_4_m3_04_back.hdr'
bin_kaki = 'kaki_day_4_m3_04_back.bin'
# Crea una instancia de la clase HSI
# # Crea una instancia de la clase HSI
# avocado_hsi = HSI(hdr_avocado, bin_avocado)
avocado_hsi_nir = HSI(hdr_avocado_nir_ripe, bin_avocado_nir_ripe, hdr_avocado_nir_unripe, bin_avocado_nir_unripe,
                      hdr_avocado_nir_overripe,
                      bin_avocado_nir_overripe)
avocado_hsi_vis = HSI(hdr_avocado_vis_ripe, bin_avocado_vis_ripe, hdr_avocado_vis_unripe, bin_avocado_vis_unripe,
                      hdr_avocado_vis_overripe,
                      bin_avocado_vis_overripe)

kiwi_hsi_nir = HSI(hdr_kiwi_nir_ripe, bin_kiwi_nir_ripe, hdr_kiwi_nir_unripe, bin_kiwi_nir_unripe,
                   hdr_kiwi_nir_overripe,
                   bin_kiwi_nir_overripe)
kiwi_hsi_vis = HSI(hdr_kiwi_vis_ripe, bin_kiwi_vis_ripe, hdr_kiwi_vis_unripe, bin_kiwi_vis_unripe,
                   hdr_kiwi_vis_overripe,
                   bin_kiwi_vis_overripe)

papaya_hsi_vis = HSI(hdr_papaya_ripe, bin_papaya_ripe, hdr_papaya_unripe, bin_papaya_unripe,
                   hdr_papaya_overripe,
                   bin_papaya_overripe)
# avocado_hsi_vis = HSI(hdr_avocado_vis, bin_avocado_vis)
# kiwi_hsi_vis = HSI(hdr_kiwi_vis, bin_kiwi_vis)
# papaya_hsi = HSI(hdr_papaya, bin_papaya)
# kaki_hsi = HSI(hdr_kaki, bin_kaki)
# Muestra la banda n con el mapa de colores 'viridis'
# img_hsi.show_band(100)
# avocado_hsi.show_band(200)

# kiwi_hsi.show_band(200, cmap='plasma')
#
# papaya_hsi.show_band(200, cmap='Oranges')
#
# kaki_hsi.show_band(150, 'plasma')
# # Muestra el hipercubo en 3D
# avocado_hsi.show_3d_hypercube()
# kiwi_hsi.show_3d_hypercube(cmap='nipy_spectral')
# papaya_hsi.show_3d_hypercube(cmap='Oranges')

# kiwi_hsi.show_3d_hypercube()
# # # Exporta la banda 200 como archivo 'avocado_day_07_04_back_banda_200.svg'
# avocado_hsi.export_band(200, 'avocado_day_07_04_back_banda_200.svg')
#
# kiwi_hsi.export_band(200, 'kiwi_day_05_01_front_banda_200.svg', cmap='plasma')
#
# papaya_hsi.export_band(200, 'papaya_day_m4_01_22_front_banda_200.svg', cmap='Oranges')

# Firmas espectrales
# avocado_hsi.plot_hsi_reflectance(NIR_BANDS, filename='avocado-nir-firma.svg')
avocado_hsi_nir.plot_hsi_reflectance(NIR_BANDS, filename='avocado-nir-firma.svg')
kiwi_hsi_nir.plot_hsi_reflectance(NIR_BANDS, filename='Kiwi-nir-firma.svg')

avocado_hsi_vis.plot_hsi_reflectance(VIS_BANDS, filename='avocado-vis-firma.svg')
kiwi_hsi_vis.plot_hsi_reflectance(VIS_BANDS, filename='Kiwi-vis-firma.svg')
papaya_hsi_vis.plot_hsi_reflectance(VIS_BANDS, filename='papaya-vis-firma.svg')
# avocado_hsi_vis.plot_hsi_reflectance(VIS_BANDS, filename='avocado-vis-firma.svg')
# kiwi_hsi_vis.plot_hsi_reflectance(VIS_BANDS, filename='Kiwi-vis-firma.svg')
# papaya_hsi.plot_hsi_reflectance(VIS_COR_BANDS, filename='papaya-vis-firma.svg')
# kaki_hsi.plot_hsi_reflectance(VIS_COR_BANDS, filename='kaki-vis-firma.svg')
# kaki_hsi.export_band(200, 'kaki_day_4_m3_04_back_banda_200.svg', cmap='Oranges')

# # Hipercubo
# kaki_hsi.show_3d_hypercube(cmap='Oranges')
