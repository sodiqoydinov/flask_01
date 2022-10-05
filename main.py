from flask import Flask, render_template, request, redirect

app = Flask(__name__)

global users_data
users_data = []

@app.route('/', methods=['GET','POST'])
def about():
	# if request.method=="POST":
	# 	return request.form.get('my')
	return render_template('testform.html')


@app.route('/testform', methods=['POST','GET'])
def testform():
	fio=request.form.get('fio')
	vaqt1 = request.form.get('vaqt1')
	ambul_kart = request.form.get('ambul_kart')
	uchastok = request.form.get('uchastok')
	tel = request.form.get('tel')
	vaqt2 = request.form.get('vaqt2')
	if not fio or not vaqt1 or not ambul_kart or not tel or not vaqt2 or not uchastok:
		return render_template('fail1.html',fio=fio, vaqt1=vaqt1,ambul_kart=ambul_kart,tel=tel,vaqt2=vaqt2,uchastok=uchastok)
	return render_template('next1.html',fio=fio, vaqt1=vaqt1,ambul_kart=ambul_kart,tel=tel,vaqt2=vaqt2,uchastok=uchastok)
	
	users_data.append(f"{ism},{familiya},{ism2},{ambul_kart},{tel},{vaqt}")

@app.route('/fail1', methods=['POST','GET'])
def failform():
	fio=request.form.get('fio')
	vaqt1 = request.form.get('vaqt1')
	ambul_kart = request.form.get('ambul_kart')
	uchastok = request.form.get('uchastok')
	tel = request.form.get('tel')
	vaqt2 = request.form.get('vaqt2')

	return render_template('next1.html',fio=fio, vaqt1=vaqt1,ambul_kart=ambul_kart,tel=tel,vaqt2=vaqt2,uchastok=uchastok)


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
	s7 = request.form.get('inlineRadioOptions7')
	s8 = request.form.get('inlineRadioOptions8')
	s9 = request.form.get('inlineRadioOptions9')
	s10 = request.form.get('inlineRadioOptions10')
	s11 = request.form.get('inlineRadioOptions11')
	s12 = request.form.get('inlineRadioOptions12')
	return render_template('result_page.html',s1=s1,s2=s2,s3=s3,s4=s4,s5=s5,s6=s6,s7=s7,s8=s8,s9=s9,s10=s10,s11=s11,s12=s12)