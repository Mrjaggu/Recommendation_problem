from sklearn.externals import joblib
from pymongo import MongoClient
import numpy as np

class testing():
    def __init__(self,similarity,vectorizer,query):
        self.similarity = similarity
        self.query = query
        self.vectorizer = vectorizer
    def vectorize(self,text):
        return self.vectorizer.transform(text)

    def connection(self):
        try:
            conn = MongoClient()
            print("Connected successfully!!!")

            # database
            db = conn.database
            # Created or Switched to collection names: my_gfg_collection
            collection = db.movie_collection
            cursor = collection.find()
            return cursor

        except:
            print("Could not connect to MongoDB")

    def movie_name(self):
        c = self.connection()
        m_name = [(record['name']) for record in c]

        return m_name

    def main(self):
        name = self.movie_name()
        id = name.index(self.query)
        similarity_score = list(enumerate(self.similarity[id]))
        indices = sorted(similarity_score, key=lambda x: x[1], reverse=True)
        indices = indices[1:10]
        movie_indices = [i[0] for i in indices]
        print("Similar movie of {} are: \n".format(self.query))
        for i in range(0,len(indices)):
            print("{}".format(name[movie_indices[i]]))

if __name__ == '__main__':
    similarity= np.load('./similarity.npy')
    vect = joblib.load('./vectorizer.pkl')
    obj = testing(similarity,vect,'Toy Story')
    obj.main()
