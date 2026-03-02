#!/usr/bin/env python3
"""
Genera photos_list.js escaneando la carpeta imagenes/
Uso: python generate_photo_list.py
"""
import os
import json

IMAGENES_DIR = "imagenes"
OUTPUT_FILE  = "photos_list.js"
EXTENSIONS   = {".jpg", ".jpeg", ".png", ".webp", ".JPG", ".JPEG", ".PNG"}

def generate():
    if not os.path.isdir(IMAGENES_DIR):
        print(f"ERROR: No existe la carpeta '{IMAGENES_DIR}'")
        return

    files = sorted([
        f for f in os.listdir(IMAGENES_DIR)
        if os.path.splitext(f)[1] in EXTENSIONS
    ])

    if not files:
        print("No se encontraron imágenes en la carpeta 'imagenes/'")
        photos_js = "const photos = [];\n"
    else:
        photos = []
        for filename in files:
            name = os.path.splitext(filename)[0]
            photos.append({
                "name":     name,
                "filename": filename,
                "path":     f"imagenes/{filename}"
            })

        lines = ["const photos = ["]
        for p in photos:
            lines.append(f"  {{ name: {json.dumps(p['name'])}, filename: {json.dumps(p['filename'])}, path: {json.dumps(p['path'])} }},")
        lines.append("];")
        photos_js = "\n".join(lines) + "\n"
        print(f"✓ {len(photos)} fotos encontradas")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(photos_js)

    print(f"✓ Generado: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate()
