from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)


#Modelagem
#Produto (id, name, price, description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)


#Definição de rota para requisitar cadastro
@app.post('/api/products/add')
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"}), 200
    return jsonify({"message": "Invalid product data"}), 400


@app.delete('/api/products/delete/<int:product_id>')
def delete_product(product_id):
    #Recuperar o Produto da base de dados
    product = Product.query.get(product_id)
    #Verificar se o Produto Existe
    if product is not None:
        #Se existir produto deletar da base de dados
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted Successfully"})
    #Se não existir Produto retorno error 404 not found
    return jsonify({"message": "Product not found"}), 404


#Definir uma rota raiz (paǵina inicial) e a função que será requisitada ao requisitar
@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
