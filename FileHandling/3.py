import random

def generate_solution():
    questions = open('test_files/questions.txt', "r")
    calculations = []
    results = []
    for calc in questions.readlines():
        first_num = calc[:2]
        operation = calc[3:4]
        second_num = calc[5:7]

        match operation:
            case "+":
                calculations.append(first_num + " " + operation + " " + second_num + " = " + str(int(first_num)+int(second_num)))
                results.append(int(first_num)+int(second_num))
            case "-":
                calculations.append(first_num + " " + operation + " " + second_num + " = " + str(int(first_num)-int(second_num)))
                results.append(int(first_num) - int(second_num))

            case "*":
                calculations.append(first_num + " " + operation + " " + second_num + " = " + str(int(first_num)*int(second_num)))
                results.append(int(first_num) * int(second_num))

            case "/":
                calculations.append(first_num + " " + operation + " " + second_num + " = " + str(int(first_num)//int(second_num)))
                results.append(int(first_num) // int(second_num))

        questions.close()

        solutions_file = open("test_files/question_solutions.txt", "w")

        for line in calculations:
            solutions_file.write(line+"\n")

        solutions_file.close()

    return results


def generate_calculations():
    questions = open("test_files/questions.txt", "w")
    op = ["+","-","/","*"]

    for i in range(10):
        first_num = random.randint(10,99)
        second_num = random.randint(10,99)
        operation = op[random.randint(0,3)]
        calculation = str(first_num)+" " +operation+" "+str(second_num) + " = "
        questions.write(calculation+"\n")
        questions.write

    questions.close()


def check_student_test(file_name):
    f = open(file_name, "r")
    score = 0

    student_answer = []
    real_answer = generate_solution()
    for calc in f.readlines():
        student_answer.append(calc[10:])
    f.close()

    for i in range(len(student_answer)):
        if int(student_answer[i][:-1]) == real_answer[i]:
            score+=10

    return score


def check_students(file1_name,file2_name,file3_name):
    s1_score = check_student_test(file1_name)
    s2_score = check_student_test(file2_name)
    s3_score = check_student_test(file3_name)

    print(s1_score,s2_score,s3_score)


if __name__ == "__main__":
    check_students("test_files/tal_solution.txt","test_files/yotam_solution.txt","test_files/david_solution.txt")

