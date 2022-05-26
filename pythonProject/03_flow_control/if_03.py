#Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce.
#W zależności od wyniku dodaj komunikaty.
#Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

print('Podaj 3 opinie na temat tej ksiazki')
Opinia1 = int(input('Podaj 1 opinie'))
Opinia2 = int(input('Podaj 2 opinie'))
Opinia3 = int(input('Podaj 3 opinie'))
result = (Opinia1 + Opinia2 + Opinia3) / 3

if result > 7:
   print('Bardzo Dobry')
if 5 <= result <= 7:
   print('przecietna')
if result < 5:
   print ('nie warta uwagi')




