from rembg import remove
from PIL import Image
import io

def remove_background_bytes(image_bytes: bytes) -> bytes:
    """
    Recebe bytes de imagem e retorna bytes PNG com fundo transparente.
    """

    # Abre a imagem a partir de bytes
    input_buffer = io.BytesIO(image_bytes)
    input_image = Image.open(input_buffer).convert("RGBA")

    # Redimensionamento opcional para não travar o PC
    MAX_SIDE = 2048
    if max(input_image.size) > MAX_SIDE:
        scale = MAX_SIDE / max(input_image.size)
        new_size = (int(input_image.width * scale), int(input_image.height * scale))
        input_image = input_image.resize(new_size, Image.LANCZOS)

    # 💡 CORREÇÃO: transforma a imagem em bytes antes de passar para o rembg
    img_byte_arr = io.BytesIO()
    input_image.save(img_byte_arr, format="PNG")
    img_bytes_for_rembg = img_byte_arr.getvalue()

    # Remove o fundo usando bytes (forma 100% compatível com rembg)
    result = remove(img_bytes_for_rembg)

    # Retorna o PNG final
    return result
