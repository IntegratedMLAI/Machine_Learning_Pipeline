import sklearn.metrics as sklm
import math

def print_metrics(y_test, y_pred, n_params):
    ## First compute R^2 and the adjusted R^2
    ## Print the usual metrics and the R^2 values
    MSE = sklm.mean_squared_error(y_test, y_pred)
    RMSE = math.sqrt(sklm.mean_squared_error(y_test, y_pred))
    MAE = sklm.mean_absolute_error(y_test, y_pred)
    MedAE = sklm.median_absolute_error(y_test, y_pred)
    r2 = sklm.r2_score(y_test, y_pred)
    r2_adj = r2 - (n_params - 1)/ \
        (y_test.shape[0] - n_params) * (1 - r2)
    
    print('Mean Square Error      = ' + str(MSE))
    print('Root Mean Square Error = ' + str(RMSE))
    print('Mean Absolute Error    = ' + str(MAE))
    print('Median Absolute Error  = ' + str(MedAE))
    print('R^2                    = ' + str(r2))
    print('Adjusted R^2           = ' + str(r2_adj))