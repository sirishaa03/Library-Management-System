from flask import Flask, jsonify, request, render_template, redirect
from flasgger import Swagger
import pymysql

app = Flask(__name__)
Swagger(app)

# Configure MySQL connection
conn = pymysql.connect(
    host='localhost',
    user='root',  # MySQL username
    password='',  # MySQL password
    database='library_db',  # Database
    cursorclass=pymysql.cursors.DictCursor
)

# Create cursor
cursor = conn.cursor()

# Home route
@app.route('/')
def home():
    try:
        # Fetch all books from the database
        sql = "SELECT * FROM books"
        cursor.execute(sql)
        books = cursor.fetchall()
        
        # Render the home.html template with the books data
        return render_template('home.html', books=books)
    except Exception as e:
        # Print the error for debugging
        print("Error:", e)
        # Return a generic error message
        return "Internal Server Error", 500

# Route for adding books
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        try:
            data = request.form
            title = data.get('title')
            author = data.get('author')
            genre = data.get('genre')
            published_year = data.get('published_year')
            availability = True if data.get('availability') else False

            sql = "INSERT INTO books (title, author, genre, published_year, availability) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (title, author, genre, published_year, availability))
            conn.commit()

            return redirect('/')
        except Exception as e:
            return jsonify({"error": "Bad Request"}), 400
    else:
        return render_template('add_book.html')

# Route for updating a book
@app.route('/update_book/<int:id>', methods=['GET', 'POST'])
def update_book(id):
    if request.method == 'POST':
        try:
            data = request.form
            title = data.get('title')
            author = data.get('author')
            genre = data.get('genre')
            published_year = data.get('published_year')
            availability = True if data.get('availability') else False

            sql = "UPDATE books SET title = %s, author = %s, genre = %s, published_year = %s, availability = %s WHERE id = %s"
            cursor.execute(sql, (title, author, genre, published_year, availability, id))
            conn.commit()
            if cursor.rowcount > 0:
                return jsonify({"message": "Book updated successfully"}), 200
            else:
                return jsonify({"error": "Book not found"}), 404
        except Exception as e:
            return jsonify({"error": "Internal Server Error"}), 500
    else:
        try:
            # Fetch the book details by ID
            sql = "SELECT * FROM books WHERE id = %s"
            cursor.execute(sql, (id,))
            book = cursor.fetchone()
            if book:
                # Render the update_book.html template with the book details
                return render_template('update_book.html', book=book)
            else:
                return jsonify({"error": "Book not found"}), 404
        except Exception as e:
            return jsonify({"error": "Internal Server Error"}), 500

# Route for deleting a book
@app.route('/delete_book/<int:id>', methods=['DELETE'])
def delete_book(id):
    try:
        sql = "DELETE FROM books WHERE id = %s"
        cursor.execute(sql, (id,))
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": "Book deleted successfully"}), 200
        else:
            return jsonify({"error": "Book not found"}), 404
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
