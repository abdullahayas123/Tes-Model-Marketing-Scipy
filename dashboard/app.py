import joblib
import pandas as pd
from flask import Flask, render_template, request

'''
https://getbootstrap.com
'''

# Opsi 1 - Klasik - Statis
'''
- Dataset 
df.to_html('dataset.html')

- Visualizasi
plt.savefig

- Prediction
Model Import
'''

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dataset')
def df():
    return render_template('data.html')

@app.route('/visualize')
def vis():
    return render_template('viz.html')

@app.route('/prediction')
def pred():
    return render_template('pred.html')

@app.route('/hasil', methods=['POST'])
def result():
    if request.method == 'POST':
        input = request.form
        #id = int(input['angka'])
        '''
        lim = int(input['limit_bal'])
        sex = int(input['sex'])
        ed = int(input['education'])
        mar = int(input['marriage'])
        age = int(input['age'])
        pmt0 = int(input['pay_0'])
        pmt2 = int(input['pay_2'])
        pmt3 = int(input['pay_3'])
        pmt4 = int(input['pay_4'])
        pmt5 = int(input['pay_5'])
        pmt6 = int(input['pay_6'])
        bill1 = int(input['bill_amt1'])
        bill2 = int(input['bill_amt2'])
        bill3 = int(input['bill_amt3'])
        bill4 = int(input['bill_amt4'])
        bill5 = int(input['bill_amt5'])
        bill6 = int(input['bill_amt6'])
        pay1 = int(input['pay_amt1'])
        pay2 = int(input['pay_amt2'])
        pay3 = int(input['pay_amt3'])
        pay4 = int(input['pay_amt4'])
        pay5 = int(input['pay_amt5'])
        pay6 = int(input['pay_amt6'])
        '''
        #prediksi = Model.predict([[id,sex,ed,mar,pmt0,pmt2,pmt3,pmt4,pmt5,pmt6,bill1,bill2,bill3,bill4,bill5,bill6,pay1,pay2,pay3,pay4,pay5,pay6]])[0]
        
        simpan = [
            int(input['age']),
            str(input['job']),
            str(input['mar']),
            str(input['edu']),
            str(input['cre']),
            str(input['hou']),
            str(input['per']),
            str(input['con']),
            str(input['mon']),
            str(input['day']),
            int(input['pdays']),
            int(input['prev']),
            str(input['pout']),
            float(input['var']),
            float(input['pri']),
            float(input['conf']),
            float(input['eur']),
            float(input['num'])
        ]

        hasil = pd.DataFrame(data=[simpan], columns=['age', 'job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'pdays', 'previous', 'poutcome', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed'])
        
        
        hasil['education'] = hasil['education'].map({'basic.4y':1
                              , 'basic.6y':2
                              , 'basic.9y' :3
                              , "high.school":4
                              , "university.degree":5
                              , 'professional.course':6
                              , 'illiterate':0
                              , 'unknown':0
                             })
        print(hasil)
        '''
        df = pd.read_excel('CreditCard.xls')
        a = df.iloc[0]
        df = df[1:]
        df.columns=a
        df.set_index('ID', inplace=True)
        df.columns = df.columns.str.lower()
        df = df.astype('int')
        '''
        # hasil = hasil.astype('int')
        # print(hasil.dtypes)
        # df.drop(columns='default payment next month', inplace=True)
        #print(df.dtypes)
        # df = pd.concat([df,hasil], axis=0)
        # print(df.dtypes)
        prediksi = Model.predict(hasil)
        if prediksi == 1:
            prediksi = 'Berhasil'
        else:
            prediksi = 'Ditolak'
        prob = Model.predict_proba(hasil)
        prob0 = round(prob[0][0], 2)
        prob1 = round(prob[0][1], 2)
    return render_template('result.html', data=input, pred=prediksi, proba=[prob0, prob1])

'''
<br>Age : <input type="number" step="1" name="age">
        <br>Job : 
        <select name="job">
          <option value="housemaid">Housemaid</option>
          <option value="services">Services</option>
          <option value="admin.">Admin</option>
          <option value="blue-collar">Blue-Collar</option>
          <option value="technician">Technician</option>
          <option value="retired">Retired</option>
          <option value="management">Management</option>
          <option value="unemployed">Technician</option>
          <option value="self-employed">Self-employed</option>
          <option value="unknown">Unknown</option>
          <option value="entrepreneur">Entepreneur</option>
          <option value="student">Student</option>
        </select> 

        <br>Marital : 
        <select name="mar">
          <option value="married">Married</option>
          <option value="single">Single</option>
          <option value="divorced">Divorced</option>
          <option value="unknown">Unknown</option>
        </select> 

        <br>Education : 
        <select name="edu">
          <option value="illiterate">Illiterate</option>
          <option value="basic.4y">Basic 4 Years</option>
          <option value="basic.6y">Basic 6 Years</option>
          <option value="basic.9y">Basic 9 Years</option>
          <option value="high.school">High School</option>
          <option value="university.degree">University Degree</option>
          <option value="professional.course">Professional Course</option>
          <option value="unknown">Unknown</option>
        </select> 

        <br>Credit in Default :
        <select name="cre">
          <option value="yes">Yes</option>
          <option value="no">No</option>
          <option value="unknown">Unknown</option>
        </select> 

        <br>Housing Loan :
        <select name="hou">
          <option value="yes">Yes</option>
          <option value="no">No</option>
          <option value="unknown">Unknown</option>
        </select> 

        <br>Personal Loan :
        <select name="per">
          <option value="yes">Yes</option>
          <option value="no">No</option>
          <option value="unknown">Unknown</option>
        </select> 

        <br>Contact Communication Type :
        <select name="con">
          <option value="telephone">Telephone</option>
          <option value="cellular">Cellular</option>
        </select> 

        <br>Month (Last Contact ) : 
        <select name="mon">
          <option value="mar">March</option>
          <option value="apr">April</option>
          <option value="may">May</option>
          <option value="jun">June</option>
          <option value="jul">July</option>
          <option value="aug">August</option>
          <option value="sep">September</option>
          <option value="oct">October</option>
          <option value="nov">November</option>
          <option value="dec">December</option>
        </select> 

        <br>Day of Week (Last Contact) : 
        <select name="day">
          <option value="mon">Monday</option>
          <option value="tue">Tuesday</option>
          <option value="wed">Wednesday</option>
          <option value="thu">Thursday</option>
          <option value="fri">Friday</option>
          <option value="sat">Saturday</option>
          <option value="sun">Sunday</option>
        </select> 

        <br>Last Contact From Previous Campaign : <input type="number" name="pdays">

        <br>Previous Number of Contact : <input type="number" name="prev">

        <br>Outcome from Previous Campaign : 
        <select name="pout">
          <option value="nonexistent">Nonexistent</option>
          <option value="failure">Failure</option>
          <option value="success">Success</option>
        </select> 

        <br>Employee Variation Rate : <input type="number" name="var">

        <br>Consumer Price Index : <input type="number" name="pri">

        <br>Consumer Confidence Index : <input type="number" name="conf">

        <br>Euribor 3 Months Rate : <input type="number" name="eur">

        <br>Number of Employees : <input type="number" name="num">

'''




if __name__ == '__main__':
    pass
    Model = joblib.load(filename='dashboard\Model_LR.jbl')
    app.run(debug=True)