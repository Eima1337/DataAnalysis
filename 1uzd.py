import datetime

# Sukurkite 4 kintamuosius, kurie saugotų jūsų vardą, pavardę, gimimo metus ir šiuos metus (nebūtinai tikrus). Parašykite kodą, kuris pagal gimimo metus paskaičiuotų jūsų amžių ir naudodamas vardo ir pavardės kintamuosius atspausdintų tokį sakinį :
# "Aš esu Vardenis Pavardenis. Man yra XX metai(ų)".

name = "Eimantas"
last_name = "Bakevicius"
birth_year = 1992
current_date = datetime.datetime.now()
current_year = current_date.year
age = str(current_year - birth_year)

print(f"As esu {name} {last_name}. Man yra arba bus {age} metai.")