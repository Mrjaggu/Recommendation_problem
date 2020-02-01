from pymongo import MongoClient
import pandas as pd

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


    def popularity(self,train,title,ids):
        train_data_grouped = train.groupby([title])[ids].count().reset_index()  #user_id  #movie title
        train_data_grouped.rename(columns = {ids: 'score'},inplace=True)
        train_data_sort = train_data_grouped.sort_values(['score',title], ascending = [0,1])
        train_data_sort['Rank'] = train_data_sort['score'].rank(ascending=0, method='first')
        popularity_recommendations = train_data_sort.head(10)
        print(popularity_recommendations)


    def main(self):
        cursor = self.connection()
        data = self.movie_db(cursor)
        self.popularity(data,'title','user_id')


if __name__ =='__main__':
    obj = training()
    obj.main()
