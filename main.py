from flask import Flask
import subprocess

app = Flask(__name__)

def get_latest_commit():
    try:
        commit_id = subprocess.check_output(
            ["git", "rev-parse", "HEAD"]
        ).decode().strip()

        commit_msg = subprocess.check_output(
            ["git", "log", "-1", "--pretty=%B"]
        ).decode().strip()

        return commit_id, commit_msg
    except Exception:
        return "N/A", "Not a git repository"

@app.route("/")
def hello():
    commit_id, commit_msg = get_latest_commit()
    return f"""
    <h1>Hello World</h1>
    <p><strong>Latest Commit ID:</strong> {commit_id}</p>
    <p><strong>Commit Message:</strong> {commit_msg}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
