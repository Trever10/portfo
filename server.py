from flask import Flask, render_template, request, send_from_directory, redirect
from markupsafe import escape
import os, csv

app = Flask(__name__)

# decorator
@app.route('/')
def my_home():
    return render_template('index.html')

# link to pages using renter_template
@app.route('/<string:page_name>')
def goTo(page_name):
    return render_template(page_name)

# save user data to TXT file. 
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

# save user data to CSV file.
def write_to_csv(data):
    with open('database.csv', 'a', newline='') as csvfile:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# sent the data to the server
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            # data = request.form['email', 'subject', 'message']
            data = request.form.to_dict()
            
            # 1. data to txt
            write_to_file(data)

            # 2. save data to CSV
            write_to_csv(data)
            return redirect('/thankyou.html') 
        except: 
            return 'did not save to database'
    else:
        return 'wrong'



# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'static/assets/favicon.ico', mimetype='image/vnd.microsoft.icon')
        
