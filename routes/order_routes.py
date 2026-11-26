from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

templates = Jinja2Templates(
    directory="templates"
)

orders = []


@router.get("/", response_class=HTMLResponse)
async def orders_page(request: Request):

    return templates.TemplateResponse(
        "orders/order.html",
        {
            "request": request,
            "orders": orders
        }
    )
@router.post("/add")
async def add_order(
    food_name: str = Form(...),
    quantity: int = Form(...),
    price: float = Form(...)
):
    total = quantity * price
    order = {
        "food_name": food_name,
        "quantity": quantity,
        "price": price,
        "total": total,
        "status": "Pending"
    }

    orders.append(order)

    return RedirectResponse(
        url="/orders/",
        status_code=303
    )


@router.post("/update/{order_id}")
async def update_order(
    order_id: int,
    status: str = Form(...)
):

    if 0 <= order_id < len(orders):
        orders[order_id]["status"] = status

    return RedirectResponse(
        url="/orders/",
        status_code=303
    )