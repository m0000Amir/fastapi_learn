from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional

from fastapi.param_functions import Depends

from router.blog_post import required_functionality


router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"



@router.get(
    "/all")
async def get_blogs(page=1, page_size: Optional[int]=None, 
                    req_parameter: dict = Depends(required_functionality)):
    return {"message": f"All {page_size} blogs on page {page}"}


@router.get(
    "/blog/{id}/comments/{comment_id}", tags=["comment"])
async def get_comment(id: int, comment_id: int, valid: bool = True, 
                      username: Optional[str] = None, 
                      req_parameter: dict = Depends(required_functionality)):
    return {"message": f"blog_id {id}, comment_id {comment_id},"
                       f"valid {valid}, username {username}"}


@router.get(
    "/blog/{id}", 
    status_code=status.HTTP_200_OK)
async def get_blog(id: int, response: Response, 
                   req_parameter: dict = Depends(required_functionality)):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id {id}"}    


@router.get(
    "/blog/type/{type}")
async def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}


