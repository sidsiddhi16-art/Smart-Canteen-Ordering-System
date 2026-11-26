from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from services.owner_services import (
    get_today_sales,
    get_yesterday_sales,
    get_total_orders,
    get_pending_orders,
    get_completed_orders,
    get_today_orders,
    get_food_order_details
)

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/owner")
def owner_dashboard(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="owner.html",
        context={
            "today_sales": get_today_sales(),
            "yesterday_sales": get_yesterday_sales(),
            "total_orders": get_total_orders(),
            "pending_orders": get_pending_orders(),
            "completed_orders": get_completed_orders(),
            "today_orders": get_today_orders(),
            "food_orders": get_food_order_details()
        }
    )