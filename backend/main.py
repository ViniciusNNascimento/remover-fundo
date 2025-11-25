from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from remover import remove_background_bytes

app = FastAPI(title="Removedor de Fundo - FastAPI + rembg")

# Permitir frontend acessar o backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Em produção você limita essa lista
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/remove-background")
async def remove_background(file: UploadFile = File(...)):
    # Valida tipo
    if not file.content_type or file.content_type.split("/")[0] != "image":
        raise HTTPException(status_code=400, detail="Arquivo enviado não é uma imagem")

    # Lê bytes da imagem enviada
    contents = await file.read()

    try:
        result_bytes = remove_background_bytes(contents)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar imagem: {e}")

    # Retorna imagem PNG sem fundo
    return Response(content=result_bytes, media_type="image/png")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
