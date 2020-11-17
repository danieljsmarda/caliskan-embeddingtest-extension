import pickle
import numpy as np
from collections import defaultdict

def save_pickle(obj, FILEPATH):
    f = open(FILEPATH, 'wb')
    pickle.dump(obj, f)
    f.close()

def open_pickle(FILEPATH):
    f = open(FILEPATH, 'rb')
    obj = pickle.load(f)
    f.close()
    return obj

def save_arrays(FILEPATH, exp_num, order, X_metrics, Y_metrics, threshold,
    pct_5, pct_95, A_biases, lower_bound, upper_bound):
    results_dict = open_pickle(FILEPATH)
    results_dict[exp_num] = results_dict.get(exp_num, defaultdict(dict))
    order_dict = results_dict[exp_num].get(order, {})
    order_dict['X_array'] = X_metrics
    order_dict['Y_array'] = Y_metrics
    order_dict['X_mean'] = np.mean(X_metrics)
    order_dict['Y_mean'] = np.mean(Y_metrics)
    order_dict['threshold'] = threshold
    #order_dict['pct_5'] = pct_5
    #order_dict['pct_95'] = pct_95
    #order_dict['A_biases'] = A_biases
    #order_dict['lower_bound'] = lower_bound
    #order_dict['upper_bound'] = upper_bound
    results_dict[exp_num][order] = order_dict
    save_pickle(results_dict, FILEPATH)
    print(f"Results array successfully saved to file {FILEPATH} under\
 keys [{exp_num}][{order}]")

def save_experiment_arbitrary_label(filepath, exp_num, order, label, data, display=None):
    results_dict = open_pickle(filepath)
    results_dict[exp_num] = results_dict.get(exp_num, defaultdict(dict))
    order_dict = results_dict[exp_num].get(order, {})
    order_dict[label] = data
    results_dict[exp_num][order] = order_dict
    save_pickle(results_dict, filepath)
    if display == 'all':
        print(f'FULL RESULTS DICT FOR EXP {exp_num}', results_dict[exp_num])
    elif display == 'some':
        print(f'SPECIFIC RESULTS FOR EXP {exp_num}, LABEL "{label}": \
        {results_dict[exp_num][order][label]}')
    print(f"Results array successfully saved to file {filepath} under\
    keys [{exp_num}][{order}][{label}]")

def save_scalers(filepath, exp_num, order, scaler): 
    results_dict = open_pickle(filepath)
    results_dict[exp_num] = results_dict.get(exp_num, defaultdict(dict))
    results_dict[exp_num][order] = scaler
    save_pickle(results_dict, filepath)

def save_array_old(FILEPATH, arr, exp_num, order, list_name):
    results_dict = open_pickle(FILEPATH)
    exp_name = str(order)+'_order_'+list_name
    results_dict[exp_num][exp_name] = arr
    save_pickle(results_dict, FILEPATH)
    print(f"Results array successfully saved to file {FILEPATH} under\
 keys [{exp_num}]['{exp_name}']")

