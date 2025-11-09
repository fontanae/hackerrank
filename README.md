API Backend simple para obtener informacion de productos, inspirada en la pagina de detalle de producto de Mercado Libre.

Objetivo: exponer endpoints que provean datos para una interfaz de detalle de producto.

Arquitectura: El proyecto esta organizado en capas para mantener una separacion de responsabilidades

HACKERRANK/
|
├ app.py
├controller
├ productController.py #casos de uso
├service
├ productService.py #acceso a json (base de datos)
├ data
├ products.json #base de datos local
├ test #pruebas con pytest
├ test_product_controller.py
├ test_product_service.py
