from flask import Flask, render_template, request

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Trendyol Milla Siyah Takım", "description": "Pamuklu Düğmeli Pijama Takımı", "price": "185,91 TL", "image": "/static/product1.jpg", "category": "Kadın"},
    {"id": 2, "name": "Trendyol Milla Beyaz Bluz", "description": "Lastikli Yüksek Bel Bluz", "price": "139,99 TL", "image": "/static/product2.jpg", "category": "Kadın"},
    {"id": 3, "name": "EmModaStyle Kazak", "description": "Polo Yaka Çizgili Kazak", "price": "145,00 TL", "image": "/static/product3.jpg", "category": "Kadın"},
    {"id": 4, "name": "Sportive Eşofman", "description": "Rahat Kesim Spor Eşofman", "price": "129,99 TL", "image": "/static/product4.jpg", "category": "Erkek"},
    {"id": 5, "name": "Adidas Koşu Ayakkabısı", "description": "Koşu İçin Hafif Ayakkabı", "price": "399,99 TL", "image": "/static/product5.jpg", "category": "Erkek"},
    {"id": 6, "name": "Nike Basketbol Ayakkabısı", "description": "Dayanıklı Tabanlı Ayakkabı", "price": "599,99 TL", "image": "/static/product6.jpg", "category": "Erkek"},
    {"id": 7, "name": "Koton Tişört", "description": "Pamuklu Basic Tişört", "price": "49,99 TL", "image": "/static/product7.jpg", "category": "Erkek"},
    {"id": 8, "name": "Hummel Mont", "description": "Su Geçirmez Mont", "price": "499,99 TL", "image": "/static/product8.jpg", "category": "Erkek"},
    {"id": 9, "name": "Puma Sırt Çantası", "description": "Spor ve Günlük Kullanım İçin Çanta", "price": "199,99 TL", "image": "/static/product9.jpg", "category": "Çocuk"},
    {"id": 10, "name": "Çocuk Ayakkabısı", "description": "Rahat Çocuk Ayakkabısı", "price": "89,99 TL", "image": "/static/product10.jpg", "category": "Çocuk"}
]

@app.route('/')
def homepage():
    return render_template('index.html', products=PRODUCTS, search_query="")

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('search', '').lower()
    filtered_products = [p for p in PRODUCTS if query in p['name'].lower() or query in p['description'].lower() or query in p['category'].lower()]
    return render_template('index.html', products=filtered_products, search_query=query)

@app.route('/category/<string:category_name>')
def category_page(category_name):
    category_name = category_name.capitalize()
    filtered_products = [p for p in PRODUCTS if p['category'] == category_name]
    return render_template('index.html', products=filtered_products, search_query=category_name)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product:
        breadcrumbs = ["Anasayfa", product['category'], product['name']]
        return render_template('product.html', product=product, breadcrumbs=breadcrumbs)
    return "Product not found", 404

if __name__ == '__main__':
    app.run(debug=True)
