import settings, platform, cpuinfo, flask
from stats import Stats
from os import getenv
from werkzeug.exceptions import HTTPException
from datetime import datetime

# .env is loaded from the settings.py import

# Set up application
static_info = {"startup": datetime.now(),
               "cpu_brand": cpuinfo.get_cpu_info()['brand_raw'],
               "py_ver": f"{platform.python_version()} {platform.python_compiler()}",
               "os_ver": f"{platform.system()} {platform.release()} - {platform.version()}",
               "flask_ver": flask.__version__}
stats = Stats(int(getenv("UPDATE_INTERVAL")))
SHOW_ERRORS = int(getenv("SHOW_ERRORS"))
PB_length = int(getenv("PG_LENGTH"))
app = flask.Flask(__name__)

# Start stats loop
stats.start()


def progressbar(p):
    f = int((PB_length/100) * p)
    return f"[{'▰' * f}{'▱' * (PB_length - f)}]"


# Index
@app.route("/")
def index():
    return flask.render_template("index.html", static_info=static_info, stats=stats, time=datetime.now(), make_pb=progressbar, round=round)


# Error handling
@app.errorhandler(Exception)
def error_handler(e):
    if SHOW_ERRORS:
        print(f"[ERROR] {e}")
    code = e.code if isinstance(e, HTTPException) else 500
    desc = e.description if isinstance(e, HTTPException) else "Internal server error"
    return flask.render_template("error.html", CODE=code, CODE_MSG=desc), code


# When file is executed directly
if __name__ == "__main__":
    app.run(host=getenv("HOST"), port=getenv("PORT"))
