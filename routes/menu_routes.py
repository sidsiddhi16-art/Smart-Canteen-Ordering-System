from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/menu",
    tags=["Menu"]
)

templates = Jinja2Templates(
    directory="templates"
)


@router.get("/", response_class=HTMLResponse)
async def menu_page(request: Request):

    menu_items = [
        {
            "id": 1,
            "name": "Pizza",
            "price": 120
        },
        {
            "id": 2,
            "name": "Burger",
            "price": 80
        },
        {
            "id": 3,
            "name": "Sandwich",
            "price": 60
        },
        {
            "id": 4,
            "name": "Tea",
            "price": 20
        }
    ]

    return templates.TemplateResponse(
        "menu/menu.html",
        {
            "request": request,
            "menu_items": menu_items
        }
    )