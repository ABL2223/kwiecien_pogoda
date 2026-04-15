import matplotlib.pyplot as plt


# x = [1,2,3,4,5]
# y = [10,15,13,17,20]

# Wykres liniowy

# plt.plot(
#     x,
#     y,
#     color="red",
#     linewidth=3,
#     marker="o",
#     markersize=10,
#     linestyle="-.",
# )
# plt.title("Wykres liniowy")
# plt.xlabel("Numer dnia")
# plt.ylabel("Wartość sprzedaży")
# plt.grid(True)
# plt.show()

# Wykres słupkpowy

# produkty = ["A","B","C","D"]
# wyniki = [12,19,7,15]
#
# plt.bar(produkty, wyniki)
# plt.barh(produkty,wyniki)
# plt.xlabel("Produkt")
# plt.ylabel("Wyniki")
#
# plt.show()


# oceny = [2,2,5,5,4,3,2,5,4,3]
#
# plt.hist(oceny, bins=4)
# plt.title("Histogram ocen")
# plt.xlabel("Ocena")
# plt.ylabel("Liczba wystąpień")
#
# plt.ylim([0,100])
#
# plt.show()


# Zadanie 1 Matplotlib
# dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
# sprzedaz = [120, 150, 180, 160, 170, 210, 190]
# Stwórz wykres liniowy, który pokaże sprzedaż sklepu w kolejnych dniach tygodnia.
# Na wykresie:
# dodaj tytuł
# opisz oś X i Y
# dodaj markery w punktach

# dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
# sprzedaz = [120, 150, 180, 160, 170, 210, 190]
# plt.plot(
#     dni,
#     sprzedaz,
#     color="red",
#     linewidth=3,
#     marker="o",
#     markersize=10,
# )
# plt.title("Dzienna sprzedaż")
# plt.xlabel("Numer dnia")
# plt.ylabel("Wartość sprzedaży")
# plt.grid(True)
# plt.show()

# Zadanie 2 Matplotlib
# produkty = ["Laptop", "Tablet", "Telefon", "Monitor"]
# sprzedaz = [25, 18, 40, 12]
# Stwórz wykres słupkowy, który pokaże sprzedaż czterech produktów.
# Na wykresie:
# dodaj tytuł
# opisz osie

# produkty = ["Laptop", "Tablet", "Telefon", "Monitor"]
# sprzedaz = [25, 18, 40, 12]
# plt.bar(produkty, sprzedaz)
# plt.xlabel("Produkty")
# plt.ylabel("Sprzedaż")
# plt.show()


# Zadanie 3 Matplotlib
# wyniki = [45, 50, 52, 48, 60, 70, 65, 55, 58, 62, 75, 80, 78, 85, 90]
# Oto wyniki testu studentów.
# Stwórz histogram, który pokaże rozkład wyników.

wyniki = [45, 50, 52, 48, 60, 70, 65, 55, 58, 62, 75, 80, 78, 85, 90]
plt.hist(wyniki)
plt.xlabel('Wyniki testu')
plt.ylabel('Liczba studentów')
plt.title('Wyniki testu studentów')
plt.show()