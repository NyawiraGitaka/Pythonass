from abc import ABC, abstractmethod

class Product:
    product_name = ""
    product_id = ""
    product_colour = ""
    product_quantity = ""
    product_image = ""

class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self):
        pass
    
    @abstractmethod
    def edit_product(self):
        pass

    @abstractmethod
    def get_product_by_id(self):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def upload_product_image(self):
        pass

    @abstractmethod
    def delete_product(self):
        pass

class ProductManager(ProductAbstract):
    def create_product(self, create_product):
        print(f"Your product is {create_product}")

    def edit_product(self, edit_product):
        print(f"Your new product ID is {edit_product}")

    def get_product_by_id(self, get_product_by_id):
        print(f"Your product ID is {get_product_by_id}")

    def get_all_products(self, get_all_products):
        print(f"Your products are {get_all_products}")

    def upload_product_image(self, upload_product_image):
        print(f"{upload_product_image}")
    
    def delete_product(self, delete_product):
        print(f"Your product has been deleted.")

product_manager = ProductManager()
product_manager.create_product("Oreo Biscuits")
product_manager.get_product_by_id(4567)
product_manager.get_all_products("")
product_manager.edit_product("")