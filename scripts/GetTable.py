"""
This is an example script to download a data table using Statistics Canada's API
Created by Joseph Kuchar,
February 10th, 2020

"""

import requests
import json

#example product ID number - CPI is 36100104
pid='36100104'

url='https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/'

R=requests.get('https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/{}/en'.format(pid))

response=R.json()

url2=response['object']

#now make second call to download the table

T=requests.get(url2)

g=open(pid+'.zip','wb')

g.write(T.content)

g.close()


