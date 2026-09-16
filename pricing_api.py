from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate-discount")
def calculate_discount(tier: str, total: float):
    """The complex if/else logic lives safely hidden inside this API."""
    discount = 0.0
    
    # Messy 10 lines of conditional business logic
    if tier.lower() == "platinum":
        discount = 0.20  # 20% off
    elif tier.lower() == "gold":
        discount = 0.10  # 10% off
    elif tier.lower() == "silver":
        discount = 0.05  # 5% off
    else:
        if total > 100:
            discount = 0.02  # 2% off for big spenders
        else:
            discount = 0.0   # No discount

    final_price = total * (1 - discount)
    
    # Return the clean calculated results
    return {"original_total": total, "discount_applied": discount, "final_price": final_price}
