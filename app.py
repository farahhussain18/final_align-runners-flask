from flask import Flask, render_template, request, redirect, url_for, flash
import json, os, time

app = Flask(__name__)
app.secret_key = "dev-only-local-secret"  # fine for local dev

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
DATA_FILE = os.path.join(DATA_DIR, "profiles.json")

def ensure_data_file():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

def load_profiles():
    ensure_data_file()
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_profiles(profiles):
    with open(DATA_FILE, "w") as f:
        json.dump(profiles, f, indent=2)

def get_profile(profile_id):
    profiles = load_profiles()
    for p in profiles:
        if str(p["id"]) == str(profile_id):
            return p
    return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/profiles")
def list_profiles():
    profiles = load_profiles()
    return render_template("profiles.html", profiles=profiles)

@app.route("/profiles/new", methods=["GET", "POST"])
def new_profile():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age = request.form.get("age", "").strip()
        city = request.form.get("city", "").strip()
        pace = request.form.get("pace", "").strip()  # min/km, e.g. 5:30 or 5.5
        fav_distance = request.form.get("fav_distance", "").strip()
        bio = request.form.get("bio", "").strip()

        if not name or not pace:
            flash("Name and pace are required.")
            return redirect(url_for("new_profile"))

        try:
            # Allow 5:30 or 5.5 formats
            if ":" in pace:
                m, s = pace.split(":")
                pace_val = float(m) + float(s) / 60.0
            else:
                pace_val = float(pace)
        except ValueError:
            flash("Pace must be a number (e.g., 5.30 or 5:30 for min/km).")
            return redirect(url_for("new_profile"))

        profiles = load_profiles()
        profiles.append({
            "id": int(time.time() * 1000),
            "name": name,
            "age": age,
            "city": city,
            "pace": pace_val,
            "fav_distance": fav_distance,
            "bio": bio,
        })
        save_profiles(profiles)
        flash("Profile created! Find matches 🙂")
        return redirect(url_for("list_profiles"))

    return render_template("new_profile.html")

@app.route("/matches")
def matches():
    """Find matches for a given profile id via ?for=<id>"""
    pid = request.args.get("for")
    if not pid:
        flash("Pick a profile to find matches.")
        return redirect(url_for("list_profiles"))

    me = get_profile(pid)
    if not me:
        flash("Profile not found.")
        return redirect(url_for("list_profiles"))

    candidates = []
    for p in load_profiles():
        if p["id"] == me["id"]:
            continue
        # Simple score: pace difference + small penalty if favorite distance differs
        pace_diff = abs(float(p["pace"]) - float(me["pace"]))
        dist_penalty = 0.5 if (p.get("fav_distance") != me.get("fav_distance")) else 0.0
        score = pace_diff + dist_penalty
        candidates.append((score, p))

    candidates.sort(key=lambda x: x[0])
    top = [c[1] for c in candidates[:5]]
    return render_template("matches.html", me=me, matches=top)

if __name__ == "__main__":
    ensure_data_file()
    app.run(debug=True)
