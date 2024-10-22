#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management.commands.runserver import Command as runserver

runserver.default_port = "80"  # Running on port 80

CHAPTER_NAMES = [
    "Acacia", "Alpha_Chi_Rho", "Alpha_Epsilon_Pi", "Alpha_Sigma_Phi", 
    "Chi_Phi", "Delta_Kappa_Epsilon", "Delta_Phi", "Lambda_Chi_Alpha", 
    "Phi_Gamma_Delta", "Phi_Kappa_Theta", "Phi_Mu_Delta", "Phi_Sigma_Kappa", 
    "Pi_Kappa_Alpha", "Pi_Lambda_Phi", "Psi_Upsilon", "Sigma_Alpha_Epsilon", 
    "Sigma_Chi", "Sigma_Phi_Epsilon", "Tau_Epsilon_Phi", "Tau_Kappa_Epsilon", 
    "Theta_Xi", "Zeta_Psi", "Delta_Tau_Delta", "Alpha_Phi_Alpha", 
    "Phi_Iota_Alpha", "Pi_Delta_Psi", "Lambda_Upsilon_Lambda", 
    "Omega_Phi_Beta", "Sigma_Iota_Alpha", "Alpha_Gamma_Delta", 
    "Alpha_Phi", "Pi_Beta_Phi", "Alpha_Omega_Epsilon", 
    "Rensselaer_Society_Of_Engineering_Innovation", "Order_Of_Omega"
]

def create_users():
    """Create admin and chapter users if they don't exist."""
    import django
    django.setup()  # Initialize Django
    from django.contrib.auth.models import User

    # Create admin user
    if not User.objects.filter(username='fscAdminUser').exists():
        User.objects.create_superuser(
            username='fscAdminUser',
            email='fscaccountemail@gmail.com',
            password='RCOSfall2024'
        )
        print("Admin user created successfully.")
    else:
        print("Admin user already exists.")

    # Create chapter users
    for chapter in CHAPTER_NAMES:
        if not User.objects.filter(username=chapter.lower()).exists():
            User.objects.create_user(
                username=chapter.lower(),  # Username in lowercase for consistency
                email=f"{chapter.lower()}@example.com",
                password=chapter.lower()  # Password is the same as username
            )
            print(f"Standard user '{chapter.lower()}' created successfully.")
        else:
            print(f"Standard user '{chapter.lower()}' already exists.")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IFC.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Create users when running the server
    if sys.argv[1] == 'runserver':
        create_users()  # Create admin and chapter users

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
