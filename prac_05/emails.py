"""
CP1404/CP5632 Practical05
Store user emails as unique keys/ names as values in dictionary
Estimate: 30 minutes
Actual: 60 minutes
"""

def main():
    """Store users' emails (keys) and names (values) in a dictionary."""
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        extracted_name = extract_name(email)
        choice = input(f"Is your name {extracted_name}? (Y/n) ").upper()
        if choice != "Y":
            name = input("Name: ").strip().title()
        else:
            name = extracted_name
        email_to_name[email] = name
        email = input("Email: ").strip()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extracts users' emails from an entered string."""
    part = email.split("@")[0]
    parts = part.split(".")
    return " ".join(parts).title()


main()
