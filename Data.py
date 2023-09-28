import pandas as pd

class Data:
    """This class  will be able to give data in csv form obtained from database"""

    def __init__(self):
        self.trainingfile = "data/customer_churn_large_dataset.xlsx"


    def datgetter(self):

        try:
            csv=pd.read_excel(self.trainingfile)
            return csv

        except Exception as e:

            raise e
