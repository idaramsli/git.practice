#Task 2
import pandas as pd
import yaml
import json


with open("config.yml") as f:
    over_due = yaml.safe_load(f) #leser inn fra yaml-fil og gjør det leselig for python
    tekst = f.read()
print(tekst)


with open("calibrations.csv") as f:
    tekst = f.read()
    calibrations = pd.read_csv("calibrations.csv")
print(calibrations)

sensors = pd.read_excel("sensors.xlsx")
print(sensors)


data = pd.merge(sensors, calibrations, on="sensor_id")
print(data)

max_days = over_due["max_days_since_calibration"]

print("These are over due for a new calibration!")
over = data[data["days_since_calibration"]> max_days ]
print(over)


over.to_json("overdue_sensors.json", orient = "records", indent = 2)



