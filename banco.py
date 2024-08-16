# saque, depósito, extrato, transferência.
# saldo, numero da conta, nome, cpf, 

class Conta:

    def __init__(self, numeroConta, titular, cpf, saldo=0):
       self.numeroConta = numeroConta
       self.titular = titular
       self.cpf = cpf
       self.saldo = saldo

    def saque(self, valor):
        if valor <= 0:
            print('valor informado incompatível com a acao')

        elif self.saldo >= valor:
            self.saldo = self.saldo - valor
            print('saque realizado com sucesso')
        else:
            print('Saldo insuficiente')
    
    def deposito(self,conta, valor):
        if valor <= 0:
            print('Insira um valor valido para realizar o deposito')
        else:
            conta.saldo = conta.saldo + valor
            print('Valor depositado com sucesso')

    def transferencia(self, destino, valor):
        self.saque(valor)
        self.deposito(destino, valor)
        print('Tranferencia realizada com sucesso')

    def transferencia(self, destino, valor):
        destino.saldo = destino (valor)
        self.extrato.append ('Saldo atual: ' + self.saldo)
        print('Tranferencia realizada com sucesso')

    def imprimirExtrato(self):
        for item in self.extrato: 
                    print(item)


conta1 = Conta('11111', 'Renan', '05794884703', 100)
conta2 = Conta('22222', 'Denise', '111111111', 30) 


conta1.transferencia(conta2, 30)
print('Saldo depois da transferencia da Conta 1:', conta1.saldo)
print('Saldo depois da transferencia da Conta 2:', conta2.saldo)

print(conta2.titular, conta2.saldo)

conta1.deposito(conta2, 30)                   
print(conta2.titular, conta2.saldo)

conta2.saque(30)
conta1.deposito(conta2,50)
print(conta2.titular, conta2.saldo)

# def deposito(conta, valor):
# conta1.saque(int(input('Digite o valor a ser sacado: ')))
# conta 1 transfere
# conta 2 recebe
# nomes de conta e referências depois com a mesma identificação

