# Stock Prediction

Projekt ma na celu badanie akcji firm, a także przewidywaniu ich wartości

## Base information - Graphs
Ten ekran umożliwia sprawdzenie takich danych o firmie jak:
- Wolumen obrotów
- Średnia ruchoma na przestrzenii 10, 20 oraz 50 dni
- Skorygowana Cena Zamknięcia
- Dzienny zwrot

Użytkownik wybiera rodzaj grafu za pomocą środkowego suwaka a następnie wybiera firme.
Może to zrobić poprzez suwak z listą firm lub wpisać jej skrót zgodnie z skrótami na Yahoo Finance.
Bo wyborze firmy oraz grafu wciskamy 'search'

## Base information - Table
Ta sekcja umożliwia uzyskanie danych odnośnie firmy w postaci tabelarycznej. 
Wybieramy firme poprzez suwak lub wpisujemy jej skrót.
Po wyborze wciskamy 'search'

## Prediction

Ta zakładka umożłiwia nam przewidzenie cen akcji firmy określoną liczbą dni do przodu
metodą monte carlo. Więcej informacji na temat metody Monte Carlo pod tym linkiem [link](http://www.investopedia.com/articles/07/montecarlo.asp). 
W skrócie: w tej metodzie przeprowadzamy symulacje, aby przewidzieć przyszłość wiele razy, a na końcu sumujemy wyniki, aby uzyskać jakąś wymierną wartość.
Wybieramy firme poprzez suwak lub skrót, a następnie określamy liczbę dni.

## Value at risk
Ta zakładka przewiduje końcowe wartości giełdy danej firmy w postaci histogramu. 
Wykres zaznacza również najniższą wartość rynkową jaką firma może osiągnąć.
Mniejsze wartości uznaje się za outliery

## Correlation
Zakładka odpowiedzialna za określanie za pomocą wykresów korelacji pomiedzy firmami.
Tworzona jest macierz wykresów, gdzie po głównej przekątnej pokazywane są histogramy
(Na przecięciu tym bowiem porównuje się te zamą firmę)

## Value at Risk
W tej części możemy zobaczyć jaką wartość narażamy na ryzyko inwestując w daną akcję.
Podstawowym sposobem ilościowego określenia ryzyka jest porównanie oczekiwanego zwrotu 
(który może być średnią dziennych zwrotów z akcji) z 
odchyleniem standardowym dziennych zwrotów.
