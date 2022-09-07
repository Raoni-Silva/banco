## ----- CLIENTE ----- ##

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def dados(self):
        return self.nome, self.idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None
        
    def inserir_conta(self, conta):
        self.conta = conta
            
            


## ----- CONTA ----- ##

class Conta(Cliente):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    def InfosConta(self):
        print(f'O saldo da conta {self.conta} é de R${self.saldo}.')

## ----- TESTE ----- ##

conta1 = Conta(1111, 2222, 120)
#conta1.InfosConta()
vini = Cliente('Vinicius', 36)
vini.inserir_conta(conta1)

## ----- TESTE GIT ----- ##
