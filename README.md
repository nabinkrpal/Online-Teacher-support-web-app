# Role-Based Doubt Resolution Web Application

A web application designed to streamline and organize doubt resolution among students and teachers through a role-based interface. It allows students to register, post queries, and view responses, while teachers can log in to manage and resolve doubts efficiently.

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: SQLite (`teacher.db`)
- **Template Engine**: Jinja2 (via Flask)


## 🔑 Features

- **Student Registration/Login**
- **Teacher Registration/Login**
- **Role-based Routing**
  - Students can:
    - Register and log in
    - Post doubts
    - View answered doubts
  - Teachers can:
    - Register and log in
    - View pending doubts
    - Respond to student queries
- **File Upload Support** (inside `uploads/`)
- **User Profiles** for both students and teachers
- **Stylized Interface** with separate CSS files for each page

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/doubt-resolution-app.git
   cd doubt-resolution-app
2.python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3.python home.py

4.http://127.0.0.1:5000/
