from decimal import Decimal, ROUND_HALF_UP

print("=== Калькулятор скидок ===")

def check_promo_code(code):
    if code == "WELCOME10":
        return 10
    elif code =="SALE20":
        return 20
    elif code == "VIP30":
        return 30
    else:
        return 0

def calculate_discount(price, discount_percent):
    price = Decimal(str(price))
    discount_percent = Decimal(str(discount_percent))

    discount_amount = price * discount_percent / Decimal("100")
    final_price = price - discount_amount

    return final_price.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )
