
import csv
import numpy as np
import pandas as pd


def update_meta_data():
    meta = pd.DataFrame(
        data={
            'file': [
                'walking_jg_1.csv', 'walking_jg_2.csv', 'walking_jg_3.csv', 'running_jg_1.csv', 'running_jg_2.csv',
                'running_nz_1.csv', 'walking_nz_1.csv', 'walking_nz_2.csv',  # added NZ 20221006
                'sitting_jg_1.csv', 'sitting_jg_2.csv',  # added JG 20221006
                'sitting_nz_3.csv', 'walking_nz_4.csv', 'running_nz_3.csv',  # added NZ 20221010
                'running_jg_3.csv', 'running_jg_4.csv', 'running_jg_5.csv',  # added JG 20221011
                'cycling_nz_3.csv',  # added NZ 20221012
                'cycling_jg_1.csv',  # added JG 20221012
                'cycling_jg_2.csv', 'cycling_jg_3.csv',  # added JG 20221017
                'cycling_jg_4.csv', 'cycling_jg_5.csv',  # added JG 20221020
            ],
            'user': [
                'jg', 'jg', 'jg', 'jg', 'jg',
                'nz', 'nz', 'nz',  # added NZ 20221006
                'jg', 'jg',  # added JG 20221006
                'nz', 'nz', 'nz',  # added NZ 20221010
                'jg', 'jg', 'jg',  # added JG 20221011
                'nz',  # added NZ 20221012
                'jg',  # added JG 20221012
                'jg', 'jg',  # added JG 20221017
                'jg', 'jg',  # added JG 20221020
            ],
            'activity': [
                'walking', 'walking', 'walking', 'running', 'running',
                'running', 'walking', 'walking',  # added NZ 20221006
                'sitting', 'sitting',  # added JG 20221006
                'sitting', 'walking', 'running',  # added NZ 20221010
                'running', 'running', 'running',  # added JG 20221011
                'cycling',  # added NZ 20221012
                'cycling',  # added JG 20221012
                'cycling', 'cycling',  # added JG 20221017
                'cycling', 'cycling',  # added JG 20221020
            ],
            'pocket': [
                'left pant pocket', 'left pant pocket', 'left pant pocket', 'left pant pocket', 'left pant pocket',
                'left jacket pocket', 'left jacket pocket', 'left jacket pocket',  # added NZ 20221006
                'left pant pocket', 'left pant pocket',  # added JG 20221006
                'left pant pocket', 'left pant pocket', 'left pant pocket',  # added NZ 20221010
                'left pant pocket', 'left pant pocket', 'left pant pocket',  # added JG 20221011
                'left pant pocket',  # added NZ 20221012
                'left pant pocket',  # added JG 20221012
                'left pant pocket', 'left pant pocket',  # added JG 20221017
                'left pant pocket', 'left pant pocket',  # added JG 20221020
            ],
            'position_x': [
                'screen towards body', 'screen towards body', 'screen towards body', 'screen towards body',
                'screen towards body',
                'screen not towards body', 'screen not towards body', 'screen towards body',  # added NZ 20221006
                'screen towards body', 'screen not towards body',  # added JG 20221006
                'screen not towards body', 'screen towards body', 'screen not towards body',  # added NZ 20221010
                'screen not towards body', 'screen not towards body', 'screen not towards body',  # added JG 20221011
                'screen not towards body',  # added NZ 20221012
                'screen towards body',  # added JG 20221012
                'screen towards body', 'screen towards body',  # added JG 20221017
                'screen not towards body', 'screen not towards body',  # added JG 20221020
            ],
            'position_y': [
                'upright', 'upside down', 'upside down', 'upside down', 'upright',
                'upright', 'upright', 'upright',  # added NZ 20221006
                'upside down', 'upside down',  # added JG 20221006
                'upright', 'upside down', 'upright',  # added NZ 20221010
                'upside down', 'upright', 'upright',  # added JG 20221011
                'upright',  # added NZ 20221012
                'upside down',  # added JG 20221012
                'upright', 'upright',  # added JG 20221017
                'upside down', 'upright',  # added JG 20221020
            ]
        }
    )

    meta = meta.sort_values(by=['user', 'activity', 'file'], axis=0).reset_index(drop=True)

    meta.to_csv('data/meta.csv', index=False)


def read_nz_file(file: str, activity: str) -> pd.DataFrame:
    df = pd.read_csv(f'data/{file}')[1200:-1200]

    # simply removes time zone (not entirely correct but good enough for our purposes)
    df['loggingTime(txt)'] = df['loggingTime(txt)'].str.split('+').str.get(0)
    df['loggingTime(txt)'] = pd.to_datetime(df['loggingTime(txt)'], format='%Y-%m-%d %H:%M:%S.%f')

    # add file name in new column
    df['y'] = activity

    my_cols = {
        'loggingTime(txt)': 'datetime',
        'accelerometerAccelerationX(G)': 'accelerometer_X(G)',
        'accelerometerAccelerationY(G)': 'accelerometer_Y(G)',
        'accelerometerAccelerationZ(G)': 'accelerometer_Z(G)',
        'gyroRotationX(rad/s)': 'gyroscope_X(rad/s)',
        'gyroRotationY(rad/s)': 'gyroscope_Y(rad/s)',
        'gyroRotationZ(rad/s)': 'gyroscope_Z(rad/s)',
        'magnetometerX(µT)': 'magnetometer_X(microT)',
        'magnetometerY(µT)': 'magnetometer_Y(microT)',
        'magnetometerZ(µT)': 'magnetometer_Z(microT)',
        'motionGravityX(G)': 'gravity_X(G)',
        'motionGravityY(G)': 'gravity_Y(G)',
        'motionGravityZ(G)': 'gravity_Z(G)',
        'motionYaw(rad)': 'orientation_Z(rad)',
        'motionRoll(rad)': 'orientation_Y(rad)',
        'motionPitch(rad)': 'orientation_X(rad)',
    }

    # rename columns
    df = df.rename(my_cols, axis=1)

    cols = list(my_cols.values()) + ['y']

    # select columns
    df = df[[c for c in cols]]

    return df


def read_jg_file(file: str, activity: str) -> pd.DataFrame:

    df = pd.read_csv(f'data/{file}', sep=';', header=1)[1200:-1200]
    df['datetime'] = pd.to_datetime(df['YYYY-MO-DD HH-MI-SS_SSS'], format='%Y-%m-%d %H:%M:%S:%f')

    # add file name in new column
    df['y'] = activity

    # transformations
    df['gravity_X(G)'] = df['GRAVITY X (m/s²)'] / -9.80665
    df['gravity_Y(G)'] = df['GRAVITY Y (m/s²)'] / -9.80665
    df['gravity_Z(G)'] = df['GRAVITY Z (m/s²)'] / -9.80665

    df['accelerometer_X(G)'] = df['ACCELEROMETER X (m/s²)'] / -9.80665
    df['accelerometer_Y(G)'] = df['ACCELEROMETER Y (m/s²)'] / -9.80665
    df['accelerometer_Z(G)'] = df['ACCELEROMETER Z (m/s²)'] / -9.80665

    df['orientation_X(rad)'] = df['ORIENTATION X (pitch °)'] / 60
    df['orientation_Y(rad)'] = df['ORIENTATION Y (roll °)'] / 60
    df['orientation_Z(rad)'] = df['ORIENTATION Z (azimuth °)'] / 60

    my_cols = {
        'GYROSCOPE X (rad/s)': 'gyroscope_X(rad/s)',
        'GYROSCOPE Y (rad/s)': 'gyroscope_Y(rad/s)',
        'GYROSCOPE Z (rad/s)': 'gyroscope_Z(rad/s)',
        'MAGNETIC FIELD X (μT)': 'magnetometer_X(microT)',
        'MAGNETIC FIELD Y (μT)': 'magnetometer_Y(microT)',
        'MAGNETIC FIELD Z (μT)': 'magnetometer_Z(microT)',
        'Time since start in ms ': 'time_since_start(ms)'
    }

    # rename columns
    df = df.rename(my_cols, axis=1)

    cols = list(my_cols.values()) + [
        'y',
        'gravity_X(G)',
        'gravity_Y(G)',
        'gravity_Z(G)',
        'accelerometer_X(G)',
        'accelerometer_Y(G)',
        'accelerometer_Z(G)',
        'orientation_X(rad)',
        'orientation_Y(rad)',
        'orientation_Z(rad)'
    ]

    # select columns
    df = df[[c for c in cols]]

    return df
