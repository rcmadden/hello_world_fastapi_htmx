from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
        <script src="https://unpkg.com/htmx.org@1.9.8"></script>
    </head>
    <body>
        <h1 id="hello">Hello, World!</h1>
        <button hx-get="/update" hx-target="#hello">Click me!</button>
    </body>
    </html>
    """

@app.get("/update", response_class=HTMLResponse)
async def update_text():
    return """
    <h1 id="hello">Hello, FastAPI & htmx!</h1>
    <button hx-get="/update" hx-target="#hello">Click me again!</button>
    """
