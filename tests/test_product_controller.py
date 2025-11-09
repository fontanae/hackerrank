from controller.productController import ProductContoller

def test_controller_get_all_products():
    controller = ProductContoller(local=True)

    result = controller.get_products({"all":True})

    assert isinstance(result,list)
    assert len(result)>0

def test_controller_get_one_product():
    controller = ProductContoller(local=True)
    result = controller.get_products({"id":"P001"})
    
    assert isinstance (result, dict)
    assert result["id"]=="P001"

def test_controller_get_one_product_not_found():
    controller = ProductContoller(local=True)
    result = controller.get_products({"id":"XXX"})
    
    assert isinstance (result, dict)
    assert "error" in result
    
