# sql_queries_simulated.py

def top_5_insurance_providers(df):
    """
    Returns top 5 insurance providers by patient count.
    """
    return df['insurance_provider'].value_counts().head(5)

def admissions_by_department(df):
    """
    Returns number of admissions per hospital department.
    """
    return df.groupby('department')['patient_id'].count().sort_values(ascending=False)

def monthly_admissions(df):
    """
    Returns admission trends by month.
    """
    df['month'] = df['admission_date'].dt.to_period("M")
    return df.groupby('month').size()

def average_insurance_claim_by_provider(df):
    """
    Returns average claim amount grouped by insurance provider.
    Assumes column 'insurance_claim_amount' exists.
    """
    return df.groupby('insurance_provider')['insurance_claim_amount'].mean().sort_values(ascending=False)
