import pandas as pd
import os

def extract_data():
    data_dir = os.path.join(os.getcwd(), 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    input_csv = os.path.join(data_dir, 'retail_data.csv')

    # Create a sample CSV if not present
    if not os.path.isfile(input_csv):
        df_init = pd.DataFrame({
            'product': ['WidgetA', 'WidgetB', 'WidgetC'],
            'sales': [120, 90, 220]
        })
        df_init.to_csv(input_csv, index=False)
        print('Sample retail_data.csv created in /data/')

    df = pd.read_csv(input_csv)
    df.to_csv('extracted_data.csv', index=False)
    print('Extraction complete!')

if __name__ == '__main__':
    extract_data()
