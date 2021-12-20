from fastapi import APIRouter
from fastapi import responses
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request

from schemas import ProductBase


router = APIRouter(
    prefix="/templates",
    tags=["templates"]
)

templates = Jinja2Templates(directory="templates")


@router.post("/product/{id}", response_class=HTMLResponse)
def get_product(id: str, 
                product: ProductBase,
                request: Request):
    return templates.TemplateResponse(
        "product.html",
        {
            "request": request,
            "id": id,
            "title": product.title,
            "description": product.description,
            "price": product.price
        }

    )