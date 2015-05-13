from pymongo import MongoClient

def get_lyricless():
    client = MongoClient()
    db = client.top_40
    cursor = db.entries.find()
    for entry in cursor:
        if 'lyrics' not in entry:
            print entry['artist'].encode('utf-8') + ':' + entry['title'].encode('utf-8')
    cursor.close()

def get_yearcount():
    client = MongoClient()
    db = client.top_40
    i = 1950
    while i < 2016:
        cursor = db.entries.find({ "year": i, "lyrics": { "$exists": True }})
        full_cursor = db.entries.find({ "year": i })
        print str(i) + " , " + str(cursor.count()) + " / " + str(full_cursor.count())
        i += 1
    cursor.close()
