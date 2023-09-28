from Data import Data
from file_operation import file_op
from preprocess import preprocess
from cluster.clustering import Cluster
from sklearn.model_selection import  train_test_split
import numpy as np
from tuner import model_finder


class training:
    def __init__(self):
        self.data=Data()
        self.preporocess=preprocess()
        self.file_op=file_op()
        self.model=model_finder()
        self.cluster=Cluster()

    def train(self):
        data=self.data.datgetter()
        data=self.preporocess.encode_cat(data)
        data=self.preporocess.scale_numerical(data)
        X=data.drop(['Churn'],axis=1)
        y=data['Churn']
        number_of_cluster=self.cluster.elbowplot(X)
        X=self.cluster.create_cluster(X,number_of_cluster)
        X['Labels'] = y
        list_of_clusters = X['Cluster'].unique()
        for i in list_of_clusters:
            cluster_data = X[X['Cluster'] == i]
            cluster_features = cluster_data.drop(['Labels', 'Cluster'], axis=1)
            cluster_label = cluster_data['Labels']
            X_train, X_test, y_train, y_test = train_test_split(cluster_features, cluster_label, test_size=1 / 3,
                                                                random_state=50)
            best_model_name, best_model=self.model.get_best_model(X_train,y_train,X_test,y_test)
            save_model = self.file_op.save_model(best_model, best_model_name + str(i))










c=training()
c.train()










