import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

def word_feats(words):
    return dict([(word, True) for word in words])

#prepare training data. Better the training data, more accurate the predictions
def train():
    positive_vocab = [ 'awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)' ]
    negative_vocab = [ 'bad', 'terrible','useless', 'hate', ':(' ]
    neutral_vocab = [ 'movie','the','sound','was','is','actors','did','know','words','not' ]

    positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
    negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
    neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]
    train_set = negative_features + positive_features + neutral_features
    return train_set


def sentiment(sentence):
    # Predict
    neg = 0
    pos = 0
    sentence = sentence.lower()
    words = sentence.split(' ')
    classifier = NaiveBayesClassifier.train(train())
    for word in words:
        classResult = classifier.classify( word_feats(word))
        if classResult == 'neg':
            neg = neg + 1
        if classResult == 'pos':
            pos = pos + 1
    return 'Positive: ' + str(float(pos)/len(words))+'\nNegative: ' + str(float(neg)/len(words))
