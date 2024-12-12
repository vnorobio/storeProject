from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models import Product, ProductEntity

def get_products(db: Session) -> list[Product]:
    return [Product.from_entity(entity) for entity in db.query(ProductEntity).all()]

def get_product(db: Session, product_id: int):
    return db.query(ProductEntity).filter(ProductEntity.id == product_id).first()

def create_product(db: Session, product: Product):
    try:
        db_product = ProductEntity.to_entity(product)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
    except IntegrityError as e:
        db.rollback()
        raise ValueError(f"Failed to create product: {e}")

def update_product(db: Session, product_id: int, updated_product: Product):
    product = get_product(db, product_id)
    if product:
        product.name = updated_product.name
        product.price = updated_product.price
        db.commit()
        db.refresh(product)
        return product
    return None

def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    if product:
        db.delete(product)
        db.commit()
        return True
    return False
  
