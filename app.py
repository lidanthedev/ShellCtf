from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Handle form submission
    text = request.args.get('text')
    if not text:
        return render_template("home.html", result="")
    # Do something with the submitted text
    resp = eval(text)

    return render_template("home.html", result=resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
