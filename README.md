# WebsiteTemplate
An RCOS project used for club websites at RPI

### Acknowledgments
This project is based on [WebsiteTemplate](https://github.com/Rezlang/WebsiteTemplate/) by Josh Moskoff and Anson Decker, which is licensed under the MIT License. The original license can be found in the `WebsiteTemplate_LICENSE` file.

# Setup
On windows, the first-time setup process can be performed completely by running the included setup.bat script.

# Starting the server
This repo comes with two VSCode launch configs; one for local device testing only (Loopback Debugger), and another for testing on remote clients (LAN Debugger). Note that the LAN Debugger binds to all available adapters, including but not limited to loopback and LAN.

To launch one of the predefined VSCode configs, navigate to 'Run & Debug' in the left sidebar, and then select a config.
To start the server normally, run `.venv\scripts\python.exe manage.py runserver`. Remember to use the venv when launching the server, and not your system's python installation!
