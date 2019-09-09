import numpy as np
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite", pool_pre_ping=True)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

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
        f"/api/v1.0/yyyy-mm-dd<br/>"
        f"/api/v1.0/api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of date and sum of precipitation for all dates in the db"""
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results = session.query(Measurement.date,func.sum(Measurement.prcp)).\
                            group_by(Measurement.date).all()
    precipitation = []
    for date,prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["total precipitation"] = prcp
        precipitation.append(precipitation_dict)
    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    """Return a dictionary of stations from the db"""
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results = session.query(Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation).\
                                group_by(Station.station).all()
    y=0
    stationlist=[]
    for _ in results:
        stationdictouter = {}
        stationdictinner = {}
        stationdictouter[results[y][0]] = stationdictinner
        stationdictinner["Station Name"] = results[y][1]
        stationdictinner["Station Latitude"] = results[y][2]
        stationdictinner["Station Longitude"] = results[y][3]
        y +=1
        stationlist.append(stationdictouter)

    return jsonify(stationlist)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of date and average temperature for last year of db"""
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results = session.query(Measurement.date,func.avg(Measurement.tobs)).\
                        filter(func.strftime(Measurement.date>query_date)).\
                        filter(func.strftime(Measurement.date<last_date)).\
                        group_by(Measurement.date).all()
    temperature = []
    for date,tobs in results:
        temperature_dict = {}
        temperature_dict["date"] = date
        temperature_dict["average_temperature"] = tobs
        temperature.append(temperature_dict)
    return jsonify(temperature)

@app.route("/api/v1.0/<start>")
def start(start):
#     """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start:
#     calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date supplied by the user"""

    session = Session(engine)
    start = str(start)
    end = last_date

    d1 = dt.date(int(start[0:4]),int(start[5:7]),int(start[8:10]))
    d2 = dt.date(int(end[0:4]),int(end[5:7]),int(end[8:10]))
    # Use the start and end date to create a range of dates
    daterange = [str(d1 + dt.timedelta(days=x)) for x in range((d2-d1).days + 1)]
    # Stip off the year and save a list of %m-%d strings
    md = [x[5:10] for x in daterange]
    # Loop through the list of %m-%d strings and calculate the normals for each date
    normals = [session.query(*sel).filter(func.strftime("%m-%d", Measurement.date) == x).all()[0] for x in md]
    normlist = []
    y = 0
    for _ in normals:
       normdictouter = {}
       normdictinner = {}
       normdictouter[daterange[y]] = normdictinner
       normdictinner["minimum temperature"] = normals[y][0]
       normdictinner["average temperature"] = normals[y][1]
       normdictinner["max temperature"] = normals[y][2]
       y +=1
       normlist.append(normdictouter)
    return jsonify(normlist )

@app.route("/api/v1.0/<start>/<end>")
def startend(start,end):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start:
    calculate TMIN, TAVG, and TMAX for all dates between the start and end date provided by user inclusive"""
    # Create our session (link) from Python to the DB
    session = Session(engine)
    start = str(start)
    end = str(end)

    d1 = dt.date(int(start[0:4]),int(start[5:7]),int(start[8:10]))
    d2 = dt.date(int(end[0:4]),int(end[5:7]),int(end[8:10]))
    # Use the start and end date to create a range of dates
    daterange = [str(d1 + dt.timedelta(days=x)) for x in range((d2-d1).days + 1)]
    # Stip off the year and save a list of %m-%d strings
    md = [x[5:10] for x in daterange]
    # Loop through the list of %m-%d strings and calculate the normals for each date
    normals = [session.query(*sel).filter(func.strftime("%m-%d", Measurement.date) == x).all()[0] for x in md]
    normlist = []
    y = 0
    for _ in normals:
       normdictouter = {}
       normdictinner = {}
       normdictouter[daterange[y]] = normdictinner
       normdictinner["minimum temperature"] = normals[y][0]
       normdictinner["average temperature"] = normals[y][1]
       normdictinner["max temperature"] = normals[y][2]
       y +=1
       normlist.append(normdictouter)
    return jsonify(normlist )

if __name__ == '__main__':
    app.run(debug=True)
