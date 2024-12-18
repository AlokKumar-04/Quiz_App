## How to Run the Code

Follow these steps to set up and run the quiz application:

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   Manually install the required packages for the project since there's no `requirements.txt` file. For example:

   ```bash
   pip install django
   ```

   Add any additional dependencies as needed.

4. **Apply Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Add Questions to the Database:**
   Use the Django admin panel or populate the database using a script as explained earlier. Make sure the questions are properly added before starting the quiz.

6. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application:**
   Open your browser and go to `http://127.0.0.1:8000` to start the quiz.

8. **Start Quiz:**

   - Click the "Start Quiz" button on the home page.
   - Follow the instructions to answer the questions.

If you encounter any issues, ensure the database is properly set up and the migrations are applied correctly.
