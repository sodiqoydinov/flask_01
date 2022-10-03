from flask import Flask, render_template, request, redirect
import pickle

app = Flask(__name__)


users_data = []

@app.route('/', methods=['GET','POST'])
def about():
	# if request.method=="POST":
	# 	return request.form.get('my')
	return render_template('main.html')


@app.route('/testform', methods=['POST','GET'])
def testform():
	ism=request.form.get('ism')
	familiya = request.form.get('familiya')
	ism2 = request.form.get('ism2')
	ambul_kart = request.form.get('ambul_kart')
	tel = request.form.get('tel')
	vaqt = request.form.get('vaqt')
	if not ism or not familiya or not ism2 or not ambul_kart or not tel or not vaqt:
		return render_template('fail1.html',ism=ism, familiya=familiya,ism2=ism2,ambul_kart=ambul_kart,tel=tel,vaqt=vaqt)
	return render_template('next1.html',ism=ism, familiya=familiya,ism2=ism2,ambul_kart=ambul_kart,tel=tel,vaqt=vaqt)
	# users_data.append(f"{ism},{familiya},{ism2},{ambul_kart},{tel},{vaqt}")

	
	return render_template('testform.html')
	
@app.route('/test', methods=['GET','POST'])
def test():

	return render_template('test.html')

@app.route('/users_table')

def users_table():
	return render_template('users_table.html')



@app.route('/result1', methods=["POST"])

def result1():
	s1 = request.form.get('inlineRadioOptions')
	s2 = request.form.get('inlineRadioOptions2')
	s3 = request.form.get('inlineRadioOptions3')
	s4 = request.form.get('inlineRadioOptions4')
	s5 = request.form.get('inlineRadioOptions5')
	s6 = request.form.get('inlineRadioOptions6')
	return render_template('result_page.html',s1=s1,s2=s2,s3=s3,s4=s4,s5=s5,s6=s6)