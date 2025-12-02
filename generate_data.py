import pandas as pd
import numpy as np
from datetime import date, timedelta
import os

# --- 1. SETUP ---
# Create 'datasets' folder if it doesn't exist (where notebook expects data)
if not os.path.exists('datasets'):
    os.makedirs('datasets')

# Define core columns and data size
start_date = date(2022, 1, 1)
end_date = date(2023, 4, 30)
date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
N = len(date_range)

# --- 2. GENERATE grammy.com DATA (High Traffic, High Volatility) ---
# Simulating 2017-01-01 to 2023-04-30 data as the notebook imports the full range.
# The Grammys site is the main traffic driver, so traffic is scaled up.
df_grammy = pd.DataFrame({'date': date_range})

# Base traffic (visitors, sessions, pageviews)
df_grammy['visitors'] = np.random.randint(5000, 15000, N)
df_grammy['pageviews'] = df_grammy['visitors'] * np.random.uniform(1.8, 2.5, N)
df_grammy['sessions'] = df_grammy['visitors'] * np.random.uniform(0.95, 1.1, N)

# Simulate Awards Week/Night spikes (assuming 2023-02-05 was a big night)
awards_night_2023 = date(2023, 2, 5)
is_awards_night = (df_grammy['date'] == awards_night_2023)
is_awards_week = (df_grammy['date'] >= awards_night_2023 - timedelta(days=7)) & \
                 (df_grammy['date'] <= awards_night_2023 + timedelta(days=7))

# Apply multiplier for awards spike
df_grammy.loc[is_awards_week, 'visitors'] *= np.random.uniform(1.5, 3.0, is_awards_week.sum())
df_grammy.loc[is_awards_night, 'visitors'] *= 5.0

# Engagement Metrics
# Bounced sessions (Bounced Rate ~ 60-70%)
df_grammy['bounced_sessions'] = df_grammy['sessions'] * np.random.uniform(0.60, 0.70, N)
# Average duration (Avg Duration ~ 80-120 seconds)
df_grammy['avg_session_duration_secs'] = np.random.randint(80, 120, N)

# Awards flags (using the same logic for the full date range)
df_grammy['awards_week'] = is_awards_week.astype(int)
df_grammy['awards_night'] = is_awards_night.astype(int)

# Clean up and save
for col in ['visitors', 'pageviews', 'sessions', 'bounced_sessions']:
    df_grammy[col] = df_grammy[col].astype(int)

df_grammy.to_csv('datasets/grammy_live_web_analytics.csv', index=False)

# --- 3. GENERATE recordingacademy.com DATA (Lower Traffic, Higher Engagement) ---
# The Recording Academy site is smaller, focusing on membership/industry.
df_ra = pd.DataFrame({'date': date_range})

# Base traffic (Visitors scale is ~1/10th of Grammys)
df_ra['visitors'] = np.random.randint(500, 1500, N)
df_ra['pageviews'] = df_ra['visitors'] * np.random.uniform(2.5, 4.0, N) # Higher pages/session
df_ra['sessions'] = df_ra['visitors'] * np.random.uniform(0.90, 1.05, N)

# Engagement Metrics
# Bounced sessions (Lower Bounced Rate ~ 40-50%)
df_ra['bounced_sessions'] = df_ra['sessions'] * np.random.uniform(0.40, 0.50, N)
# Average duration (Higher Avg Duration ~ 120-180 seconds)
df_ra['avg_session_duration_secs'] = np.random.randint(120, 180, N)

# Awards flags
df_ra['awards_week'] = is_awards_week.astype(int)
df_ra['awards_night'] = is_awards_night.astype(int)

# Clean up and save
for col in ['visitors', 'pageviews', 'sessions', 'bounced_sessions']:
    df_ra[col] = df_ra[col].astype(int)

df_ra.to_csv('datasets/ra_live_web_analytics.csv', index=False)

print("Generated dummy data files successfully in the 'datasets/' folder.")
