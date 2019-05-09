#!/usr/bin/env python3
import urllib.request
import json
import yaml

def main():
    
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
    startdate = 'start_date=2019-05-08'
    enddate = '&end_date=END_DATE'
    mykey = '&api_key=DEMO_KEY'

    neourl += startdate + mykey
    neojson = (urllib.request.urlopen(neourl)).json()

    print(neojson)

main()

zfile = open("Thurschal.yml", "w")
yaml.dump(neojson)
zfile.close()

