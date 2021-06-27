from flask import Flask, render_template, url_for # import Flask

app = Flask(__name__)  # flask application object

@app.route('/')
@app.route('/index')  # view function, defines function for route
def index():
    return render_template('index.html', title="This is the title", text=["first",2,"banana"])

@app.route('/add')
def add():
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)  # will run website on localhost