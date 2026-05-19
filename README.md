🗳️ Voting Machine System using Python (Tkinter)
📌 Project Overview

This project is a GUI-based Voting Machine System developed using Python and Tkinter. It simulates a real-world electronic voting process with role-based authentication, allowing admins to manage elections and users to cast votes securely. Voting data is stored persistently using JSON files, ensuring data is retained between sessions.

The system is designed for college elections, classroom voting, and learning purposes, with a focus on simplicity, security, and usability.

🎯 Objectives

Implement a secure and user-friendly voting system

Provide role-based access (Admin & User)

Enable candidate management and vote casting

Store voting data persistently

Display election results transparently

🛠️ Technologies Used

Programming Language: Python

GUI Framework: Tkinter

Image Handling: Pillow (PIL)

Data Storage: JSON

OS Utilities: os module

👥 User Roles
🔹 Admin

Login using admin credentials

Add new candidates

View election results

Reset data for a new election

🔹 User

Login using user credentials

Select and vote for a candidate

Vote only once per session

⚙️ Features

Role-based login authentication

Candidate addition and management

Secure vote casting

Persistent data storage using JSON

Result display for admin

New election / reset functionality

GUI with images and improved font readability

📂 Project Structure
voting-Machine-using-python/
│
├── users.json (Auto-generated on first run)
├── candidates.json (Auto-generated on first run)
├── university_logo.png
├── voting.png
├── main.py
└── README.md

▶️ How to Run the Project
1️⃣ Install Required Library
pip install pillow

2️⃣ Ensure the Following Files Are Present

university_logo.png

voting.png

(Note: `users.json` and `candidates.json` are automatically generated on the first run, loaded with default credentials.)

3️⃣ Run the Program
python main.py

🔐 Default Login Credentials
Admin

Username: admin

Password: admin123

Users

user1 / user123

user2 / user456

user3 / user789

user4 / userabc

user5 / userdef

📊 Output

Users can successfully cast votes

Admin can view vote counts for each candidate

Election data is saved automatically

Data can be reset for a new election

🚀 Future Enhancements

Prevent multiple votes using user voting status

Encrypt stored passwords

Database integration (MySQL / MongoDB)

Web-based version using Flask or Django

Result visualization using charts

👨‍💻 Author

Ayush Choudhary
B.Tech CSE (Cybersecurity)
JK Lakshmipat University, Jaipur

📜 License

This project is created for educational purposes only.
