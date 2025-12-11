# resume-screener
# 📄 AI Resume Screening App  
A machine-learning powered web application built using **Streamlit**, designed to automatically classify resumes into different job categories such as *Python Developer*, *Data Scientist*, *Java Developer*, *Full Stack Developer*, etc.

This tool helps recruiters, HR teams, and job portals to quickly filter candidates based on skills extracted from their resumes.

---

## 🚀 Features

- 🔍 **Upload Resume** in `.pdf` or `.txt` format  
- 🤖 **Automatic Text Cleaning** using NLP  
- 🧠 **Machine Learning Classification** (Pickle models: `model.pkl`, `tfidf.pkl`)  
- 📑 **Predicts Resume Category** based on skill relevance  
- ⚡ **Simple & Fast UI** using Streamlit  

---

## 🧠 ML Model

The app uses:
- **TF-IDF Vectorizer** (`tfidf.pkl`)
- **Classifier Model** (`model.pkl`)  
Trained on labeled resume datasets to identify job roles.

---

## 📁 Project Structure


---

## 📥 Installation & Setup

### **1️⃣ Clone the repository**
```sh
git clone https://github.com/Thareesh2311/resume-screener
cd resume-screener
2️⃣ Install dependencies
sh
Copy code
pip install -r requirements.txt
3️⃣ Run the app
sh
Copy code
streamlit run app.py
📌 Usage
Open the Streamlit UI in the browser.

Upload a .pdf or .txt resume.

The system extracts text, cleans it, vectorizes it, and predicts the job category.

The predicted category and ID are displayed.

🛠 Technologies Used
Python

Streamlit

scikit-learn

NLTK

Pickle

TF-IDF Vectorization

📌 Resume Categories (Example)
Your current category mapping includes:

ID	Category
15	Java Developer
23	Testing
8	DevOps Engineer
20	Python Developer
2	Hadoop
7	C++ Developer
18	Ruby on Rails
6	Data Science
69	Full Stack Developer

🧩 Future Enhancements
PDF-to-text extraction improvement

Add more job role categories

Model retraining using bigger datasets

Deploy to Streamlit Cloud / Render / HuggingFace
