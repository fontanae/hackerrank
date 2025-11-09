import json
import os


class ProductService:
    def __init__(self, local=True):
        base_path = os.path.join(os.path.dirname(__file__))
        self.file_path = os.path.join(base_path, "..","data", "products.json")

    def load_data(self):
        with open(self.file_path,"r", encoding="utf-8") as f:
            return json.load(f)
        
    def to_number (self, value):
        if value is None:
            return None
        try:
            return float(value)
        except:
            return None


    def get_all_products(self, name=None, min_price=None, max_price=None):
        products = self.load_data()
        name = name.lower().strip() if isinstance(name,str) and name.strip() != "" else None
        min_p = self.to_number(min_price)
        max_p = self.to_number(max_price)

        if name is None and min_p is None and max_p is None:
            return [{"name":p["name"], "value": p["value"]} for p in products]
        
        results=products

        if name is not None:
            results = [p for p in results if name in p.get("name","").lower()]                     

        if min_p is not None:
            results = [p for p in results 
                       if self.to_number(p.get("value")) is not None and self.to_number(p.get("value")) >= min_p]
        
        if max_price is not None:
            results = [p for p in results 
                       if self.to_number(p.get("value")) is not None and self.to_number(p.get("value")) <= max_p]
        
        return [{"name":p["name"], "value": p["value"]} for p in results]
    
    def get_one_product(self, product_id):
        products = self.load_data()
        for p in products:
            if p.get("id")==product_id:
                return p
        return{"error": "Producto no encontrado"}