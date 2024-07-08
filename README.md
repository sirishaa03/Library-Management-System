# Flask Library Management System

Welcome to the Flask Library Management System! This project is a web application designed to streamline the management of books within a library. Whether you're a librarian looking to digitize traditional library operations or a library patron seeking a user-friendly interface to browse and search for books, this project has you covered.

## Setup Instructions

Follow these steps to set up and run the Flask Library Management System on your local machine:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/sirishaa03/flask-library-management.git
    cd flask-library-management
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Database Setup:**
    - Install MySQL if you haven't already.
    - Create a new MySQL database named `library_db`.
    - Execute the SQL script `database_setup.sql` to create the necessary tables and schema.

## Usage

Once you have completed the setup, you can start using the Flask Library Management System:

- **Run the Flask application:**
    ```bash
    python app.py
    ```
- Access the application in your web browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).

- Use the provided API endpoints to perform CRUD operations on the books in the library.

## API Documentation

For detailed documentation on the available API endpoints, refer to the Swagger documentation generated for this project. You can access the Swagger UI by visiting [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/apidocs) while the application is running.

## Contributing

Contributions to the Flask Library Management System are welcome! If you would like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Commit your changes and push to your forked repository.
5. Submit a pull request to the main repository.
