# Student Management System

## Overview
The **Student Management System** is a Python-based application designed to manage student records efficiently. It allows users to add, view, delete, and reset student information, including name, email, contact number, gender, date of birth, and class. This application utilizes a graphical user interface (GUI) built with Tkinter and stores data in an SQLite database.

## Features
- **Add Student Records**: Input and store student information.
- **View Records**: Display all student records in a tabular format.
- **Delete Records**: Remove specific student records from the database.
- **Reset Fields**: Clear input fields for new data entry.
- **Database Management**: Create and manage a local SQLite database for data persistence.

## Technologies Used
- Python 3.x
- Tkinter (for GUI)
- SQLite (for database management)
- `tkcalendar` (for date selection)

## Installation
To run the Student Management System, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/student-management-system.git
   cd student-management-system


2. **Install required packages**:
   Ensure you have Python installed, then install the required packages using pip:
   ```bash
   pip install tkcalendar

3. **Run the application**:
    Execute the following command to start the application:
    ```bash
    python student_management_system.py

## Usage
1. **Launch the application**: Run the application by executing the Python script.
2. **Fill in the student details**: Enter the required student information in the fields provided in the left frame.
3. **Submit and Add Record**: Click on the **Submit and Add Record** button to save the information to the database.
4. **Manage Records**: Use the buttons in the center frame to:
   - **Delete Record**: Remove a selected record from the database.
   - **View Record**: Display the details of a selected record in the input fields for editing.
   - **Reset Fields**: Clear all input fields to prepare for new data entry.
5. **View Student Records**: The right frame displays all student records in a scrollable table format.

## Database
The application creates a SQLite database named `SchoolManagement.db` to store student records. The database will be created automatically upon running the application if it does not already exist.
