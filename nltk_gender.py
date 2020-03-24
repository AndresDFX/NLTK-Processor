import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

#Gender prediction: input a person's name and predict if it is male or female
def gender_features(word):
    return {'last_letter': word[-1]}

#Training Data prediction
def train():
    nombres = ([(name, 'male') for name in names.words('male.txt')] +
             [(name, 'female') for name in names.words('female.txt')])
    featuresets = [(gender_features(n), g) for (n,g) in nombres]
    train_set = featuresets
    return train_set

def predictionGender(name):
    classifier = nltk.NaiveBayesClassifier.train(train());
    return classifier.classify(gender_features(name))
