import os

class Client:

    def __init__(self, dni, name, surname, address):
        self.dni = dni
        self.name = name
        self.surname = surname
        self.address = address

    def __str__(self):
        return f"{self.dni} - {self.name} {self.surname} - {self.address}"
    
    @classmethod
    def from_csv(cls, string):
        l = string.split(";")
        return cls(l[0],l[1],l[2],l[3])
    
    def to_csv(self):
        return f"{self.dni};{self.name};{self.surname};{self.address};\n"



class Producte:

    def __init__(self, id, desc, pvp, stock):
        self.id = id
        self.desc = desc
        self.pvp = pvp
        self.stock = stock

    def total(self):
        return self.pvp * self.stock

    def __str__(self):
        return f"{self.id} - {self.desc} - {self.pvp}€ - {self.stock}"
    
    @classmethod
    def from_csv(cls, string):
        l = string.split(";")
        return cls(l[0],l[1],float(l[2]),int(l[3]))
    
    def to_csv(self):
        return f"{self.id};{self.desc};{self.pvp};{self.stock};\n"


class Factura:

    def __init__(self, client_dni, date, products):
        self.client_dni = client_dni
        self.date = date
        self.products = products


class ModelBotiga:

    def __init__(self):
        self.client_file = "data/client.txt"
        self.product_file = "data/producte.txt"
        self.clients = {}
        self.productes = {}
        self.read()

    def add_producte(self, p: Producte):
        if self.find_producte(p.id) is None:
            self.productes[p.id] = p
            return 1
        else:
            return 0
        
    def update_producte(self, p: Producte):
        if self.find_producte(p.id) is None:
            self.productes[p.id] = p
            return 1
        else:
            return 0

    def find_producte(self, id):
        for k, v in self.productes.items():
            if k == id:
                return v
        return None
    
    def find_producte_by_name(self, name: str):
        l = list()
        for k, v in self.productes.items():
            try:
                if k.index(name) > 0:
                    l.append(v)
            except ValueError:
                pass
        return l

    def all_productes(self):
        if self.productes:
            return list(self.productes.values())
        else:
            return None
        
    def add_client(self, c: Client):
        if self.find_client(c.dni) is None:
            self.clients[c.dni] = c
            return 1
        else:
            return 0

    def find_client(self, dni: str):
        for k, v in self.clients.items():
            if k == dni:
                return v
        return None

    def write(self):
        """
        Guarda la llista de dades a un arxiu en disc.
        """
        with open(self.product_file, "w") as f:
            for v in self.productes.values():
                f.write(v.to_csv())

        with open(self.client_file, "w") as f:
            for v in self.clients.values():
                f.write(v.to_csv())

    def read(self):
        """
        Llegeix dades d'un arxiu en disc.

        Si no s'han pogit llegir dades, crea una llista buida.
        Si l'arxiu no existeix, crea un de nou.
        """
        try:
            f = open(self.product_file)
            data = f.readlines()

            for l in data:
                p = Producte.from_csv(l)
                self.productes[p.id] = p
            print(self.productes)
        except FileNotFoundError:
            self.productes = {}
            f = open(self.product_file, "x")
            f.close()


        try:
            f = open(self.client_file)
            data = f.readlines()
            for l in data:
                p = Client.from_csv(l)
                self.clients[p.dni] = p
        except FileNotFoundError:
            self.clients = {}
            f = open(self.client_file, "x")
            f.close()