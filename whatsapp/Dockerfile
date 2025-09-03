FROM node:20-alpine

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar package.json y package-lock.json
COPY package.json package-lock.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto de los archivos
COPY . .

ENV TZ=America/Asuncion

# Exponer el puerto
EXPOSE 3000

# Comando por defecto
CMD ["node", "index.js"]