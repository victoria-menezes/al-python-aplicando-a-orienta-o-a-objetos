# Exercícios

# Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
# Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. 
# Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
# Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

# Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from livro import Livro

# Crie duas instâncias da classe Livro e imprima essas instâncias.
livro1 = Livro('Dom Casmurro','Machado de Assis', 1899)
livro2 = Livro('Macunaíma','Mário de Andrade', 1928)
Livro.listar_livros()

# No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
print('EMPRESTADO: {}'.format(livro2.titulo))
livro2.emprestar()
Livro.listar_livros()

# No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
print('Livros de 1899 disponiveis:')
print(Livro.verificar_disponibilidade(1899))

# Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
