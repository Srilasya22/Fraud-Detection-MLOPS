import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import deepchecks
from deepchecks.tabular.checks import LabelDrift, FeatureDrift
from deepchecks.tabular.suites import data_integrity
from imblearn.over_sampling import SMOTE


class DataPreprocessor:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def preprocess_data(self):
        self.df = self.df.drop(['nameDest', 'nameOrig'], axis=1)
        # Feature Engineering
        self.df['errorBalanceOrig'] = self.df.newbalanceOrig + self.df.amount - self.df.oldbalanceOrg
        self.df['errorBalanceDest'] = self.df.oldbalanceDest + self.df.amount - self.df.newbalanceDest
        self.df = self.df.drop(['newbalanceOrig', 'oldbalanceOrg', 'oldbalanceDest', 'newbalanceDest'], axis=1)

        type_mapping = {'CASH_OUT': 0, 'PAYMENT': 1, 'CASH_IN': 2, 'TRANSFER': 3, 'DEBIT': 4}

        # Use the map function to encode the 'type' column
        self.df['type_encoded'] = self.df['type'].map(type_mapping)
        self.df = self.df.drop('type', axis=1)

        x = self.df.drop('isFraud', axis=1)
        y = self.df['isFraud']
        x_resample, y_resample = SMOTE().fit_resample(x, y.values.ravel())
        return self.df, x_resample, y_resample
    
class DatasetCreator:
    def __init__(self, df, label_col, cat_features=[]):

        self.dataset = deepchecks.tabular.Dataset(df=df, label=df[label_col], cat_features=cat_features)

class DataIntegrityChecker:
    def __init__(self):
        self.integ_suite = data_integrity()

    def run_check(self, dataset):
        integ_result = self.integ_suite.run(dataset)
        integ_result.save_as_html('report/DataIntegrity.html')

class LabelDriftChecker:
    def __init__(self):
        self.label_check = LabelDrift()

    def run_check(self, train_dataset, test_dataset):
        label_result = self.label_check.run(train_dataset, test_dataset)
        label_result.save_as_html('report/LabelDrift.html')

class FeatureDriftChecker:
    def __init__(self):
        self.feature_checks = FeatureDrift()

    def run_check(self, train_dataset, test_dataset):
        feature_results = self.feature_checks.run(train_dataset=train_dataset, test_dataset=test_dataset)
        feature_results.save_as_html('report/FeatureDrift.html')

# Load and preprocess data
preprocessed = DataPreprocessor('data/01_raw/raw.csv')
preprocessed_data,x_resampled,y_resampled = preprocessed.preprocess_data()
x_train, x_test, y_train, y_test = train_test_split(x_resampled, y_resampled, test_size=0.2, random_state=42)


# Reset the index of x_train to have a default RangeIndex
x_train = x_train.reset_index(drop=True)


train_dataset = deepchecks.tabular.Dataset(df=x_train, label=pd.Series(y_train, index=x_train.index), cat_features=[])
test_dataset=deepchecks.tabular.Dataset(df=x_test, label=pd.Series(y_test, index=x_test.index), cat_features=[])

# Run data integrity check
data_integrity_checker = DataIntegrityChecker()
data_integrity_checker.run_check(train_dataset)

# Run label drift check
label_drift_checker = LabelDriftChecker()
label_drift_checker.run_check(train_dataset, test_dataset)

# Run feature drift check
feature_drift_checker = FeatureDriftChecker()
feature_drift_checker.run_check(train_dataset, test_dataset)