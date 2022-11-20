from fastapi import FastAPI, Query
from random import randint
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
     "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:27376",
    "http://127.0.0.1:27376",
    "https://randomizer-service-mathieudj.cloud.okteto.net",
    "https://MathieuDJ.github.io",
    "https://mathieudj.github.io."
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ferrari = [{'brand': 'ferrari',
            'model': '812',
            'horsepower': '789'},

           {'brand': 'ferrari',
            'model': '296GTB',
            'horsepower': '800'},

           {'brand': 'ferrari',
            'model': 'SF90',
            'horsepower': '910'},

           {'brand': 'ferrari',
            'model': 'F8',
            'horsepower': '754'},

           {'brand': 'ferrari',
            'model': 'Monza SP1',
            'horsepower': '900'},


           {'brand': 'ferrari',
            'model': '166 Inter',
            'horsepower': '560'},


           {'brand': 'ferrari',
            'model': '348',
            'horsepower': '780'}
           ]


mercedes = [{'brand': 'mercedes',
            'model': 'G-500',
            'horsepower': '416'},

            {'brand': 'mercedes',
             'model': 'GLA',
             'horsepower': '230'},

            {'brand': 'mercedes',
             'model': 'C-Class',
             'horsepower': '354'},

            {'brand': 'mercedes',
             'model': 'GLS',
             'horsepower': '280'},

            {'brand': 'mercedes',
             'model': 'AMG GT',
             'horsepower': '680'},

            {'brand': 'mercedes',
             'model': 'AMG G63',
             'horsepower': '516'},

            {'brand': 'mercedes',
             'model': 'V-Class',
             'horsepower': '416'},]


class Ferrari(BaseModel):
    brand: str = Query(default="ferrari")
    model: str
    horsepower: int

class Mercedes(BaseModel):
    brand: str = Query(default="mercedes")
    model: str
    horsepower: int

@app.get("/car/ferrari/") #mss met while loop
async def get_car(number: int = Query(default=2, le=len(ferrari), description="This parameter is for determining how many ferrari's you want to see, the default value is 2")):
    cars = []
    for i in range(number):
        new_car = ferrari[randint(0, len(ferrari) - 1)]
        cars.append(new_car)
    return {"ferraris": cars}

@app.get("/car/mercedes/")
async def get_car(number: int = Query(default=2, le=len(mercedes), description="This parameter is for determining how many mercedes you want to see, the default value is 2")):
    cars = []
    for i in range(number):
        new_car = mercedes[randint(0, len(mercedes) - 1)]
        cars.append(new_car)
    return {"Mercedes": cars}

@app.post("/car/ferrari/")
async def create_ferrari(ferrarie: Ferrari):
    ferrari.append(ferrarie.dict())
    return ferrari

@app.post("/car/mercedes/")
async def create_mercedes(mercedees: Mercedes):
    mercedes.append(mercedees.dict())
    return mercedes
