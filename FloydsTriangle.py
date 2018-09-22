#!/usr/bin/python
def main():
    num = 1
    for i in range(3):
        for j in range(i + 1):
            print num,
            num = num + 1
        print 

if __name__ == "__main__":
    main()