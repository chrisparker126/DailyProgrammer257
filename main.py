
import csv


def getint(year_string):
    if year_string == "":
        return 0;
    else:
        return int(year_string)


def get_earliest(presidents):
    result = 50000;
    for president in presidents:
        if president[1] < result:
            result = president[1];
    return result;


def get_latest(presidents):
    result = 0;
    for president in presidents:
        if president[2] > result:
            result = president[2];
    return result;


def get_count(year, presidents):
    count = 0
    for president in presidents:
        birth_year = president[1]
        death_year = president[2]
        if death_year == 0 :
            death_year = 50000
        if (year >= birth_year) and (year <= death_year):
            count = count + 1
    return count


def get_max(year_counts):
    result = 0;
    for year_count in year_counts:
        if year_count[1] > result:
            result = year_count[1];
    return result;


def years(maxCount, year_counts):
    years = []
    for year_count in year_counts:
        if year_count[1] == maxCount:
            years.append(year_count[0])
    return years

PRESIDENTS_FILE = "presidents.txt"

if __name__ == '__main__':
    # read file in and get dates
    presidents = []
    with open('presidents.txt', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            presidents.append((row[0], int(row[1][-4:]),
                    getint(row[3][-4:].strip())))
    yearCounts = []
    for i in range(get_earliest(presidents), get_latest(presidents)+1, 1):
        yearCounts.append((i, get_count(i, presidents)));

    maxYear = get_max(yearCounts)
    print(years(maxYear, yearCounts))
