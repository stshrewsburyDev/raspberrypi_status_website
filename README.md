Raspberry Pi status website
===========================

##### Created by Steven Shrewsbury (stshrewsburyDev)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/stshrewsburyDev/raspberrypi_status_website)
![Python version](https://img.shields.io/badge/python-3.5+-yellow)
![Flask version](https://img.shields.io/badge/flask-1.1.2-3264FA)
![GitHub](https://img.shields.io/github/license/stshrewsburyDev/raspberrypi_status_website)

Installation:
-------------
###### Download with git:
```
git clone https://github.com/stshrewsburyDev/raspberrypi_status_website.git
```

###### Install dependencies:
```
pip install -r requirements.txt

# For some users pip links to Python2
pip3 install -r requirements.txt
```

**Warning:** Sometimes installing matplotlib via pip can freeze your rpi.
To solve this remove it from the requirements and install via:
```
sudo apt-get install python3-matplotlib
```

Setup:
------
Within the repository you will find a file named `sample.env`, rename it to `.env` before attempting to run this project.
Most of the settings that you can configure can be found within this `.env` file.

| Var:            | Default:  | Value:                                                                                                                                                                                                               |
|:---------------:|:---------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| HOST            | 0.0.0.0   | The IP address that you wish to host the website to. (only works when project is run via the `app.py` file)                                                                                                          |
| PORT            | 5000      | The port number of the IP address that you wish to host the website to. (only works when project is run via the `app.py` file)                                                                                       |
| LIBRARIES       | Flask:pip | A list of PyPi modules to check the currently installed versions for. (separate modules with ":")                                                                                                                     |
| PIP             | "pip"     | The command that the application uses to check installed library versions. (for example `python3 -m pip` or `pip3`)                                                                                                   |
| UPDATE_INTERVAL | 30        | The time in seconds that the application waits to auto update the stats. (**Note:** Making this lower than 30 seconds may break things or create lag)                                                                |
| PG_LENGTH       | 20        | The number symbols used in progress bar's.                                                                                                                                                                           |
| SHOW_ERRORS     | 0         | Boolean number (0 - off and 1 - on) to determine whether errors are shown in terminal, recommended to keep this set to 0 when in production.                                                                         |
| CHECK_PYPI      | 1         | Boolean number (0 - off and 1 - on) to determine whether to check for the latest version of the modules in `LIBRARIES` using PyPi.org, recommended to keep this set to 0 if your `UPDATE_INTERVAL` is lower than 30. |

Running:
--------
###### Run with Python
```
python app.py

# For some users python links to Python2
python3 app.py
```

###### Run with Flask
```
flask run
```
For more in depth info about running/deploying this to a production web server see here: [Deploying to a web server](https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment "Flask - Deployment Options")

Links:
------
* [My GitHub](https://github.com/stshrewsburyDev/ "GitHub | stshrewsburyDev")
* [GitHub repo](https://github.com/stshrewsburyDev/raspberrypi_status_website/ "GitHub | raspberrypi_status_website")
* [My website](https://stshrewsburydev.github.io/ "My website")
