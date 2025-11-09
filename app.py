from controller.productController import ProductContoller
import json

def lambda_handler(event, context=None):
    path = event.get("path", "")
    controller = ProductContoller
    
    if path == "/get-all-products" :
        return {"statusCode":200,"body":controller.get_products({"all":True})}

    if path.startswith ("/get-product/"):
        product_id = path.split("/")[-1]
        return {"statusCode":200,"body":controller.get_products({"id":product_id})}
                
    return {"statusCode":400,"body": "Ruta no valida"}