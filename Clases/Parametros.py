class Parametros:
    def __init__(self, nombre, coordenadas, tipo_fuente, tam_fuente, color, grosor):
        """
        Clase que contiene los parametros como nombre, coordenadas, tipo de fuente, tamaño de fuente y color.
        :param nombre: Nombre del parametro.
        :param coordenadas: Coordenadas del parametro.
        :param tipo_fuente: Tipo de fuente del parametro.
        :param tam_fuente: Tamaño de fuente del parametro.
        :param color: Color del parametro.
        """
        self.nombre: str = nombre
        self.coordenadas: tuple[int, int] = coordenadas  # (x, y)
        self.tipo_fuente: str = tipo_fuente
        self.tam_fuente: int = tam_fuente
        self.color: tuple[int, int, int] = color   # (b, g, r)
        self.grosor: int = grosor
