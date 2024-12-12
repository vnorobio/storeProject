from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Float
from database import Base

# Modelo de la tabla Products
class ProductEntity(Base):
    __tablename__ = "products"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, index=True)
    price: float = Column(Float)

    @classmethod
    def to_entity(cls, product: "Product") -> "ProductEntity":
        """
        Create a ProductEntity instance from a Product instance.

        :param product: The Product instance to convert.
        :return: A ProductEntity instance.
        """
        return ProductEntity(
            id=product.id,
            name=product.name,
            price=product.price,
        )
    
    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"


class Product(BaseModel):
    id: Optional[int] = Field(None, description="The unique identifier for the product")
    name: str = Field(..., max_length=255, description="The name of the product")
    price: float = Field(..., gt=0, description="Price of the product, must be greater than 0")

    @classmethod
    def from_entity(cls, entity: ProductEntity) -> "Product":
        """
        Create a Product instance from a ProductEntity instance.
    
        :param entity: The ProductEntity instance to convert.
        :return: A Product instance.
        """
        return cls(
            id=entity.id,
            name=entity.name,
            price=entity.price,
        )

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"
