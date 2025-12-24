from fastapi import FastAPI
from typing import List

from models import BOMItem, PurchaseItem
from mouser import search_mouser

app = FastAPI(title="BOM → Mouser Einkaufsliste")

@app.post("/purchase-list", response_model=List[PurchaseItem])
def create_purchase_list(items: List[BOMItem]):
    result = []

    for item in items:
        data = search_mouser(item.mpn)
        parts = data["SearchResults"]["Parts"]

        if not parts:
            continue

        part = parts[0]
        price = float(part["PriceBreaks"][0]["Price"].replace("€", "").strip())
        stock = int(part.get("AvailabilityInStock") or 0)

        result.append({
            "mpn": item.mpn,
            "mouser_part": part["MouserPartNumber"],
            "quantity": item.quantity,
            "price_per_unit": price,
            "total_price": round(price * item.quantity, 4),
            "stock": stock
        })

    return result