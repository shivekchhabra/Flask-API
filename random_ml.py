from ricebowl import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle


## Overveiew:
# This code contains a random machine learning model.
# The goal was to save it as a pickle to be used by Flask service

def simple_modeling(data, label):
    xtrain, xtest, ytrain, ytest = train_test_split(data, label, test_size=0.3, random_state=7)
    classifier = RandomForestClassifier()
    classifier.fit(xtrain, ytrain)
    pred = classifier.predict(xtest)
    # acc = accuracy_score(ytest, pred)
    return classifier


def pickle_model(model, path_and_filename):
    pickle_out = open(path_and_filename, 'wb')
    pickle.dump(model, pickle_out)
    pickle_out.close()
    print('Model saved {}'.format(path_and_filename))


if __name__ == '__main__':
    df = preprocessing.read_csv('banknote.csv')
    label = df['class']
    data = df.drop(columns='class')
    model = simple_modeling(data, label)
    pickle_model(model, './model.pkl')