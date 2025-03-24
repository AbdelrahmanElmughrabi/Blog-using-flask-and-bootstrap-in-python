# Blog using Flask and Bootstrap in Python

This project is a simple blog application built using Flask and Bootstrap in Python. It allows users to create, read, update, and delete blog posts.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
## Features

- Create, read, update, and delete blog posts.
- User authentication and authorization.
- Responsive design using Bootstrap.
- Database integration using SQLAlchemy.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AbdelrahmanElmughrabi/Blog-using-flask-and-bootstrap-in-python.git
    ```

2. Change directory to the project folder:
    ```bash
    cd Blog-using-flask-and-bootstrap-in-python
    ```

3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Set up the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

## Usage

1. Run the application:
    ```bash
    flask run
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.
