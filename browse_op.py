from products import dao

class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def load(cls, data):
        """Class method to load a product from data"""
        return cls(data['id'], data['name'], data['description'], data['cost'], data.get('qty', 0))


def list_products() -> list[Product]:
    """Retrieve all products and return as Product instances"""
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """Retrieve a single product by its ID"""
    product_data = dao.get_product(product_id)
    if product_data:
        return Product.load(product_data)
    else:
        raise ValueError(f"Product with ID {product_id} not found")


def add_product(product: dict):
    """Add a product to the database"""
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """Update the quantity of a specific product"""
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
