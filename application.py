from flask import Flask, render_template, flash, session,redirect,url_for

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/aws/glue')
def awsglue():
    return render_template('awsglue.html')


@app.route('/aws/emr')
def awsemr():
    return render_template('awsemr.html')

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')
