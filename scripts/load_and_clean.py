# load_and_clean.py

import pandas as pd

def load_data(filepath):
    """
    Loads hospital CSV data into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(filepath)
        print("✅ Data loaded successfully.")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def clean_data(df):
    """
    Cleans the hospital dataset: trims strings, handles missing values, and standardizes columns.
    """
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Example cleaning
    df = df.drop_duplicates()
    df = df.dropna(subset=["patient_id", "admission_date"])
    
    # Convert dates
    if 'admission_date' in df.columns:
        df['admission_date'] = pd.to_datetime(df['admission_date'], errors='coerce')
    
    # Standardize text fields
    if 'gender' in df.columns:
        df['gender'] = df['gender'].str.strip().str.upper()
    
    print("🧹 Data cleaned.")
    return df
