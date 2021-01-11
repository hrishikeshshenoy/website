from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')    
def hello_world2():
    return render_template('index.html')  

@app.route('/<page_name>')
def hello_world6(page_name):
    return render_template(page_name)

def write_to_data(data):
    with open('database.csv',mode='a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_bulla=csv.writer(database,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_bulla.writerow([email,subject,message])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=="POST":
        data=request.form.to_dict()
        write_to_data(data)
        return redirect('thankyou.html')
    else:
        return 'Something Went Wrong'    