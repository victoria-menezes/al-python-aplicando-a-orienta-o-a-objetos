# Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção de bases sólidas.
# Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem. Bora praticar então?
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'


# Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_praca.categoria = 'Italiana'

# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
nome = restaurante_praca.nome

# Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
ativo = 'ativo' if restaurante_praca.ativo else 'inativo'
print('O restaurante {} está {}.'.format(restaurante_praca.nome, ativo))

# Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = Restaurante.categoria

# Altere o valor do atributo nome de restaurante_praca para 'Bistrô'.
restaurante_praca.nome = 'Bistrô'

# Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
txt = 'é' if restaurante_pizza.categoria == 'Fast Food' else 'não é'
print('A categoria de {} {} Fast Food.'.format(restaurante_pizza.nome,txt))

# Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True


# Imprima no console o nome e a categoria da instância restaurante_praca.
print('Nome: {}\nCategoria: {}'.format(restaurante_praca.nome, restaurante_praca.categoria))