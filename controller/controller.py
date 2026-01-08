import sys, datetime
from view.view import ViewBotiga
from model.model import ModelBotiga

class Botiga:

    def __init__(self):
        self.view = ViewBotiga()
        self.model = ModelBotiga()
        self.client = None
        self.cistella = {}

    def app(self):
        while True:
            self.view.show_menu()
            op = self.view.get_option()
            self.options(op)

    def options(self, option):
        match option:
            case 0:
                self.sortir()
            case 1:
                self.login()
            case 2:
                self.mostrar_productes()
            case 3:
                self.mostrar_cistella()
            case 4:
                self.comprar()
            case 5:
                self.generar_factura()

    def sortir(self):
        self.model.write()
        sys.exit(0)

    def login(self):
        dni = self.view.ask_input("Introdueix DNI de client: ")
        c = self.model.find_client(dni)

        if c is not None:
            self.client = c
            self.view.show_message(f"Benvingut, {self.client.name}")
        else:
            self.view.show_message("Login incorrecte.")


    def mostrar_productes(self):
        l = self.model.all_productes()
        self.view.show_products(l)

    def mostrar_cistella(self):
        self.view.show_products(self.cistella)

    def comprar(self):

        self.mostrar_productes()
        id = int( self.view.ask_input("Escull un id de producte: ") )
        
        p = self.model.find_producte(id)

        if p is not None:
            quantitat = int( self.view.ask_input("Escull quantitat de producte") )
            if p.stock - quantitat >= 0:
                p.stock -= quantitat
                self.cistella[p.id] = p
            else:
                self.view.show_message("Quantitat invàlida")
        else:
            self.view.show_message("Id de producte invàlid")


    def generar_factura(self):
        self.view.show_message("Generant factura...")
        
        date = datetime.datetime.now()