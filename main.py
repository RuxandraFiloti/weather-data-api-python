from flask import Flask, render_template #Flask = class
import pandas as pd #import pandas library

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17) #read the stations file and skip some rows
stations = stations[["STAID", "STANAME                                 "]] #select only the columns we need


#integrate the index.html in main.py
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html()) #.to_html() converts the dataframe to HTML table format

@app.route("/api/v1/<station>/<date>") #create a route for the API and is dynamic (station and date)
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt" #takes the path of file and reads it
    df= pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"]) #skips some rows in the file
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10 #locates the date and squeezes the value to get the temperature
    return {"station": station,
            "date": date,
             "temperature": temperature}

@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records") #dictionary with rows as records from df
    return result

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20) #daca las parse_dates=["    DATE"], da eroare din cauza ca nu e string
    df["    DATE"] = df["    DATE"].astype(str) #converts the date column to string
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records") #filters the dataframe by year and converts it to dictionary
    return result


#run the app
if(__name__) == "__main__":
  app.run(debug=True) # port=5001 to run another time with this app. include it in app.run(..., port=5001)