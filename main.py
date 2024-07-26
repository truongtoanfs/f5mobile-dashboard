from fastapi import FastAPI
from routes import categories, products
import uvicorn

app = FastAPI()

app.include_router(categories.router)
app.include_router(products.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, log_level="info", reload=True)
