# 🩺 Muscle Spasm Severity Classifier

A lightweight clinical decision support tool built with **Python + Streamlit** for classifying muscle spasm severity in basic clinical and educational settings.

---

## 📌 Problem Statement

Muscle spasm severity is traditionally assessed in a subjective, inconsistent manner — leading to:

- Inconsistent documentation between clinicians
- Difficulty comparing or researching patient data
- No simple, structured classification system for quick use

---

## ✅ Solution

This tool provides a **rule-based scoring system** that classifies muscle spasm severity into three categories:

| Classification | Score Range |
|----------------|-------------|
| 🟢 Mild         | 2 – 4       |
| 🟡 Moderate     | 5 – 7       |
| 🔴 Severe       | 8 – 11      |

---

## 📊 Scoring Factors

| Factor | Options | Points |
|--------|---------|--------|
| **Frequency** | Low / Medium / High | 1 / 2 / 3 |
| **Duration** | Short / Medium / Long | 1 / 2 / 3 |
| **Trigger Present** | Yes / No | 2 / 0 |
| **Pain Intensity** | Mild / Moderate / Severe | 1 / 2 / 3 |

**Maximum score: 11**

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/spasm-classifier.git
cd spasm-classifier
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
spasm-classifier/
├── streamlit_app.py   # Main Streamlit application
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## ☁️ Deploy for Free (Streamlit Cloud)

1. Push this repo to **GitHub**
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set `streamlit_app.py` as the entry point
5. Click **Deploy** — done!

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** — web UI framework
- No database or backend required

---

## 🎯 Use Cases

- DPT (Doctor of Physical Therapy) students learning clinical assessment
- Quick severity screening in basic clinical settings
- Teaching tool for standardized documentation practices

---

## ⚠️ Disclaimer

This tool is an **educational aid only**. It does not replace clinical judgment, formal diagnosis, or professional medical advice. Always consult a qualified healthcare professional for patient care decisions.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)
