from pymongo import MongoClient


# crea una funcion que reciba una lista de cabeceras y una lista de parametros y devuelva un diccionario
def transformar(cabeceras: list, parametros: list) -> dict:
    diccionario = {}
    for i in range(len(cabeceras)):
        diccionario[cabeceras[i]] = parametros[i]
    return diccionario


class Mongo:
    def __init__(self):
        self.client = MongoClient('localhost', 27017, username='ivan', password='ivan')
        self.database = self.client['DocuMaker']

    def add_one(self, nombre, data):
        """
        Agrega una persona a la base de datos
        :param nombre:
        :param data: Datos de la persona
        """
        self.database[nombre].insert_one(data)

    def add_multiple(self, nombre, data):
        """
        Agrega varias personas a la base de datos
        :param nombre:
        :param data: Datos de las personas
        """
        self.database[nombre].insert_many(data)

    def get_all(self, nombre):
        """
        Obtiene todos los datos de la base de datos
        :return: Datos de todas las personas
        """
        return self.database[nombre].find()

    def get_name_colletions(self):
        name_calletions = []
        for coll in self.database.list_collection_names():
            name_calletions.append(coll)
        return name_calletions

