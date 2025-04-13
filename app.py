from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
    return render_template("Main.html")

@app.route('/Timeline')
def timeline():  # put application's code here
    return render_template("Timeline.html")

@app.route('/Materials')
def materials():  # put application's code here
    return render_template("Materials.html")

@app.route('/Connections')
def connections():  # put application's code here
    return render_template("Connections.html")

@app.route('/Procedure')
def sources():  # put application's code here
    return render_template("Procedure.html")

if __name__ == '__main__':
    app.run()
