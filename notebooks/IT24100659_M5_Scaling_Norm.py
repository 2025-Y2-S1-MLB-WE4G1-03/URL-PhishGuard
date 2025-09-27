# IT24100659_M5_Scaling_Norm.py
# Normalization & Scaling (MinMax)

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ================================
# 1. Load Dataset
# ================================
data_path = "phishing_site_urls.csv"

if not os.path.exists(data_path):
    raise FileNotFoundError(f" Dataset not found at: {data_path}")

df = pd.read_csv(data_path)
print(" Data loaded successfully")
print("Data shape:", df.shape)
print(df.head())

# Step 2: Create numeric features
df['url_length'] = df['URL'].apply(len)
df['num_dots'] = df['URL'].str.count('\.')
df['num_slashes'] = df['URL'].str.count('/')
df['has_https'] = df['URL'].str.startswith('https').astype(int)

# ================================
# 3. Select Numerical Features
# ================================
numeric_features = ['url_length', 'num_dots', 'num_slashes', 'has_https']
print("\n Numeric Features:", numeric_features)


# ================================
# 4. Handle Missing Values
# ================================
if df[numeric_features].isnull().values.any():
    print(" Missing values detected. Filling with median...")
    df[numeric_features] = df[numeric_features].fillna(df[numeric_features].median())

# ================================
# 5. Apply MinMax Scaling
# ================================
scaler = MinMaxScaler()
scaled_values = scaler.fit_transform(df[numeric_features])

# Create scaled DataFrame
df_scaled = df.copy()
df_scaled[numeric_features] = scaled_values

# ================================
# 6. Visualization (Before vs After)
# ================================

for feature_to_plot in numeric_features:
    plt.figure(figsize=(12, 5))
    # Before Scaling
    plt.subplot(1, 2, 1)
    sns.histplot(df[feature_to_plot], bins=50, kde=True, color="blue")
    plt.title(f"Before Scaling: {feature_to_plot}")

    # After Scaling
    plt.subplot(1, 2, 2)
    sns.histplot(df_scaled[feature_to_plot], bins=50, kde=True, color="green")
    plt.title(f"After MinMax Scaling: {feature_to_plot}")
    plt.tight_layout()
    plt.show()

    # Print range comparison
    print(f"\n  Original range of '{feature_to_plot}': {df[feature_to_plot].min()} to {df[feature_to_plot].max()}")
    print(f" Scaled range of '{feature_to_plot}': {df_scaled[feature_to_plot].min()} to {df_scaled[feature_to_plot].max()}")


# ================================
# 7. Save Scaled Dataset
# ================================
output_dir = "results/outputs"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "features_scaled.csv")
df_scaled.to_csv(output_path, index=False)
print(f"  Scaled dataset saved at: {output_path}")

# 8. Check class balance /Class Balance Visualization
print(df['Label'].value_counts())
plt.figure(figsize=(6,4))
sns.countplot(x='Label', data=df, palette='pastel')
plt.title("Class Balance: Good vs Bad URLs")
plt.xlabel("Label")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 9. Summary Table of Feature Ranges
summary = []
for feature in numeric_features:
    summary.append({
        'Feature': feature,
        'Min (Before)': df[feature].min(),
        'Max (Before)': df[feature].max(),
        'Min (After)': df_scaled[feature].min(),
        'Max (After)': df_scaled[feature].max()
    })
summary_df = pd.DataFrame(summary)
print(summary_df)
