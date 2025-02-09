# Exercícios

# Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
# Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. 
# Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
# Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
class Livro:
    livros = []

    def __init__(self, titulo='', autor='', ano_publicacao=0):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)
    
    def __str__(self):
        return '{} {} | {}'.format((self._titulo + ' ('+str(self._ano_publicacao)+')').ljust(25), self._autor.ljust(25), self.disponivel)
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def ano_publicacao(self):
        return self._ano_publicacao
        
    @property
    def disponivel(self):
        return 'Disponivel' if self._disponivel else 'Indisponível'
    
    @classmethod
    def listar_livros(cls):
        print('{} {} | {}'.format(('LIVRO' + ' (ANO)').ljust(25), 'AUTOR'.ljust(25), 'DISPONIBILIDADE'))
        for l in cls.livros:
            print(l)
        print('\n\n')
    
    @staticmethod
    def verificar_disponibilidade(ano):
        disponiveis = []
        for l in Livro.livros:
            if l.ano_publicacao == ano and l._disponivel:
                disponiveis.append(l.__str__())
        return disponiveis

    def emprestar(self):
        self._disponivel = False

# Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
# No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
# No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
# Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
