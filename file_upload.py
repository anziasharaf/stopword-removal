from flask import Flask, render_template, request,send_file
from werkzeug import secure_filename
import stop_removal
app = Flask(__name__)

@app.route('/')
def upload():
   return render_template('upload2.html')
#this function is to upload input file	
@app.route('/uploader', methods = ['POST','GET'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
      		#print(f.filename)
		result=stop_removal.main_program(f.filename)
		print("printing result in flask")
		print(result)
		return  result
	
#this function is to download the output file
@app.route("/download",methods = ['POST','GET'])
def download():
	with open("out.txt","r") as file:
		print(file)
		return send_file("out.txt", as_attachment="True",cache_timeout=0)
if __name__ == '__main__':
   app.run('0.0.0.0',debug = True)
