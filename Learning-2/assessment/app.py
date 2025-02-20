# Project: Task Management Application
# Project Overview

# The Task Management Application allows users to create, update, delete, and manage tasks. 
# Users can categorize tasks, set deadlines, and mark them as complete. 
# This project can be built as a web application using a combination of technologies.

import streamlit as st
import sqlite3
from datetime import datetime

# Database Setup
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT DEFAULT 'Pending',
    due_date TEXT,
    category TEXT
)
""")
conn.commit()

# Function to load tasks
def load_tasks():
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()

# Function to add a task
def add_task(title, due_date, category):
    cursor.execute("INSERT INTO tasks (title, due_date, category) VALUES (?, ?, ?)", (title, due_date, category))
    conn.commit()

# Function to update task status
def update_task(task_id, status):
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
    conn.commit()

# Function to delete a task
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

# Streamlit UI
st.title("📝 Task Management App")

# Input for new task
new_task = st.text_input("Add a new task")

# Input for Due Date and Category
due_date = st.date_input("Set Due Date", min_value=datetime.today())
category = st.selectbox("Select Category", ["Work", "Personal", "Urgent"])

if st.button("Add Task"):
    if new_task.strip():
        add_task(new_task, due_date.strftime("%Y-%m-%d"), category)
        st.success(f"Task '{new_task}' added!")
    else:
        st.warning("Task cannot be empty!")

# Display tasks
tasks = load_tasks()
if tasks:
    for task in tasks:
        col1, col2, col3 = st.columns([4, 2, 2])
        col1.write(f"✅ {task[1]} - {task[3]} - {task[4]}" if task[2] == "Completed" else f"🔲 {task[1]} - {task[3]} - {task[4]}")
        if col2.button("Mark Complete", key=f"complete_{task[0]}"):
            update_task(task[0], "Completed")
            st.success(f"Task '{task[1]}' marked as complete.")
        if col3.button("❌ Delete", key=f"delete_{task[0]}"):
            delete_task(task[0])
            st.success(f"Task '{task[1]}' deleted.")
else:
    st.write("No tasks found. Add one above!")

# Close DB connection
conn.close()
