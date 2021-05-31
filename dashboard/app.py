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
        #prediksi = Model.predict([[id,sex,ed,mar,pmt0,pmt2,pmt3,pmt4,pmt5,pmt6,bill1,bill2,bill3,bill4,bill5,bill6,pay1,pay2,pay3,pay4,pay5,pay6]])[0]
        hasil = pd.DataFrame(data=[input], columns=['limit_bal', 'sex', 'education', 'marriage', 'age', 'pay_0', 'pay_2', 'pay_3', 'pay_4', 'pay_5', 'pay_6', 'bill_amt1', 'bill_amt2', 'bill_amt3', 'bill_amt4', 'bill_amt5', 'bill_amt6', 'pay_amt1', 'pay_amt2', 'pay_amt3', 'pay_amt4', 'pay_amt5', 'pay_amt6'])
        df = pd.read_excel('CreditCard.xls')
        a = df.iloc[0]
        df = df[1:]
        df.columns=a
        df.set_index('ID', inplace=True)
        df.columns = df.columns.str.lower()
        df = df.astype('int')
        hasil = hasil.astype('int')
        # print(hasil.dtypes)
        df.drop(columns='default payment next month', inplace=True)
        #print(df.dtypes)
        df = pd.concat([df,hasil], axis=0)
        # print(df.dtypes)
        df['education'][df['education'] == 0] = 4
        df['education'][df['education'] >=4] = 4
        df['marriage'][df['marriage'] == 0] = 3
        df['pay_0'][df['pay_0'] == -2] = -1
        df['pay_2'][df['pay_2'] == -2] = -1
        df['pay_3'][df['pay_3'] == -2] = -1
        df['pay_4'][df['pay_4'] == -2] = -1
        df['pay_5'][df['pay_5'] == -2] = -1
        df['pay_6'][df['pay_6'] == -2] = -1
        df = pd.get_dummies(data=df, columns=['sex', 'education', 'marriage', 'pay_0', 'pay_2', 'pay_3', 'pay_4', 'pay_5', 'pay_6'])
        print(df.columns)
        hasil = df.iloc[[30000]]
        prediksi = Model.predict(hasil)
    return render_template('result.html', data=input, pred=prediksi)

'''
 <br>Limit Balance : <input type="number" step="1000" name="limit_bal">
        <br>Sex : <input type="number" name="sex">
        <br>Education : <input type="number" name="education">
        <br>Marriage : <input type="number" name="marriage">
        <br>Payment 0 : <input type="number" name="pay_0">
        <br>Payment 2 : <input type="number" name="pay_2">
        <br>Payment 3 : <input type="number" name="pay_3">
        <br>Payment 4 : <input type="number" name="pay_4">
        <br>Payment 5 : <input type="number" name="pay_5">
        <br>Payment 6 : <input type="number" name="pay_6">
        <br>Bill Amount 1 : <input type="number" name="bill_amt1">
        <br>Bill Amount 2 : <input type="number" name="bill_amt2">
        <br>Bill Amount 3 : <input type="number" name="bill_amt3">
        <br>Bill Amount 4 : <input type="number" name="bill_amt4">
        <br>Bill Amount 5 : <input type="number" name="bill_amt5">
        <br>Bill Amount 6 : <input type="number" name="bill_amt6">
        <br>Payment Amount 1 : <input type="number" name="bill_amt1">
        <br>Payment Amount 2 : <input type="number" name="bill_amt2">
        <br>Payment Amount 3 : <input type="number" name="bill_amt3">
        <br>Payment Amount 4 : <input type="number" name="bill_amt4">
        <br>Payment Amount 5 : <input type="number" name="bill_amt5">
        <br>Payment Amount 6 : <input type="number" name="bill_amt6">
'''




if __name__ == '__main__':
    pass
    Model = joblib.load(filename='dashboard\Model_LR.jbl')
    app.run(debug=True)