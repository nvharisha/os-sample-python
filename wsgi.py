import csv
import json
from flask import Flask
application = Flask(__name__)

## ----- HARI ADDED
fieldnames = ("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30") 
## ---- END
@application.route("/")



def world():
  csvfilename = 'one.csv'
  jsonfilename = csvfilename.split('.')[0] + '.json'
  csvfile = open(csvfilename, 'r')
  jsonfile = open(jsonfilename, 'w')
  reader = csv.DictReader(csvfile)


  output = []

  for each in reader:
    row = {}
    for field in fieldnames:
       row[field] = each[field]
    output.append(row)
  return json.dumps(output, indent=4, sort_keys=True)


def hello():
    return "Hello World!"

if __name__ == "__main__":
    application.run()
