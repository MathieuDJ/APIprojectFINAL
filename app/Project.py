from fastapi import FastAPI, Query
from random import randint
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
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
            'model': 'test1',
            'horsepower': '800'},

           {'brand': 'ferrari',
            'model': 'test2',
            'horsepower': '900'},

           {'brand': 'ferrari',
            'model': 'test4',
            'horsepower': '900'},

           {'brand': 'ferrari',
            'model': 'test5',
            'horsepower': '900'},


           {'brand': 'ferrari',
            'model': 'test6',
            'horsepower': '900'},


           {'brand': 'ferrari',
            'model': 'test7',
            'horsepower': '900'}
           ]


mercedes = [{'brand': 'mercedes',
            'model': 'G-500',
            'horsepower': '416'},

            {'brand': 'mercedes',
             'model': 'G-501',
             'horsepower': '416'},

            {'brand': 'mercedes',
             'model': 'G-502',
             'horsepower': '416'},

            {'brand': 'mercedes',
             'model': 'G-503',
             'horsepower': '416'},

            {'brand': 'mercedes',
             'model': 'G-504',
             'horsepower': '416'},

            {'brand': 'mercedes',
             'model': 'G-505',
             'horsepower': '416'},

            {'brand': 'mercedes',
             'model': 'G-506',
             'horsepower': '416'},]


class Ferrari(BaseModel):
    brand: str = Query(default="ferrari")
    model: str
    horsepower: int

@app.get("/car/ferrari/") #mss met while loop
async def get_car(number: int = Query(default=2, le=len(ferrari), description="This parameter is for determining how many ferrari's you want to see, the default value is 2")):
    cars = []
    for i in range(number):
        new_car = ferrari[randint(0, len(ferrari) - 1)]
        cars.append(new_car)
    return {"ferrari's": cars}

@app.get("/car/mercedes/")
async def get_car(number: int = Query(default=2, le=len(mercedes), description="This parameter is for determining how many mercedes you want to see, the default value is 2")):
    cars = []
    for i in range(number):
        new_car = mercedes[randint(0, len(mercedes) - 1)]
        cars.append(new_car)
    return {"Mercedes": cars}

@app.post("/car/ferrari/")
async def create_ferrari(ferrarie: Ferrari):
    ferrari.append(ferrarie)
    return ferrari

