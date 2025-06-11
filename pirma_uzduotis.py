import datetime

# Pirma uzduotis

name = "Eimantas"
last_name = "Bakevicius"
birth_year = 1992
current_date = datetime.datetime.now()
current_year = current_date.year
age = str(current_year - birth_year)

print(f"As esu {name} {last_name}. Man yra arba bus {age} metai.")