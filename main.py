from fastapi import FastAPI

app = FastAPI()

# La barra del get "/" se usa para mostrar donde se visualizarán


@app.get("/")
async def root():
    return "¡Hola FastAPI!"

# Aquí se mostrará en /url
# No es correcto llamar a lo mismo siempre


@app.get("/url")
async def root():
    return {"url_curso": "https://francodev.com/python"}


# Operación GET
# 1.29.47 - MoureDev
