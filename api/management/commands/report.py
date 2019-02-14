from django.core.management.base import BaseCommand, CommandError
from django.template.loader import render_to_string
from django.conf import settings
import csv


class Command(BaseCommand):
    help = 'Report ocr result'

    def read_csv(self, file_name, sorted_key="image"):
        with open(file_name) as csvfile:
            reader = csv.DictReader(csvfile)
            return sorted(list(reader), key= lambda k: k[sorted_key])

    def merge_csv_files(self, base_file, base_key, merge_file, merge_key ):
        base= self.read_csv(settings.BASE_DIR + base_file)
        merge =  self.read_csv(settings.BASE_DIR + merge_file)
        for i in range(len(base)):
            base[i][base_key] = merge[i][merge_key]
        return base

    def handle(self, *args, **options):
        tesseract = self.read_csv(settings.BASE_DIR+"/static/tesseract.csv")
        base = self.read_csv(settings.BASE_DIR+"/static/report.csv")
        for i in range(len(base)):
            base[i]["tesseract2"] = tesseract[i]["tesseract"]
        for i in range(len(base)):
            print(base[i])
        # list_rows = self.read_csv(settings.BASE_DIR+"/static/report.csv")
        # context = {"list_rows": list_rows}
        # rendered = render_to_string('report.html',context)
        # with open(settings.BASE_DIR+"/static/report.html","w+") as file:
        #     file.write(rendered)



