Align 🏃❤️ — A Dating Web App for Runners

Align is a simple Flask-based web application that helps runners create profiles, explore others, and find matches based on pace and favorite distances. This project is an MVP (Minimum Viable Product) meant to demonstrate multi-page navigation, profile persistence, and basic matching logic.

🚀 Features

Landing page → Welcome screen with branding.

Create Profile → Add your running details (name, pace, distance, bio).

Profiles List → View all registered runners.

Matching Engine → Finds closest matches based on pace + distance.

Styled UI → Using base.html template inheritance + styles.css for consistent layout and design.

Persistent Data → Profiles stored locally in JSON (data/profiles.json).

📂 Project Structure
final_align-runners-flask/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Project dependencies
├── venv/                  # Virtual environment (not committed)
├── data/
│   └── profiles.json      # Stores runner profiles
├── static/
│   └── styles.css         # CSS styling
└── templates/
    ├── base.html          # Layout template
    ├── index.html         # Landing page
    ├── new_profile.html   # Create new profile form
    ├── profiles.html      # List of all profiles
    └── matches.html       # Show matches for a profile

⚙️ Installation
1. Clone the repository
git clone git@github.com:farahhussain18/final_align-runners-flask.git
cd final_align-runners-flask

2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the app
python3 app.py


The app will start at:
👉 http://127.0.0.1:5000

🖥️ Usage

Open the app in your browser.

Create your runner profile with:

Name

Pace (min/km)

Favorite distance (5K, 10K, Half, etc.)

Bio

Browse all existing profiles.

Select a profile → find best matches based on pace similarity and distance preference.

🛠️ Tech Stack

Backend → Flask (Python)

Frontend → HTML, Jinja2 templates, CSS

Data → JSON file storage

🌱 Future Enhancements

User authentication (login with email/Google/Strava).

Database integration (SQLite/Postgres).

Richer matching algorithm (interests, location).

Mobile-friendly responsive UI.

Deploy to cloud (Heroku, Render, or Railway).

🤝 Contributing

Fork the repo

Create a branch: git checkout -b feature-name

Commit your changes: git commit -m "Added new feature"

Push the branch: git push origin feature-name

Open a Pull Request

📜 License

This project is licensed under the MIT License.
Feel free to fork, modify, and build upon it.

👟 Inspiration

Built with ❤️ by runners, for runners — because finding your pace should also mean finding your person.
