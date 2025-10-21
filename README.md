⚽ Football Match Predictor (Season 2018–19)
A machine learning-based football match outcome predictor trained on data from the 2018–2019 season. This project focuses on clean data preprocessing, model training, and match result prediction using team statistics and recent form.
📌 Overview
This project aims to predict the outcome of football matches (Win/Draw/Loss) using historical data from the 2018–19 season. It includes data wrangling, feature engineering, model training, and evaluation — all built with reproducibility and clarity in mind.
🧠 Features
- 📅 Season-Specific Data: Trained exclusively on 2018–19 season match data
- 🧹 Data Preprocessing: Handles missing values, encodes categorical features, and normalizes numerical stats
- 🤖 Modeling: Logistic Regression (with optional support for other classifiers like Random Forest or XGBoost)
- 📈 Evaluation Metrics: Accuracy, Precision, Recall, F1 Score, and Confusion Matrix
- 🧪 Test Suite: Unit tests for core modules ensure robustness
📁 Project Structure
football-predictor-1819/
├── data/
│   └── season-1819-matches.csv
├── src/
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── predict.py
├── tests/
│   └── test_pipeline.py
├── models/
│   └── trained_model.pkl
├── README.md
└── requirements.txt


🚀 Getting Started
- Clone the repository
git clone https://github.com/your-username/football-predictor-1819.git
cd football-predictor-1819
- Install dependencies
pip install -r requirements.txt
- Run the pipeline
- Preprocess data:
python src/preprocess.py
- Train model:
python src/train_model.py
- Predict match outcome:
python src/predict.py --team1 "Liverpool" --team2 "Arsenal"


📊 Data Source
- Dataset: English Premier League 2018–19 season
- Source: [Insert source here, e.g., football-data.co.uk or Kaggle]
✅ Testing
Run all tests using:
pytest tests/


📌 Notes
- This project is intended for educational and experimental purposes.
- Feel free to extend it with additional seasons, advanced models, or live data integration.
👤 Author
Developed by Debraj — blending technical curiosity with a love for football analytics.
