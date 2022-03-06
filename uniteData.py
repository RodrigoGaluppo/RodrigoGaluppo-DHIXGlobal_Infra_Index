import csv

countriesList = []
idhList = []
infraData = []

with open('idh.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            country = row[0]
            countriesList.append(country)
            idhList.append(row[1])
            line_count += 1

with open('infra.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            for country in countriesList:
                if country == row[0]:
                    infraData.append(row[1])

with open('final.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')

    spamwriter.writerow(["country", "score idh", "score infra"])
    i = 0
    for c in countriesList:
        spamwriter.writerow([c, idhList[i], infraData[i]])
        i += 1
