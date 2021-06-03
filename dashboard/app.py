import joblib
import pandas as pd
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import seaborn as sns
import os
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

@app.route('/gambar', methods=['POST'])
def pic():
    strFile = "./dashboard/static/chart.png"
    df = pd.read_csv('bank-additional-full.csv', sep=';')
    plt.figure(figsize=(15,8))
    num_col = ['campaign', 'age', 'pdays', 'previous', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']
    if request.method == 'POST':
      input = request.form
      jumlah = str(input['jumlah'])
      kol1 = str(input['kolom1'])
      print(kol1)
      if jumlah == 'uni':
        if kol1 in num_col:
          sns.histplot(x=df[kol1])
          plt.legend()
          if os.path.isfile(strFile):
            os.remove(strFile) 
          plt.savefig(strFile)
          pass
        else:
          temp = pd.crosstab(index = df[kol1], columns = 'Sum')
          sns.barplot(data=temp.reset_index(), x=kol1, y='Sum')
          plt.legend()
          if os.path.isfile(strFile):
            os.remove(strFile) 
          plt.savefig(strFile)
          pass
      elif jumlah == 'multi':
        if kol1 in num_col:
          plt.figure(figsize = (20,6))
          plt.subplot(1,2,1)
          plt.hist(x = df[df['y']=='yes'][kol1],bins=15)
          # plt.title('Comparison Graph of Job Groups with Bank Deposit Subscribed as yes')
          # plt.xticks(rotation=45)
          plt.subplot(1,2,2)
          plt.hist(x = df[df['y']=='no'][kol1],color='r',bins=15)
          if os.path.isfile(strFile):
            os.remove(strFile) 
          plt.savefig(strFile)
          # plt.title('Comparison Graph of Job Groups with Bank Deposit Subscribed as no')
          # plt.xticks(rotation=45)
          plt.legend()
          pass
        else:
          plt.figure(figsize = (15,8))
          sns.countplot(x = kol1, data = df , hue = 'y')
          if os.path.isfile(strFile):
            os.remove(strFile) 
          plt.savefig(strFile)
          # plt.title('Comparison Graph of Contact Communication Type with Bank Deposit Subscribed')
          # plt.xticks(rotation=45)
          plt.legend()
    return render_template('viz.html')

@app.route('/hasil', methods=['POST'])
def result():
    if request.method == 'POST':
        input = request.form

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
        
        hasil['education'] = hasil['education'].map({
          'basic.4y':1
        , 'basic.6y':2
        , 'basic.9y' :3
        , "high.school":4
        , "university.degree":5
        , 'professional.course':6
        , 'illiterate':0
        , 'unknown':0
        })
        # print(hasil)

        prediksi = Model.predict(hasil)
        if prediksi == 1:
            prediksi = 'Berhasil'
        else:
            prediksi = 'Ditolak'
        prob = Model.predict_proba(hasil)
        prob0 = prob[0][0]
        prob1 = prob[0][1]
        print(prob0, prob1)
    return render_template('result.html', data=input, pred=prediksi, proba=[prob0, prob1])

if __name__ == '__main__':
    pass
    Model = joblib.load(filename='dashboard\Model_LR.jbl')
    app.run(debug=True)