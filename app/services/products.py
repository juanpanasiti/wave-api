from app.database.product_model import ProductModel
from ..database import ProductModel


class ProductService():
    def __init__(self) -> None:
        self.model = ProductModel

    def get_all_products(self):
        try:
            query = self.model.select()
            results = query.execute()
            return [product.__dict__['__data__'] for product in results]
        except:
            # !DELETE PRINT
            print('\033[91m', 'Algo malio sal', '\033[0m')
