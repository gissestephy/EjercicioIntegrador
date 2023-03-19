# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
# - Un constructor, donde los datos pueden estar vacíos.
# - Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
# - mostrar(): Muestra los datos de la cuenta.
# - ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
# - retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos


class Persona:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor
        
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, valor):
        self.__apellido = valor 

    @property
    def nombre_completo(self):
        return f"El titular de la cuenta es {self.__nombre} {self.__apellido}"

#Se crea una clase llamada Cuenta con 2 atributos titular y cantidad
class Cuenta():
    def __init__(self,titular, cantidad):
        self.titular= titular
        self.__cantidad= 0
    
    def get_titular(self):
        return self.titular
    
    def set_titular(self):
        return self.titular
    
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def get_cantidad(self):
        return self.__cantidad
 
#Se muestran los datos de la cuenta   
    def mostrar(self):
        print("Titular: ", self.titular)
        print("Cantidad: ", self.__cantidad)
    
#Se realizan dos operaciones cuando Ingresa dinero y cuando Retira dinero
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        self.__cantidad -= cantidad

print("Bienvenido a la cuenta BBVA!")   
cuenta_kaz = Cuenta("Kaz", 55900.5)  
person=Persona("Kaz", "Brekker")      
print(person.nombre_completo)

# Mostrar los datos de la cuenta
cuenta_kaz.mostrar()

# Ingresar 500 a la cuenta
cuenta_kaz.ingresar(55900.5)
cuenta_kaz.mostrar()

# Retirar 1200 de la cuenta
cuenta_kaz.retirar(1200.0)
cuenta_kaz.mostrar()