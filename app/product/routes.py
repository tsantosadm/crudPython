from flask_openapi3 import APIBlueprint, Tag
from .models import ProductsQuery, ProductsResponse, ProductResponse, ProductRequest, ProductIdPath, ProductNotFound
from db_config import db, Product

product_tag = Tag(name='Product', description='All products operations')
bp = APIBlueprint('product', __name__, url_prefix='/api/product', abp_tags=[product_tag])


@bp.get(
    '',
    summary='List all products',
    responses={200: ProductsResponse}
)
def products_get(query: ProductsQuery):
    products = Product.query
    if query.name is not None:
        products.filter(Product.name.like(query.name))
    products = products.paginate(
        page=query.page, per_page=query.per_page
    )
    return ProductsResponse(
        products=[p.to_dict() for p in products.items],
        total_pages=products.pages
    ).dict()


@bp.post(
    '',
    summary='Create new product',
    responses={201: ProductResponse}

)
def product_post(body: ProductRequest):
    product = Product(**body.dict())
    db.session.add(product)
    db.session.commit()
    return product.to_dict(), 201


@bp.delete(
    '/<int:product_id>',
    summary='Delete one product',
    responses={404: ProductNotFound}
)
def product_delete(path: ProductIdPath):
    if path.product_id == 404:
        return ProductNotFound().dict(), 404



