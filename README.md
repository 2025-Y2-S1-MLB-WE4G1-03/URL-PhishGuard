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

### M1 - URL Length & Hostname Length Analysis

- **Focus**: Extract URL and hostname length features
- **Visualization**: Boxplot showing URL length distribution differences between Good/Bad URLs
- **Notebook**: `IT_M1_URL_Length.ipynb`

### M2 - Malicious Character Counts

- **Focus**: Count suspicious characters (@ and //) in URLs
- **Visualization**: Histogram showing @ character count distribution per label
- **Notebook**: `IT_M2_Char_Counts.ipynb`

### M3 - IP-based Detection & Digit Density

- **Focus**: Detect direct IP usage and calculate digit density
- **Visualization**: Bar chart showing IP address frequency per label
- **Notebook**: `IT_M3_IP_Detection.ipynb`

### M4 - Subdomain & Path Depth Analysis

- **Focus**: Count subdomains and directory depth in URL paths
- **Visualization**: Violin plot comparing subdomain count distributions
- **Notebook**: `IT_M4_Depth_Count.ipynb`

### M5 - Normalization & Scaling

- **Focus**: Apply MinMax scaling to all numerical features
- **Visualization**: Side-by-side histograms showing before/after scaling
- **Notebook**: `IT_M5_Scaling_Norm.ipynb`

### M6 - Label Encoding & Feature Selection

- **Focus**: Encode labels and select top features using Chi-squared test
- **Visualization**: Feature importance bar plot showing χ² scores
- **Notebook**: `IT_M6_Selection_Encoding.ipynb`

## Repository Structure

```
URL-PhishGuard/
├── README.md                                # This file
├── data/
│   ├── raw/                                 # Original dataset
│   └── external/                            # External reference datasets
├── notebooks/
│   ├── IT24103625_M1_URL_Length.ipynb          # M1: URL Length Analysis
│   ├── IT24100950_M2_Char_Counts.ipynb         # M2: Character Count Analysis
│   ├── IT24103925_M3_IP_Detection.ipynb        # M3: IP Detection Analysis
│   ├── IT24103016_M4_Depth_Count.ipynb         # M4: Depth Analysis
│   ├── IT24100659_M5_Scaling_Norm.ipynb        # M5: Scaling & Normalization
│   ├── IT24104208_M6_Selection_Encoding.ipynb  # M6: Feature Selection
│   └── group_pipeline.ipynb                    # Integrated pipeline
├── results/
│   ├── eda_visualizations/                     # Generated plots and charts
│   ├── logs/                                   # Execution logs
│   └── outputs/                                # Processed datasets and features
```

### Execution Order

1. **Individual Analysis**: Run each member's notebook (M1-M6) independently
2. **Integrated Pipeline**: Execute `group_pipeline.ipynb` for complete workflow
3. **Results**: Check `results/` directory for visualizations and outputs

### Running Individual Notebooks

```bash
# Navigate to project directory
cd URL-PhishGuard

# Start Jupyter Notebook
jupyter notebook

# Open and run notebooks in this order:
# 1. IT_M1_URL_Length.ipynb
# 2. IT_M2_Char_Counts.ipynb
# 3. IT_M3_IP_Detection.ipynb
# 4. IT_M4_Depth_Count.ipynb
# 5. IT_M5_Scaling_Norm.ipynb
# 6. IT_M6_Selection_Encoding.ipynb
# 7. group_pipeline.ipynb
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

1. **Feature Engineering** (M1-M4): Extract security-relevant features
2. **Normalization** (M5): Scale features for model compatibility
3. **Feature Selection** (M6): Identify most discriminative features
4. **Integration**: Combine all steps in unified pipeline

## Expected Outcomes

- Comprehensive feature set for phishing detection
- Clear visualizations showing feature discriminative power
- Processed dataset ready for machine learning models
- Insights into URL patterns that indicate phishing attempts

---
