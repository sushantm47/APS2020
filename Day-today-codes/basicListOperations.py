if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    ans=sum(student_marks[query_name])/3
    print("%.2f"%ans)
#input mtd to obtain both list and string in same line
