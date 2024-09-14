![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

# FastApi Random Person

An extremely basic REST API with a single GET request that returns info for a random person.

-   Built With FastAPI
-   Random info is generated with Faker package

## Person Route

By default this will return 1 person. You can request more by supplying the `amount` query param

```
{API_URL}/person?amount=10
```
