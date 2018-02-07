import markdown
from flask import Flask
from flask import request
from flask import Response
from flask import render_template
from flask import Markup
import json
from support import render

app = Flask(__name__)
app.matrix = {}


@app.route("/")
def index():
    content = open('README.md', 'r').read()
    content = Markup(markdown.markdown(content))
    return render_template('index.html', **locals())


@app.route("/lights", methods=['GET', 'PATCH'])
def lights():
    if request.method == 'GET':
        return Response(json.dumps({'matrix': app.matrix}), status=200, mimetype='application/json')

    else:
        try:
            app.matrix = json.loads(request.data)['matrix']
        except KeyError:
            app.matrix = [[]]

        try:
            decimals = json.loads(request.data)['decimals']
        except KeyError:
            decimals = []

        render(app.matrix, decimals)

        return Response(json.dumps({'success': True}), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
