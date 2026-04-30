import string
import secrets

def generate_password(length,use_digits,use_symbols):
    password=[]
    password.append(secrets.choice(string.ascii_letters))
        
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice("!@#$%&*"))
        
    characters=string.ascii_letters
    if use_digits:
        characters+=string.digits
    if use_symbols:
        characters+="!@#$%&*"   

    while len(password)<length:
        password.append(secrets.choice(characters))
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)    


def main():
    print("\n==== Password Generator ====")
    try:
        length=int(input("Enter password length:"))
        if length<4:
            print("Password length should be at least 4.") 
            return
    except:
        print("Invalid input.Enter a number.")
        return
    choice_digits=input("Include digits?(Yes/No):").lower()
    choice_symbols=input("Include symbols?(Yes/No):").lower()               
    use_digits=choice_digits=="yes"
    use_symbols=choice_symbols=="yes"

    if not use_digits and not use_symbols:
        print("Warning: Password will be weak(only letters).")
    password=generate_password(length,use_digits,use_symbols)
    print("\nGenerate Password:")
    print(password)

if __name__ == "__main__":
    main()

        