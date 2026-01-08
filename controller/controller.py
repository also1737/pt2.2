import sys, datetime
from view.view import ViewBotiga
from model.model import ModelBotiga, Producte

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
        while True:
            op = self.view.ask_input("Estàs segur? (s/n): ")
            match op:
                case "s" | "S":
                    self.view.show_message("Sortint del programa...")
                    self.model.write()
                    sys.exit(0)
                case "n" | "N":
                    break
                case _:
                    self.view.show_message("Opció incorrecta")

    def login(self):
        if self.client is None:
            dni = self.view.ask_input("Introdueix DNI de client: ")
            c = self.model.find_client(dni)

            if c is not None:
                self.client = c
                self.view.show_message(f"Benvingut, {self.client.name}")
            else:
                self.view.show_message("Login incorrecte.")
        else:
            self.view.show_message(f"Sessió ja iniciada com a {self.client.name}")


    def mostrar_productes(self):
        l = self.model.all_productes()
        if l:
            self.view.show_products(l)
            return True
        else:
            self.view.show_message("No hi han productes disponibles")
            return False


    def mostrar_cistella(self):
        if self.client:
            if self.cistella:
                self.view.show_products(list(self.cistella.values()))
            else:
                self.view.show_message("Cistella buida")
        else:
            self.view.show_message("No hi ha client enregistrat")
            self.login()


    def comprar(self):
        if self.client is not None:
            if self.mostrar_productes():
                id = self.view.ask_input("Escull un id de producte: ")

                p = self.model.find_producte(id)

                if p is not None:
                    quantitat = int( self.view.ask_input("Escull quantitat de producte: ") )
                    if p.stock - quantitat >= 0:
                        p.stock -= quantitat
                        p2 = Producte(p.id, p.desc,p.pvp, quantitat)
                        self.cistella[p2.id] = p2
                    else:
                        self.view.show_message("Quantitat invàlida")
                else:
                    self.view.show_message("Id de producte invàlid")
        else:
            self.view.show_message("No hi ha client enregistrat")
            self.login()


    def generar_factura(self):
        self.view.show_message("Generant factura...")
        
        date = datetime.datetime.now()