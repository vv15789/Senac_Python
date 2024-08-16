# saque, depósito, extrato, transferência.
# conta: saldo, numero da conta, nome do usuario, cpf

class Conta:

    def __init__(self, numeroConta, usuario, cpf, saldo=0): 
        self.saldo = saldo
        self.numeroConta = numeroConta
        self.titular = usuario
        self.cpf = cpf
        self.extrato = []

    def saque(self, valor):
        if valor <= 0:
            print('Valor informado incompativel com a acao') 
        elif self.saldo >= valor:
            self.saldo = self.saldo - valor
            self.extrato.append('Saque de R$ ' + str(valor) +
                                ' realizado com sucesso.\n'+
                                'Saldo atual: ' + str(self.saldo)+'\n')
        else:
            print('Saldo insuficiente')

    def deposito(self,conta, valor):
        if valor <= 0:
            print('Insira um valor valido para realizar o deposito')
        else:
            conta.saldo = conta.saldo + valor
            self.extrato.append('Deposito de R$ ' + str(valor) +
                                ' realizado com sucesso.\n'+
                                'Saldo atual: ' + str(self.saldo)+'\n')
            
    def transferencia(self, destino, valor):
        self.extrato.append('Iniciando transferencia de valor R$ ' 
                            + str(valor) + ' para a conta ' +
                            destino.numeroConta + '.\n')
        self.saque(valor)
        destino.saldo = destino.saldo + valor
        self.extrato.append('Saldo atual: ' + str(self.saldo) + 
                            '. Transferencia realizada com sucesso.\n')

    def imprimirExtrato(self):
        for item in self.extrato:
            print(item)


conta1 = Conta('11111', 'Renan', '05794884703', 100)
conta2 = Conta('22222', 'Denise', '1111111111', 30)
conta1.saque(30)
conta1.deposito(conta1,50)
conta1.transferencia(conta2,20)
conta1.imprimirExtrato() 


# conta1
# conta1.transferencia(conta2, 30)
# print('Saldo depois da transferencia da Conta 1:', conta1.saldo)
# print('Saldo depois da transferencia da Conta 2:', conta2.saldo)

# conta1.saque(30)
# # conta1.saque(int(input('Digite o valor a ser sacado: '))
# print(conta1.titular, conta1.saldo)
