correct = 0
control = ""
student = 0
answer = []

for i in range(1, 11):
    z = input(f"Type the answer of the {i}º question: ")
    ans_p = z.upper()
    answer.append(ans_p)

while control != "N":
    for c in range(1, 11):
        x = input(f"Type the answer to the {c}º question: ")
        st_answer = x.upper()
        if c == 1 and st_answer == answer[1]:
            correct += 1
        elif c == 2 and st_answer == answer[2]:
            correct += 1
        elif c == 3 and st_answer == answer[3]:
            correct += 1
        elif c == 4 and st_answer == answer[4]:
            correct += 1
        elif c == 5 and st_answer == answer[5]:
            correct += 1
        elif c == 6 and st_answer == answer[6]:
            correct += 1
        elif c == 7 and st_answer == answer[7]:
            correct += 1
        elif c == 8 and st_answer == answer[8]:
            correct += 1
        elif c == 9 and st_answer == answer[9]:
            correct += 1
        elif c == 10 and st_answer == answer[10]:
            correct += 1
    if ('high_score' not in vars()) or (correct > high_score):
        high_score = correct
    elif ('lower_score' not in vars()) or (correct < lower_score):
        lower_score = correct
    print(f"You got {correct} in the test.")
    y = input("Another student will take the test(Y/N): ")
    control = y.upper()
    student += 1

print(f"The highest score was {high_score}")
print(f"The lowest score was {lower_score}")
print(f"A total of {student} students did the test.")
print(f"The average is {round(correct/student, 2)}")
