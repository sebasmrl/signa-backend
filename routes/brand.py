from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, update, delete

from config.db import conn
from models.brand import brands
from schemas.brand import Brand


brand = APIRouter(prefix='/brands')


@brand.get('', response_model=list[Brand])
def get_brand():
    result = conn.execute(select(brands))     
    rows = result.mappings().all()            
    return jsonable_encoder(rows) 

@brand.get("/{id}", response_model=Brand)
def get_brand(id: int):
    result = conn.execute(
        select(brands).where(brands.c.id == id)
    ).mappings().first()

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Marca con {id} no encontrada")

    return result

@brand.post('', status_code=status.HTTP_201_CREATED, response_model=Brand)
def create_brand(brand: Brand):
    new_brand = brand.model_dump(include={"brand", "owner", "state"})

    rs = conn.execute(brands.insert().values(new_brand))
    conn.commit()
    
    result = conn.execute(
        brands.select().where(brands.c.id == rs.lastrowid)
    )
    row = result.mappings().first() 
    return jsonable_encoder(row)   


@brand.put("/{id}", status_code=status.HTTP_200_OK, response_model=Brand)
def update_brand(id: int, brand: Brand):
    rs = conn.execute(
        update(brands)
        .where(brands.c.id == id)
        .values(owner=brand.owner, brand=brand.brand, state=brand.state)
    )
    conn.commit()

    if rs.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Marca con {id} no encontrda")

    updated = conn.execute(
        select(brands).where(brands.c.id == id)
    ).mappings().first()
    return updated


@brand.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_brand(id: int):
    rs = conn.execute(delete(brands).where(brands.c.id == id))
    conn.commit()

    if rs.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Marca con {id} no encontrada")

    return {"msg": f"Marca con {id} ha sido eliminada"}
