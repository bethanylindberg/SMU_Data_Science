import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

# Calculate the date 1 year ago from the last data point in the database
last_date = session.query(func.strftime(Measurement.date)).order_by(Measurement.date.desc()).first()[0]
#Slice string as int then perform timedelta calculation and convert back to string
query_date = str(dt.date(int(last_date[0:4]),int(last_date[5:7]),int(last_date[8:10])) - dt.timedelta(days=365))
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
        f"/api/v1.0/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of date and sum of precipitation for all dates in the db"""
    results = session.query(Measurement.date,func.sum(Measurement.prcp)).\
                            group_by(Measurement.date).all()
    precipitation = []
    for date,prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precipitation.append(precipitation_dict)
    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations from the db"""
    results = session.query(Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation).\
                                group_by(Station.station).all()
    stations = list(np.ravel(results))

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of date and average temperature for last year of db"""
    results = session.query(Measurement.date,func.avg(Measurement.tobs)).\
                        filter(func.strftime(Measurement.date>query_date)).\
                        filter(func.strftime(Measurement.date<last_date)).\
                        group_by(Measurement.date).all()
    temperature = []
    for date,tobs in results:
        temperature_dict = {}
        temperature_dict["date"] = date
        temperature_dict["tobs"] = tobs
        temperature.append(temperature_dict)
    return jsonify(temperature)

@app.route("/api/v1.0/start/<start>")
def start(start):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start:
    calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date supplied by the user, or a 404 if not date is not in db."""

    canonicalized = str(start)
    
    results = session.query(Measurement.date,func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
            filter(func.strftime(Measurement.date>canonicalized)).all()

    for result in results:
        search_term = str(results[0][0])

        temperatures = []
        if search_term == canonicalized:
            for result in results:
                temperature_dict = {}
                temperature_dict["tmin"] = result[0][1]
                temperature_dict["tavg"] = result[0][2]
                temperature_dict["tmax"] = result[0][3]
                temperatures.append(temperature_dict)
        
            return jsonify(temperatures)
            
        return jsonify({"error": "Date not found."}), 404

@app.route("/api/v1.0/start/<start>/end/<end>")
def startend(start,end):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start:
    calculate TMIN, TAVG, and TMAX for all dates between the start and end date provided by userinclusive, or a 404 if not date is not in db."""

    canonicalizedstart = str(start)
    canonicalizedend = str(end)

    results = session.query(func.min(Measurement.date),func.max(Measurement.date),func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
            filter(func.strftime(Measurement.date>canonicalizedstart)).\
            filter(func.strftime(Measurement.date<canonicalizedend)).all()

    for result in results:
        search_termstart = str(result[0][0])
        search_termend = str(result[0][1])

        temperaturese = []
        if search_termstart == canonicalizedstart and search_termend == canonicalizedend:
            for result in results:
                temperature_dict = {}
                temperature_dict["tmin"] = result[0][2]
                temperature_dict["tavg"] = result[0][3]
                temperature_dict["tmax"] = result[0][4]
                temperaturese.append(temperature_dict)
        
            return jsonify(temperaturese)
            
        return jsonify({"error": "Date not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
