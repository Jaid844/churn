import unittest
from file_operation import file_op
import numpy as np
import pandas as pd

class TestMLModel(unittest.TestCase):


    def __init__(self, methodName='runTest'):
        super(TestMLModel, self).__init__(methodName)
        self.f = file_op()
    def setUp(self):
        # Initialize the ML model or load it
        model =self.f.load_model('Knn1')
        return model

    def test_prediction(self):
        # Test a specific prediction using your ML model
        input_features = [0,1,0,0,1,0,0,63,0.6511,0.41061,0.2942]
        df = pd.DataFrame.from_dict(input_features)
        df = df.to_numpy()
        reshaped_data = df.reshape(1, -1)
        model=self.setUp()
        predicted_class =model.predict(reshaped_data)
        expected_class = 0
        self.assertEqual(predicted_class, expected_class, "Prediction should match the expected class.")



if __name__ == '__main__':
    unittest.main()
