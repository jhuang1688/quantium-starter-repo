import glob
import csv

path = "data/*.csv"

with open('output.csv', mode='w') as csv_file:
  fieldnames = ['Sales', 'Date', 'Region']
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  writer.writeheader()

for fname in glob.glob(path):
  print(fname)

  with open(fname, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if row['product'] == 'pink morsel':
        sales = float(row['price'].split('$')[1]) * float(row['quantity'])
        with open('output.csv', mode='a') as csv_file:
          writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
          writer.writerow({'Sales': sales, 'Date': row['date'], 'Region': row['region']})


