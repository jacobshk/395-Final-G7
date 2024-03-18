import pymongo

url = 'mongodb+srv://tk:ilove395@cluster0.5itsxbk.mongodb.net/'
client = pymongo.MongoClient(url)

db = client['Cluster0']