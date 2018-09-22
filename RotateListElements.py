#!usr/bin/python
def rotate(l, s):
    return l[s:] + l[:s]

def main():
    lis = [1,2,3,4,5]
    ro = 4 #number of rotations
    print rotate(lis, ro)
    
    
if __name__ == "__main__":
    main()