# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
from pathlib import Path

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import Engine, create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(Engine, reflect = True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
