import markdown
from flask import Flask
from flask import request
from flask import Response
from flask import render_template
from flask import Markup
import json
from support import render

app = Flask(__name__)
app.matrix = []
app.decimals = []


@app.route("/")
def index():
    content = open('README.md', 'r').read()
    content = Markup(markdown.markdown(content))
    return render_template('index.html', **locals())


@app.route("/lights", methods=['GET', 'PATCH'])
def lights():
    if request.method == 'GET':
        return Response(json.dumps({'matrix': app.matrix, 'decimals': app.decimals}), status=200, mimetype='application/json')

    else:
        try:
            app.matrix = json.loads(request.data.decode('utf-8'))['matrix']

        except KeyError:
            app.matrix = [[]]

        try:
            app.decimals = json.loads(request.data.decode('utf-8'))['decimals']
        except KeyError:
            app.decimals = []

        render(app.matrix, app.decimals)

        return Response(json.dumps({'success': True}), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
