from flask import Flask

app = Flask(__name__)

@app.route('/')
#def hello_world():
    #return 'Hello world'

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
