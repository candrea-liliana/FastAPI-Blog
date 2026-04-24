from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app =  FastAPI()

# Whow to access statit folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Template rendering
templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Lili Candrea",
        "title": "FastApi is awesome",
        "content": "This is the content",
        "date_posted": "April 24, 2026"
    },
    {
        "id": 2,
        "author": "Author2",
        "title": "FastApi is great",
        "content": "This is the second content",
        "date_posted": "April 24, 2026"
    }
]


@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request,"home.html", {"posts": posts, "title": "Home"})


@app.get("/api/posts")
def get_posts():
    return posts