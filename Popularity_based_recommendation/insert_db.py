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
        db = conn.Advanced_recommendation

        # Created collection in database
        collection = db.ad_recommendation

        for idx,movie_name in (enumerate(data['title'])):
            name = movie_name
            movie_id = data['movie_id'][idx]
            user_id = data['user_id'][idx]
            movie_ratings = data['rating'][idx]
            sex = data['sex'][idx]
            occupation = data['occupation'][idx]

            movie_data = {
                    "name":name,
                    "movie_id":str(movie_id),
                    "user_id":str(user_id),
                    "movie_ratings":str(movie_ratings),
                    "sex":sex,
                    "occupation":occupation
                    }

            # Insert Data
            rec_id1 = collection.insert_one(movie_data)

if __name__ == '__main__':
    movie = pd.read_csv('final_movielens.csv')
    obj = storage(movie)
    obj.main()
