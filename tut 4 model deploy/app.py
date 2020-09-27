from flask import Flask, render_template, redirect, request
import joblib
from nltk.stem import WordNetLemmatizer
# import nltk
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.corpus import wordnet
from re import sub

app = Flask(__name__)

classifier = joblib.load('text_classifier.pkl')
tfidf = joblib.load('tfidf.pkl')
label_y = joblib.load('label_y.pkl')

@app.route('/')
def home() :
	return render_template('index.html')

# Function to convert into simple pos tags
def get_simple_pos(tag) :
    if tag.startswith('J'):
        return 'a'
    elif tag.startswith('V'):
        return 'v'
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return 'r'
    else:
        return wordnet.NOUN

# function for single prediction
def single_prediction(sentence) :
	b = []
	single_predict = sub('[^a-zA-Z]', " ", sentence)
	single_predict = single_predict.strip().split()
	lemmatizer = WordNetLemmatizer()
	single_predict = [lemmatizer.lemmatize(word, pos = get_simple_pos(pos_tag([word])[0][1])).lower() for word in single_predict if not word.lower() in set(stopwords.words('english'))]
	single_predict = " ".join(single_predict)
	b.append(single_predict)
	single_predict = tfidf.transform(b).toarray()
	single_predict = classifier.predict(single_predict)
	return label_y.inverse_transform(single_predict)[0]

@app.route('/', methods = ['POST'])
def classify() :
	sentence = request.form['text_box']
	pred = single_prediction(sentence)
	pred = pred.split('.')
	pred = ' '.join(pred)
	return render_template('index.html', prediction = pred)

if __name__ == '__main__':
	# app.run(debug = True)
	app.run()