import markdown
import json

from flask import Flask
from flask import request
from flask import Response
from flask import render_template
from flask import Markup
from inky import render

app = Flask(__name__)
app.display = []


@app.route("/")
def index():
    content = open('README.md', 'r').read()
    content = Markup(markdown.markdown(content))
    return render_template('index.html', **locals())


@app.route("/paper", methods=['PATCH'])
def lights():
    try:
        app.display = json.loads(request.data.decode('utf-8'))['matrix']
    except KeyError:
        app.display = [[]]

    render(app.display)

    return Response(
        json.dumps({'success': True}), status=200, mimetype='application/json'
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0')
