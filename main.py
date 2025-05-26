from flask import Flask, render_template #Flask = class

app = Flask(__name__)

#integrate the index.html in main.py
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>") #create a route for the API and is dynamic (station and date)
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
             "temperature": temperature}

#run the app
if(__name__) == "__main__":
  app.run(debug=True) # port=5001 to run another time with this app. include it in app.run(..., port=5001)