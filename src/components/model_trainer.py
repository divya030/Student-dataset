import os 
import sys
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object,evaluate_model

from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('Artifact','model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_file_path = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info('Split training and test input data')

            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models = {
                "Linear Regression" : LinearRegression(),
                "KNN" : KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest": RandomForestRegressor(),
                "Ada Boost": AdaBoostRegressor(),
                "Gradiant Boost": GradientBoostingRegressor(),
                "Cat boost": CatBoostRegressor(),
                "XG Boost": XGBRegressor()
            }

            model_report = evaluate_model(X_train=X_train,X_test=X_test,
                                          y_train=y_train,y_test=y_test,models=models)
            
            
            # To get best model score
            best_model_score= max(sorted(model_report.values()))

            # To get best model name

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]


            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException ('No Best model found')
            logging.info('Best Model Found on both training and test dataset')

            save_object(
                file_path=self.model_file_path.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            return r2_square
        



        except Exception as e:
            raise CustomException(e,sys)




