from datetime import date, datetime
from fastapi import FastAPI
from pydantic import BaseModel
from faker import Faker

app = FastAPI()
faker = Faker()

@app.get("/")
async def root():
    return {"message": "Welcome"}

class AddressModel(BaseModel):
    street_address: str
    postal: str
    city: str
    country: str

class PersonModelList(BaseModel):
    uid: str
    name: str
    email: str
    date_of_birth: date
    phone_number: str
    ssn: str
    occupation: str
    address: AddressModel

class PersonModel(BaseModel):
    success: int
    results: int
    data: list[PersonModelList]

@app.get("/person", response_model=PersonModel)
async def get_person(amount: int = 1):
    persons = []
    
    for _ in range(amount):
        name = faker.name()
        email = name.split()[0].lower() + "." + name.split()[1].lower() + "@" + faker.free_email_domain()

        persons.append({
            "uid": faker.ean(length=13),
            "name": name,
            "email": email,
            "date_of_birth": faker.date_of_birth(),
            "phone_number": faker.phone_number(),
            "ssn": faker.ssn(),
            "occupation": faker.job(),
            "address": {
                "street_address": faker.street_address(),
                "postal": faker.postcode(),
                "city": faker.city(),
                "country": faker.country() 
            }
        })
    
    # name = faker.name()
    return {
        "success": 1,
        "results": amount,
        "data": persons
    }

