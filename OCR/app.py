import os 
from flask import Flask,render_template,request

from ocr_try import ocr_try
UPLOAD_FOLDER='/static/uploads/'

ALLOWED_EXTENSIONS=set(['png','jpg','jpeg'])

app=Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')

def home_page():
    return render_template('index.html')

@app.route('/upload',methods=['GET','POST'])
def upload_page():
    if request.method == 'POST':

        if 'file' not in request.files:
            return render_template('upload.html',msg='No file selected !')
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html',msg='No file selected')

        if file and allowed_file(file.filename):
            extracted_text=ocr_try(file)
            return render_template('upload.html',msg="Sucessfully processed",extracted_text=extracted_text,img_src=UPLOAD_FOLDER + file.filename)

    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run()
