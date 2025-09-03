# PEA

Proyecto PEA — backend y servicios relacionados.

Estructura principal:

- `backend/` — API Flask
- `flow/` — archivos de flujo
- `whatsapp/` — servicio WhatsApp (Node.js)

Cómo ejecutar (local):

1. Backend Python

   - Crear y activar virtualenv
   - Instalar dependencias: `pip install -r backend/requirements.txt`
   - Ejecutar: `python backend/app.py`

2. WhatsApp

   - Entrar en `whatsapp/` e instalar dependencias con npm
   - Ejecutar: `node index.js`

Docker: usar `docker-compose.yml` para levantar servicios.
