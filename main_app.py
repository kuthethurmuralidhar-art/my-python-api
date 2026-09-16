import requests

def get_final_bill(customer_tier: str, bill_amount: float):
    """Calls the API to handle the complex math/logic in one line."""
    url = f"http://localhost:8000/calculate-discount?tier={customer_tier}&total={bill_amount}"
    
    # Single step: Ask the API for the answer
    response = requests.get(url).json()
    return response["final_price"]

# --- Main App Execution ---
if __name__ == "__main__":
    # Clean and simple inputs
    tier = "Gold"
    amount = 200.00
    
    # Call our logic with zero local if/else statements!
    to_pay = get_final_bill(tier, amount)
    
    print(f"Customer Tier: {tier}")
    print(f"Final Amount to Pay: ${to_pay}")
