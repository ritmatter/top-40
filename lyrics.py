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

def sanitize_title(title):

    # Remove featuring from title
    title = re.sub(' ft.*', '', title, flags=re.I)
    title = re.sub(' feat.*', '', title, flags=re.I)
    title = re.sub(' \(feat.*', '', title, flags=re.I)
    title = re.sub(' \(ft.*', '', title, flags=re.I)

    # Replace common spelling mistakes
    title = re.sub('Im', 'I\'m', title)
    title = re.sub('Ive', 'I\'ve', title)
    title = re.sub('Youre', 'You\'re', title)
    title = re.sub('Its ', 'It\'s ', title)
    title = re.sub('Doesnt', 'Doesn\'t ', title)
    return title

def sanitize_artist(artist):

    # Remove featuring from artist titles
    artist = re.sub(' ft.*', '', artist, flags=re.I)
    artist = re.sub(' feat.*', '', artist, flags=re.I)
    artist = re.sub(' \(feat.*', '', artist, flags=re.I)
    artist = re.sub(' \(ft.*', '', artist, flags=re.I)

    # Replace 'And His'
    artist = re.sub(' And His.*', '', artist, flags=re.I)

    # Try Replacing &
    artist = re.sub(' \&.*', '', artist)

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
    year = entry['year']

    artist_clean = urllib2.quote(sanitize_artist(artist).replace(" ", "_"))
    title_clean = urllib2.quote(sanitize_title(title).replace(" ", "_"))
    url = 'http://lyrics.wikia.com/' + artist_clean + ':' + title_clean
    page = requests.get(url)
    if page.status_code != 200:
        print "404 error getting lyrics for " + title + " by " + artist + ", " + str(year)
        errors += 1
    else:
        page_soup = BeautifulSoup(page.text)
        lyrics = page_soup.select(".lyricbox")
        if len(lyrics) == 0:
            print "Parsing error getting lyrics for " + title + " by " + artist + ", " + str(year)
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
