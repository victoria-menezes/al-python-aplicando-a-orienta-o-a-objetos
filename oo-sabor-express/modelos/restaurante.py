class Restaurante:
    # Variáveis criadas fora do __init__ são compartilhadas por todos os objetos da mesma classe
    restaurantes = []
    
    # Método construtor: sempre que criarmos uma instância, esse método será chamado
    # self = se refere à instância ativa, e não qualquer outra. Não precisa ser chamado de self, pode ser 'this' ou qualquer outra variavel. Só precisa ser o primeiro argumento.
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self) # Adicionar o objeto criado à lista restaurantes
    
    # Definir como esse objeto será exibido em texto (por exemplo, em print()s)
    def __str__(self):
        return '{} - {} | {}'.format(self.nome, self.categoria, 'Ativo' if self.ativo else 'Inativo')
    
    def listar_restaurantes():
        for r in restaurantes:
            print(r)

# Um objeto = uma instancia de uma classe
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

# para dar print nos atributos de um objeto cuja classe nao tem um __str__, se usa vars(OBJETO)
# print (vars(restaurante_praca))

Restaurante.listar_restaurantes()