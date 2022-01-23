#Stock Prediction
Projekt ma na celu na badaniu działań firmy na giełdzie oraz na przewidywaniu wartości ich akcji

## Base information - Graphs
Ten ekran umożliwia sprawdzenie takich danych o firmie jak:
- Wolumen obrotów
- Średnia ruchoma na przestrzenii 10, 20 oraz 50 dni
- Skorygowana Cena Zamknięcia
- Dzienny zwrot

Użytkownik wybiera rodzaj grafu za pomocą środkowego suwaka a następnie wybiera firme.
Może to zrobić poprzez suwak zlistą firm lub wpisać jej skrót zgodnie z skrótami na Yahoo Finance.
Bo wyborze firmy oraz grafu wciskamy 'search'

## Base information - Table
Ta sekcja umożliwia uzyskanie danych odnośnie firmy w postaci tabelarycznej. 
Wybieramy firme poprzez suwak lub wpisujemy jej skrót.
Po wyborze wciskamy 'search'

## Prediction
Ta zakładka umożłiwia nam przewidzenie cen akcji firmy określoną liczbą dni do przodu
metodą monte carlo.
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
W tej części możemy jaką wartość narażamy na ryzyko inwestując w daną akcję