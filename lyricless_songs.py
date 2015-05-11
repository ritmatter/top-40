from pymongo import MongoClient

client = MongoClient()
db = client.top_40
cursor = db.entries.find()
for entry in cursor:
    if 'lyrics' not in entry:
        print entry['artist'].encode('utf-8') + ':' + entry['title'].encode('utf-8')
cursor.close()

