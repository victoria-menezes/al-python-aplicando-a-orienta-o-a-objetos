# Exercícios

# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro():
    def __init__(self, modelo = '', cor='',ano=0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

honda = Carro('Honda','Branco',1999)
print(vars(honda))
print()

# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria.
# Exiba essa mensagem para uma instância de restaurante.

class Restaurante():
    def __init__(self, nome, categoria,estado,tamanho):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.estado = estado
        self.tamanho = tamanho
    def __str__(self):
        return '{} é um restaurante de comida {}.'.format(self.nome,self.categoria)

empanadas = Restaurante('Empanadas', 'Espanhola', 'RJ', 'Médio')
print(empanadas)

# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 4 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente():
    def __init__(self, nome, sobrenome, idade, estado):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.estado = estado

ana = Cliente('Ana', 'Salgueiro',52, 'BA')
joao = Cliente('João', 'Tanaka', 73, 'RJ')
pedro = Cliente('Pedro','Silva', 34, 'RO')
leticia = Cliente('Leticia','Torres',43,'ES')