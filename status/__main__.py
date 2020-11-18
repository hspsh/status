from flask import Flask, render_template

app = Flask(__name__)

BASE_RES = {
    "api": "0.13",
    "space": "Hackerspace Pomorze",
    "logo": "https://hsp.sh/assets/hsp-gray.png",
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
            "open": "http://shackspace.de/sopen.gif",
            "closed": "http://shackspace.de/sopen.gif",
        },
        "open": false,
    },
    "projects": [
        "http://github.com/shackspace",
        "http://shackspace.de/wiki/doku.php?id=projekte",
    ],
}


@app.route("/api/now")
def spaceapi():
    global BASE_RES
    result = {**BASE_RES}
    result["status"]["open"] = false
    return jsonify(result)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
