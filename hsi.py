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


class HSI:
    """
    Clase que lee, muestra y guarda la imagen Hiperespectral.
    """

    def __init__(self, hdr_file, bin_file):
        """
        Constructor de la clase HSI.
        :param hdr_file: archivo hdr de la imagen hiperespectral.
        :param bin_file: archivo binario de la imagen hiperespectral.
        """
        self.hdr_file = hdr_file
        self.bin_file = bin_file

        # Abrir el archivo HDR para obtener los metadatos
        with open(self.hdr_file, 'r') as hdr:
            lines = hdr.readlines()

        # Buscar la línea que contiene información sobre las longitudes de onda o frecuencias
        for line in lines:
            if line.startswith('wavelength') or line.startswith('frequency'):
                # Imprimir la línea que contiene la información de longitud de onda o frecuencia
                print(line.strip())

        # Cargar la imagen utilizando rasterio
        with rasterio.open(self.bin_file) as src:
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
        plt.show()

    def export_band(self, band, filename, format='svg'):
        """
        Guarda como imagen SVG una banda específica de la imagen hiperespectral.
        :param band: número de la banda a guardar o exportar.
        :param filename: nombre del archivo.
        :param format: formato o extensión con la que se crea el archivo.
        :return: imagen exportada.
        """
        if band < 1 or band > self.img_data.shape[0]:
            raise ValueError(f"El número de banda {band} está fuera del rango disponible.")

        # Convierte el número de banda base 1 a base 0
        band_idx = band - 1

        # Seleccionar la banda especificada
        band_data = self.img_data[band_idx]

        # Normalizar la banda al rango 0-255
        band_normalized = ((band_data - np.min(band_data)) / (np.max(band_data) - np.min(band_data))) * 255
        band_normalized = band_normalized.astype(np.uint8)

        # Configurar una figura de matplotlib
        fig, ax = plt.subplots(figsize=(self.img_data.shape[2] / 100, self.img_data.shape[1] / 100), dpi=100)
        ax.imshow(band_normalized, cmap='viridis')
        ax.axis('off')  # Ocultar ejes
        plt.title(f"Banda {band}")

        # Guardar la figura en formato SVG
        plt.savefig(filename, format=format, bbox_inches='tight', pad_inches=0, transparent=True)

        # Cerrar la figura de matplotlib
        plt.close()

    def show_3d_hypercube(self):
        """
        Muestra el hipercubo en 3D utilizando Mayavi.
        """
        if self.img_data is None:
            raise ValueError("La imagen hiperespectral no ha sido cargada.")

        # Crear una figura 3D con Mayavi
        mlab.figure()

        # Asegurarse de que el hipercubo esté en el rango [0, 1]
        hipercubo = self.img_data / np.max(self.img_data)

        # Crear una superficie 3D con el hipercubo
        src = mlab.pipeline.scalar_field(hipercubo)
        mlab.pipeline.image_plane_widget(src, plane_orientation='z_axes',
                                         slice_index=0, colormap='viridis')
        mlab.pipeline.image_plane_widget(src, plane_orientation='y_axes',
                                         slice_index=0, colormap='viridis')
        mlab.pipeline.image_plane_widget(src, plane_orientation='x_axes',
                                         slice_index=0, colormap='viridis')

        # Añadir una barra de colores
        mlab.colorbar(orientation='vertical')

        # Mostrar el hipercubo en una ventana interactiva
        mlab.show()


# Salvaguarda
if __name__ == '__main__':
    # Pruebas
    # ----------------------------------------------------
    # Archivos de imágen hiperespectral
    hdr_file = "NIR/day_07/avocado_day_07_01_front.hdr"
    bin_file = "NIR/day_07/avocado_day_07_01_front.bin"

    image_hsi = HSI(hdr_file, bin_file)
    image_hsi.show_band(101)  # Muestra la banda 101
