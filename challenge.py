"""
Susheel Kona
Snaptravel Data Engineer Co-op Case Study Summer 2022
Python 3
"""

from io import StringIO
import pandas as pd
import re

def read_data(data: str) -> pd.DataFrame:
    """Parse provided stringified table"""

    csv_data = StringIO(data)
    df = pd.read_csv(csv_data, sep=';')
    return df


def clean_data(old_df: pd.DataFrame) -> pd.DataFrame:
    """Apply transformations to clean data"""

    new_df = pd.DataFrame()

    # Keep only Alphanumeric characters in Airline Code
    new_df['Airline Code'] = old_df['Airline Code'].map(lambda x: re.sub(r'[^a-zA-Z\s:]', '', x).strip())

    new_df['DelayTimes'] = old_df['DelayTimes']

    # Fill in missing Flight Codes
    init_code = old_df['FlightCodes'][0]
    new_codes = [int(x + init_code) for x in range(0, old_df.shape[0] * 10, 10)]
    new_df['FlightCode'] = new_codes

    # Clean To and From
    new_df['To'] = old_df['To_From'].map(lambda x: x.split('_')[0].capitalize())
    new_df['From'] = old_df['To_From'].map(lambda x: x.split('_')[1].capitalize())

    return new_df


def main():
    data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'
    old_df = read_data(data)

    # This contains the cleaned data in a Pandas DataFrame
    new_df = clean_data(old_df) 

    # This contains a stringified representation of the cleaned data
    stringified = new_df.to_csv(index=False)
    
    print(new_df, '\n\n', stringified)
    

if __name__ == '__main__':
    main()
