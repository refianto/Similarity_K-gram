from flask import *
from kgram import kgram, similarity 
app = Flask (__name__)

@app.route('/')
def index():
	return render_template('index.php')

@app.route('/result')
def result():
	a = request.args.get('text1')
	b = request.args.get('text2')

	t1 = kgram(a)
	t2 = kgram(b)

	return  str(similarity(t1,t2))
