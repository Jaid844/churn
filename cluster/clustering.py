from sklearn.cluster import KMeans
from kneed import KneeLocator
import matplotlib.pyplot as plt
from file_operation import file_op

class Cluster:
    def __init__(self):

        self.file_op=file_op()


    def elbowplot(self,data):

         wcss = []  # initializing an empty list
         try:
             for i in range(1, 11):
                 kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)  # initializing the KMeans object
                 kmeans.fit(data)  # fitting the data to the KMeans Algorithm
                 wcss.append(kmeans.inertia_)
             plt.plot(range(1, 11), wcss)  # creating the graph between WCSS and the number of clusters
             plt.title('The Elbow Method')
             plt.xlabel('Number of clusters')
             plt.ylabel('WCSS')
             # plt.show()
             plt.savefig('preprocessing_data/K-Means_Elbow.PNG')  # saving the elbow plot locally
             # finding the value of the optimum cluster programmatically
             self.kn = KneeLocator(range(1, 11), wcss, curve='convex', direction='decreasing')

             return self.kn.knee

         except :
              raise Exception()


    def create_cluster(self,data,number_of_clusters):

        try:
            self.kmeans = KMeans(n_clusters=number_of_clusters, init='k-means++', random_state=42)
            # self.data = self.data[~self.data.isin([np.nan, np.inf, -np.inf]).any(1)]
            self.y_kmeans = self.kmeans.fit_predict(data)  # divide data into clusters

            self.save_model = self.file_op.save_model(self.kmeans, 'KMeans')  # saving the KMeans model to directory
            # passing 'Model' as the functions need three parameters

            data['Cluster'] = self.y_kmeans  # create a new column in dataset for storing the cluster information

            return data
        except Exception as e:
            raise Exception()

