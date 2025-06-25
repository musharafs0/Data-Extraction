
from itemadapter import ItemAdapter
import json
import csv

class BayutScraperPipeline:
    def open_spider(self, spider):
        self.file_json = open('output.json', 'w', encoding='utf-8')
        self.file_csv = open('output.csv', 'w', newline='', encoding='utf-8')
        self.csv_writer = None

    def process_item(self, item, spider):
        
        self.file_json.write(json.dumps(dict(item)) + "\n")


        if not self.csv_writer:
            self.csv_writer = csv.DictWriter(self.file_csv, fieldnames=item.keys())
            self.csv_writer.writeheader()
        self.csv_writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.file_json.close()
        self.file_csv.close()
