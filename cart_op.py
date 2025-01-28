import json
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @classmethod
    def load(cls, data):
        """Class method to load cart data from dictionary"""
        return cls(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    """Retrieve the products in a cart for a given user"""
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    items = []
    for cart_detail in cart_details:
        try:
            contents = eval(cart_detail['contents'])  # Assuming contents is a string representation of a list
            # Add the products associated with the contents directly
            items.extend([products.get_product(content_id) for content_id in contents])
        except (SyntaxError, ValueError) as e:
            print(f"Error processing cart contents: {e}")  # log the error for better troubleshooting
    
    return items


def add_to_cart(username: str, product_id: int):
    """Add a product to the user's cart"""
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    """Remove a product from the user's cart"""
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    """Delete the user's entire cart"""
    dao.delete_cart(username)
