from flask import Flask, render_template, url_for, request, redirect
import requests
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('./index.html')


@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name)

# --------------- Write to Text File ------------


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email}, {subject}, {message}')

# --------------- Write to CSV File ------------


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:  # database2
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # print(f'\n {email}, {subject}, {message}')
        csv_writer = csv.writer(database2, delimiter=',',  lineterminator='\n',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # conver the form data into dict
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again'
