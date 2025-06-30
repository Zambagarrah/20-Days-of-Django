# 📚 Library & Members – A Linked Django Project

This is a simple Django project built as part of my **20 Days of Django** journey (Day 4). It features two connected apps:  
- `library`: Displays a list of books  
- `members`: Shows community members and which books they've borrowed  

The project includes styled templates using Bootstrap and CSS gradients to create a clean, modern frontend.

---

## 🚀 Features

- Django app architecture with separate `library` and `members` apps  
- Connected models using `ForeignKey` relationship  
- Templates styled with Bootstrap 5 and custom backgrounds  
- URL routing for both apps  
- Isolated Python environment using `venv`

---

## 🏗️ Tech Stack

- Python 3  
- Django 5+  
- Bootstrap 5 (CDN)  
- HTML/CSS

---

## 📦 Setup Instructions

# Clone the project
```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

# Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

# Install dependencies
```
pip install django
```

# Apply migrations
```
python manage.py makemigrations
python manage.py migrate
```

# Start the development server
```
python manage.py runserver
```
