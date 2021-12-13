import csv
from itertools import islice


def create_csv(name, csv_head):
    path = 'csv_file/' + name + '.csv'
    with open(path, 'w') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(csv_head)


def read_csv(name):
    path = '../csv_file/' + name + '.csv'
    res = []
    with open(path, "r") as f:
        csv_read = csv.reader(f)
        for p in islice(csv_read, 1, None):
            tmp = map(float, p)
            res.append(list(tmp))

    return res

def write_csv(name, data_row):
    pass
    # path = '../CMAB/' + name + '.csv'
    # with open(path, 'a', newline="") as f:
    #     csv_write = csv.writer(f)
    #     csv_write.writerow(data_row)


if __name__ == '__main__':
    print(read_csv("Point"))
