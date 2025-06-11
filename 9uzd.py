import random
from datetime import time, timedelta, datetime
# Padarykite skaitmeninį laikrodį, rodantį valandas, minutes ir sekundes. Valandom, minutėm ir sekundėm sugeneruoti panaudokite funkciją random.randint(x,x). Sugeneruokite skaičių nuo 0 iki 300. Tai papildomos sekundės. Skaičių pridėkite prie jau sugeneruoto laiko. Atspausdinkite laikrodį prieš ir po sekundžių pridėjimo ir pridedamų sekundžių skaičių.

hours = random.randint(0, 23)
minutes = random.randint(0, 59)
seconds = random.randint(0, 59)
extra_seconds = random.randint(0, 300)
# start_time = datetime(2025, 6, 11, hours, minutes, seconds)
# new_time = start_time + timedelta(seconds=extra_seconds)
#
# print(f"Pradinis laikrodis {start_time.time()}")
# print(f"Laikrodis su pridetomis sekundemis {new_time.time()}")

print(f"Start time: {hours:02d}:{minutes:02d}:{minutes:02d}")
print(f"Added seconds: {extra_seconds}")

seconds += extra_seconds

if seconds >= 60:
    added_minutes = seconds // 60
    seconds = seconds % 60
    minutes += added_minutes

if minutes >= 60:
    added_hours = minutes // 60
    minutes = minutes % 60
    hours += added_hours

if hours >= 24:
    hours = hours % 24

print(f"New time: {hours:02d}:{minutes:02d}:{seconds:02d}")



