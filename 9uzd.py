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

if (seconds + extra_seconds) > 59:
    if (minutes + extra_minutes) > 59:
        if (hours + extra_hours) > 23:

            if (extra_seconds / 60) >= 1:
                if (extra_seconds % 60) >= 1:
                    extra_minutes = (round(extra_seconds / 60))
                    seconds = seconds + (extra_seconds % 60)

            print(f"{extra_seconds}, {extra_minutes}")


