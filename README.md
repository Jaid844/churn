
# Churn Prediction
 Churn prediction, a vital application in the realm of customer relationship management, aims to forecast the likelihood of customers ending their association with a service or product. In this context, the dataset includes pertinent customer information such as CustomerID, Name, Age, Gender, and Location. Additionally, it incorporates factors like Subscription_Length_Months, Monthly_Bill, and Total_Usage_GB, which are crucial features for understanding customer behavior. The ultimate objective is to use this data to predict the Churn status, indicating whether a customer is likely to leave or stay with the service. By applying machine learning algorithms to such datasets, businesses can proactively identify at-risk customers, enabling them to tailor retention strategies and ultimately minimize churn, thus fostering customer loyalty and business sustainability.
For Deployment use this link

 
https://churn-aoiz.onrender.com
![Screenshot 2023-10-14 125026](https://github.com/Jaid844/churn/assets/112820053/6b64575f-e3ed-4c71-88b4-e53a0f759948)


![Screenshot 2023-10-14 125222](https://github.com/Jaid844/churn/assets/112820053/5a30a1c5-5619-4c7b-adcd-ceb4557c353a)

## Dataset
The dataset used for training and testing the Kaggle website 

## Features
The features or attributes considered for Churn Prediction are churned(1) or not (0).
## Model Training
In this machine learning workflow, two distinct algorithms, Decision Trees and k-Nearest Neighbors (KNN), have been trained and evaluated for classification or regression tasks. To further optimize the predictive power of these models and tailor them to the specific characteristics of the data, a clustering step has been introduced. Clustering techniques,  K-Means, is applied to group similar data points together. The key innovation lies in the selection of the most appropriate algorithm for each cluster. By calculating the accuracy of both Decision Trees and KNN on the training data within each cluster, the algorithm with the highest performance is chosen. When new, unlabeled data arrives, it is assigned to a cluster based on the clustering model. Subsequently, the algorithm pre-selected for that cluster during the training phase is applied to make predictions for the new data points. Regular monitoring and re-evaluation ensure the adaptability and continued effectiveness of this dynamic modeling approach, which can be deployed in production environments to maximize predictive accuracy across various data clusters.

The training process involves:

Data preprocessing: Cleaning the dataset, handling missing values, and performing feature encoding or scaling if required.
Splitting the dataset: Dividing the dataset into training and test sets for model evaluation.

Model training: Training the chosen model using the training dataset.
Model evaluation: Assessing the performance of the trained model using evaluation metrics such as accuracy, precision, recall, or F1 score.
## Docker Containerization 
I have  containerize the app with base image of ubuntu linux
This Dockerfile is a set of instructions used to create a Docker image. It starts with the base image "ubuntu:latest," which is the latest Ubuntu operating system. The subsequent commands are executed in order to set up the environment.The Dockerfile defines the environment, dependencies, and the entry point for your Python application, making it easier to package and distribute your application with all its requirements

![Screenshot 2023-10-14 131100](https://github.com/Jaid844/churn/assets/112820053/1c416aa6-0009-4cb3-a5e2-b6bc92cddc2b)
## Circle ci 
![Screenshot 2023-10-14 130324](https://github.com/Jaid844/churn/assets/112820053/5bf1b89d-e029-4961-afea-f8306b31fc0e)

After each commits a automatic CI CD  will work  for Machine learning app

A test case has been written for machine learning model ,to check the model working 
![Screenshot 2023-10-14 130603](https://github.com/Jaid844/churn/assets/112820053/fa2525ec-52c9-4438-8b75-307c01bfcdd2)

## Technology Used
Python ,Flask,scikit-learn,Gunicorn
## How to Get Started

## Clone the Project

You can also use this project in your system by following thses simple steps -:

```bash
https://github.com/Jaid844/churn.git
```

## Install the requirements -
```bash
pip install -r requirements.txt
```

## For Docker 
For building images from docker container use this command
```bash
docker pull zaid683/churn
```



## Run the main.py file
```bash
python main.py
```

## You are done Good to go
## Authors

- [Muhammad Jaid]()


## Licence
This project is licensed under the MIT License, permitting open-source contributions and usage.

Feel free to tailor and expand upon this introduction based on the specific details and objectives of your mushroom classification project.