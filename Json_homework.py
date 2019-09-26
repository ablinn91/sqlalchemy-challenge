#import all the things  
#import numpy as np ---have to have this comented out becouse numbpy has not ben able to use in
#the system. 

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Precipitation = Base.precipitation


app = Flask(__name__)

#welcome = "welcome to my 'Home' page here is a list of routs: "

@app.route("/")
def home():
    print("server received request  for 'Home' page...")
    #show the user the list of differnet pates 
    return (
        f"welcome to my 'Home' page here is a list of routs:<br/>"
        f":/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tops<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

if __name__ =="__main__":
    app.run(debug=True)    