from pymongo import MongoClient
import pandas as pd

class storage():
    def __init__(self,data):
        self.movie = data

    def main(self):
        try:
            conn = MongoClient()
            print("Connected successfully!!!")
        except:
            print("Could not connect to MongoDB")

        # database
        db = conn.database

        # Created collection in database
        collection = db.movie_collection

        for idx,movie_name in enumerate(self.movie['title']):
            name = movie_name
            overview = movie['overview'][idx]

            # creating schema for collections
            movie_data = {
                    "name":name,
                    "summary":overview,
                    }

            # Inserting data one by one in collection
            rec_id1 = collection.insert_one(movie_data)

if __name__ == '__main__':
    movie = pd.read_csv('movie_database.csv',nrows=5000)
    obj = storage(movie)
    obj.main()
