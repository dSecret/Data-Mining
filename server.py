import os.path

from flask import Flask, Response


# To load the saved module
import pickle

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')


@app.route('/', methods=('GET'))
def hompage():
  content = get_file('jenkins_analytics.html')
  return Response(content, mimetype="text/html")
  
@app.route('/predict', methods=('POST'))
def contact():
  # load the model from disk
  loaded_model = pickle.load(open(filename, 'rb'))
  result = loaded_model.score(X_test, Y_test)
