from flask import Flask, render_template, request 
from odds import get_odds
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#group is sport name in JSON
@app.route('/odds')
def get_odds():
    group = request.args.get('group')
    odds_data = get_odds(group)
    return render_template(
        'odds.html', 
        title = odds_data["group"],
        has_outrights=odds_data["description"]["has_outrights"],
        description=odds_data["title"]["active"],
        )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port = 8000)
