def calculate_discount(price: float, discount: float) -> float:
    if discount < 0 or discount > 1:
        raise ValueError('Discount must be between 0 and 1')

    return price - price * discount
