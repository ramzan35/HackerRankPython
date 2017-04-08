if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

total = 0
count = 0
for marks in student_marks[query_name]:
    total += marks
    count+=1

print("{0:.2f}".format(round(total/count,2)))
