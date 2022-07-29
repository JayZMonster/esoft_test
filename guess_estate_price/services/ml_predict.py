import pickle
import numpy as np
import pandas as pd
import os


class XGBRegressionService:

    def __init__(self):
        if not os.path.exists('guess_estate_price/services/model.pkl'):
            raise Exception
        self.__reg_model = pickle.load(open('guess_estate_price/services/model.pkl', 'rb'))

    def make_prediction(self, *args, _import=False):
        if not _import:
            input_data = np.array(args)
            pred = self.__reg_model.predict(input_data)
        else:
            pred = []
            for data in args:
                input_data = np.array(data)
                pred.append(self.__reg_model.predict(input_data))
        return pred


def predict(form):
    excl = 'csrfmiddlewaretoken'

    data = [float(form[param]) for param in form if param not in excl]
    return XGBRegressionService().make_prediction(data)


def predict_csv(file):
    _params = [
        'city_id',
        'district_id',
        'street_id',
        'floors_cnt',
        'rooms_cnt',
        'building_year',
        'area_total',
        'area_kitchen',
        'series_id'
    ]
    csv = pd.read_csv(file)
    X = csv[_params]
    X = X.fillna(-1)

    return XGBRegressionService().make_prediction(X, _import=True)
