import markdown
from flask import Flask
from flask import request
from flask import render_template
from flask import Markup
import json

app = Flask(__name__)

from support import render

@app.route("/")
def index():
  content = open('README.md', 'r').read()
  content = Markup(markdown.markdown(content))
  return render_template('index.html', **locals())

@app.route("/lights", methods=['PATCH'])
def lights():
    try:
        matrix = json.loads(request.data)['matrix']
    except KeyError:
        matrix = [[]]

    try:
        decimals = json.loads(request.data)['decimals']
    except KeyError:
        decimals = []

    render(matrix, decimals)

    status = {'success': True}, \
             200, \
             {'ContentType': 'application/json'}

    return json.dumps(status)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
