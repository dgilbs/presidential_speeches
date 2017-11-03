from nltk.corpus import movie_reviews

fileids = movie_reviews.fileids()
#print(fileids[0])
print(movie_reviews.categories(fileids[0])[0])
#print([movie_reviews.categories(fid)[0] for fid in fileids])