import numpy as  np

def main() :
    Score = np.random.randint(100, size=(10, 4))

    Q1(Score)
    print()
    Q2(Score)
    print()
    Q3(Score)
    print()
    Q4(Score)

def Q1(s) :
    print(s[:11, 2])

def Q2(s) :
    for score in s :
        print(sum(score))

def Q3(s) :
    index = [True, False, False, False, True, False, True, False, True, True]
    print(s[index])

def Q4(s) :
    print(s.transpose(1, 0))
    
main()