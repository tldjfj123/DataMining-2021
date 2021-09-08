import random

# Q1. 
def concatenate_list() :
    tmp1 = [random.randint(1, 100) for num in range(20)]
    tmp2 = [random.randint(1, 100) for num in range(20)]
    print(tmp1 + tmp2)
    print(list(set(tmp1 + tmp2)))

# Q2.
def calculateGrade() :
    # Answers = A ~ E (ASCII 65 ~ 69)
    answer = [chr(random.randint(65, 69)) for _ in range(10)]
    student = [[chr(random.randint(65, 69)) for _ in range(10)] for _ in range(8)]

    for p in range(8) :
        count = 0
        for i in range(len(answer)) :
            if student[p][i] == answer[i] :
                count += 1
        print("{} 번 학생의 정답 문항의 개수는 {} 입니다.".format(p, count))

def main() :
    concatenate_list()
    calculateGrade()

main()