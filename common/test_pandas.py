import pandas as pd
import openpyxl

# # Series
#
# numbers = [10, 20, 30, 40]
# ids = ["a", "b", "c", "d"]
#
# # s = pd.Series(numbers)
# s = pd.Series(numbers, index=ids)
#
# # DataFrame
#
# # data = [
# #     {
# #         "miasto":"Warszawa",
# #         "temperatura": 20
# #     },
# #     {
# #         "miasto":"Kraków",
# #         "temperatura":18
# #     }
# # ]
#
# data = {
#     "miasto": ["Warszawa","Kraków","Gdańsk"],
#     "temperatura": [20, 18, 17]
# }
#
# df = pd.DataFrame(data)
#
# print(df)
#
# # loc,
#
# a = df.loc[0]
# b = df.loc[0, "miasto"]
# c = df.loc[ df["temperatura"] >= 18 ]
#
# #  iloc
#
# d = df.iloc[0]
# e = df.iloc[0,0]
# f = df.iloc[0:3]
# # print(f)
#
# # g = df.head(1)
# #
# # print(g)
#
# h = df[["miasto","temperatura"]]
#
# # Tworzenie nowej kolumny
# df["temp_f"] = df["temperatura"] * 1.8 + 32
#
# # Usuwanie kolumny
# # test = df.drop("temp_f", axis=1)
# # print(test)
#
# df.to_csv("test.csv", index=False)
# df.to_json("test.json")
#
# df.to_excel("test.xlsx", index=False)
#
# df.to_html("test.html")







# import requests
# import pandas as pd
#
# def wszystkie_kraje():
#     url = "https://restcountries.com/v3.1/all?fields=name,flags,population,subregion,independent"
#     odpowiedz = requests.get(url)
#     dane = odpowiedz.json()
#
#     kraje = []
#     for x in dane:
#         nowy = {
#             "nazwa": x.get("name").get("common"),
#             "oficjalna_nazwa": x.get("name").get("official"),
#             "flaga": x.get("flags").get("png"),
#             "populacja": x.get("population"),
#             "niepodleglosc": x.get("independent"),
#             "region": x.get("subregion"),
#
#         }
#         kraje.append(nowy)
#
#     return kraje
#
#
# result = wszystkie_kraje()
#
# df = pd.DataFrame(result)
# df.to_excel("kraje.xlsx", index=False)



df = pd.read_excel("kraje.xlsx")

a = df.head(3)
b = df.tail(3)

# df.info()

c = df.describe()

d = list(df.columns)

# pd.set_option("display.max_columns", None)
# pd.set_option('display.max_rows', None)
# SORTOWANIE
# e = df.sort_values("populacja", ascending=False)
# print(e[["nazwa","populacja"]])
f = df.sort_values("nazwa")
# print(f)

# FILTROWANIE
g = df[ df["populacja"] > 500_000_000 ]
h = df[ df["region"] == "Eastern Asia" ]
i = df[ (df["region"] == "Eastern Asia") & (df["populacja"] > 100_000_000) ]
j = df[ (df["region"] == "Eastern Europe") | (df["region"] == "Eastern Asia") ]

k = df["region"].value_counts()
l = df["niepodleglosc"].value_counts()

# GRUPOWANIE
n = df.sort_values("populacja", ascending=True)
m = n.groupby("region")["populacja"].mean() # TODO

df["populacja_mln"] = round(df["populacja"] / 1_000_000)

o = df.groupby("region")["populacja_mln"].mean()

df = df.dropna()


#1 Znajdź kraje o populacji mniejszej niż 1 milion.
# p = df[ df["populacja"] < 100_000_000 ]
# print(p)
#2 Znajdź kraje, które nie są niepodległe (independent == False).
# r = df[ df["niepodleglosc"] == False]
# print(r)
#3 Znajdź 5 krajów o największej populacji w Europie.
europe = df[df["region"].str.contains("Europe")]
top_5 = europe.sort_values(by="populacja", ascending=False).head(5)
print(top_5)