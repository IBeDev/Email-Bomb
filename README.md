# Email Bomber

## Description

This is an educational project designed to demonstrate the use of Python for sending bulk emails programmatically. The script allows users to specify the number of emails to send, attach files, and configure various email server settings. **This tool is strictly for educational purposes only. Any misuse of this script is the sole responsibility of the user.**

---

## Features

- Select from predefined bombing modes (e.g., 1000, 500, 250 emails) or set a custom amount.
- Supports Gmail, Yahoo, and Outlook servers.
- Allows file attachments.
- Implements threading and delay options to prevent emails from being flagged as spam.

---

## Prerequisites

Ensure the following are installed on your system:

- Python 3.x
- `smtplib`, `email`, `os`, and `threading` modules (standard Python libraries)

---

## Setting Up Gmail App Password

To use this script with Gmail, you must create an app password due to Google’s restrictions on less secure apps.

### Steps to Create an App Password

1. Open [Google Account Security Settings](https://myaccount.google.com/security).
2. Under the **"Signing in to Google"** section, enable **2-Step Verification** if not already enabled.
3. Click **App Passwords** (you may need to re-enter your password).
4. Select **Mail** as the app and **Other (Custom Name)** for the device.
5. Enter a custom name (e.g., "Email Bomber") and click **Generate**.
6. Copy the generated 16-character password.
7. Use this app password as the `from password` when running the script.

---

## Usage

### Running the Script

1. Clone the repository:

   ```bash
   git clone https://github.com/IBeDev/Email-Bomb.git
   cd email-bomber
   ```

2. Run the script:

   ```bash
   python email_bomber.py
   ```

3. Follow the prompts to configure your bombing mode, target email, email server, and other settings.

---

## Example

![Image](https://github.com/user-attachments/assets/7fe358d0-8a41-4256-a06c-11d05d597d26)
![Image](https://github.com/user-attachments/assets/9882d71d-0534-4c59-a7c3-e722f41d8d81)

## Important Notes

- **Use Responsibly**: This script is for educational purposes only. Sending unauthorized bulk emails can violate laws and terms of service.
- **Avoid Spam Filters**: Use appropriate delays and do not abuse this tool to avoid being flagged by spam filters.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- Python `smtplib` documentation
- Open-source contributors who inspire learning and ethical development

