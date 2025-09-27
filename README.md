# URL PhishGuard: Phishing Detection Through URL Analysis

## Project Overview

This project implements a comprehensive phishing detection system that analyzes URLs to classify them as either legitimate ("Good") or malicious ("Bad"). Using a dataset of 549,346 URLs with no missing values, we employ feature engineering and machine learning techniques to identify phishing attempts.

## Dataset

- **Source**: Phishing Site URLs Dataset
- **Size**: 549,346 entries
- **Columns**:
  - URL: The web address to be analyzed
  - Label: Classification ("Good" or "Bad")
- **Quality**: No missing values

## Team Member Roles & Responsibilities

### M1 - URL Length & Hostname Length Analysis (IT24103625)

- **Focus**: Extract URL and hostname length features
- **Visualization**: Boxplot showing URL length distribution differences between Good/Bad URLs
- **Input**: Raw dataset
- **Output**: `m1_url_length_features.csv`
- **Notebook**: `IT24103625_M1_URL_Length.ipynb`

### M2 - Malicious Character Counts (IT24100950)

- **Focus**: Count suspicious characters (@ and //) in URLs
- **Visualization**: Histogram showing @ character count distribution per label
- **Input**: M1 output (URL length features)
- **Output**: `m2_character_features.csv`
- **Notebook**: `IT24100950_M2_Char_Counts.ipynb`

### M3 - IP-based Detection & Digit Density (IT24103925)

- **Focus**: Detect direct IP usage and calculate digit density
- **Visualization**: Bar chart showing IP address frequency per label
- **Input**: M2 output (Character count features)
- **Output**: `m3_ip_features.csv`
- **Notebook**: `IT24103925_M3_IP_Detection.ipynb`

### M4 - Subdomain & Path Depth Analysis (IT24103016)

- **Focus**: Count subdomains and directory depth in URL paths
- **Visualization**: Violin plot comparing subdomain count distributions
- **Input**: M3 output (IP detection features)
- **Output**: `m4_structure_features.csv`
- **Notebook**: `IT24103016_M4_Depth_Count.ipynb`

### M5 - Normalization & Scaling (IT24100659)

- **Focus**: Apply MinMax scaling to all numerical features from M1-M4
- **Visualization**: Side-by-side histograms showing before/after scaling
- **Input**: M4 output (All structural features)
- **Output**: `m5_scaled_features.csv`
- **Notebook**: `IT24100659_M5_Scaling_Norm.ipynb`

### M6 - Label Encoding & Feature Selection (IT24104208)

- **Focus**: Encode labels and select top features using Chi-squared test
- **Visualization**: Feature importance bar plot showing χ² scores
- **Input**: M5 output (Scaled features)
- **Output**: `m6_final_selected_features.csv` (Ready for ML)
- **Notebook**: `IT24104208_M6_Selection_Encoding.ipynb`

## Repository Structure

```
URL-PhishGuard/
├── README.md                                    # This file
├── data/
│   └── raw/                                     # Original dataset
│       └── phishing_site_urls.csv              # Source dataset
├── notebooks/
│   ├── IT24103625_M1_URL_Length.ipynb          # M1: URL Length Analysis
│   ├── IT24100950_M2_Char_Counts.ipynb         # M2: Character Count Analysis  
│   ├── IT24103925_M3_IP_Detection.ipynb        # M3: IP Detection Analysis
│   ├── IT24103016_M4_Depth_Count.ipynb         # M4: Subdomain & Path Analysis
│   ├── IT24100659_M5_Scaling_Norm.ipynb        # M5: Scaling & Normalization
│   ├── IT24104208_M6_Selection_Encoding.ipynb  # M6: Feature Selection & Encoding
│   └── group_pipeline.ipynb                    # Complete Integrated Pipeline
├── results/
│   └── outputs/                                 # Processed datasets and features
│       ├── m1_url_length_features.csv          # M1 output
│       ├── m2_character_features.csv           # M2 output  
│       ├── m3_ip_features.csv                  # M3 output
│       ├── m4_structure_features.csv           # M4 output
│       ├── m5_scaled_features.csv              # M5 output
│       ├── m6_final_selected_features.csv      # M6 final output (ML-ready)
│       ├── minmax_scaler_M5.pkl                # Trained scaler object
│       └── m6_label_encoder.pkl                # Label encoder object
```

## Pipeline Execution Flow

**Sequential Processing**: Each module builds on the previous module's output, creating a step-by-step feature engineering pipeline.

```
Raw Data → M1 → M2 → M3 → M4 → M5 → M6 → ML-Ready Dataset
```

### Execution Order (IMPORTANT: Follow this sequence)

1. **M1**: `IT24103625_M1_URL_Length.ipynb` → Creates URL length features
2. **M2**: `IT24100950_M2_Char_Counts.ipynb` → Adds character count features (uses M1 output)
3. **M3**: `IT24103925_M3_IP_Detection.ipynb` → Adds IP detection features (uses M2 output)
4. **M4**: `IT24103016_M4_Depth_Count.ipynb` → Adds structure features (uses M3 output)
5. **M5**: `IT24100659_M5_Scaling_Norm.ipynb` → Scales all features (uses M4 output)
6. **M6**: `IT24104208_M6_Selection_Encoding.ipynb` → Final processing (uses M5 output)
7. **Pipeline**: `group_pipeline.ipynb` → Complete analysis and ML demo

### Running the Pipeline

```bash
# Navigate to project directory
cd URL-PhishGuard

# Start Jupyter Notebook
jupyter notebook

# MUST run in this exact order:
# 1. IT24103625_M1_URL_Length.ipynb         (Raw → M1 features)
# 2. IT24100950_M2_Char_Counts.ipynb        (M1 → M2 features) 
# 3. IT24103925_M3_IP_Detection.ipynb       (M2 → M3 features)
# 4. IT24103016_M4_Depth_Count.ipynb        (M3 → M4 features)
# 5. IT24100659_M5_Scaling_Norm.ipynb       (M4 → Scaled features)
# 6. IT24104208_M6_Selection_Encoding.ipynb (M5 → Final ML dataset)
# 7. group_pipeline.ipynb                   (Complete pipeline analysis)
```

## Key Features Extracted

- **URL Length**: Total character count in the URL
- **Hostname Length**: Character count in the hostname portion
- **Malicious Characters**: Count of @ and // characters
- **IP Detection**: Binary flag for direct IP address usage
- **Digit Density**: Ratio of digits to total characters
- **Subdomain Count**: Number of subdomains in the URL
- **Path Depth**: Number of directories in the URL path

## Security Insights

- Phishing URLs often use longer, more complex structures to deceive users
- Suspicious character patterns can indicate URL obfuscation techniques
- Direct IP usage bypasses domain name resolution, a common phishing tactic
- Excessive subdomains may indicate domain spoofing attempts

## Data Processing Pipeline

**🔗 Sequential Feature Engineering Pipeline:**

1. **M1 - Foundation** (IT24103625): Extract URL and hostname length features
2. **M2 - Character Analysis** (IT24100950): Add suspicious character counts (uses M1 output)
3. **M3 - Security Features** (IT24103925): Add IP detection and digit density (uses M2 output)
4. **M4 - Structure Analysis** (IT24103016): Add subdomain and path depth features (uses M3 output)
5. **M5 - Normalization** (IT24100659): Apply MinMax scaling to all features (uses M4 output)
6. **M6 - Final Processing** (IT24104208): Label encoding and feature selection (uses M5 output)

**Key Benefits:**
- ✅ **No Feature Duplication**: Each member focuses on specific feature types
- ✅ **Sequential Dependencies**: Each module builds on previous work
- ✅ **Maintainable Code**: Clear separation of concerns
- ✅ **Scalable Architecture**: Easy to add new feature engineering steps

## Expected Outcomes

- Comprehensive feature set for phishing detection
- Clear visualizations showing feature discriminative power
- Processed dataset ready for machine learning models
- Insights into URL patterns that indicate phishing attempts

## Quick Start Guide

### 1. First Time Setup
```bash
# Clone or download the project
cd URL-PhishGuard

# Ensure you have the dataset
ls data/raw/phishing_site_urls.csv

# Start Jupyter
jupyter notebook
```

### 2. Execute Pipeline (Sequential Order)
```python
# Run each notebook in order:
# 1. M1: IT24103625_M1_URL_Length.ipynb
# 2. M2: IT24100950_M2_Char_Counts.ipynb  
# 3. M3: IT24103925_M3_IP_Detection.ipynb
# 4. M4: IT24103016_M4_Depth_Count.ipynb
# 5. M5: IT24100659_M5_Scaling_Norm.ipynb
# 6. M6: IT24104208_M6_Selection_Encoding.ipynb
```

### 3. View Complete Analysis
```python
# Run the integrated pipeline notebook
# group_pipeline.ipynb
```

### 4. Use Final Dataset for ML
```python
import pandas as pd

# Load the final ML-ready dataset
df = pd.read_csv('results/outputs/m6_final_selected_features.csv')

# Features (X) and target (y) are ready for machine learning
X = df.drop(['URL', 'Label', 'Label_Encoded'], axis=1)
y = df['Label_Encoded']  # 0=good, 1=bad
```

## Output Files Summary

| File | Description | Producer |
|------|-------------|----------|
| `m1_url_length_features.csv` | URL + hostname length features | M1 |
| `m2_character_features.csv` | + Character count features | M2 | 
| `m3_ip_features.csv` | + IP detection & digit density | M3 |
| `m4_structure_features.csv` | + Subdomain & path features | M4 |
| `m5_scaled_features.csv` | + MinMax scaled features | M5 |
| `m6_final_selected_features.csv` | **Final ML-ready dataset** | M6 |

## Team Collaboration Notes

- 🚫 **No code duplication**: Each member has unique feature engineering responsibilities
- 🔗 **Sequential dependencies**: M2 uses M1 output, M3 uses M2 output, etc.
- 💾 **Intermediate outputs**: Each module saves progress for next module
- 🔄 **Easy debugging**: Can restart pipeline from any module
- 📊 **Individual contributions**: Each member creates specific visualizations

---
