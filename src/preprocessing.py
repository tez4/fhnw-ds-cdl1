import os
import yaml
import pickle
import random
import numpy as np
import pandas as pd
from keras.utils import to_categorical
from src import (
    read_nz_file, read_jg_file, split_df, add_moving_window, add_moving_window_2)


def one_hot_encode(array):
    # expects np array as input
    for i, v in enumerate(array):
        if v == 'sitting':
            array[i] = 0
        elif v == 'walking':
            array[i] = 1
        elif v == 'running':
            array[i] = 2
        elif v == 'cycling':
            array[i] = 3

    array = to_categorical(np.array(array))

    return array


def preprocess_sequential(
        moving_window_seconds, hz, step_size, meta, test_proportion=0.2, select_train_files='all'):

    # create empty data frames
    train = pd.DataFrame()
    test = pd.DataFrame()

    # create empty lists of start indexes
    train_indexes = []
    test_indexes = []

    all_train_files = []
    all_test_files = []

    for index, (file, user, activity, position_x) in enumerate(
            zip(meta['file'], meta['user'], meta['activity'], meta['position_x'])):

        if user == 'nz':
            df = read_nz_file(file, activity)
            df = df.drop(columns=['datetime'])

        elif user == 'jg':
            df = read_jg_file(file, activity)

        print(file, user, activity, position_x, df.shape)

        # split into train-test
        my_train_files, my_test_files = split_df(
            df, hz=hz, test_proportion=test_proportion, moving_window_size=moving_window_seconds,
            select_train_files=select_train_files, user=user, position_x=position_x, index=index
        )

        print(f'Train: {len(my_train_files)}, Test: {len(my_test_files)}')

        all_train_files += my_train_files
        all_test_files += my_test_files

    print([len(i) for i in all_train_files])
    print([len(i) for i in all_test_files])

    lookback = hz * moving_window_seconds
    # aggregate data points (try moving average) transform to mean, sd, ...
    for i, v_train in enumerate(all_train_files):

        # save possible start indexes for training and test sequences
        max_train_index = len(v_train) - 1
        train_rows = np.arange(lookback, max_train_index, step_size)

        # append start indexes of sequences to total lists
        train_indexes += list(train_rows + len(train))

        # append files to total file
        train = pd.concat([train, v_train])

    for i, v_test in enumerate(all_test_files):

        # save possible start indexes for training and test sequences
        max_test_index = len(v_test) - 1
        test_rows = np.arange(lookback, max_test_index, step_size)

        # append start indexes of sequences to total lists
        test_indexes += list(test_rows + len(test))

        # append files to total file
        test = pd.concat([test, v_test])

    # split x and y
    cols = [
        'v_accelerometer',
        'v_gyroscope',
        'v_magnetometer',
        'v_gravity',
        'v_orientation',
        'min_accelerometer',
        'max_accelerometer',
        'min_gyroscope',
        'max_gyroscope',
        'min_magnetometer',
        'max_magnetometer',
        'min_gravity',
        'max_gravity',
        'min_orientation',
        'max_orientation'
    ]

    print(f'Train length: {len(train)}')
    print(f'Test length: {len(test)}')

    y_train = train['y']
    # x_train = train.drop(columns=['y', 'time_since_start(ms)'])
    x_train = train[cols]

    y_test = test['y']
    # x_test = test.drop(columns=['y', 'time_since_start(ms)'])
    x_test = test[cols]

    # normalize data by training aggregates
    mean = x_train.mean(axis=0)
    x_train -= mean
    x_test -= mean
    std = x_train.std(axis=0)
    x_train /= std
    x_test /= std

    # one hot encode labels
    y_train = one_hot_encode(np.array(y_train))
    y_test = one_hot_encode(np.array(y_test))

    # shuffle the list of indexes
    random.shuffle(train_indexes)
    random.shuffle(test_indexes)

    return x_train, x_test, y_train, y_test, train_indexes, test_indexes


def save_sequential_preprocessing(
        X_train, X_test, y_train, y_test, train_indexes, test_indexes, folder: str, settings: str):

    if not os.path.exists(f'./tmp/{folder}'):
        os.mkdir(f'./tmp/{folder}')

    with open(f'tmp/{folder}/X_train.pickle', 'wb') as f:
        pickle.dump(X_train, f)
    with open(f'tmp/{folder}/X_test.pickle', 'wb') as f:
        pickle.dump(X_test, f)
    with open(f'tmp/{folder}/y_train.pickle', 'wb') as f:
        pickle.dump(y_train, f)
    with open(f'tmp/{folder}/y_test.pickle', 'wb') as f:
        pickle.dump(y_test, f)
    with open(f'tmp/{folder}/train_indexes.pickle', 'wb') as f:
        pickle.dump(train_indexes, f)
    with open(f'tmp/{folder}/test_indexes.pickle', 'wb') as f:
        pickle.dump(test_indexes, f)

    with open(rf'./tmp/{folder}/metadata.yaml', 'w') as file:
        yaml.dump(settings, file)

    print(f'Saved files to "./tmp/{folder}"')


def preprocess_data(
        moving_window_seconds, hz, step_size, meta, agg_func, test_proportion=0.2, select_train_files='all'):
    '''
    agg_func: aggregate function to apply eg add_moving_window or add_moving_window_2
    '''
    # create empty data frames
    train = pd.DataFrame()
    test = pd.DataFrame()

    all_train_files = []
    all_test_files = []

    for index, (file, user, activity, position_x) in enumerate(
            zip(meta['file'], meta['user'], meta['activity'], meta['position_x'])):
        if user == 'nz':
            df = read_nz_file(file, activity)

        elif user == 'jg':
            df = read_jg_file(file, activity)

        print(file, user, activity, position_x, df.shape)

        # split into train-test
        my_train_files, my_test_files = split_df(
            df, hz=hz, test_proportion=test_proportion, moving_window_size=moving_window_seconds,
            select_train_files=select_train_files, user=user, position_x=position_x, index=index
        )

        print(f'Train: {len(my_train_files)}, Test: {len(my_test_files)}')

        all_train_files += my_train_files
        all_test_files += my_test_files

    print(f'Train: {[len(i) for i in all_train_files]}')
    print(f'Test: {[len(i) for i in all_test_files]}')

    # aggregate every file in training set
    for i, v_train in enumerate(all_train_files):
        if agg_func == 'add_moving_window_2':
            v_train = add_moving_window_2(
                v_train, hz_old_data=hz, seconds=moving_window_seconds, step_size=step_size
            )

        elif agg_func == 'add_moving_window':
            v_train = add_moving_window(
                v_train, hz_old_data=hz, seconds=moving_window_seconds, step_size=step_size
            )

        train = pd.concat([train, v_train])

    # aggregate every file in test set
    for i, v_test in enumerate(all_test_files):
        if agg_func == 'add_moving_window_2':
            v_test = add_moving_window_2(
                v_test, hz_old_data=hz, seconds=moving_window_seconds, step_size=step_size
            )
        elif agg_func == 'add_moving_window':

            v_test = add_moving_window(
                v_test, hz_old_data=hz, seconds=moving_window_seconds, step_size=step_size
            )

        test = pd.concat([test, v_test])

    print(f'Train length: {len(train)}')
    print(f'Test length: {len(test)}')

    # X - y split for train and test data, shuffle data!?
    y_train = train['y'].to_frame()
    X_train = train.drop(columns=['y'])
    y_test = test['y'].to_frame()
    X_test = test.drop(columns=['y'])

    return X_train, X_test, y_train, y_test


def save_preprocessing(X_train, X_test, y_train, y_test, folder: str, settings: str, file_type: str = 'parquet'):
    if not os.path.exists(f'./tmp/{folder}'):
        os.mkdir(f'./tmp/{folder}')

    if file_type == 'parquet':
        X_train.to_parquet(f'tmp/{folder}/X_train.parquet')
        X_test.to_parquet(f'tmp/{folder}/X_test.parquet')
        y_train.to_parquet(f'tmp/{folder}/y_train.parquet')
        y_test.to_parquet(f'tmp/{folder}/y_test.parquet')
    elif file_type == 'pickle':
        with open(f'tmp/{folder}/X_train.pickle', 'wb') as f:
            pickle.dump(X_train, f)
        with open(f'tmp/{folder}/X_test.pickle', 'wb') as f:
            pickle.dump(X_test, f)
        with open(f'tmp/{folder}/y_train.pickle', 'wb') as f:
            pickle.dump(y_train, f)
        with open(f'tmp/{folder}/y_test.pickle', 'wb') as f:
            pickle.dump(y_test, f)

    with open(rf'./tmp/{folder}/metadata.yaml', 'w') as file:
        yaml.dump(settings, file)

    print(f'Saved files to "./tmp/{folder}"')
