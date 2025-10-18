"""
CP1404/CP5632 Practical05
Wimbledon
Estimate: 45 minutes
Actual: ...Days
"""

FILENAME = "wimbledon.csv"
YEAR_INDEX = 0
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Read file, process data and display champions/winning countries."""
    records = []
    load_records(FILENAME, records)
    name_to_score = determine_number_of_wins(records)
    countries = determine_countries(records)
    print("Wimbledon Champions:")
    for champion, wins in name_to_score.items():
        print(f"{champion} {wins}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def load_records(filename, records):
    """Load Wimbledon data from file into records list."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            if len(parts) >= 3:
                year, champion, country = parts[YEAR_INDEX], parts[CHAMPION_INDEX], parts[COUNTRY_INDEX]
                records.append((year, champion, country))


def determine_number_of_wins(records):
    """Count how many times each champion has won."""
    name_to_score = {}
    for record in records:
        champion = record[1]
        name_to_score[champion] = name_to_score.get(champion, 0) + 1
    return name_to_score


def determine_countries(records):
    """Return a set of all winning countries."""
    countries = set()
    for record in records:
        countries.add(record[2])
    return countries


main()
