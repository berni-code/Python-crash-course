class Car():

    """Un simple intento para representar un carro electrico."""

    def __init__(self,hacer,modelo,year):
        self.hacer = hacer
        self.modelo = modelo
        self.year = year
        self.medida_odometro = 0 
    
    def dar_nombre_descriptivo(self):
        nombre_largo = str(self.year) + ' ' + self.hacer + ' ' + self.modelo
        return nombre_largo.title()
    
    def lee_odometro(self):
        print("Este carro tiene "  + str (self.medida_odometro) + " km en el.")

    def actualiza_odometro(self, kilometraje):
        if kilometraje >= self.medida_odometro:
            self.medida_odometro = kilometraje
        else:
            print("No puedes regresar el odometro!")
        
    def incremento_odometro (self, kilometros):
        self.medida_odometro += kilometros

class Bateria():
    """Un simple intento de modelar una bateria para un carro electrico"""
    def __init__(self, tamaño_bateria=70):
        "Inicia los atributos de la bateria."
        self.tamaño_bateria = tamaño_bateria

    def describe_bateria(self):
        """Imprime una declaracion describieno el tamaño de la bateria"""
        print("Este carro tiene " + str(self.tamaño_bateria) + "-KWh")

    def dar_rango(self):
        """Imprime una declaracion acerca del rango de la bateria"""
        if self.tamaño_bateria == 70:
            range = 240
        elif self.tamaño_bateria == 85:
             range = 270

        mensaje = "Este carro puede ir aproximadamente " + str(range)
        mensaje += " km en una carga completa."
        print(mensaje)  

class ElectricCar(Car):
    """Representa aspectos de un carro, especifico a los vehiculos electricos."""

    def __init__(self, hacer, modelo, year):
        """Inicia atributos de la clase padre.
        Luego inicia atributos especificos a un carro electrico."""
        super().__init__(hacer, modelo, year)
        self.bateria = Bateria()
    
mi_tesla = ElectricCar('tesla', 'modelo', 2016)
print(mi_tesla.dar_nombre_descriptivo())
mi_tesla.bateria.describe_bateria()
mi_tesla.bateria.dar_rango()
