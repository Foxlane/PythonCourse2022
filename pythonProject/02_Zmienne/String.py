#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = 'Pepsi'
s2 = 'Cola'
s3 = s1.join(s2)
print(s3)
#Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
Tytul = input("Podaj Tytul")
Nazwisko = input("Podaj Nazwisko Autora")
Liczba_stron = input('Podaj Liczbe stron')
#Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
print(Tytul.isalpha())
print(Nazwisko.isalpha())
print(Liczba_stron.isdigit())

#Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
print(Tytul.capitalize())
print(Nazwisko.capitalize())

#Połącz dane w jeden ciąg book za pomocą spacji
book = (Tytul.capitalize(), Nazwisko.capitalize(), Liczba_stron)
print(*book)

#Policz liczbę wszystkich znaków w napisie book
print(len(Tytul))
print(len(Nazwisko))
print(len(Liczba_stron))





