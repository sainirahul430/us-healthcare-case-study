# utils.py

def calculate_readmission_rate(df):
    """
    Calculates hospital readmission rate.
    Assumes a column 'readmitted' with Yes/No values.
    """
    readmitted = df['readmitted'].str.upper().value_counts()
    total = readmitted.sum()
    rate = (readmitted.get("YES", 0) / total) * 100
    return round(rate, 2)

def avg_stay_duration(df):
    """
    Returns average hospital stay duration in days.
    Assumes 'admission_date' and 'discharge_date' exist.
    """
    df['discharge_date'] = pd.to_datetime(df['discharge_date'], errors='coerce')
    df['stay_duration'] = (df['discharge_date'] - df['admission_date']).dt.days
    return round(df['stay_duration'].mean(), 2)
