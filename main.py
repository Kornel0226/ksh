import asyncio
from fetch import download_file
from record import load_records
from statistics import man_female_population, man_woman_average_age

asyncio.run(download_file("https://www.ksh.hu/stadat_files/nep/hu/nep0002.xlsx", "./data/table.xlsx"))
_, xd = load_records("./data/table.xlsx", 1)
man_female_population(xd)
man_woman_average_age(xd)
