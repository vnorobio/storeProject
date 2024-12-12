from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Product
from services import (
    get_products,
    get_product,
    create_product,
    update_product,
    delete_product
)

router = APIRouter()

# Obtener todos los productos
@router.get("/products/")
def fetch_products(db: Session = Depends(get_db)):
    return get_products(db)

# Obtener un producto por ID
@router.get("/products/{product_id}")
def find_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Producto noencontrado")
    return product

# Crear un nuevo producto
@router.post("/products/")
def save_product(product: Product, db: Session = Depends(get_db)):
    new_product = create_product(db, product)
    return {"mensaje": "Producto creado exitosamente", "producto":new_product}

# Actualizar un producto
@router.put("/products/{product_id}")
def update_a_product(product_id: int, updated_product: Product, db: Session = Depends(get_db)):
    product = update_product(db, product_id, updated_product)
    if not product:
        raise HTTPException(status_code=404, detail="Producto noencontrado")

    return {"mensaje": "Producto actualizado exitosamente", "producto":product}

# Eliminar un producto
@router.delete("/products/{product_id}")
def delete_a_product(product_id: int, db: Session = Depends(get_db)):
    deleted = delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Producto noencontrado")
    return {"mensaje": "Producto eliminado exitosamente"}
  
