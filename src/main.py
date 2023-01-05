
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
                'sitting_jg_3.csv', 'sitting_jg_4.csv',  # added JG 20221020
                'walking_jg_4.csv', 'walking_jg_5.csv',  # added JG 20221025
                'walking_nz_5.csv', 'running_nz_6.csv', 'running_nz_7.csv', 'cycling_nz_8.csv',
                'cycling_nz_9.csv',  # added 20221108
                'sitting_nz_10.csv','sitting_nz_11.csv'
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
                'jg', 'jg',  # added JG 20221020
                'jg', 'jg',  # added JG 20221025
                'nz', 'nz', 'nz', 'nz',
                'nz',  # added 20221108
                'nz','nz',
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
                'sitting', 'sitting',  # added JG 20221020
                'walking', 'walking',  # added JG 20221025
                'walking', 'running', 'running', 'cycling',
                'cycling',  # added 20221108
                'sitting', 'sitting',
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
                'left pant pocket', 'left pant pocket',  # added JG 20221020
                'left pant pocket', 'left pant pocket',  # added JG 20221025
                'left pant pocket', 'left pant pocket', 'left pant pocket', 'left pant pocket',
                'left pant pocket',  # added 20221108
                'left pant pocket','left pant pocket',
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
                'screen towards body', 'screen not towards body',  # added JG 20221020
                'screen not towards body', 'screen not towards body',  # added JG 20221025
                'screen towards body', 'screen towards body', 'screen towards body', 'screen towards body',
                'screen towards body',  # 20221108
                'screen towards body', 'screen towards body',
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
                'upright', 'upright',  # added JG 20221020
                'upside down', 'upright',  # added JG 20221025
                'upside down', 'upside down', 'upright', 'upside down',
                'upright',  # 20221108
                'upside down', 'upside down',
            ]
        }
    )

    meta = meta.sort_values(by=['user', 'activity', 'file'], axis=0).reset_index(drop=True)

    meta.to_csv('data/meta.csv', index=False)


# added function NZ 20221108
# NZ - remove unnecessary columns from SensorLog File/below list
remove_cols = [
    'loggingSample(N)', 'locationTimestamp_since1970(s)', 'locationCourseAccuracy(°)',
    'locationVerticalAccuracy(m)', 'locationHorizontalAccuracy(m)', 'locationFloor(Z)',
    'locationHeadingTimestamp_since1970(s)', 'locationHeadingX(µT)',
    'locationHeadingY(µT)', 'locationHeadingZ(µT)', 'locationTrueHeading(°)', 'locationMagneticHeading(°)',
    'locationHeadingAccuracy(°)', 'accelerometerTimestamp_sinceReboot(s)',
    'gyroTimestamp_sinceReboot(s)', 'magnetometerTimestamp_sinceReboot(s)',
    'motionTimestamp_sinceReboot(s)', 'motionAttitudeReferenceFrame(txt)',
    'motionQuaternionX(R)', 'motionQuaternionY(R)', 'motionQuaternionZ(R)',
    'motionQuaternionW(R)', 'motionHeading(°)', 'motionMagneticFieldCalibrationAccuracy(Z)',
    'activityTimestamp_sinceReboot(s)', 'activity(txt)', 'activityActivityConfidence(Z)',
    'activityActivityStartDate(txt)', 'pedometerStartDate(txt)', 'pedometerNumberofSteps(N)',
    'pedometerAverageActivePace(s/m)', 'pedometerCurrentPace(s/m)', 'pedometerCurrentCadence(steps/s)',
    'pedometerDistance(m)', 'pedometerFloorAscended(N)', 'pedometerFloorDescended(N)',
    'pedometerEndDate(txt)', 'altimeterTimestamp_sinceReboot(s)', 'altimeterReset(bool)',
    'altimeterRelativeAltitude(m)', 'altimeterPressure(kPa)', 'deviceOrientationTimeStamp_since1970(s)',
    'deviceOrientation(Z)', 'label(N)'
]


def load_clean(from_file, remove_cols, to_file):
    ''' This function is required for cleaning raw data from source SensorLog only. i.e. sensor data from nz

    arguments:
        from_file: path to raw data file [path]
        remove_cols: List of column name to be dropped from df [list]
        to_file: filename to output as [text]
    '''
    # load data
    df = pd.read_csv(from_file)

    # change the 'loggingTime(txt)' to datetime
    df['loggingTime(txt)'] = pd.to_datetime(df['loggingTime(txt)'], format='%Y-%m-%dT%H:%M:%S.%f')

    # Drop unnecessary columns, round to 6 decimal places, output to csv file
    df.drop(remove_cols, axis=1).round(6).to_csv(to_file, index=False)

#added 30.12.2022
def vector_magnitude(df, x,y,z):
    '''
    function to calculate the vector magnitude
    '''
    v =(df[x]**2 + df[y]**2 + df[z]**2).pow(1/2)
    return v

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

    min = df['datetime'].min()
    df['time_since_start(ms)'] = df["datetime"].map(lambda name: int((name - min).total_seconds() * 1000))

    cols = list(my_cols.values()) + ['time_since_start(ms)', 'y']

    # select columns
    df = df[[c for c in cols]]

    # additional variables - Vector magnitude
    df['v_accelerometer'] = vector_magnitude(df, 'accelerometer_X(G)', 'accelerometer_Y(G)', 'accelerometer_Z(G)')
    df['v_gyroscope'] = vector_magnitude(df, 'gyroscope_X(rad/s)', 'gyroscope_Y(rad/s)', 'gyroscope_Z(rad/s)')
    df['v_magnetometer'] = vector_magnitude(df, 'magnetometer_X(microT)', 'magnetometer_Y(microT)',
                                            'magnetometer_Z(microT)')
    df['v_gravity'] = vector_magnitude(df, 'gravity_X(G)', 'gravity_Y(G)', 'gravity_Z(G)')
    df['v_orientation'] = vector_magnitude(df, 'orientation_X(rad)', 'orientation_Y(rad)', 'orientation_Z(rad)')

    # absolute values of min/max from each sensor coordinate X,Y,Z
    df['min_accelerometer'] = abs(df[['accelerometer_X(G)', 'accelerometer_Y(G)', 'accelerometer_Z(G)']].min(axis=1))
    df['max_accelerometer'] = abs(df[['accelerometer_X(G)', 'accelerometer_Y(G)', 'accelerometer_Z(G)']].max(axis=1))
    df['min_gyroscope'] = abs(df[['gyroscope_X(rad/s)', 'gyroscope_Y(rad/s)', 'gyroscope_Z(rad/s)']].min(axis=1))
    df['max_gyroscope'] = abs(df[['gyroscope_X(rad/s)', 'gyroscope_Y(rad/s)', 'gyroscope_Z(rad/s)']].max(axis=1))
    df['min_magnetometer'] = abs(
        df[['magnetometer_X(microT)', 'magnetometer_Y(microT)', 'magnetometer_Z(microT)']].min(axis=1))
    df['max_magnetometer'] = abs(
        df[['magnetometer_X(microT)', 'magnetometer_Y(microT)', 'magnetometer_Z(microT)']].max(axis=1))
    df['min_gravity'] = abs(df[['gravity_X(G)', 'gravity_Y(G)', 'gravity_Z(G)']].min(axis=1))
    df['max_gravity'] = abs(df[['gravity_X(G)', 'gravity_Y(G)', 'gravity_Z(G)']].max(axis=1))
    df['min_orientation'] = abs(df[['orientation_X(rad)', 'orientation_Y(rad)', 'orientation_Z(rad)']].min(axis=1))
    df['max_orientation'] = abs(df[['orientation_X(rad)', 'orientation_Y(rad)', 'orientation_Z(rad)']].max(axis=1))

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

    # additional variables - Vector magnitude
    df['v_accelerometer'] = vector_magnitude(df, 'accelerometer_X(G)', 'accelerometer_Y(G)', 'accelerometer_Z(G)')
    df['v_gyroscope'] = vector_magnitude(df, 'gyroscope_X(rad/s)', 'gyroscope_Y(rad/s)', 'gyroscope_Z(rad/s)')
    df['v_magnetometer'] = vector_magnitude(df, 'magnetometer_X(microT)', 'magnetometer_Y(microT)',
                                            'magnetometer_Z(microT)')
    df['v_gravity'] = vector_magnitude(df, 'gravity_X(G)', 'gravity_Y(G)', 'gravity_Z(G)')
    df['v_orientation'] = vector_magnitude(df, 'orientation_X(rad)', 'orientation_Y(rad)', 'orientation_Z(rad)')

    # absolute values of min/max from each sensor coordinate X,Y,Z
    df['min_accelerometer'] = abs(df[['accelerometer_X(G)', 'accelerometer_Y(G)', 'accelerometer_Z(G)']].min(axis=1))
    df['max_accelerometer'] = abs(df[['accelerometer_X(G)', 'accelerometer_Y(G)', 'accelerometer_Z(G)']].max(axis=1))
    df['min_gyroscope'] = abs(df[['gyroscope_X(rad/s)', 'gyroscope_Y(rad/s)', 'gyroscope_Z(rad/s)']].min(axis=1))
    df['max_gyroscope'] = abs(df[['gyroscope_X(rad/s)', 'gyroscope_Y(rad/s)', 'gyroscope_Z(rad/s)']].max(axis=1))
    df['min_magnetometer'] = abs(
        df[['magnetometer_X(microT)', 'magnetometer_Y(microT)', 'magnetometer_Z(microT)']].min(axis=1))
    df['max_magnetometer'] = abs(
        df[['magnetometer_X(microT)', 'magnetometer_Y(microT)', 'magnetometer_Z(microT)']].max(axis=1))
    df['min_gravity'] = abs(df[['gravity_X(G)', 'gravity_Y(G)', 'gravity_Z(G)']].min(axis=1))
    df['max_gravity'] = abs(df[['gravity_X(G)', 'gravity_Y(G)', 'gravity_Z(G)']].max(axis=1))
    df['min_orientation'] = abs(df[['orientation_X(rad)', 'orientation_Y(rad)', 'orientation_Z(rad)']].min(axis=1))
    df['max_orientation'] = abs(df[['orientation_X(rad)', 'orientation_Y(rad)', 'orientation_Z(rad)']].max(axis=1))

    return df


def split_df(df: pd.DataFrame, hz: float, test_proportion: float, moving_window_size: float):
    # select every nth row
    if test_proportion > 100:
        raise Exception('hz must be less than 100!')
    nth = int(100 / hz)
    df = df.iloc[::nth, :]

    # split into train and test
    if test_proportion >= 1 or test_proportion <= 0:
        raise Exception('test_proportion must be between 0 and 1!')

    my_train_files = []
    my_test_files = []

    # test_per_minute = int(60 * test_proportion * hz)
    # train_per_minute = int((60 * hz) - test_per_minute)

    while len(df) / hz > 0:
        if len(df) / hz < 600:
            x = df
            df = pd.DataFrame()
        else:
            x = df[:300 * hz:]
            df = df[300 * hz:]

        train_count = int((len(x) - (moving_window_size * hz * 2)) * (1 - test_proportion)) + (moving_window_size * hz)

        my_train_files.append(x.iloc[: train_count])
        my_test_files.append(x.iloc[train_count:])

    return (my_train_files, my_test_files)


def aggregate_files(files: list, aggregate: pd.DataFrame) -> pd.DataFrame:
    for v in files:
        aggregate = pd.concat([aggregate, v])

    return aggregate


def add_moving_window(df, hz_old_data, seconds, step_size):
    rows = hz_old_data * seconds

    y = df.iloc[::step_size, :]['y'].iloc[int(rows / step_size):]

    # get mean and std for rolling window
    df = df.rolling(window=rows, step=step_size).agg(
        {
            'gyroscope_X(rad/s)': ["mean", "std"],
            'gyroscope_Y(rad/s)': ["mean", "std"],
            'gyroscope_Z(rad/s)': ["mean", "std"],
            'magnetometer_X(microT)': ["mean", "std"],
            'magnetometer_Y(microT)': ["mean", "std"],
            'magnetometer_Z(microT)': ["mean", "std"],
            'gravity_X(G)': ["mean", "std"],
            'gravity_Y(G)': ["mean", "std"],
            'gravity_Z(G)': ["mean", "std"],
            'accelerometer_X(G)': ["mean", "std"],
            'accelerometer_Y(G)': ["mean", "std"],
            'accelerometer_Z(G)': ["mean", "std"],
            'orientation_X(rad)': ["mean", "std"],
            'orientation_Y(rad)': ["mean", "std"],
            'orientation_Z(rad)': ["mean", "std"],
        }
    )[int(rows / step_size):]

    # remove multi-index
    df.columns = ['_'.join(col) for col in df.columns.values]

    # add y
    df['y'] = y

    return df

#added 30.12.2022 - updated 05.01.2023
def add_moving_window_2(df, hz_old_data, seconds, step_size):
    rows = hz_old_data * seconds

    y = df.iloc[::step_size, :]['y'].iloc[int(rows / step_size):]

    # get mean and std for rolling window
    df = df.rolling(window=rows, step=step_size).agg(
        {
            'v_accelerometer' : ["mean", "std"],
            'v_gyroscope':  ["mean", "std"],
            'v_magnetometer':  ["mean", "std"],
            'v_gravity':  ["mean", "std"],
            'v_orientation':  ["mean", "std"],
            'min_accelerometer': ["mean", "std"],
            'max_accelerometer': ["mean", "std"],
            'min_gyroscope': ["mean", "std"],
            'max_gyroscope': ["mean", "std"],
            'min_magnetometer': ["mean", "std"],
            'max_magnetometer': ["mean", "std"],
            'min_gravity': ["mean", "std"],
            'max_gravity': ["mean", "std"],
            'min_orientation': ["mean", "std"],
            'max_orientation': ["mean", "std"]

        }
    )[int(rows / step_size):]

    # remove multi-index
    df.columns = ['_'.join(col) for col in df.columns.values]

    # add y
    df['y'] = y

    return df