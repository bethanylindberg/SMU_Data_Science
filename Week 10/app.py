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
        f"/api/v1.0/preciptation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/station"
    )


@app.route("/api/v1.0/precipitation")
def precipation():
    """Return a list of all precipitation"""
    # Calculate the date 1 year ago from the last data point in the database
    last_date = session.query(func.strftime(Measurement.date)).order_by(Measurement.date.desc()).first()[0]
    #Slice string as int then perform timedelta calculation and convert back to string
    query_date = str(dt.date(int(last_date[0:4]),int(last_date[5:7]),int(last_date[8:10])) - dt.timedelta(days=365))

    results = session.query(Measurement.date,func.sum(Measurement.prcp)).\
                    filter(func.strftime(Measurement.date>query_date)).\
                    filter(func.strftime(Measurement.date<last_date)).\
                    group_by(Measurement.date).all()
    precipitation = []
    for date,prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precipitation.append(precipitation_dict)
    return jsonify(precipitation)

if __name__ == '__main__':
    app.run(debug=True)
