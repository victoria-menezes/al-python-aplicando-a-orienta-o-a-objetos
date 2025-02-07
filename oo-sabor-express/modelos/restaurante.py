class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

# Um objeto = uma instancia de uma classe
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

# para dar print nos atributos de um objeto, se usa vars(OBJETO)
print (vars(restaurantes))