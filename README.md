# ⚽ Player Registration Backend (FastAPI + PostgreSQL)

This is a clean and simple backend API for registering football players. It handles age-based validations, conditional parent info requirements, password security, and full form validation using FastAPI and PostgreSQL.

---

## 🚀 Features

- FastAPI-based RESTful API
- Age-based validation: Parent info required if player is under 13
- Password confirmation and hashing with bcrypt
- Email and phone validation
- Conditional mandatory fields and consent validation
- PostgreSQL integration using SQLAlchemy
- Swagger UI for easy API testing

---

## 📁 Project Structure

user-registration-backend/
│
├── main.py # FastAPI application entry point
├── models.py # SQLAlchemy database models
├── schemas.py # Pydantic validation schemas
├── database.py # DB connection and session config
├── email_utils.py # Email utilities (if needed later)
├── requirements.txt # Python dependencies
├── .env # Environment variable config

yaml
Copy
Edit

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/user-registration-backend.git
cd user-registration-backend
2. Set up a virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate  # macOS/Linux
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Create .env file
Add your PostgreSQL credentials:

bash
Copy
Edit
DATABASE_URL=postgresql://postgres:yourpassword@localhost/yourdbname
5. Run the application
bash
Copy
Edit
uvicorn main:app --reload
Open your browser to http://127.0.0.1:8000/docs to explore and test the API.

✅ Example Test Case (Age < 13, Requires Parent Info)
json
Copy
Edit
{
  "firstname": "Emily",
  "middlename": "Rose",
  "lastname": "Smith",
  "dob": "2015-05-20",
  "email": "emily.kid@example.com",
  "phone": "0700000000",
  "password": "StrongPass123!",
  "confirm_password": "StrongPass123!",
  "club_name": "Junior Stars",
  "country": "UK",
  "parent_name": "Sarah Smith",
  "parent_email": "sarah.parent@example.com",
  "parent_phone": "07111222333",
  "parent_consent": true,
  "terms_accepted": true,
  "data_consent": true
}
✅ Example Test Case (Age ≥ 13, No Parent Info)
json
Copy
Edit
{
  "firstname": "James",
  "middlename": "Lee",
  "lastname": "Turner",
  "dob": "2008-01-15",
  "email": "james.teen@example.com",
  "phone": "07123456789",
  "password": "StrongTeen123!",
  "confirm_password": "StrongTeen123!",
  "club_name": "Future Stars FC",
  "country": "UK",
  "terms_accepted": true,
  "data_consent": true
}
📌 Notes
Password must be at least 8 characters with a number and special character

If the player is under 13, parent details and consent are mandatory

All fields are validated for proper formatting and completeness
