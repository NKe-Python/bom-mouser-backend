from pydantic import BaseModel

class BOMItem(BaseModel):
    quantity: int
    manufacturer: str
    mpn: str

class PurchaseItem(BaseModel):
    mpn: str
    mouser_part: str
    quantity: int
    price_per_unit: float
    total_price: float
    stock: int