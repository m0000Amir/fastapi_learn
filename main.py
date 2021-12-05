"""

HERE database is created

"""
from fastapi import FastAPI, HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.responses import PlainTextResponse
from exceptions import StoryException
from router import blog_get, blog_post
from router import user
from router import article
from db import models
from db.database import engine

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)


@app.get("/hello")
async def index():
    return {"message": "Hello world"}


@app.exception_handler(StoryException)
def story_exceptions_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={"detail": exc.name}
    )


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)


models.Base.metadata.create_all(engine)
