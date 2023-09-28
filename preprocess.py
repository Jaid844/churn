import pandas as pd
from sklearn.preprocessing import StandardScaler
from Data import Data
import csv


class preprocess:
    def __init__(self):
        self.data=Data()

    def removecolumn(self, data, column):
        self.column = column
        self.data = data
        try:
            self.file = open('Training_Logs/Preprocess', 'w')
            usefuldata = self.data.drop(self.column, axis=1)

            self.file.close()
            return usefuldata
        except Exception as e:
            raise e

    def sepratelabelandfeature(self, data, columns):
        self.data = data
        self.column = columns
        try:

            self.X = self.data.drop(labels=self.column, axis=1)
            self.Y = self.data[self.column]
            return self.X, self.Y
        except Exception as e:
             raise e



    def encode_cat(self,data):
        self.data= data
        self.cat_df = self.data.select_dtypes(include=["object"]).copy()
        #expected_columns=['Gender_Male','Gender_Female','Location_Houston','Location_Los Angeles','Location_Miami','Location_New York','Location_Chicago']

        try:
            self.cat_df.drop(columns=['Name'],inplace=True)
            self.data.drop(columns=['CustomerID'], inplace=True)

        except:
            pass

        for t in self.cat_df:
            self.cat_df = pd.get_dummies(self.cat_df, columns=[t],prefix=[t], drop_first=False, dtype=int)
       # self.cat_df = self.cat_df[expected_columns]
        #self.data.drop(columns=self.data.select_dtypes(include=['object']).columns, inplace=True)
        #for column in self.data.columns:
            #user_data_dict[column + '_' + self.data[column].iloc[0]] = 1

        if 'Gender' in self.data.columns:
          if 'Female' in self.data['Gender'].values:
            self.cat_df['Gender_Male'] = 0
            self.cat_df['Gender_Female'] = 1
          else:
             self.cat_df['Gender_Male'] = 1
             self.cat_df['Gender_Female'] = 0
        if 'Location' in self.data.columns:
          if 'New York' in self.data['Location'].values:
              self.cat_df['Location_New York'] = 1
              self.cat_df['Location_Miami'] = 0
              self.cat_df['Location_Houston'] = 0
              self.cat_df['Location_Los Angeles'] = 0
              self.cat_df['Location_Chicago'] = 0
          elif 'Miami' in self.data['Location'].values:
              self.cat_df['Location_Miami'] = 1
              self.cat_df['Location_New York'] = 0
              self.cat_df['Location_Los Angeles'] = 0
              self.cat_df['Location_Houston'] = 0
              self.cat_df['Location_Chicago'] = 0
          elif 'Houston' in self.data['Location'].values:
              self.cat_df['Location_New York'] = 0
              self.cat_df['Location_Miami'] = 0
              self.cat_df['Location_Houston'] = 1
              self.cat_df['Location_Los Angeles'] = 0
              self.cat_df['Location_Chicago'] = 0
          else:
              self.cat_df['Location_New York'] = 0
              self.cat_df['Location_Miami'] = 0
              self.cat_df['Location_Houston'] = 0
              self.cat_df['Location_Los Angeles'] = 1
              self.cat_df['Location_Chicago'] = 0






       # cities = ['New York', 'Chicago', 'Miami', 'Houston']
        #for city in cities:
            #if city in self.data.columns:
               # self.cat_df['Location_' + city] = 1
            #else:
               # self.cat_df['Location_' + city] = 0

        self.data.drop(columns=self.data.select_dtypes(include=['object']).columns, inplace=True)
        self.data = pd.concat([self.cat_df, self.data], axis=1)
        return self.data



    def scale_numerical(self,data):
        self.data=data
        try:
            standardScaler = StandardScaler()
            columns_to_fit = ['Subscription_Length_Months', 'Monthly_Bill', 'Total_Usage_GB']
            self.data[columns_to_fit] = standardScaler.fit_transform(self.data[columns_to_fit])
            return self.data

        except Exception as e:
            raise e

