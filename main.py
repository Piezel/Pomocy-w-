#Funkcje tekstowe
def  funkcjeTekstowe():
    teksta = "Teskt, tekst2"
    tekstb = teksta.split(",")
    print(tekstb)
    print(teksta.replace("tekst2","bimbimbambam"))
funkcjeTekstowe();

#Listy
def listy():
    lista = ["bim","bim","bam","bam"]
    print(lista[1],lista[-1],lista[:1],lista[1:3]) #Index 1, Index ostatni, Index w zbiorze (1, +inf), Indeks w zbiorze (1,3>
    #W przypadku : , 1 element jest exlusive, 2 jest inclusive
    print(len(lista)) #Długość listy
    lista.append('bim') #Dodawanie do listy
    lista.insert(1,'bim') #list.insert(index,element)
    lista.pop() #Usuwa index podany w nawiasach + zwraca usunięty element
    lista.remove("bam") #Usuwa 1 wystąpienie podanego elementu
    print(lista)
    lista.clear() #Czyści liste

    #Szukanie w listach
    suka = ["bim","bim","bam","bam"]
    if "bim" in suka: #Tylko True i False
        print("bimbimbambam")
    print(suka.index("bam")) #Index 1 wystąpienia + Można dodać zakres: list.index(element,początek,koniec)
    print(suka.count("bam")) #Liczy wystąpienia
    max(suka) #max
    min(suka) #min
    suka.sort() #Sortuje, przyjuje parametr reverse
    suka.reverse() #Odwraca kolejność
    blyat = ["bam","bim","bim"]
    sukablyat= suka + blyat #Listy są upośledzone
    print(sukablyat)
    seks = sukablyat.copy() #Kopiowanie bo inaczej będzie referencja jak zrobisz seks = sukablyat
    krotka = ("owo","uwu",">w<") #Niemodyfikowalne tablice, krotki
listy()

#Słowniki
def slowniki():
    #Podstawy
    pierog = {
        'Mięsne': "Z mięsem",
        "Grzybne": "Z grzybami"
    }
    print(pierog["Mięsne"])
    print(pierog.keys()) #Klucze W FORMIE LISTY
    print(pierog.values()) #Wartości W FORMIE LISTY
slowniki()

#Sety
def sety():
    #podstawy
    setowanie = {2,3,73,126,1,5,2}
    print(setowanie) #Sortuje je automatycznie + Nie przyjmuje duplikatów
    setowanie.add(200) #Dodawanie do setu A i btw można dodawać listy itd. przy pomocy update
    setowanie.remove(1) #Usuwanie elementu
    setowanie.pop() #Usuwa tylko ostatni
    niesetowanie = frozenset(setowanie) #Frozenset czyli niemodyfikowalny set
sety()

#ZAPAMIĘTAJ DEBILU PYTHON JEST UPOŚLEDZONY I MA ELIF A NIE ELSE IF

for i in range(1,10): #Zwykła pętla for niczym w innych ucywilizowanych językach, 10 jest exclusive, można też dodać 3 parametr w range jeśli chcesz realną pętlę for
    print(f"i: {i}")

#Funkcje
def funkcje():
    def przyklad(a=20,b=''): #Paramentr domyślny + parametr opcjonalny
        print(a,b)
    przyklad()
    #Rest tutaj to jest * dla tuple i ** dla set
funkcje()

#Konwersje
def konwersje():
    a = 20.214
    print(int(a)) #na int
    print(float(a)) #na float
    print(str(a)) #na string
    b = ("bim","bim","bam","bam")
    c = ["bim","bim","bam","bam"]
    print(tuple(c)) #zamiana list na tuple
    print(list(b)) #zamiana tuple na list
    #dosłownie to samo z set i frozenset 
    #tak samo można na dict() zamienić tuple lub list 2 wymiarową
    #cokolwiek na boola to true, nic to false
    print(bool(None))
    print(bool(2))
    #przy okazji id czyli miejsce w pamięci
    print(id(a))
konwersje()

#CZAS NA BIBLIOTEKI

#math
import math
#pozwala nam na 2 zmienne pi i e (tak na serio jest jeszcze inf itd.) i operacja matematyczne
def matematyka():
    print(math.cos(45)) #cos z 45 stopni wow
    print(math.pi) #wow pi
    print(math.sqrt(16)) #wow pierwiastek kwadratowy (Ale ta biblioteka nudna >w<) (Trace psychikę pomocy)
matematyka()

#random
import random
def losowanie():
    print(random.random()) #Losowa liczba od 0 do 1
    print(random.randrange(1,10)) #od 1 do 10
    print(random.choice([2,6,12,"ala ma kota"])) #losowy wybór działa też z literami ze stringa
    pythonistrash = ["blyat","suka","bimbimbambam"]
    random.shuffle(pythonistrash)
    print(pythonistrash) #wow shuffle
losowanie()

#Funkcje tekstowe v2
def funkcjetekstowev2():
    print(">w<".center(50,"_")) #centruje tekst podanymi w 2 parametrze znakiem
    print("UwU".startswith("U")) #zwraca bool z wynikiem czy zaczyna się, istnieje też endswith
    print("Jestem chory psychicznie >w<".find(">w<")) #Szuka czy występuje, jeśli tak to podaje ile znaków od lewej, jeśli nie to -1. Istnieje też rfind czyli od prawej
funkcjetekstowev2()

#czas, spanie i który dziś jest :3
import time
import datetime

def czas():
    #Time

    print(time.time()) #Ile sekund mineło od 1 styczna 1970 (Po co to komu >-<)
    print(time.localtime()) #Akurat struktura zawierająca poprawną datę: tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec,tm_wday,tm_yday,tm_isdst >w<
    print(time.localtime().tm_wday) #Wyciąga ze struktury dzień tygodnia
    print(time.asctime(time.localtime())) #Ładnie nam czas formatuje
    print(time.strftime("%d >w< %m >w< %Y", time.localtime())) #Formatuje nam czas tak jak chcemy: %Y, %m, %d, %H, %M, %S
    time.sleep(2) #Ile czasu przespać
    start=time.perf_counter() #Zapisuje czas
    time.sleep(1)
    stop=time.perf_counter() #Zapisuje czas
    print(stop-start)

    #Czas na datetime
    print(datetime.datetime.now()) #Pełna data + godzina
    print(datetime.datetime.now().date()) #Tylko Data
    print(datetime.datetime.now().time()) #Tylko godzina
    print(datetime.datetime.now().weekday()) #Tylko dzień tygodnia
    Czas = datetime.datetime(1212,12,12,12,12) #Ustawiamy czas na 1212 rok 12 miesiąc 12 dzień 12 godzina 12 minuta uwu
    print(Czas.date()) #I wyświetlamy datę >w<

    #Porównywanie dat
    if datetime.datetime.now().date() > Czas.date(): 
        print("Dawno mineło uwu")
    else:
        print("Jeszcze czekamy owo")
czas()

#Straciłem już wszystkie kurwa komórki mózgowe >-<

class console:
    def log(input):
        print(input)
        
console.log("UwU")
console.log("Nie ten język >w<")
console.log("Pojebało mnie do reszty")