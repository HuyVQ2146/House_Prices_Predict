import pandas as pd

def fill_missing(data_set):
    # Nhóm 1:
    cols_none = [
    'PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu', 
    'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond',
    'BsmtExposure', 'BsmtFinType2', 'BsmtQual', 'BsmtCond', 'BsmtFinType1',
    'MasVnrType', 'MSZoning', 'Utilities', 'Functional', 'Exterior1st', 
    'Exterior2nd', 'SaleType', 'KitchenQual', 'Electrical'
    ]
    for col in cols_none:
        data_set[col] = data_set[col].fillna("None")
    
    # Nhóm 2:
    cols_fill_zero = ['MasVnrArea', 'GarageYrBlt', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtFullBath', 'BsmtHalfBath', 
                       'BsmtUnfSF', 'TotalBsmtSF', 'GarageCars', 'GarageArea']
    data_set[cols_fill_zero] = data_set[cols_fill_zero].fillna(0)
    
    # Nhóm 3:
    data_set["LotFrontage"] = data_set["LotFrontage"].fillna(data_set["LotFrontage"].median())
    
    # Nhóm 4:
    for col in ["MSZoning", "Utilities", "Functional", "Exterior1st", "Exterior2nd", 
            "KitchenQual", "SaleType", "Electrical"]:
        data_set[col] = data_set[col].fillna(data_set[col].mode()[0])
    
    return data_set


def one_hot_encoding(training_set, test_set):
    training_set = pd.get_dummies(training_set)
    test_set = pd.get_dummies(test_set)
    
    training_set, test_set = training_set.align(test_set, join='left', axis=1, fill_value=0)
    return training_set, test_set


def create_features_and_target(train):
    X_train = train.drop('SalePrice', axis=1)
    y_train = train['SalePrice']
    
    return X_train, y_train
