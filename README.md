# Inotebook-Backend

![Python version](https://img.shields.io/badge/python-3.10-green)

### 📄 Project Description:

Backend code for the iNotebook project, which is a clone of Google Keep but with fewer features as it was built for learning purposes. This is the backend of the project; the frontend is built in React.js.

### 🎯 Purpose and Achievement:
This project is a part of my React.js learning. The main goal was to understand how to manage both frontend and backend and write APIs according to the frontend requirements. As a result, I learned different backend patterns to better manage code.

### ⚙️🚀 Technologies and Frameworks Utilized

- FastAPI
- MongoDB(motor)
- Pydantic

### 💡 Features

- JWT authentication
- User CRUD APIs
- Note CRUD APIs
- Custom error handling messages

### 🔜 Future Development and Features
For future development, I would like to add more features.

### ▶️ Run


1. Clone the repository

  ```bash
  git clone git@github.com:Ja-yy/Inotebook_backend.git
  ```

2. Set up this environment variable in `.env` file

  ```bash
  DATABASE_URL="<Your mongodb URL>"
  DATABASE_COLLECTION="<Collection Name>"
  DATABASE_NAME="<Database Name>"
  CORS_ORIGINS = ["*"]
  CORS_ALLOW_CREDENTIALS = False
  CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "PATCH","DELETE"]
  CORS_ALLOW_HEADERS = ["Content-Type", "Authorization"]
  ```

3. Create Environment:

   - Set up a virtual environment using Pipenv (you can use any other methods):

     ```bash
     pipenv install -r requirements.txt
     ```

     Activate the virtual environment:

     ```bash
     pipenv shell
     ```

Now, go to [http://localhost:8000](http://localhost:8000/)

Enjoy the app :)

