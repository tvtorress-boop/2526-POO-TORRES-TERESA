# Programa que aplica Programación Orientada a Objetos (POO)
# Ejemplo: Sistema simple de cuentas bancarias

class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado (encapsulación)

    def get_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto

    def mostrar_info(self):
        return f"Titular: {self.titular} | Saldo: ${self.__saldo}"


class CuentaAhorro(Cuenta):  # Herencia
    def __init__(self, titular, saldo, interes):
        super().__init__(titular, saldo)
        self.interes = interes

    # Polimorfismo: se redefine el método
    def mostrar_info(self):
        return f"Cuenta de Ahorro | Titular: {self.titular} | Saldo: ${self.get_saldo()} | Interés: {self.interes}%"


# Creación de objetos
cuenta1 = Cuenta("María", 500)
ahorro1 = CuentaAhorro("Luis", 1000, 5)

# Uso de métodos
cuenta1.depositar(200)
ahorro1.retirar(100)

print(cuenta1.mostrar_info())
print(ahorro1.mostrar_info())
