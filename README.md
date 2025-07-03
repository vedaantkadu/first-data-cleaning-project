# 🧹 First Data Cleaning Project

This is my first hands-on **data cleaning project** using Python and Pandas.  
It involved taking a messy, unstructured dataset and turning it into a clean, usable format — ready for analysis.

---

## 📁 Project Files

| File Name               | Description                                 |
|------------------------|---------------------------------------------|
| `raw_data.xlsx`        | Original messy dataset                      |
| `cleaned_data.xlsx`    | Cleaned version of the dataset              |
| `First_Data_Cleaning.py` | Python script with all cleaning steps      |

---

## 🧼 Key Cleaning Tasks Performed

- ✅ Removed or filled **missing values** (`NaN`)
- ✅ Cleaned up **inconsistent phone numbers** (standardized format)
- ✅ **Split address column** into `Street_Address`, `State`, `Zip_Code`
- ✅ Removed unnecessary or duplicate rows
- ✅ Dropped irrelevant columns
- ✅ Standardized text fields (like "Yes"/"Y" → consistent format)
- ✅ Reset the index after row drops

---

## 🛠️ Technologies Used

- Python 🐍
- Pandas 🐼
- JupyterLab / VS Code
- Excel for viewing raw/cleaned data

---

## 💡 What I Learned

- How to identify and handle missing or invalid data
- How to use `str.split()`, `fillna()`, `dropna()`, and other core Pandas methods
- How to clean columns step-by-step and build a proper data pipeline
- How to push projects to GitHub

---

## 🧠 Sample Before vs After

| Field         | Raw                              | Cleaned             |
|---------------|----------------------------------|---------------------|
| Phone Number  | `123/643/9775`                   | `1236439775`        |
| Address       | `25th Main Street, New York, 10001` | Split into 3 columns |
| Do_Not_Contact | `Y`                              | Removed those rows  |

---

## 🚀 Next Steps

This was just the beginning. I plan to:
- Work on more datasets
- Start exploratory data analysis (EDA)
- Learn data visualization using Matplotlib and Seaborn
- Build a full portfolio

---

## 🔗 Connect with Me

**Vedant Kadu**  
📧 vedantarunkadu@gmail.com  
📍 India  

---

