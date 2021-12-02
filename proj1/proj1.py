from flask import Flask,render_template,url_for,request,redirect,flash
from flask_mail import Mail, Message
import csv,os,pandas as pd
from werkzeug.utils import secure_filename
import helper
app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'prasanthkanakala481@gmail.com'
app.config['MAIL_PASSWORD'] = 'Prasanth@313'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
dict_bool = {
    'master_response': '',
    'responses_response': '',
    'positive_response':'',
    'negative_response': ''
}
sample_input_path = "./sample_input"
sample_output_path = "./sample_output"
correct_marks,wrg_marks = 0,0

app.secret_key= b'Prasanth@77777'

@app.route('/RollNo',methods=['GET','POST'])
def rollno():
    if not handle_cases(request):
        return redirect(url_for('index')) 
    if request.form.get('positive')!='':
        crt_marks = float(request.form.get('positive'))  
    if request.form.get('negative')!='':
        wrg_marks = float(request.form.get('negative'))
    helper.generate_marksheet(crt_marks,wrg_marks)
    dict_bool["rollno_response"] = "Generated Successfully"  
    return redirect(url_for('index'))

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html',data = dict_bool)

@app.route('/response',methods=['GET','POST'])
def response():
    FileObject = request.files.get("response")
    handle_file_save(FileObject,"responses.csv","responses_response")
    return redirect(url_for('index'))

def handle_cases(request):
    if not os.path.exists(os.path.join(sample_input_path,"master_roll.csv")):
        dict_bool["rollno_response"] = "You have not Uploaded master_roll.csv"
        return False
    if not os.path.exists(os.path.join(sample_input_path,"responses.csv")):
        dict_bool["rollno_response"] = "You have not Uploaded responses.csv"
        return False
    if request.form.get('positive')=='':
        dict_bool["positive_response"] = "This field is required"
        return False
    if request.form.get('negative')=='':
        dict_bool["negative_response"] = "This field is required"
        return False

    return True
    
def handle_file_save(FileObject,req_file_name,req_resp_name):
    if not FileObject.filename:
        dict_bool[f"{req_resp_name}"] = "Didn't upload any file."
        return   
    name_file = FileObject.filename
    if name_file!=req_file_name:
        dict_bool[f"{req_resp_name}"] = "Uploaded a wrong file..plz Upload {}".format(req_file_name)
        return 
    sample_input= os.path.join(os.getcwd(),"sample_input")
    os.makedirs(sample_input,exist_ok = True)
    if os.path.exists(f"./sample_input/{name_file}"):
        os.remove(f"./sample_input/{name_file}")
    filename = secure_filename(name_file)
    FileObject.save(os.path.join(sample_input_path,filename))  
    dict_bool[f"{req_resp_name}"] = "Uploaded Successfully"
    return 


#@app.route('/',methods=['GET'])
#def index():
#    return render_template('index.html',data = dict_bool)

@app.route('/master',methods=['GET','POST'])
def master():
    if request.method=="POST":
        FileObject = request.files.get("master")
        handle_file_save(FileObject,"master_roll.csv","master_response")
    return redirect(url_for('index'))

#@app.route('/response',methods=['GET','POST'])
#def response():
#    FileObject = request.files.get("response")
#    handle_file_save(FileObject,"responses.csv","responses_response")
#    return redirect(url_for('index')) 


#@app.route('/RollNo',methods=['GET','POST'])
#def rollno():
#    if not handle_cases(request):
#        return redirect(url_for('index')) 
#    if request.form.get('positive')!='':
#        crt_marks = float(request.form.get('positive'))  
#    if request.form.get('negative')!='':
#        wrg_marks = float(request.form.get('negative'))
#    helper.generate_marksheet(crt_marks,wrg_marks)
#    dict_bool["rollno_response"] = "Generated Successfully"  
#    return redirect(url_for('index'))


@app.route('/concise',methods=['GET','POST'])
def concise():
    if not handle_cases(request):
        return redirect(url_for('index'))
    helper.generate_concise_marksheet()
    dict_bool["concise_response"] = "Generated Successfully"
    return redirect(url_for('index'))


@app.route('/sendemail',methods=['GET','POST'])
def send_email():
    files = os.listdir('sample_output\marksheet')
    roll_email_list = helper.get_roll_email()
    for roll_no,email1,email2 in roll_email_list:
        msg = Message('Your marks',sender ='prasanthkanakala481@gmail.com',recipients = [email1,email2])
        msg.body = 'Your Quiz Marks'
        with app.open_resource("sample_output\marksheet\{}.xlsx".format(roll_no)) as fp:  
            msg.attach(f"{roll_no}", "application/xlsx", fp.read()) 
            mail.send(msg)
            print(f"Success mail sent{roll_no}")
    dict_bool["email_response"] = "Email Sent Successfully"
    return redirect(url_for('index')) 


if __name__ == "__main__":
    app.run(debug=True)