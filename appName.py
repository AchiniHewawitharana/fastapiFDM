
from pydantic import BaseModel

class AppName(BaseModel):
    # island: str
    # culmenLength: float
    # culmenDepth: float
    # flipperLength: float
    # bodyMass: float
    # sex: str
    # species: str
    ##############################    name : str
    name = 'Online Girls Chat Group'

    def __getitem__(self, item):
        return getattr(self, item)

    # web: gunicorn -w 1 -k uvicorn.workers.UvicornWorker main:app