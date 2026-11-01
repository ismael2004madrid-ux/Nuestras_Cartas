from PIL import Image, ImageDraw, ImageFont
from datetime import date
from zoneinfo import ZoneInfo
from pathlib import Path

# Configuración
FECHA_INICIO = date(2026, 10, 2)
COLOR = "#713D4B"
ANCHO, ALTO = 1400, 220

# Calcular días transcurridos en España
hoy = date.today()
dias = (hoy - FECHA_INICIO).days

# Crear imagen transparente
imagen = Image.new("RGBA", (ANCHO, ALTO), (0, 0, 0, 0))
dibujo = ImageDraw.Draw(imagen)

# Cargar tipografía Domine en cursiva y negrita
fuente_principal = ImageFont.truetype(
    "fonts/Domine-Italic.ttf", 66
)
fuente_subtitulo = ImageFont.truetype(
    "fonts/Domine-Italic.ttf", 32
)

# Aplicar grosor 700 si la fuente es variable
fuente_principal.set_variation_by_axes([700])
texto_subtitulo = "Desde el 2 de octubre de 2026"
corazon = "♥"
fuente_corazon = ImageFont.truetype("fonts/Corazon.ttf", 32)

# Textos
texto_principal = f"Llevamos {dias} días juntos"
texto_subtitulo = "Desde el 2 de octubre de 2026 ♥"

# Centrar textos
caja1 = dibujo.textbbox((0, 0), texto_principal, font=fuente_principal)
ancho1 = caja1[2] - caja1[0]
x1 = (ANCHO - ancho1) / 2
dibujo.text((x1, 35), texto_principal, font=fuente_principal, fill=COLOR)

caja2 = dibujo.textbbox((0, 0), texto_subtitulo, font=fuente_subtitulo)
ancho2 = caja2[2] - caja2[0]

caja_corazon = dibujo.textbbox((0, 0), corazon, font=fuente_corazon)
ancho_corazon = caja_corazon[2] - caja_corazon[0]

espacio = 12
ancho_total = ancho2 + espacio + ancho_corazon
x2 = (ANCHO - ancho_total) / 2

dibujo.text((x2, 125), texto_subtitulo, font=fuente_subtitulo, fill=COLOR)
dibujo.text(
    (x2 + ancho2 + espacio, 125),
    corazon,
    font=fuente_corazon,
    fill=COLOR
)

# Guardar PNG
imagen.save("contador.png")
print(f"Contador generado: {dias} días")
