from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

import sys 
sys.path.insert(0,'/Users/vadimatlassov/Desktop/MistralProject/mistral_model')

from mistral_llm import run_mistral, user_message

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    data = {"message": "Main Page"}
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@app.get("/user", response_class=HTMLResponse)
async def get_responses(request: Request):
    data = {"message":"Get User"}
    return templates.TemplateResponse("user.html", {"request": request, "data": data})

@app.get("/responses", response_class=HTMLResponse)
async def get_responses(request: Request):
    data = {"message":"Get Responses"}
    return templates.TemplateResponse("responses.html", {"request": request, "data": data})

@app.get("/settings", response_class=HTMLResponse)
async def get_settings(request: Request):
    data = {"message": "Get Settings"}
    return templates.TemplateResponse("settings.html",{"request":request, "data": data})


@app.post("/query")
async def post_query(request: Request, inp_text: str = Form(...)):
    if not inp_text:
        raise HTTPException(status_code=400, detail="Input text cannot be empty")
    mist_clf = run_mistral(user_message(inp_text))
    return templates.TemplateResponse("index.html", {"request": request, "bot_resp": mist_clf})
