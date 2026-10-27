from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.rotas import cliente

app = FastAPI(
    title = "TechLog Solutions API",
    description = "CRM para TechLog Solutions.",
    version = "1.0.0",
)

@app.get("/")
async def health_check():
    return {"status" : "OK"}

app.include_router(cliente.router)

@app.get("/front", response_class = HTMLResponse)
async def front_page():
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>FrontTechLogSolutions</title>
        </head>
        <body>
            <h1>TechLog Solutions</h1>
            <p>Sistema de Gestão de Ordens de Serviço</p>
            <p>Status: <strong>Operacional</strong></p>
        </body>
    </html>
    """
    return html_content