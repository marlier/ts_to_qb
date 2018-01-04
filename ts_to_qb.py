import argparse
import csv
import dateutil.parser
import time


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', action="store", dest="file", required=True)
args = parser.parse_args()

class Writer(object):
    def __init__(self):
        self.rows_written = 0
        self.filename = "/Users/imarlier/Desktop/import.{}".format(time.time())
        self.writer = self.init_writer(0)

    def init_writer(self, part):
        writer = csv.writer(open("{}.{}.csv".format(self.filename, part), "w"))
        writer.writerow(['Date', 'Description', 'Amount'])
        return writer

    def writerow(self, row):
        if self.rows_written % 800 == 0:
            self.writer = self.init_writer(int(self.rows_written / 800))
        self.writer.writerow(row)
        self.rows_written += 1


with open(args.file, 'r', encoding='utf-8') as csvfile:
    l = 1
    try:
        reader = csv.DictReader(csvfile)
        filename = "/Users/imarlier/Desktop/import.{}".format(time.time())
        writer = Writer()

        if 'product' in reader.fieldnames:
            product_field = 'product'
        else:
            product_field = '\ufeff"product"'

        for line in reader:
            if float(line['total_cost']) == 0:
                continue
            l = l + 1
            d = dateutil.parser.parse(line['processed_at']).strftime('%m/%d/%Y')
            description = line[product_field] + " - " + line['transaction_id']
            amount = float(line['total_cost'])
            writer.writerow([d, description, amount])
            if float(line['processing_cost']) != 0:
                writer.writerow([d, 'Stripe processing fee - {}'.format(line['transaction_id']), float(line['processing_cost']) * -1])
            if float(line['service_cost']) != 0:
                writer.writerow([d, 'TopScore service fee - {}'.format(line['transaction_id']), float(line['service_cost']) * -1])
            if float(line['total_paid_refund']) != 0:
                description = "Refund - " + line[product_field] + " - " + line['transaction_id']
                amount = float(line['total_paid_refund']) * -1
                writer.writerow([d, description, amount])
    except UnicodeDecodeError as ex:
        print("Unicode exception on line {}".format(l))