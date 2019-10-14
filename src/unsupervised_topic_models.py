from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans
from sklearn.feature_extraction import text

def LDA(data, n_topics, num_features, num_top_words):

    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=num_features, stop_words='english')
    tf = tf_vectorizer.fit_transform(data)
    
    tf_feature_names = tf_vectorizer.get_feature_names() #theses are the words in our bag of words
    
    lda = LatentDirichletAllocation(n_components=n_topics, max_iter=5, learning_method='online',random_state=0, n_jobs=-1)
    lda.fit(tf)
    
    return display_topics(lda, tf_feature_names, num_top_words)




def cluster_model(data, n_clusters = 10, n_words = 10, stopwords = 'english'):
    
    count_vect = CountVectorizer(lowercase=True, tokenizer=None, stop_words=stopwords,
                                 analyzer='word', max_df=1.0, min_df=1,
                                 max_features=None)
    count_vect.fit(data)
    word_counts = count_vect.transform(data)

    km = KMeans(n_clusters)
    km.fit(word_counts)
    centroids = np.array(km.cluster_centers_)

    topwords_index = np.zeros((n_clusters,n_words))
    for i in range(centroids.shape[0]):
        topwords_index[i] += centroids[i].argsort()[::-1][:n_words]
    topwords_index = topwords_index.astype(int)
    topiclist = []
    for i in range(topwords_index.shape[0]):
        wordlist = []
        for j in range(topwords_index.shape[1]):
            wordlist.append(count_vect.get_feature_names()[topwords_index[i][j]])
        words = ', '.join(wordlist)
        topiclist.append(words)
    return topiclist