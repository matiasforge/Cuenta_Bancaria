class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(tasa_interes=0.02, balance=0)

    def hacer_depósito(self, amount):
        self.cuenta.depósito(amount)

    def hacer_retiro(self, amount):
        self.cuenta.retiro(amount)

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Email: {self.email}")
        self.cuenta.mostrar_info_cuenta()

class CuentaBancaria:
    def __init__(self, tasa_interes=0.02, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance
    def depósito(self, amount):
        self.balance += amount
    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance:.2f}")

usuario1 = Usuario("michaelJ", "michaelj@gamil.com")
usuario2 = Usuario("Martha Gomez", "marthaG@dojo.com")

usuario1.hacer_depósito(1000)
usuario2.hacer_depósito(500)
usuario1.hacer_retiro(200)
usuario2.hacer_retiro(100)

usuario1.mostrar_balance_usuario()
usuario2.mostrar_balance_usuario()
