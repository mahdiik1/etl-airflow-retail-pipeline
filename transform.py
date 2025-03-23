import pandas as pd

def transform_data():
    df = pd.read_csv('extracted_data.csv')
    df['sales_tax'] = df['sales'] * 0.08
    df.to_csv('transformed_data.csv', index=False)
    print('Transformation complete!')

if __name__ == '__main__':
    transform_data()
