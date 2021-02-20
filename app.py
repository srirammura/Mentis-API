
from flask import Flask,render_template,url_for,request
import re
import pandas as pd
import spacy
from spacy.tokens import Span
from spacy import displacy
import en_core_web_sm
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
	if request.method == 'POST':
		rawtext = request.form['rawtext']
		doc = nlp(rawtext)
		d = []
		results=[]
		for ent in doc.ents:
			d.append((ent.label_, ent.text))
			df = pd.DataFrame(d, columns=('Text', 'Category'))
			df = df.loc[(df['Text'] == 'PERSON') | (df['Text'] == 'GPE') | (df['Text'] == 'PRODUCT')]
	return render_template("index.html", column_names=df.columns.values, row_data=list(df.values.tolist()), zip=zip)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080,debug=False,threaded=True)
