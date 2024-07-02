def make_shirt(size, text):
    print(f"Text of shirt: {text}")
    print(f"Size of shirt: {size}")

text1 = input("Shirt text: ")
size1 = input("Size? ")

make_shirt(size1, text1)
make_shirt(size='XXL', text="Some Text!")
