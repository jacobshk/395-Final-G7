from pymongo import MongoClient
import certifi
ca = certifi.where()

uri = "mongodb+srv://enzo:poopybutthead@cluster0.5itsxbk.mongodb.net/"
client = MongoClient(uri, tlsCAFile=ca)
db = client["Cluster0"]
collection = db["Poodle_Classroom"]

def create(data):
    obj = collection.insert_one(data)

def read():
    objects = collection.find()
    for obj in objects:
        print(obj)

def update(query, new_data):
    obj = collection.update_one(query, {'$set': new_data})

def delete(query):
    obj = collection.delete_one(query)

def main():
    # Example usage of functions
    data_to_insert = {"name": "Max", "age": 5, "breed": "Poodle"}
    create(data_to_insert)

    print("Data in the collection:")
    read()

    # Example update
    update_query = {"name": "Max"}
    new_data = {"age": 6}
    update(update_query, new_data)

    print("\nData after update:")
    read()

    # Example deletion
    delete_query = {"name": "Max"}
    delete(delete_query)

    print("\nData after deletion:")
    read()

if __name__ == "__main__":
    main()
