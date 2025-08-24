![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![XGBoost](https://img.shields.io/badge/XGBoost-enabled-orange)
![SVM](https://img.shields.io/badge/Model-SVM-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)

# 📈 AI-Driven Trading Pattern Predictor

This project implements an ensemble-based machine learning system to predict stock market trading signals (Buy, Hold, Sell) based on synthetic technical indicators.

## 🚀 Features
- Synthetic stock market data generator
- Feature engineering and preprocessing
- Ensemble model using **XGBoost + SVM**
- Real-time trading signal classification
- Export results to CSV for Power BI visualization

## 🧠 Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Power BI

## 📂 Project Structure
```
AI_Trading_Predictor_Project/
├── trading_pattern_predictor.py          # Full standalone script
├── AI_Trading_Predictor_Notebook.ipynb   # Jupyter Notebook version
├── predictions_for_power_bi.csv          # Output CSV for Power BI
├── README.md                             # Project documentation
```

## 📊 Power BI Dashboard
Use `predictions_for_power_bi.csv` to build dashboards:
- Actual vs Predicted Trading Signals
- Signal distribution and accuracy tracking

## 📌 How to Run

### Option 1: Python Script
```bash
python trading_pattern_predictor.py
```

### Option 2: Jupyter Notebook
Open `AI_Trading_Predictor_Notebook.ipynb` and run all cells.

## 📞 Contact
Developed by [Roshan Yarlagadda](http://www.linkedin.com/in/yarlagaddaroshan)

## 📃 License
This project is open for educational and non-commercial use.
