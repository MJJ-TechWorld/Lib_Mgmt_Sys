def test():
    try:
        print("Try")
        return 10
    finally:
        print("Finally")

print(test())


