# safely open
file = open("hello.txt", "w")
try:
    file.write("Hello, World!")
except Exception as e:
    print(f"An error occured while writing to the file: {e}")
finally:
    # making sure to close it.
    file.close()
