"""
En este script se crea una clase llamada 'HSI' la cual permite leer una imagen
hiperespectral, mostrarla y guardarla.


"""
metadata = {
    "autor": "Yeison Stiven Jiménez Mejía",
    "fecha": "agosto de 2023",
    "descripcion": "Clase que recibe una imagen hiperespectral",
}

import rasterio
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from mayavi import mlab
import spectral


# from mayavi.mlab import pipeline, show, surface, move


class HSI:
    """
    Clase que lee, muestra y guarda la imagen Hiperespectral.
    """

    def __init__(self, hdr_ripe, bin_ripe, hdr_unripe, bin_unripe,
                             hdr_overripe, bin_overripe):
        """
        Constructor de la clase HSI.
        :param hdr_file: archivo hdr de la imagen hiperespectral.
        :param bin_file: archivo binario de la imagen hiperespectral.
        """

        # Cargar los datos de la imagen hiperespectral
        self.hdr_ripe = hdr_ripe
        self.bin_ripe = bin_ripe
        self.hdr_unripe = hdr_unripe
        self.bin_unripe = bin_unripe
        self.hdr_overripe = hdr_overripe
        self.bin_overripe = bin_overripe
        img_ripe = spectral.envi.open(self.hdr_ripe, self.bin_ripe)
        data1 = img_ripe.load()

        img_unripe = spectral.envi.open(self.hdr_unripe, self.bin_unripe)
        data2 = img_unripe.load()

        img_overripe = spectral.envi.open(self.hdr_overripe, self.bin_overripe)
        data3 = img_overripe.load()

        # Selecciona un píxel (en este caso, el píxel en el centro de la imagen)
        x1, y1 = data1.shape[0] // 2, data1.shape[1] // 2
        self.spectrum1 = np.mean(data1, axis=(0, 1)) # data1[x1, y1, :].flatten()

        # Selecciona un píxel (en este caso, el píxel en el centro de la imagen)
        x2, y2 = data2.shape[0] // 2, data2.shape[1] // 2
        self.spectrum2 = np.mean(data2, axis=(0, 1)) # data2[x2, y2, :].flatten()

        # Selecciona un píxel (en este caso, el píxel en el centro de la imagen)
        x3, y3 = data3.shape[0] // 2, data3.shape[1] // 2
        self.spectrum3 = np.mean(data3, axis=(0, 1))  # data3[x3, y3, :].flatten()

        # Abrir el archivo HDR para obtener los metadatos
        with open(self.hdr_ripe, 'r') as hdr:
            lines = hdr.readlines()

        # Buscar la línea que contiene información sobre las longitudes de onda o frecuencias
        for line in lines:
            if line.startswith('wavelength') or line.startswith('frequency'):
                # Imprimir la línea que contiene la información de longitud de onda o frecuencia
                print(line.strip())

        # Cargar la imagen utilizando rasterio
        with rasterio.open(self.bin_ripe) as src:
            self.img_data = src.read()

    def show_band(self, band, cmap='viridis'):
        """
        Muestra una banda específica de la imagen hiperespectral.
        :param band: El índice o número de banda a mostrar (base 0 o base 1).
        :param cmap: El mapa de colores a utilizar (por defecto, 'viridis').
        """
        if band < 1:
            raise ValueError("El número de banda debe ser mayor o igual a 1.")

        # Convierte el número de banda base 1 a base 0
        band_idx = band - 1

        if band_idx >= self.img_data.shape[0]:
            raise ValueError(f"El número de banda {band} está fuera del rango disponible.")

        # Seleccionar la banda especificada
        band_data = self.img_data[band_idx]

        # Normalizar la banda al rango 0-255
        band_normalized = ((band_data - np.min(band_data)) / (np.max(band_data) - np.min(band_data))) * 255
        band_normalized = band_normalized.astype(np.uint8)

        # Convertir el arreglo de numpy a una imagen PIL
        img = Image.fromarray(band_normalized)

        # Mostrar la imagen con el mapa de colores especificado
        plt.imshow(img, cmap=cmap)
        plt.title(f"Banda {band}")
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.show()

    def export_band(self, band, filename, format='svg', cmap='viridis'):
        """
        Guarda como imagen SVG una banda específica de la imagen hiperespectral.
        :param band: número de la banda a guardar o exportar.
        :param filename: nombre del archivo.
        :param format: formato o extensión con la que se crea el archivo.
        :return: imagen exportada.
        """

        if band < 1:
            raise ValueError("El número de banda debe ser mayor o igual a 1.")

        # Convierte el número de banda base 1 a base 0
        band_idx = band - 1

        if band_idx >= self.img_data.shape[0]:
            raise ValueError(f"El número de banda {band} está fuera del rango disponible.")

        # Seleccionar la banda especificada
        band_data = self.img_data[band_idx]

        # Normalizar la banda al rango 0-255
        band_normalized = ((band_data - np.min(band_data)) / (np.max(band_data) - np.min(band_data))) * 255
        band_normalized = band_normalized.astype(np.uint8)

        # Convertir el arreglo de numpy a una imagen PIL
        img = Image.fromarray(band_normalized)

        # Mostrar la imagen con el mapa de colores especificado
        plt.imshow(img, cmap=cmap)
        plt.title(f"Banda {band}")
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.savefig(filename, bbox_inches='tight', format=format, transparent=True)
        plt.show()

    def show_3d_hypercube(self, title='Hipercubo 3D', cmap='viridis'):
        """
        Muestra el hipercubo en 3D utilizando Mayavi.
        """
        if self.img_data is None:
            raise ValueError("La imagen hiperespectral no ha sido cargada.")

        # Crear una figura 3D con Mayavi
        fig = mlab.figure()

        # Asegurarse de que el hipercubo esté en el rango [0, 1]
        hipercubo = self.img_data / np.max(self.img_data)

        # Crear una superficie 3D con el hipercubo
        src = mlab.pipeline.scalar_field(hipercubo)
        mlab.pipeline.image_plane_widget(src, plane_orientation='z_axes',
                                         slice_index=0, colormap=cmap)
        mlab.pipeline.image_plane_widget(src, plane_orientation='y_axes',
                                         slice_index=0, colormap=cmap)
        mlab.pipeline.image_plane_widget(src, plane_orientation='x_axes',
                                         slice_index=0, colormap=cmap)

        # Añadir una barra de colores
        mlab.colorbar(orientation='vertical')

        # Set the title of the interactive 3D plot
        mlab.title(title, color=(0, 0, 0), height=0.9)

        # Mostrar el hipercubo en una ventana interactiva
        mlab.show()

    def plot_hsi_reflectance(self, wavelengths, filename, format='svg'):

        # # Crea un arreglo de longitudes de onda para el eje x
        # wavelengths = img.metadata['wavelength']
        # plt.figure(figsize=(10, 6))
        plt.plot(wavelengths, self.spectrum1, color='y', label='Ripe')
        plt.plot(wavelengths, self.spectrum2, color='g', label='Unripe')
        plt.plot(wavelengths, self.spectrum3, color='r', label='Overripe')
        plt.xlabel('Longitud de onda (nm)', fontdict={'family': 'serif', 'size': 12})
        plt.ylabel('Reflectancia media', fontdict={'family': 'serif', 'size': 12})
        plt.title('Firma Espectral', fontdict={'family': 'serif', 'size': 16})
        plt.legend()
        # plt.grid()
        plt.savefig(filename, bbox_inches='tight', format=format, transparent=True)
        plt.show()



# Salvaguarda
if __name__ == '__main__':
    # Pruebas
    # ----------------------------------------------------
    # Archivos de imágen hiperespectral
    hdr_file = "kiwi_day_05_01_back.hdr"
    bin_file = "kiwi_day_05_01_back.bin"

    image_hsi = HSI(hdr_file, bin_file)
    image_hsi.show_band(101)  # Muestra la banda 101
