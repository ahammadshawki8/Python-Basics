def function13(x):
    return 2000*x

print("imported helpers ...")

#python38
print("__name__ value:",__name__)

def main():
    print("Current Module Name:",__name__)

if __name__ == "__main__":
    main()
    print("run directly")
else:
    print("Run from import")


def found_index(to_search,target):
    for index,value in enumerate(to_search):
        if value == target:
            return index
    return "could not found"

shawki="good boy"

## we can find python prooblems in http://www.codingbat.com  and http://www.projecteuler.net
# we can do this without recursive function.
