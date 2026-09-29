def get_num(msg):
    while True:
        try:
            n = float(input(msg))
            if n > 0:
                return n
            print("Enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

def get_names(msg):
    while True:
        names = [x.strip().title() for x in input(msg).split(",") if x.strip()]
        names = list(dict.fromkeys(names))
        if names:
            return names
        print("Enter at least one name.")
