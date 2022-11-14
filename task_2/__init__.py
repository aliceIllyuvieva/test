from flask import Flask
import pandas as pd
import dbd
import json
import numpy as np
app = Flask(__name__)



@app.route('/get_categories_by_products', methods=['GET'])
def def_1():
    engine = dbd.get_connection()
    df = pd.read_sql(f"""select * from TestBase""", engine)
    df = df.groupby('product')['category'].apply(list)
    return str(df)


@app.route('/get_products_by_categories', methods=['GET'])
def def_2():
    engine = dbd.get_connection()
    df = pd.read_sql(f"""select * from TestBase""", engine)
    df = df.groupby('category')['product'].apply(list)
    return str(df)


@app.route('/get_all_pairs', methods=['GET'])
def def_3():
    engine = dbd.get_connection()
    df = pd.read_sql(f"""select * from TestBase""", engine)
    return str(df)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
