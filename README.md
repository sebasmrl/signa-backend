
## Actualizar pip 
```
python.exe -m pip install --upgrade pip
```

## Instalaciones
```bash
#para desarrollo se pueden ejecutar las dependencias directamente en consola de comandos

# O bien hacer lo mismo para produccion ejecutando:
# requirements.txt es quien contiene las depencias con las versiones explicitas con als que el proyecto se ejecuta correctamente
pip install -r requirements.txt

```



## Levantar servidor
Posicionate en la raiz del proyecto backend ``cd ./signa/backend`` y luego ejecuta:

```bash

#Desarrollo
fastapi dev main.py

#Con live reloading
uvicorn main:app --reload 

#Sin live reloading
uvicorn main:app

#Produccion
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

```

## Dependencias

``` bash
#Trae a uvicorn pydantic python-multipart etc
pip install fastapi[standard]
pip install SQLAlchemy
```
