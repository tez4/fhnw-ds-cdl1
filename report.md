# Sensor based Activity Recognition

<img align="right" height="50" src="/media/fhnw-logo.svg">

**Team members:** Navjot Zubler, Joël Grosjean

**Instructor:** Marcel Messerli

**Date:** 20.01.2023 

## Table of Contents
- [Sensor based Activity Recognition](#sensor-based-activity-recognition)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Methodology](#methodology)
    - [Date collection](#date-collection)
    - [Data wrangling](#data-wrangling)
    - [Model training](#model-training)
  - [Results](#results)
  - [Key learnings](#key-learnings)

## Introduction

## Methodology

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