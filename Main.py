import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json

# Function to load previous data
def load_previous_data():
    global users, candidates
    try:
        with open(USERS_FILE, "r") as users_file:
            users = json.load(users_file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = {}

    try:
        with open(CANDIDATES_FILE, "r") as candidates_file:
            candidates = json.load(candidates_file)
    except (FileNotFoundError, json.JSONDecodeError):
        candidates = {}

# Function to add admin and users to the JSON file
def add_admin_and_users():
    # Define admin and users data
    admin_data = {"admin": {"password": "admin123", "role": "admin", "voted": False}}
    user_data = {
        "user1": {"password": "user123", "role": "user", "voted": False},
        "user2": {"password": "user456", "role": "user", "voted": False},
        "user3": {"password": "user789", "role": "user", "voted": False},
        "user4": {"password": "userabc", "role": "user", "voted": False},
        "user5": {"password": "userdef", "role": "user", "voted": False}
    }
    
    # Check if the file exists
    if not os.path.exists('users.json'):
        # Create the file if it does not exist
        with open('users.json', 'w') as file:  # Use 'w' mode here
            json.dump({}, file)  # Write an empty JSON object
    
    # Load existing data from the JSON file
    with open('users.json', 'r') as file:
        data = json.load(file)
    
    # Update data with admin and users
    data.update(admin_data)
    data.update(user_data)
    
    # Write the updated data back to the JSON file
    with open('users.json', 'w') as file:
        json.dump(data, file, indent=4)

# File paths
USERS_FILE = "users.json"
CANDIDATES_FILE = "candidates.json"

# Load previous data
load_previous_data()

# Function to save data to JSON files
def save_data():
    with open(USERS_FILE, "w") as users_file:
        json.dump(users, users_file, indent=4)

    with open(CANDIDATES_FILE, "w") as candidates_file:
        json.dump(candidates, candidates_file, indent=4)

# Function to verify user login
def login():
    global current_user
    username = username_entry.get()
    password = password_entry.get()
    role = role_var.get()
    
    if username in users and users[username]["password"] == password and users[username]["role"] == role:
        messagebox.showinfo("Success", "{} verified.".format(role.capitalize()))
        current_user = users[username]
        if role == "admin":
            admin_frame.grid(row=1, column=0, columnspan=2)
            reset_data_button.config(state=tk.NORMAL)
            results_button.config(state=tk.NORMAL)  # Enable results button for admin
        else:
            user_frame.grid(row=1, column=0, columnspan=2)
            cast_vote_button.config(state=tk.NORMAL)
            add_candidate_button.config(state=tk.NORMAL)
    else:
        messagebox.showerror("Error", "Invalid credentials.")

# Function to cast vote
def cast_vote():
    selected_candidate = candidate_var.get()
    candidates[selected_candidate] += 1
    messagebox.showinfo("Success", "Vote casted successfully for {}.".format(selected_candidate))
    cast_vote_button.config(state=tk.DISABLED)
    # Save data after vote is casted
    save_data()

# Function to add a new candidate
def add_candidate():
    if current_user["role"] == "admin":
        new_candidate = new_candidate_entry.get()
        if new_candidate.strip() != "":
            if new_candidate not in candidates:
                candidates[new_candidate] = 0
                candidate_var.set(new_candidate)  # Set the variable value
                candidate_menu['menu'].add_command(label=new_candidate, command=lambda: candidate_var.set(new_candidate))
                messagebox.showinfo("Success", "{} added as a new candidate.".format(new_candidate))
                new_candidate_entry.delete(0, tk.END)
                # Save data after adding a new candidate
                save_data()
            else:
                messagebox.showerror("Error", "Candidate already exists.")
        else:
            messagebox.showerror("Error", "Please enter a candidate name.")
    else:
        messagebox.showerror("Error", "You are not authorized to add candidates.")

# Function to display results
def display_results():
    if current_user["role"] == "admin":
        results_text = "Previous Votes:\n"
        for candidate, votes in candidates.items():
            results_text += "{}: {}\n".format(candidate, votes)
        messagebox.showinfo("Previous Votes", results_text)
    else:
        messagebox.showerror("Error", "You are not authorized to view previous votes.")

# Function to reset data for a new election
def reset_data():
    global users, candidates
    if current_user["role"] == "admin":
        # Clear the existing data
        users = {}
        candidates = {}
        # Save the cleared data to JSON files
        save_data()
        # Show a message indicating data has been reset
        messagebox.showinfo("Data Reset", "Previous data cleared for a new election.")
        reset_data_button.config(state=tk.DISABLED)
        cast_vote_button.config(state=tk.DISABLED)
        add_candidate_button.config(state=tk.DISABLED)
    else:
        messagebox.showerror("Error", "You are not authorized to reset data.")

# GUI setup
root = tk.Tk()
root.title("Login")

# Increase font size
root.option_add("*Font", "Helvetica 14")

# Load university logo
try:
    university_logo = Image.open("university_logo.png")
    university_logo = university_logo.resize((200, 200))
    university_logo = ImageTk.PhotoImage(university_logo)
    logo_label = tk.Label(root, image=university_logo)
    logo_label.grid(row=1, column=0, columnspan=2)
except FileNotFoundError:
    messagebox.showerror("Error", "University logo image not found.")

# Add "Voting Machine" text above logo
heading_label = tk.Label(root, text="Voting Machine", font=("Helvetica", 20))
heading_label.grid(row=0, column=0, columnspan=2, pady=10)

# Load voting image and create a PhotoImage object
try:
    voting_image = Image.open("voting.png")
    voting_image = voting_image.resize((200, 200))
    voting_image = ImageTk.PhotoImage(voting_image)
    # Create a label to display the voting image
    voting_label = tk.Label(root, image=voting_image)
    voting_label.grid(row=1, column=2, columnspan=2)
except FileNotFoundError:
    messagebox.showerror("Error", "Voting image not found.")

# Frames for admin and user functionality
admin_frame = tk.Frame(root)
user_frame = tk.Frame(root)

# Username label and entry
username_label = tk.Label(admin_frame, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
username_entry = tk.Entry(admin_frame)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password label and entry
password_label = tk.Label(admin_frame, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
password_entry = tk.Entry(admin_frame, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Role label and option menu
role_label = tk.Label(admin_frame, text="Role:")
role_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
role_var = tk.StringVar()
role_var.set("user")
role_menu = tk.OptionMenu(admin_frame, role_var, "user", "admin")
role_menu.grid(row=2, column=1, padx=10, pady=5)

# Login button
login_button = tk.Button(admin_frame, text="Login", command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=5)

# Candidate selection
candidate_var = tk.StringVar()
candidates_label = tk.Label(user_frame, text="Select Candidate:")
candidates_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
candidate_names = list(candidates.keys())  # Get the list of candidate names
candidate_var.set(candidate_names[0] if candidate_names else "")  # Set default value
if candidate_names:  # Check if candidate names exist
    candidate_menu = tk.OptionMenu(user_frame, candidate_var, *candidate_names)
    candidate_menu.grid(row=0, column=1, padx=10, pady=5)
else:
    candidate_menu = tk.OptionMenu(user_frame, candidate_var, "No candidates")
    candidate_menu.grid(row=0, column=1, padx=10, pady=5)

# Add new candidate entry and button
new_candidate_label = tk.Label(user_frame, text="Enter New Candidate:")
new_candidate_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
new_candidate_entry = tk.Entry(user_frame)
new_candidate_entry.grid(row=1, column=1, padx=10, pady=5)
add_candidate_button = tk.Button(user_frame, text="Add Candidate", command=add_candidate, state=tk.DISABLED)
add_candidate_button.grid(row=2, column=0, columnspan=2, pady=5)

# Cast vote button (disabled initially)
cast_vote_button = tk.Button(user_frame, text="Cast Vote", command=cast_vote, state=tk.DISABLED)
cast_vote_button.grid(row=3, column=0, columnspan=2, pady=5)

# Display results button
results_button = tk.Button(admin_frame, text="Display Results", command=display_results, state=tk.DISABLED)
results_button.grid(row=4, column=0, columnspan=2, pady=5)

# New Election / Reset Data button (disabled initially)
reset_data_button = tk.Button(admin_frame, text="New Election / Reset Data", command=reset_data, state=tk.DISABLED)
reset_data_button.grid(row=5, column=0, columnspan=2, pady=5)

# Initially display the admin frame
admin_frame.grid(row=1, column=0, columnspan=2)

# Hide the user frame initially
user_frame.grid_forget()

root.mainloop()
