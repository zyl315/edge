import csv
from itertools import islice


def create_csv(name, csv_head):
    path = '../../results/' + name + '.csv'
    with open(path, 'w', newline="") as f:
        csv_write = csv.DictWriter(f, csv_head)
        csv_write.writeheader()


def read_csv(name):
    path = '../../data/csv_file/' + name + '.csv'
    res = []
    with open(path, "r") as f:
        csv_read = csv.reader(f)
        for p in islice(csv_read, 1, None):
            tmp = map(float, p)
            res.append(list(tmp))

    return res


def write_csv(name, data_row):
    path = '../../results/' + name + '.csv'
    with open(path, 'a', newline="") as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data_row)
