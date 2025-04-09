from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import RedirectResponse
import base64

app = FastAPI()
BASE_URL = "http://localhost:8000"

@app.get("/acortar")
def acortar(url: str = Query(..., description="URL a acortar")):
    encoded = base64.urlsafe_b64encode(url.encode()).decode()
    return {"short_url": f"{BASE_URL}/{encoded}"}

@app.get("/{slug}")
def redirigir(slug: str):
    try:
        decoded = base64.urlsafe_b64decode(slug.encode()).decode()
        return RedirectResponse(url=decoded)
    except Exception:
        raise HTTPException(status_code=400, detail="Slug inválido")
