from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)
# -----------------------------------------
# Food Data
# -----------------------------------------
foods = [
    {
        "name": "Pizza",
        "category": "Fast Food",
        "price": 120,
        "description": "Delicious cheese pizza"
    },
    {
        "name": "Burger",
        "category": "Fast Food",
        "price": 80,
        "description": "Fresh and tasty burger"
    },
    {
        "name": "French Fries",
        "category": "Snacks",
        "price": 60,
        "description": "Crispy golden french fries"
    },
    {
        "name": "Sandwich",
        "category": "Snacks",
        "price": 70,
        "description": "Fresh vegetable sandwich"
    },
    {
        "name": "Noodles",
        "category": "Chinese",
        "price": 90,
        "description": "Hot and tasty noodles"
    },
    {
        "name": "Veg Thali",
        "category": "North Indian",
        "price": 100,
        "description": "Complete delicious veg thali"
    },
    {
        "name": "Cold Drink",
        "category": "Drinks",
        "price": 40,
        "description": "Refreshing cold drink"
    },
    {
        "name": "Tea",
        "category": "Drinks",
        "price": 20,
        "description": "Hot and refreshing tea"
    },
    {
        "name": "Coffee",
        "category": "Drinks",
        "price": 30,
        "description": "Hot and refreshing coffee"
    }
]
# -----------------------------------------
# Owner Dashboard
# -----------------------------------------
@app.get("/owner")
def owner_dashboard(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="owner.html"
    )

# -----------------------------------------
# Home
# -----------------------------------------
@app.get("/home")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="home.html"
    )
# -----------------------------------------
# Menu
# -----------------------------------------
@app.get("/menu")
def menu(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="menu.html",
        context={
            "foods": foods
        }
    )
# -----------------------------------------
# Add Food Page
# -----------------------------------------
@app.get("/add-food")
def add_food_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="add_food.html"    )
# -----------------------------------------
# Orders
# -----------------------------------------
@app.get("/orders")
def orders(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="orders.html",
        context={
            "foods": foods
        }
    )
# -----------------------------------------
# Bill
# -----------------------------------------

@app.get("/bill")
def bills(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="bill.html"
    )
