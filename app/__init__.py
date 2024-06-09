from flask_openapi3 import OpenAPI
from db_config import db


def create_app() -> OpenAPI:
    app = OpenAPI(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    db.init_app(app)

    from .product.routes import bp as product_bp
    app.register_api(product_bp)

    return app
