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
    db.entries.update({ "title": "Come On  A My House" }, { "$set": { "title": "Come On-A My House" }})
    db.entries.update({ "artist": "Four Aces" }, { "$set": { "artist": "The Four Aces" }})
    db.entries.update({ "title": "Walkin' My Baby Back Home" }, { "$set": { "title": "Walking My Baby Back Home" }})
    db.entries.update({ "title": "Pittsburgh, Pennsylvania" }, { "$set": { "title": "Pittsburgh Pennsylvania" }})
    db.entries.update({ "artist": "Everly Brothers" }, { "$set": { "artist": "The Everly Brothers" }})
    db.entries.update({ "artist": "Anton Karas" }, { "$set": { "artist": "Guy Lombardo" }})
    db.entries.update({ "title": "The Third" }, { "$set": { "title": "The Third Man Theme" }})
    db.entries.update({ "title": "If I Knew You Were Comin'" }, { "$set": { "title": "If I Knew You Were Comin' I'd've Baked A Cake", "artist": "Fred Penner" }})
    db.entries.update({ "artist": "Perry Como And Fontane Sisters" }, { "$set": { "artist": "Perry Como" }})
    db.entries.update({ "artist": "Perry Como And Betty Hutton" }, { "$set": { "artist": "Perry Como" }})
    db.entries.update({ "artist": "Gary Crosby And His Friend (Bing Crosby)" }, { "$set": { "artist": "Bing Crosby" }})
    db.entries.update({ "title": "Hoop Dee Doo" }, { "$set": { "title": "Hoop-Dee-Doo" }})
    db.entries.update({ "title": "Sin" }, { "$set": { "title": "(It's No) Sin" }})
    db.entries.update({ "title": "My Truly, Truly Fair" }, { "$set": { "title": "My Truly Truly Fair" }})
    db.entries.update({ "title": "Rudolph, The RedNosed Reindeer" }, { "$set": { "title": "Rudolph The Red-Nosed Reindeer" }})
    db.entries.update({ "title": "I Said My Pajamas" }, { "$set": { "title": "I Said My Pajamas (And Put On My Pray'rs)", "artist": "Tony Martin" }})
    db.entries.update({ "artist": "Weavers" }, { "$set": { "artist": "The Weavers" }})
    db.entries.update({ "title": "On Top Of Old Smoky" }, { "$set": { "title": "On Top Of Old Smokey" }})

sanitize_data()
