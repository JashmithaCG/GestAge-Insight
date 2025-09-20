# NeoGest Predictor 🍼✨

**NeoGest Predictor** is a machine learning–powered web application that estimates a baby’s gestational age (in weeks) based on key growth parameters like **weight, length, and head circumference**.  
It combines a trained regression model with a Flask-based web interface to provide real-time predictions in a clean and user-friendly way.

---

## 🚀 Features
- Predicts gestational age from growth parameters  
- Linear Regression model trained using scikit-learn  
- Flask backend with modern HTML/CSS UI  
- Real-time predictions through a web form  
- Easy to extend for healthcare research  

---

## 🛠️ Tech Stack
- **Python 3**  
- **scikit-learn** (ML model)  
- **pandas / numpy** (data handling)  
- **Flask** (web framework)  
- **HTML / CSS** (frontend UI)  

---

## 📂 Project Structure
Preterm/
│── train.py # Trains the regression model
│── app.py # Flask web app
│── baby_model.pkl # Saved trained model
│── templates/
│ └── index.html # Web UI
│── baby_data.csv # Dataset (not included in repo)


---

## ⚙️ Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/neogest-predictor.git
   cd neogest-predictor
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

📊 Example Prediction

Input: Weight = 3.2 kg, Length = 50 cm, Head Circumference = 13 cm

Output: Predicted Gestational Age ≈ 38.5 weeks

🧩 Future Improvements

Add support for larger datasets

Enhance model accuracy with advanced algorithms

Deploy on cloud (Heroku/AWS/GCP) for live access

Add visualization dashboards

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📜 License

This project is licensed under the MIT License.

👶 About

This project is designed to assist healthcare professionals, researchers, and parents in understanding neonatal growth and estimating gestational maturity in an accessible, data-driven way.
<img width="1073" height="900" alt="image" src="https://github.com/user-attachments/assets/4d4bb1a0-04fb-4a68-bdd5-f6df3c4aff74" />

