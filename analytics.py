import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("app/data/cleaned_booking_data.csv")

def get_analytics_report():
    # Revenue trends
    df['revenue'] = df['adr'] * (df['stays_in_weekend_nights'] + df['stays_in_week_nights'])
    revenue_trend = df.groupby('arrival_date')['revenue'].sum().reset_index()

    # Cancellation rate
    cancellation_rate = df['is_canceled'].mean() * 100

    # Top geographical locations by booking
    geo_distribution = df['country'].value_counts().head(5).to_dict()

    # Booking lead time distribution
    lead_time_dist = df['lead_time'].describe().to_dict()

    return {
        "revenue_trend": revenue_trend.to_dict(orient='records'),
        "cancellation_rate": f"{cancellation_rate:.2f}%",
        "geo_distribution": geo_distribution,
        "lead_time_distribution": lead_time_dist
    }
