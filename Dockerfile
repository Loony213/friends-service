FROM golang:1.20

WORKDIR /app

# Copiar los archivos del proyecto
COPY go.mod ./
COPY go.sum ./
RUN go mod download

COPY . .

# Compilar el binario
RUN go build -o friends-service

# Exponer el puerto
EXPOSE 8080

# Ejecutar
CMD ["./friends-service"]
