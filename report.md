# Sensor based Activity Recognition
By Navjot Zubler and Joël Grosjean

## Introducition

## Methdology

### Date collection

- frequency: 100 hz
- application: AndroSensor (android) and SensorLog (IOS)
- position: generally in pant pockets
- gps data like latitude, longitude and altitude are sadly useless because they're not always recorded.
- recorded meta data about collected .csv files in a meta data frame

### Data wrangling

- transformations of some columns required
  - Accelerometer ($/ -9.80665$) -> $m/s^2$ wird zu $G$ 
  - Gravity  ($/ -9.80665$) -> $m/s^2$ wird zu $G$
  - Orientation ($/ -60$) -> $deg$ wird zu $rad$
- renaming the columns (same names)

### Model training

## Results

## Key learnings