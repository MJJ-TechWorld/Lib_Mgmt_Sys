def greet():
    print("Welcome")

greet()

if __name__ == "__main__":
    with open("abc.txt", "r") as f :
        d = f.readlines()

    print(d)



    var = '1,Hrry,Sanket,4\n'

    for i in var:
        print(i)
        break

    print("Ye part to still execute hoga ")

