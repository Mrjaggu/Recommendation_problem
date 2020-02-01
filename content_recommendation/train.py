#importing package
from sklearn.metrics.pairwise import linear_kernel
from pymongo import MongoClient
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import re
import numpy as np
from sklearn.externals import joblib
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


class training():
    def __init__(self,query):
        self.query = query

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


    def movie_name(self,cursor):
        m_name = [(record['name']) for record in cursor]
        return m_name

    def pre_processing(self,text):
        try:
            if (type(text)!=int) and (text!=np.nan):
                string=""
                for words in text.split():
                    word = ("".join(e for e in words if e.isalnum()))
                    word = word.lower()
                    word = re.sub(":",'',word)
                    if not word in stop_words:
                        string+=word + " "
                return string
        except:
            return ''

    def vectorize(self,df):
        vectorizer = TfidfVectorizer()
        overview_bow = vectorizer.fit_transform(df)
        joblib.dump(overview_bow, 'vectorizer.pkl')
        return overview_bow

    def get_similarity(self,vect):
        #using linear kernel we calculate similarity matrix
        similarity  = linear_kernel(vect,vect)

        return similarity

    def main(self):
        #db connection for collection
        cursor = self.connection()
        #pre pre-processing our data
        summary = [self.pre_processing(record['summary']) for record in cursor]
        name = self.movie_name(cursor)
        # vectorizing our data
        s = self.vectorize(summary)
        # getting similarity matrix
        similarity = self.get_similarity(s)
        np.save('./similarity.npy',similarity)
        #getting query as title index
        id = name.index(self.query)
        #getting similarity_score
        similarity_score = list(enumerate(similarity[id]))
        #sorting
        indices = sorted(similarity_score, key=lambda x: x[1], reverse=True)
        #top 10
        indices = indices[1:10]
        movie_indices = [i[0] for i in indices]
        print("Similar movie of {} are: \n".format(self.query))
        for i in range(0,len(indices)):
            print("{}".format(name[movie_indices[i]]))


if __name__ =='__main__':
    call = training('Malice')
    call.main()
