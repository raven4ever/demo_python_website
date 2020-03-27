import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_pages(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.csv', newline='', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            return redirect('/thankyou.html')
        except:
            return 'Something went wrong!'
    else:
        return 'something went wrong'


if __name__ == '__main__':
    app.run()
