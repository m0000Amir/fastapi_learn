from fastapi import APIRouter
from fastapi.params import Query, Body, Path


from pydantic import BaseModel
from typing import Optional, List, Dict



router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comment: int
    published: Optional[str]
    tags: List[str] = []
    metadata: Dict[str, str] = {"key": "value"}    
    image: Optional[Image] = None


@router.post("/new")
async def create_post(blog: BlogModel,
                      id: int,
                      version: int = 1):
    return {
        "id": id,
        "data": blog,
        "version": version
        }

    
@router.post("/new/{id}/comment{comment_id}")
async def create_comment(
    blog: BaseModel,
    id: int,
    comment_title: int = Query(None,
                            title="Id of the comment",
                            description="Some description for comment title",
                            alias="commentTitle", 
                            deprecated=True),
    content: str = Body(..., min_length=4, regex="^[a-z\s]*$"),
    v: Optional[List[str]] = Query(["1.0", "1.1", "1.2"]),
    comment_id:int = Path(None, gt=5, le=10)
    ):
    return {
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "v": v,
        "comment_id":  comment_id
    }


def required_functionality():
    return {"message": "Learning FastAPI is important"}