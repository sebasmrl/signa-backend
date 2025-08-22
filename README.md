
# Instalaciones

``` bash
#Traer a uvicorn pydantic python-multipart etc
pip install fastapi[standard]
```


## Actualizar pip 
```
python.exe -m pip install --upgrade pip
```

## Levantar servidor
Posicionate en la raiz del proyecto backend ``cd ./signa/backend`` y luego ejecuta:

```bash
#Desarrollo
fastapi dev main.py

# con Uvicorn directo
uvicorn main:app

```