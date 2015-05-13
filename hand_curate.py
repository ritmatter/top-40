import sys
import urllib
import json
from lxml import html
import urllib2
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import re

# A series of commands to curate the data by hand
def sanitize_data():
    client = MongoClient()
    db = client.top_40

    db.entries.update({ "artist": "Ames Brothers" }, { "$set": { "artist": "The Ames Brothers" }})

    db.entries.update({ "title": "Youre Beautiful" }, { "$set": { "title": "You're Beautiful" }})

    db.entries.update({ "artist": "Andrews Sisters" }, { "$set": { "artist": "The Andrews Sisters" }})
    db.entries.update({ "title": "I Can Dream, Can't I" }, { "$set": { "title": "I Can Dream, Can't I?" }})

    db.entries.update({ "artist": "Sammy Kaye And His Orchestra" }, { "$set": { "artist": "Sammy Kaye" }})

    db.entries.update({ "artist": "Les Baxter & His Orchestra" }, { "$set": { "artist": "Les Baxter" }})

    db.entries.update({ "artist": "Ne Yo" }, { "$set": { "artist": "Ne-Yo" }})
    db.entries.update({ "artist": "Lady Antebellem" }, { "$set": { "artist": "Lady Antebellum" }})
    db.entries.update({ "title": "Leavin" }, { "$set": { "title": "Leavin'" }})
    db.entries.update({ "artist": "Nat \'king\' Cole" }, { "$set": { "artist": "Nat King Cole" }})
    db.entries.update({ "artist": "Natalia La Rose" }, { "$set": { "artist": "Natalie La Rose" }})
    db.entries.update({ "artist": "Jason Durelo" }, { "$set": { "artist": "Jason Derulo" }})
    db.entries.update({ "title": "Truffle" }, { "$set": { "title": "Truffle Butter" }})
    db.entries.update({ "title": "Where Is The Love" }, { "$set": { "title": "Where Is The Love?" }})
    db.entries.update({ "title": "Only The Lonley" }, { "$set": { "title": "Only The Lonely" }})
    db.entries.update({ "title": "The Glow Worm" }, { "$set": { "title": "Glow Worm" }})
    db.entries.update({ "artist": "The Mills Brothers" }, { "$set": { "artist": "The Mills Brothers" }})
    db.entries.update({ "artist": "Beatles" }, { "$set": { "artist": "The Beatles" }})



sanitize_data()
