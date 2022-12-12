class Main:
    pass

from Cliente import Cliente
c1 = Cliente("Rafael", "11912345678")
print(f"O nome do cliente eh: {c1.nome} e o telefone eh {c1.telefone}")

from Conta import Conta
c1 = Conta("Rafael", "12345", "R$100,00")
print(f"Titular: {c1.titular}\nNumero da conta: {c1.numero}\nSaldo disponivel: {c1.saldo}")