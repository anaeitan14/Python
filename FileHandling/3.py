import random

def three():
    generate_calculations()
    questions = open("math.txt", "r")
    solutions = []
    for calc in questions.readlines():
        first_num = calc[:2]
        operation = calc[3:4]
        second_num = calc[5:7]
        match operation:
            case "+":
                solutions.append(first_num + " " + operation + " " + second_num + " = " + str(int(first_num)+int(second_num)))
            case "-":
                solutions.append(first_num + " " + operation + " " + second_num + " = " + str(int(first_num)-int(second_num)))
            case "*":
                solutions.append(first_num + " " + operation + " " + second_num + " = " + str(int(first_num)*int(second_num)))
            case "/":
                solutions.append(first_num + " " + operation + " " + second_num + " = " + str(int(first_num)//int(second_num)))

        questions.close()

        solutions_file = open("solutions.txt", "w")

        for solution in solutions:
            solutions_file.write(solution+"\n")


def generate_calculations():
    questions = open("math.txt", "w")
    op = ["+","-","/","*"]

    for i in range(10):
        first_num = random.randint(10,99)
        second_num = random.randint(10,99)
        operation = op[random.randint(0,3)]
        calculation = str(first_num)+" " +operation+" "+str(second_num) + " = "
        questions.write(calculation+"\n")
        questions.write

if __name__ == "__main__":
    three()