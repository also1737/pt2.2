class ViewBotiga:

    def __init__(self):
        self.title = "App Botiga"

    def show_menu(self):
        print(f"=========[{self.title}]=========")
        print("1 - Iniciar Sessió")
        print("2 - Mostrar producte")
        print("3 - Mostrar cistella")
        print("4 - Comprar producte")
        print("5 - Generar factura")
        print("0 - Sortir")

    def get_option(self):
        opt = -1
        try:
            opt = int(input("Selecciona una opció: "))
            if opt < 0 or opt > 5:
                opt = -1
        except ValueError:
            opt = -1

        return opt
    
    def show_message(self, message):
        print(message)

    def ask_input(self, message):
        inp = input(message)
        return inp
    
    def show_products(self, data):
        print("ID - Nom - Preu/Unitat - Quantitat en stock")
        for producte in data:
            print(producte.__str__())