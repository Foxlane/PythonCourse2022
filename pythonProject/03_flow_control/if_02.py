#Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
#Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.
number1 = int(input('Podaj pierwsza liczbe calkowita'))
number2 = int(input('Podaj druga liczbe calkowita'))
result = number1 + number2
if result > 100:
   print(result)
else: print('Koniec')