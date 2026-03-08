## 🏠 My House Price Prediction System

### **What is this?**

This is a small but powerful data science project where I built a machine learning model to predict house prices. I then turned that model into a real, clickable web app using **Streamlit** so anyone can use it!

---

### **What’s inside?**

I used a dataset called **Housing.csv**, which has 545 records. My app looks at these features to guess the price:

* **The Basics:** Area, Bedrooms, Bathrooms, and Stories.
* **The Extras:** Does it have a Guest Room, Basement, or Air Conditioning?
* **The Setup:** Parking spots, Main Road access, and Furnishing status.

---

### **How I Built It**

I followed a professional machine learning pipeline to get this working:

1. **Data Cleaning:** I made sure the data was ready for the computer to read.
2. **Training:** I used a **Linear Regression** model to learn how features affect price.
3. **Testing:** I checked my accuracy using **Mean Absolute Error (MAE)**.
4. **Deployment:** I saved the model with **Joblib** and built the interface with **Streamlit**.

---

### **The Tech Stack**

* **Python** (The language)
* **Pandas & NumPy** (For organizing the data)
* **Scikit-learn** (The "brain" of the model)
* **Streamlit** (For the interactive web app)
* **Joblib** (To save and load my trained model)

---

### **How to Run My Project 🚀**

Ready to predict some house prices? Just follow these steps:

1. **Get the tools:**
Make sure you have all the libraries installed by running:
`pip install -r requirements.txt`
2. **Fire up the app:**
Launch the web interface with this command:
`streamlit run app.py`
3. **Predict away:**
Once the app opens in your browser, just enter the house details and watch the price prediction update instantly!

---

### **My Project Files**

* `app.py`: The code for my web app.
* `Housing.csv`: My dataset.
* `house_model.pkl`: My saved, ready-to-use model.
* `requirements.txt`: The list of tools needed to run this.

