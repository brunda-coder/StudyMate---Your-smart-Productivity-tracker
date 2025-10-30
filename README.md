# StudyMate---Your-smart-Productivity-tracker
StudyMate is a simple Python-based productivity tracker designed for students who want to manage text reports and visual charts. their daily study habits. It allows users to log subjects, study duration, and break time, then summarizes productivity stats through easy-to-read.

Key Features:
1. Add daily study sessions (subject, duration, focus level).
2. Automatically calculate total study time per day.
3. Display a weekly summary report.
4. Visualize progress using matplotlib (like a bar chart for hours per subject).
5. Option to save and load data from a .csv file.

Bonus: motivational quotes after logging a study session 🎯

⚙️ Tech Stack:
Language: Python 3
Libraries: csv, datetime, matplotlib, random (for quotes)

📁 Project Structure:

StudyMate/
│
├── main.py                # main program logic
├── tracker.py             # functions for adding, viewing, and saving sessions
├── data/
│   └── sessions.csv       # stores user data
├── assets/
│   └── quotes.txt         # optional motivational quotes
├── requirements.txt       # library dependencies
└── README.md              # project documentation

Installation:
git clone https://github.com/<your-username>/StudyMate.git
cd StudyMate
pip install -r requirements.txt
python main.py

Sample Output:
📘 Subject: Python Programming
⏱  Duration: 2 hours
🌈  Focus Level: 8/10
✨  Great job! Consistency builds genius.

Future Scope (for resume mention)
1. Add GUI with tkinter
2. Integrate Pomodoro timer
3. Sync with Google Calendar or To-Do APIs
