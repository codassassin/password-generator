import secrets
import string


class passwordGenerator:
    def __init__(self):
        self.secure_password = None

    def password_gen(self, password_length):
        characters = string.ascii_letters + string.digits + string.punctuation

        self.secure_password = ''.join(secrets.choice(characters) for i in range(password_length))

        return self.secure_password

    def main(self):
        user_password_length = int(input("Input number of digits for password: "))

        print("Password Generated:", self.password_gen(user_password_length))


if __name__ == '__main__':
    pg = passwordGenerator()
    pg.main()
