def print_triangle(num):
    for i in range(num):
        for j in range(i+1):
            print("*",end="")   
        print("")

if __name__ == "__main__":
    print_triangle(5)