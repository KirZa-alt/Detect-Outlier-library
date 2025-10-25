import pandas as pd
import numpy as np
from scipy import stats
from sklearn.ensemble import IsolationForest

def outliers(self, method='iqr', contamination=0.05):
    numeric = self.select_dtypes(include=np.number)
    
    if method.lower() == 'zscore':
        z = np.abs(stats.zscore(numeric))
        return self[(z > 3).any(axis=1)]
    
    elif method.lower() == 'iqr':
        Q1 = numeric.quantile(0.25)
        Q3 = numeric.quantile(0.75)
        IQR = Q3 - Q1
        return self[(numeric < (Q1 - 1.5 * IQR)) | (numeric > (Q3 + 1.5 * IQR))].dropna(how='all')
    
    elif method.lower() == 'isolationforest':
        model = IsolationForest(contamination=contamination, random_state=42)
        preds = model.fit_predict(numeric)
        return self[preds == -1]
    
    else:
        raise ValueError("method must be 'iqr', 'zscore', or 'isolationforest'")

# Add method to pandas DataFrame
pd.DataFrame.outliers = outliers
