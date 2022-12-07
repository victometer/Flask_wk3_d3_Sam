from flask import render_template
from models.order_list import Order
from app import app
from models.order_list import *

@app.route('/')
def index ():
    return render_template ('index.html', order_for_html=order_list)

@app.route('/<url_index>')
def index_single_order(url_index):
    return render_template('index_single_order.html', single_order_for_html=order_list[int(url_index)])
