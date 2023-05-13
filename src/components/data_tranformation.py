import os 
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
import numpy as np 
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from src.utils import save_object

@ dataclass
class DataTransformationConfig:
    model_pkl_file_path = os.path.join('Artifact','model.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object (self):
        try:
            numerical_column = ['writing score','reading score']
            categorical_column = ['gender','race/ethnicity','parental level of education','lunch','test preparation course']

            numerical_pipeline = Pipeline(
                steps= [
                    ('imputer', SimpleImputer(strategy='median')),
                    ('StandardScaler', StandardScaler(with_mean=False))
                    ]

            )

            categorical_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehot Encoder', OneHotEncoder()),
                    ('StandardScaler', StandardScaler(with_mean=False))
                ]
            )


            logging.info('Numerical columns standard scaling completed')
            logging.info('categorical column encoding completed')

            preprocessor = ColumnTransformer(
                [
                ('numerical_pipeline',numerical_pipeline,numerical_column),
                ('categorical_pipeline',categorical_pipeline,categorical_column)
                ]
            )


            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read train and test data')

            logging.info('Starting preprocessing procee')

            preprocessor_obj = self.get_data_transformation_object()

            target_column = 'math score'

            input_feature_train_df = train_df.drop(columns=[target_column],axis = 1)
            input_feature_test_df = test_df.drop(columns=[target_column],axis = 1)

            target_feature_train_df = train_df[target_column]
            target_feature_test_df = test_df[target_column]

            logging.info('Applying preprocessing object to traing and test data')

            
            input_feature_train_df_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_df_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_df_arr,np.array(target_feature_train_df)
            ]

            test_arr = np.c_[
                input_feature_test_df_arr,np.array(target_feature_test_df)
            ]

            logging.info('saving preprocessing object')

            save_object(

                file_path = self.data_transformation_config.model_pkl_file_path,
                obj = preprocessor_obj

            )
            

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.model_pkl_file_path
            )


        except Exception as e:
            raise CustomException(e,sys)

