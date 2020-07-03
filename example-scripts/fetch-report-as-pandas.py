import requests
from io import StringIO
import pandas as pd

fields = {
    'token': 'REDCAPSECRETTOKEN',
    'content': 'report',
    'format': 'csv',
    'report_id': '5', # Get report_id from REDCap web frontend
    'csvDelimiter': '',
    'rawOrLabel': 'label',
    'rawOrLabelHeaders': 'label',
}

r = requests.post('https://redcap-api-end-point-url', fields)
pr = StringIO(r.text)
df = pd.read_csv(pr, header=0, squeeze=True)
