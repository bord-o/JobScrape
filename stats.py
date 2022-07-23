from textblob import TextBlob
from nltk.corpus import stopwords

with open('./stor/tech1k.txt', 'r') as tf:
    tech = tf.read()
    blob = TextBlob(tech)
    stop_wds = stopwords.words("english")

    # get word counts and remove stopwords 'a, the, he, etc.'
    counts = blob.word_counts
    for w in stop_wds:
        if w in counts:
            counts.pop(w)

    # get sorted word frequencies
    s_counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}

    # get the list of all words with only one occurence
    uniques = list(filter(lambda t: t[1] == 1, s_counts.items()))
    uniques = map(lambda t: t[0], uniques)

    # remove one occurence words from sorted count
    for w in uniques:
        if w in s_counts:
            s_counts.pop(w)

    print(s_counts)

    # uniq_words = list(set(blob.words))

    # lwds = list(map(lambda s: s.lower(), uniq_words))


    # print(lwds)
    # print(len(set(blob.words)))

