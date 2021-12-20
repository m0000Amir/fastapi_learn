"""

HERE database is created

"""
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions import StoryException
from router import blog_get, blog_post, user, article, product, file
from auth import authentification
from db import models
from db.database import engine
from fastapi.staticfiles import StaticFiles
from templates import templates


app = FastAPI()
app.include_router(authentification.router)
app.include_router(file.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(templates.router)



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

origins = [
    "http://localhost:3000"
]

# TODO: I skipped part8 with CORS. It is necessary to be back in future.


app.mount("/files", StaticFiles(directory="files"), name="files")
app.mount("/templates/static", 
          StaticFiles(directory="templates/static"),
          name="static")   


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
