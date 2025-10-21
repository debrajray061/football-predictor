⚽ Football Match Predictor — LaLiga 2018–19 Edition
A machine learning-based football match outcome predictor trained on match data from the LaLiga 2018–2019 season. This project focuses on clean data preprocessing, model training, and match result prediction using team statistics and recent form.


📌 Overview
This project predicts match outcomes (Win/Draw/Loss) using historical data from Spain's top-flight league — LaLiga — for the 2018–19 season. It includes data wrangling, feature engineering, model training, and evaluation, with modular code for easy extension.


🧠 Features
- 🇪🇸 League-Specific Dataset: Focused on LaLiga 2018–19 matches
- 🧹 Data Preprocessing: Handles missing values, encodes categorical features, and normalizes numerical stats
- 🤖 Modeling: Logistic Regression (with optional support for Random Forest or XGBoost)
- 📈 Evaluation Metrics: Accuracy, Precision, Recall, F1 Score, and Confusion Matrix
- 🧪 Test Suite: Unit tests for core modules ensure robustness


📁 Project Structure
laliga-predictor-1819/
├── data/
│   └── laliga-1819-matches.csv
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
git clone https://github.com/your-username/laliga-predictor-1819.git
cd laliga-predictor-1819
- Install dependencies
pip install -r requirements.txt
- Run the pipeline
- Preprocess data:
python src/preprocess.py
- Train model:
python src/train_model.py
- Predict match outcome:
python src/predict.py --team1 "Barcelona" --team2 "Valencia"


📊 Data Source
- Dataset: LaLiga 2018–19 season
- Source: Given in the repository


✅ Testing
Run all tests using:
pytest tests/


📌 Notes
- This project is intended for educational and experimental purposes.
- Extendable to other seasons or leagues with minimal changes to the pipeline.








👤 Author
Developed by Debraj — blending technical curiosity with football analytics and a love for clean, meaningful code.
