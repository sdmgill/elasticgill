from flask import Flask, render_template, flash, session,redirect,url_for

application=Flask(__name__)

@application.route('/')
def home():
    return render_template('home.html')


@application.route('/about')
def about():
    return render_template('about.html')


@application.route('/aws/glue')
def awsglue():
    return render_template('awsglue.html')


@application.route('/aws/emr')
def awsemr():
    return render_template('awsemr.html')

if __name__ == '__main__':
    application.run(debug=True)
    application.run(host='0.0.0.0')
