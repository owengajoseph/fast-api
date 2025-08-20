from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = False, sort: Optional[str] = None):
    # return published
    if published:
        return {'data': f'{limit} published blog from db'}
    else:
        return {'data': f'{limit} from db'}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return request
    return {'data': {'blog created'}}
