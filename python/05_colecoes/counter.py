from collections import Counter

my_list = [1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 5, 6, 7]

result = Counter(my_list)

print(result)
print(type(result))

# Contando quanto cada palavra se repete em um texto
texto = """
Styracosaurus (em português Estiracossauro, que significa "lagarto espinhoso" do grego styrax/στύραξ, que significa "espinho na ponta de uma haste de lança" e sauros/σαῦρος, que quer dizer "lagarto") foi um gênero de dinossauro herbívoro e quadrúpede que viveu durante o período Cretáceo, no andar Campaniano entre 75,5 e 75 milhões de anos atrás. Ele tinha de quatro a seis pontas parietais longas que se estendiam do folho do pescoço, um chifre jugal menor em cada uma das bochechas e um único chifre projetando-se do nariz, que podia ter até 60 centímetros de comprimento e 15 centímetros de largura. A função ou funções dos chifres e babados têm sido debatidas há muitos anos.

Styracosaurus era um dinossauro relativamente grande, atingindo comprimentos de 5 a 5,5 metros e pesando cerca de 1,8 a 2,7 toneladas. Tinha cerca de 1,8 metro de altura. Possuía quatro pernas curtas e um corpo volumoso. Sua cauda era bastante curta. O crânio tinha bico e dentes cortantes dispostos em baterias dentárias contínuas, sugerindo que o animal cortava plantas. Tal como outros ceratopsianos, este dinossauro pode ter sido um animal de rebanho, viajando em grandes grupos, como sugerido pelas camadas ósseas.
"""

texto_split = texto.split()
repeticoes = Counter(texto_split)

print(repeticoes.most_common(5))

c1 = Counter(a=3, b=2, c=1)
c2 = Counter(a=4, b=3, c=2)
c3 = Counter(d=1, e=1, f=1)

print(c1 + c2)
print(c1 + c3)
print(c1 - c3)
print(c1 & c3)
print(c1 | c3)


