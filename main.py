from flask import Flask, render_template #Flask = class
import pandas as pd #import pandas library

app = Flask(__name__)



#integrate the index.html in main.py
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>") #create a route for the API and is dynamic (station and date)
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt" #takes the path of file and reads it
    df= pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"]) #skips some rows in the file
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10 #locates the date and squeezes the value to get the temperature
    return {"station": station,
            "date": date,
             "temperature": temperature}

#run the app
if(__name__) == "__main__":
  app.run(debug=True) # port=5001 to run another time with this app. include it in app.run(..., port=5001)