from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import  DecisionTreeClassifier
from sklearn.metrics import roc_auc_score,accuracy_score

class model_finder:
      def __init__(self):

          self.logictic=LogisticRegression(solver='liblinear')
          self.DT= DecisionTreeClassifier()
          self.knn=KNeighborsClassifier()


      def parms_for_log(self,train_X,train_Y):
          try:

              self.param_grid = {
            'penalty': ['l1', 'l2'],            # Regularization type
            'C': [0.001, 0.01, 0.1, 1, 10]     # Inverse of regularization strength
        }
              self.grid=GridSearchCV(estimator= self.logictic,param_grid=self.param_grid,cv=7,verbose=3)
              self.grid.fit(train_X,train_Y)

              self.penalty=self.grid.best_params_['penalty']
              self.C=self.grid.best_params_['C']
              self.model_logistic=LogisticRegression(C=self.C,penalty=self.penalty, solver='liblinear')
              self.model_logistic.fit(train_X,train_Y)

              return  self.model_logistic

          except Exception as e:
                raise e


      def param_for_decisontree(self,train_x,train_y):
          try:

              self.param_grid={'criterion':['gini', 'entropy', 'log_loss'],
                               'splitter':['best', 'random'],
                               'max_features':[ 'auto', 'sqrt', 'log2']}
              self.grid=GridSearchCV(estimator=self.DT,param_grid=self.param_grid,cv=7,verbose=3)
              self.grid.fit(train_x, train_y)
              self.citreion=self.grid.best_params_['criterion']
              self.splitter=self.grid.best_params_['splitter']
              self.model_DT=DecisionTreeClassifier(criterion=self.citreion,splitter=self.splitter)
              self.model_DT.fit(train_x,train_y)
              return self.model_DT
          except Exception as e:
              raise e

      def param_knn(self,train_x,train_y):
          try:
              param_grid = {
                  'n_neighbors': [3, 5, 7],  # You can adjust the values
                  'weights': ['uniform', 'distance'],
                  'metric': ['euclidean', 'manhattan'],
                  'algorithm':['auto', 'ball_tree', 'kd_tree', 'brute']
              }

              # Create a grid search object
              grid = GridSearchCV(estimator=self.knn, param_grid=param_grid, cv=5, verbose=3)

              # Fit the grid search to your data
              grid.fit(train_x, train_y)

              # Get the best hyperparameters
              self.best_n_neighbors = grid.best_params_['n_neighbors']
              self.best_weights = grid.best_params_['weights']
              self.best_metric = grid.best_params_['metric']
              self.model_knn = KNeighborsClassifier(
                  n_neighbors=self.best_n_neighbors,
                  weights=self.best_weights,
                  metric=self.best_metric
              )
              self.model_knn.fit(train_x, train_y)
              return self.model_knn
          except Exception as e:
              raise e




      def get_best_model(self,train_x,train_y,test_x,test_y):
          try:
              file_name = "custom_message.txt"
              self.Dt=self.param_for_decisontree(train_x,train_y)
              prediction_of_dt=self.Dt.predict(test_x)
              if len(test_y.unique())==1:
                   self.dt_score=accuracy_score(test_y,prediction_of_dt)
                   with open(file_name, 'a+') as file:
                       custom_message="score of Decisson Tree is "+str(self.dt_score)
                       file.write(custom_message)
              else:

                   self.dt_score=roc_auc_score(test_y,prediction_of_dt)
                   with open(file_name, 'a+') as file:
                       custom_message="score of Decisson Tree is "+str(self.dt_score)
                       file.write(custom_message)
              self.Kn=self.param_knn(train_x,train_y)
              prediction_of_Kn=self.Kn.predict(test_x)
              if len(test_y.unique()) == 1:

                  self.Kn_score = accuracy_score(test_y, prediction_of_Kn)
                  with open(file_name, 'a+') as file:
                      custom_message = "score of KNN is " + str(self.Kn_score)
                      file.write(custom_message)

              else:

                  self.Kn_score = roc_auc_score(test_y, prediction_of_Kn)
                  with open(file_name, 'a+') as file:
                      custom_message = "score of KNN is " + str(self.Kn_score)
                      file.write(custom_message)
              if self.Kn_score>self.dt_score:
                 return "Knn",self.Kn
              else:
                 return 'Decisiion Tree',self.Dt


          except  Exception as e:
              raise e









