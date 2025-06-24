# 🧠 PhysioCare — Physiotherapy Web Portal

Welcome to **PhysioCare**, a complete web solution for managing physiotherapy consultations, patient feedback, online appointments, and chatbot-powered health guidance.


---

## 💡 Project Overview

**PhysioCare** is a full-stack physiotherapy website that enables:
- 👨‍⚕️ Doctors to manage consultations and appointments
- 🧑‍🤝‍🧑 Patients to book online consultations
- 💬 AI-powered chatbot for instant physiotherapy-related FAQs
- ⭐ Feedback and rating system to improve patient care

This project is aimed at enhancing accessibility, automation, and digital health management — ideal for clinics or solo physiotherapy practitioners.

---

## 🚀 Features

- 🔐 User registration & login system
- 💬 Chatbot integrated with OpenAI GPT (securely accessed via `.env`)
- 📅 Appointment request & admin dashboard
- 📝 Feedback submission with star ratings
- 💻 Online consultation form (Symptoms, Preferred Time, Mode)
- 🌐 Admin panel with search & filter capabilities
- 🧾 Payment simulation before consultation confirmation
- 📱 Floating WhatsApp button & contact options
- 🧠 Blog & recovery stories section
- 🎨 Responsive UI with modern CSS transitions

---

## 🛠️ Tech Stack

| Frontend                      | Backend                   | Other                     |
|------------------------------|---------------------------|---------------------------|
| HTML5, CSS3, Bootstrap        | Django (Python)           | SQLite, Git, GitHub       |
| JavaScript (for interactivity) | Django Templates & Views | python-dotenv for secrets |
| OpenAI API (Chatbot)          | Admin Panel via Django    |                           |


---
## 📂 Folder Structure

```
physiotherapy-website/
├── chatbot/                # Chatbot logic and views
├── appointments/           # Consultation & feedback features
├── media/                  # Uploaded media (images/docs)
├── static/                 # CSS, JS, icons, etc.
├── templates/              # HTML template files
├── physio/                 # Project settings
├── .env                    # API key (excluded from Git)
├── .gitignore              # Git exclusions
├── db.sqlite3              # SQLite database
├── manage.py
└── README.md
```

## 🧪 How to Run Locally

1. **Clone the Repository**

```bash
git clone https://github.com/Shweta741/physiotherapy-website.git
cd physiotherapy-website
```

2. **Create Virtual Environment & Activate**

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate   # macOS/Linux
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

(Or manually if `requirements.txt` is missing: `pip install django python-dotenv openai`)

4. **Create `.env` File**

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=sk-your-api-key-here
```

⚠️ Never commit this file to GitHub.

5. **Run Migrations**

```bash
python manage.py migrate
```

6. **Run the Server**

```bash
python manage.py runserver
```

Access your project at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🔒 Admin Access (Demo)

- URL: `/admin-login/`  
- Username: `tridisha`  
- Password: `123456789`

## 📦 Key Pages

| Feature                  | URL                     |
|--------------------------|--------------------------|
| Home                     | `/`                      |
| About                    | `/about/`                |
| Register/Login           | `/register/`, `/login/`  |
| Chatbot                  | `/chatbot/`              |
| Feedback                 | `/feedback/`             |
| Consult Request          | `/consultation/`         |
| Admin Dashboard          | `/admin-dashboard/`      |

## 🚧 Future Enhancements

- 📧 Email/SMS notifications for appointments  
- 📊 Analytics dashboard for admin  
- 🌐 Live deployment (Render / PythonAnywhere / Vercel)  
- 📱 Progressive Web App (PWA) support  

## 👩‍💻 Author

**Shweta Chakraborty**  
🎓 B.Tech Student | 💡 Web Developer | 🤖 AI Enthusiast  
📍 India  
🔗 [LinkedIn](https://www.linkedin.com/in/shweta-chakraborty/)  
💻 [GitHub](https://github.com/Shweta741)


## ⭐ Support & Feedback

If you found this project helpful, consider giving it a ⭐ on GitHub.  
Feedback, issues, and contributions are always welcome!
