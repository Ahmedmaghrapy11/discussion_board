# Discussion Board Web Application

## Introduction
This project is a **Discussion Board Web Application** built using **Python** and the **Django Web Framework**. It allows users to create discussion threads, post replies, and engage in conversations on different topics. The front-end is developed with **HTML** and **CSS** for structure and styling, while Django handles the back-end logic and data storage.

## Technologies
- **Python**: 3.9
- **Django**: 4.1 (Web framework)
- **HTML**: Front-end structure
- **CSS**: Styling the front-end
- **SQLite3**: Default database for Django

## Features
- **Discussion Threads**: Users can create new discussion posts on various topics.
- **User Authentication**: Secure user login and registration system (optional for viewing posts, required for posting).

## Setup

### 1. Clone the Repository
To get started, clone this repository to your local machine:
```bash
git clone https://github.com/Ahmedmaghrapy11/discussion_board.git
cd discussion_board
```

### 2. Install Dependencies

- Create virtual environment
```bash
python3 -m venv env
```

- Activate virtual environment
 
  **On macOS/Linux**:
```bash
source env/bin/activate
```
  **On Windows**:
```bash
.\env\Scripts\activate
```

- Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```
