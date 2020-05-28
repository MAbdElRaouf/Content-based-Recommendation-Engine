import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

netflix_titles_df = pd.read_csv('netflix_titles.csv')

netflix_titles_df.drop(netflix_titles_df.columns[[0,1,5,6,7,9]], axis=1, inplace=True)

netflix_titles_df.fillna('', inplace=True)

netflix_titles_df[['director','cast']] = netflix_titles_df[['director','cast']].applymap(lambda x: ' '.join(x.replace(' ', '').split(',')[:3]))

netflix_titles_df['title_dup'] = netflix_titles_df['title']

titles_corpus = netflix_titles_df.apply(' '.join, axis=1)

tfidf_vectorizer_params = TfidfVectorizer(lowercase=True, stop_words='english', ngram_range=(1, 3), max_df = .5)

tfidf_vectorizer = tfidf_vectorizer_params.fit_transform(titles_corpus)

pickle.dump(tfidf_vectorizer, open('tfidf_vectorizer.pickle', 'wb'))