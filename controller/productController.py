from service.productService import ProductService

class ProductContoller:
    def __init__(self, local=True):
        self.service = ProductService(local)

    def get_products(self, search):
        if "all" in search: #obtener todos los productos con o sin filtro
            return self.service.get_all_products(
                name=search.get("name"),
                min_price=search.get("min_price"), 
                max_price=search.get("max_price"))
        if "id" in search: #obtener un solo producto --detalle-
            return self.service.get_one_product(search["id"])