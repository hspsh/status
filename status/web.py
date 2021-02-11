from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

BASE_RES = {
    "api": "0.13",
    "space": "Hackerspace Pomorze",
    "logo": "https://hsp.sh/assets/logo_accent.png",
    "url": "https://hsp.sh",
    "location": {
        "address": "Do Studzienki 28, Gdańsk, Poland",
        "lon": 18.61124,
        "lat": 54.37116,
    },
    "contact": {
        "email": "kontakt@pomorze.hackerspace.pl",
        "irc": "irc://irc.freenode.net/hsp.sh",
        "twitter": "@hspomorze",
    },
    "issue_report_channels": ["email"],
    "state": {
        "icon": {
            # TODO: proper logos
            "open": "https://hsp.sh/assets/logo_accent.png",
            "closed": "https://hsp.sh/assets/logo.png",
        },
        "open": False,
    },
    "projects": [
        "https://github.com/hspsh",
        "https://wiki.hsp.sh",
    ],
}

WHOHACKS_ENDPOINT = "https://whois.at.hsp.sh/api/now"


def get_whohacks():
    res = requests.get(WHOHACKS_ENDPOINT)
    return res.json()


@app.route("/api/now")
def spaceapi():
    global BASE_RES
    res = {**BASE_RES}

    try:
        wh = get_whohacks()
        res["status"]["open"] = True if wh["headcount"] > 0 else False
    except Exception:
        pass  # TODO: Logging

    return jsonify(res)


@app.route("/")
def index():
    try:
        wh = get_whohacks()
    except Exception:
        pass  # TODO: Logging

    return render_template("index.html", **BASE_RES, **wh)


if __name__ == "__main__":
    app.run(debug=True)
