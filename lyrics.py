import sys
import urllib
import json
from lxml import html
import urllib2
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import re

def santize(lyrics):
    lyrics = lyrics.lower()
    words = ['(', ')', '.', ',', '?', '!', '*']
    for w in words:
        lyrics = lyrics.replace(w, '')
    return lyrics

def sanitize_artist(artist):
    artist = re.sub(' ft.*', '', artist, flags=re.I)
    artist = re.sub(' feat.*', '', artist, flags=re.I)
    artist = re.sub(' \(feat.*', '', artist, flags=re.I)
    artist = re.sub(' \(ft.*', '', artist, flags=re.I)
    return artist

def get_top_40_lyrics():
    global successes
    global errors
    client = MongoClient()
    db = client.top_40
    cursor = db.entries.find()
    for entry in cursor:
        if 'lyrics' not in entry:
            get_lyrics(entry, db)
    cursor.close()
    print "Finished with " + str(successes) + " successes and " + str(errors) + " errors"

def get_lyrics(entry, db):
    global errors
    global successes

    title = entry['title'].encode('utf-8')
    artist = entry['artist'].encode('utf-8')

    title_clean = urllib2.quote(title.replace(" ", "_"))
    artist_clean = urllib2.quote(sanitize_artist(artist).replace(" ", "_"))
    url = 'http://lyrics.wikia.com/' + artist_clean + ':' + title_clean
    page = requests.get(url)
    if page.status_code != 200:
        print "Error getting lyrics for " + title + " by " + artist
        errors += 1
    else:
        page_soup = BeautifulSoup(page.text)
        lyrics = page_soup.select(".lyricbox")
        if len(lyrics) == 0:
            print "Error getting lyrics for " + title + " by " + artist
            errors += 1
            return

        lyrics = lyrics[0]
        [x.extract() for x in lyrics.findAll('script')]
        lyrics = lyrics.get_text(' ', strip=True).encode('utf-8')
        lyrics = santize(lyrics)
        entry['lyrics'] = lyrics
        db.entries.save(entry)
        successes += 1
        print "Successfully extracted lyrics for " + title + " by " + artist

errors = 0
successes = 0
get_top_40_lyrics()
