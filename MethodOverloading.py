class Operations:
    @staticmethod
    def sumar(*args):
        """
        Calculates the sum of numbers.
        This method uses an asterisk (*) to accept a variable number of arguments.
        """
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            raise ValueError("The 'sumar' method expects either two or three arguments.")

class Main:
    @staticmethod
    def main():
        c = 3.2
        d = 5.0
        a = 2
        b = 6
        e = 3

        # Python handles these additions correctly because it's dynamically typed.
        # It'll automatically determine the result type (int, float, etc.).
        print("Sumar: ", Operations.sumar(a, b))
        print("Sumar: ", Operations.sumar(a, b, e))
        print("Sumar: ", Operations.sumar(c, d))
        # Additional calls that would work:
        # print("Sumar: ", Operations.sumar(a, c))
        # print("Sumar: ", Operations.sumar(c, a))

# The entry point of the script
if __name__ == '__main__':
    Main.main()