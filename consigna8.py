# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en
# tanto por ciento. Crear los siguientes métodos para la clase:
# - Un constructor.
# - Los setters y getters para el nuevo atributo.
# - En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
# mayor de edad pero menor de 25 años y falso en caso contrario.
# - Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# - El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

from consigna7 import Cuenta
import datetime
from datetime import date

#Se crea una clase llamada Cuenta Joven agregando el atributo bonificación
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

#El titular de la cuenta debe ser mayor de edad
    def es_titular_valido(self):
        # Suponemos que la fecha de nacimiento del titular se encuentra en el atributo fecha_nacimiento
        edad = (datetime.date.today() - self.get_titular().fecha_nacimiento).days // 365
        return edad > 18 and edad < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
    
    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificación: ", self.__bonificacion)

cuenta_joven = CuentaJoven("Jack", 512000, 5)
cuenta_joven.mostrar()