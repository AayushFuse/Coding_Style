"""
Function for validating the email address
"""
import re


def validate_email(email):
    """
    Validates an email address based on specific rules.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, email):
        return False
    if " " in email:
        return False
    providers = ["yahoo.com", "gmail.com", "outlook.com"]
    domain = email.split("@")[1]
    if domain not in providers:
        return False

    disposable_emails = ["yopmain.com", "example.com"]
    if domain in disposable_emails:
        return False

    return True
