import pandas as pd


class Record:
    def __init__(self, year, man_population, female_population, average_male_age, average_female_age, average_age):
        self.year = year
        self.man_population = man_population
        self.female_population = female_population
        self.average_male_age = average_male_age
        self.average_female_age = average_female_age
        self.average_age = average_age

    def __str__(self):
        return f"{self.year, self.man_population, self.female_population, self.average_male_age, self.average_female_age, self.average_age}"


def load_records(path_to_file, header_index):
    print("Excel fájl beolvasása...")
    data = pd.read_excel(path_to_file, engine="calamine", header=header_index)
    records = []

    for index, row in data.iterrows():
        records.append(Record(
            row["Év"],
            row["A férfi népesség száma, január 1., ezer fő"],
            row["A női népesség száma, január 1., ezer fő"],
            row["A népesség száma összesen, január 1., ezer fő"],
            row["A nők átlagéletkora, év  január 1."],
            row["Átlagéletkor összesen, év január 1."]
        )
        )
    print("Táblázat beolvasva.")
    return records, data
