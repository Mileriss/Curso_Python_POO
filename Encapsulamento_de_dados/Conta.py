class Conta:
    def __init__(self, titular, saldo, numero):
        self.titular = titular
        self.saldo = 0
        self.numero = numero

# Método GET e SET
        def get_saldo(self):
            return self._saldo

        def set_saldo(self, saldo):
            if (saldo < 0):
                print("O saldo não pode ser negativo!")
            else:
                self._saldo = saldo
                
# Método @Property
        @property
        def saldo(self):
            return self._saldo

        @saldo.setter
        def saldo(self, saldo):
            if (saldo < 0):
                print("O saldo não pode ser negativo!")
            else:
                self._saldo = saldo
        