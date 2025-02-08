# Desafios

# Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
# Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. 
# Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True.
# Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

class ContaBancaria:
    def __init__(self, titular = '', saldo = 0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return '{} Saldo: {}'.format(self._titular.ljust(10), self._saldo)

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return 'ativa' if self._ativo else 'inativa'

# Crie duas instâncias da classe e imprima essas instâncias.
conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)

print(conta1)
print(conta2)

# Chame o método de classe e imprima o valor de ativo.
conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta {conta3.ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta {conta3.ativo}")

# Imprima o valor da propriedade titular.
conta4 = ContaBancaria("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.titular}")


# Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
# Crie um método de classe para a conta ClienteBanco.

class ClienteBanco:
    def __init__(self, nome='', sobrenome='', idade=0, genero='', estado=''):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade
        self._genero = genero
        self._estado = estado
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def sobrenome(self):
        return self._sobrenome
    
    @property
    def idade(self):
        return self._idade
    
    @property
    def genero(self):
        return self._genero
    
    @property
    def estado(self):
        return self._estado
    
    @classmethod
    def criar_conta(cls, cliente, saldo_inicial=0):
        conta = ContaBancaria(cliente._nome,saldo_inicial)
        return conta

cliente1 = ClienteBanco('Ana','Silva',34,'F','AM')
cliente2 = ClienteBanco('João','Salgueiro',54,'H','PA')

conta5 = ClienteBanco.criar_conta(cliente1, 240)
print(conta5)