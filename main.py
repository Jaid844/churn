from flask import Flask, request, render_template
from  flask import Response
import os
from flask_cors import CORS, cross_origin
from flask import Flask,request,app,jsonify,url_for,render_template
import pandas as pd
from preprocess import preprocess
from file_operation import file_op
import numpy as np

c=preprocess()
f=file_op()
app = Flask(__name__)
CORS(app)

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/predict', methods=['POST'])
@cross_origin()
def predict_route():
    customer_id = int(request.form['CustomerID'])
    name = str(request.form['Name'])
    age = int(request.form['Age'])
    gender = str(request.form['Gender'])
    location = str(request.form['Location'])
    subscription_length = int(request.form['Subscription_Length_Months'])
    monthly_bill = int(request.form['Monthly_Bill'])
    total_usage = int(request.form['Total_Usage_GB'])
    data = {
        'CustomerID': [customer_id],
        'Name': [name],
        'Age': [age],
        'Gender': [gender],
        'Location': [location],
        'Subscription_Length_Months': [subscription_length],
        'Monthly_Bill': [monthly_bill],
        'Total_Usage_GB': [total_usage]
    }
    df = pd.DataFrame.from_dict(data)
    columns_to_drop = ['CustomerID', 'Name']
    df = df.drop(columns=columns_to_drop, errors='ignore')
    df=c.encode_cat(df)
    print(df)
    df=c.scale_numerical(df)
    kmeans=f.load_model('KMeans')
    clusters = kmeans.predict(df)
    df['clusters'] = clusters
    for i in clusters:
       # cluster_data = data[data['clusters'] == i]
        #cluster_data = cluster_data.drop(['clusters'], axis=1)
        df=df.drop(columns='clusters')
        #data_array = df.to_numpy()
        #reshaped_data = data_array.reshape(1, -1)\
        df = df.to_numpy()
        model_name = f.find_correct_model(i)
        reshaped_data = df.reshape(1, -1)
        model = f.load_model(model_name)
        result = model.predict(reshaped_data)
    #result = (model.predict(cluster_data))
        print(result)
    return render_template("home.html", prediction_text="The Prediction of churn is {}".format(result))













port = int(os.getenv("PORT",5000))
if __name__ == "__main__":
    app.run(port=port,debug=True,host="0.0.0.0")




