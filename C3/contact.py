from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def root_GET():
    return RedirectResponse("/contacts", status_code=302)


@app.get("/contacts")
def contacts_GET(search_term: str | None = None):
    pass
