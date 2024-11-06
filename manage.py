#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management.commands.runserver import Command as runserver
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IFC.settings')

runserver.default_port = "80"  # Running on port 80


def main():
    """Run administrative tasks."""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    if (os.environ.get('RUN_MAIN') != 'true'):  # prevent second execution by django autoloader
        if (sys.argv[1] == 'project_init'):
            from _project_setup import project_setup
            print("Performing live init tasks")
            project_setup()
            exit()

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
