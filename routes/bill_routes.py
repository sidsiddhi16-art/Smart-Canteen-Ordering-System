from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/bills",
    tags=["Bill"]
)

templates = Jinja2Templates(
    directory="templates"
)


@router.get("/", response_class=HTMLResponse)
async def bill_page(request: Request):

    bill_items = [
        {
            "name": "Pizza",
            "quantity": 1,
            "price": 120,
            "total": 120
        },
        {
            "name": "Burger",
            "quantity": 2,
            "price": 80,
            "total": 160
        }
    ]

    grand_total = sum(
        item["total"] for item in bill_items
    )

    return templates.TemplateResponse(
        "bill/bill.html",
        {
            "request": request,
            "bill_items": bill_items,
            "grand_total": grand_total
        }
    )