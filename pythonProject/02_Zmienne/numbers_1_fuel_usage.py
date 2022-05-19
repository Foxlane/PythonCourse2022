#Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny. Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
price = 5.04
usage = 6.4
distance = 120

cost = price * usage * distance / 100

print('Koszt podrozy to', round(cost,2), 'PLN')

#Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.
price_1 = input('Price')
usage_1 = input('Usage')
distance_1 = input('Distance')

a = int(price_1)
b = int(usage_1)
c = int(distance_1)

cost_1 = a * b * c / 100

print('Koszt podrozy to', round(cost_1,2), 'PLN')
