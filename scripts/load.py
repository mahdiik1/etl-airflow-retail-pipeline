import pandas as pd

def load_data():
    df = pd.read_csv('transformed_data.csv')
    print('Loading data into (mock) DB table: retail_sales')
    for _, row in df.iterrows():
        print(f"Loaded product={row['product']}, sales={row['sales']}, tax={row['sales_tax']}")
    print('Load complete!')

if __name__ == '__main__':
    load_data()
