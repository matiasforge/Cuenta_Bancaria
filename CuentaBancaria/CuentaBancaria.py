class CuentaBancaria:
    cuentas_activas = []
    def __init__(self, tasa_interes=0.01, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas_activas.append(self)
    def depósito(self, amount):
        self.balance += amount
        return self
    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self
    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")
        return self
    def generar_interés(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes
        return self

    @classmethod
    def mostrar_todas_las_cuentas(cls):
        for cuenta in cls.cuentas_activas:
            cuenta.mostrar_info_cuenta()

cuenta1 = CuentaBancaria(tasa_interes=0.03, balance=1000)
cuenta2 = CuentaBancaria(tasa_interes=0.02, balance=500)

cuenta1.depósito(100).depósito(200).depósito(300).retiro(50).generar_interés()
cuenta2.depósito(200).depósito(300).retiro(100).retiro(50).retiro(50).retiro(100).generar_interés()

CuentaBancaria.mostrar_todas_las_cuentas()
