# Sistema de Cuenta Bancaria usando POO

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular} - Saldo: ${self.saldo}")


# Uso de la clase
cuenta = CuentaBancaria("Teresa", 100)
cuenta.depositar(50)
cuenta.retirar(30)
cuenta.mostrar_saldo()