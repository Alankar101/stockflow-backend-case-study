from flask import Flask, jsonify
from models import db, Company, Warehouse, Product, Inventory, Supplier

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stockflow.db'
db.init_app(app)

def get_recent_sales(product_id, days=30):
    """
    Mock logic for recent sales — 
    in a real system this would pull from a sales/order table.
    """
    return 10

@app.route('/api/companies/<int:company_id>/alerts/low-stock')
def low_stock_alerts(company_id):
    alerts = []

    inventories = Inventory.query.all()

    for inv in inventories:
        product = Product.query.get(inv.product_id)
        warehouse = Warehouse.query.get(inv.warehouse_id)
        if not warehouse or warehouse.company_id != company_id:
            continue

        threshold = product.low_stock_threshold or 10
        if inv.quantity >= threshold:
            continue

        recent_sales = get_recent_sales(product.id)
        if recent_sales == 0:
            continue

        daily_usage = recent_sales / 30
        days_left = int(inv.quantity / daily_usage) if daily_usage > 0 else 0

        supplier = Supplier.query.first()

        alerts.append({
            "product_id": product.id,
            "product_name": product.name,
            "sku": product.sku,
            "warehouse_id": warehouse.id,
            "warehouse_name": warehouse.name,
            "current_stock": inv.quantity,
            "threshold": threshold,
            "days_until_stockout": days_left,
            "supplier": {
                "id": supplier.id if supplier else None,
                "name": supplier.name if supplier else "",
                "contact_email": supplier.contact_email if supplier else ""
            }
        })

    return jsonify({
        "alerts": alerts,
        "total_alerts": len(alerts)
    })

if __name__ == "__main__":
    app.run(debug=True)
