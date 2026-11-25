import csv


seen = set()
result = []

with open("ideas_for_test/work_with_csv/r-m-c.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 17:
            continue
        key = (row[0], row[15], row[16])
        if key in seen:
            continue

        seen.add(key)
        result.append(row)

with open("ideas_for_test/work_with_csv/random-michaels.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 17:
            continue
        key = (row[0], row[15], row[16])
        if key in seen:
            continue

        seen.add(key)
        result.append(row)

with open("result_voloshyn.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(result)