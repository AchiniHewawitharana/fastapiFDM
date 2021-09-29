#import General.Plotting.auxiliary_plotting_functions as aux_plot  # pylint: disable=import-error
#import General.Misc.general_tools as tools  # type: ignore
from fastapi import FastAPI

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.
@app.get("/")
def home():
    return {"message":"Hello TutLinks.com"}
    #web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app