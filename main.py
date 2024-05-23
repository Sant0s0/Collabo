from funciones import convert, decimal

def main() -> None:
    option = int(input("1. Caracter a Byte\n2.Palabra a Byte\n3. Byte a ASCII\n"))
    if option == 1:
        a = input("Ingresa el caracter: ")
        print(convert(ord(a)))
    elif option == 2:
        a = input("Ingresa la palabra: ")
        result = ""
        for x in a:
            result += f"{convert(ord(x))} "

        print(result)

    elif option == 3:
        a = input("Escribe el byte: ")
        result = decimal(a)
        print(f"{chr(result)}:{result}")
    
if __name__ == "__main__":
    main()