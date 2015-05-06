import sys
import urllib
import json
from lxml import html
import urllib2
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

def get_current_40(year, db):
    print "Getting page for year: " + str(year)
    page = requests.get('http://top40charts.net/index.php?page=' + str(year) + '-music-charts').text
    page_soup = BeautifulSoup(page)
    tables = page_soup.select("#table_1")

    # HTML structure slightly different for some pages
    if len(tables) == 0:
        table = page_soup.select("#table_2")[0]
    else:
        table = tables[0]
    trs = table.select("tr")
    for tr in trs:
        tds = tr.select("td")
        if len(tds) == 5:
          artist = tds[3].text.encode('utf-8').strip()
          title = tds[4].text.encode('utf-8').strip()

          print title
          print artist
          entry = {
            "year": year,
            "title": title,
            "artist": artist
          }
          db.entries.insert_one(entry)
          print ""

def get_top_40():
    print "Connecting to database..."
    client = MongoClient()
    db = client.top_40
    year = 1950
    while year < 2016:
        print year
        print ""
        get_current_40(year, db)
        year += 1

get_top_40()
