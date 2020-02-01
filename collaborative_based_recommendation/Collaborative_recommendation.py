from pymongo import MongoClient
import pandas as pd
import numpy as np
from pandas import DataFrame

class training():

    def connection(self):
        try:
            conn = MongoClient()
            print("Connected successfully!!!")

            # database
            db = conn.Advanced_recommendation

            # Created collection in database
            collection = db.ad_recommendation
            cursor = collection.find()
            return cursor

        except:
            print("Could not connect to MongoDB")

    def movie_db(self,cursor):
        user_id = []
        movie_id = []
        rating = []
        title = []

        for ix,record in enumerate(cursor):
            user_id.append(int(record['user_id']))
            movie_id.append(int(record['movie_id']))
            rating.append(int(record['movie_ratings']))
            title.append(record['name'])

        m_data = pd.DataFrame()
        m_data['user_id']=user_id
        m_data['movie_id']=movie_id
        m_data['rating']=rating
        m_data['title']=title

        return m_data


    def collaborative(self,m_data,title):
        #creating pivot_table with index as user_id and cols as movie name and value as ratings
        movie_ratings = m_data.pivot_table(index=['user_id'],columns=['title'],values='rating')
        # here title is query if user click movie this we need to recommend similar movies
        Query_movie = movie_ratings[title]
        #finding correlation with query and movies
        similarmovies = movie_ratings.corrwith(Query_movie)
        #dropping na value
        similarmovies =similarmovies.dropna()
        df = pd.DataFrame(similarmovies)
        # group by according to the ratings
        movie_stats = m_data.groupby('title').agg({'rating':[np.size,np.mean]})
        #Using threshold to avoid obscure movie watched by user
        popularmovies = movie_stats['rating']['size']>=100
        # joining dataframe with similar movies
        df = movie_stats[popularmovies].join(DataFrame(similarmovies,columns=['similarity']))
        # returning top 20
        result = df.sort_values('similarity',ascending=False)[:20]
        print(result)


    def main(self,title):
        cursor = self.connection()
        data = self.movie_db(cursor)
        self.collaborative(data,title)


if __name__ =='__main__':
    obj = training()
    #here query movie or clicked by user i.e Star Wars
    obj.main('Star Wars (1977)')
