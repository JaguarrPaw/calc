import pygame
import time
pygame.init()

black = (0,0,0)
grey = (211, 211, 211)

window = pygame.display.set_mode((800,800))
pygame.display.set_caption("ALEX Calculator")
window.fill(grey)
fps = pygame.time.Clock()


one = pygame.image.load("./imges/one.png")
two = pygame.image.load("./imges/two.png")
three = pygame.image.load("./imges/three.png")
four = pygame.image.load("./imges/four.png")
five = pygame.image.load("./imges/five.png")
six = pygame.image.load("./imges/six.png")
seven = pygame.image.load("./imges/seven.png")
eight = pygame.image.load("./imges/eight.png")
nine = pygame.image.load("./imges/nine.png")
plus_sign = pygame.image.load("./imges/addition-sign.png")
minus_sign = pygame.image.load("./imges/minus-sign.png")
multiplication_sign = pygame.image.load("./imges/multiplication-sign.png")
division_sign = pygame.image.load("./imges/division-sign.png")
dot_sign = pygame.image.load("./imges/dot.png")
equal_sign = pygame.image.load("./imges/equal.png")

number_pics = [one, two, three, four, five, six, seven, eight, nine]
sign_pics = [equal_sign, plus_sign, minus_sign, multiplication_sign, division_sign, dot_sign]

font = pygame.font.SysFont('comicsans', 50, True,)

class Sign:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

equal = Sign(610, 250, "=")
plus = Sign(540, 400, "+")
minus = Sign(620, 400, "-")
multiplication = Sign(700, 400, "*")
division = Sign(540, 500, "/")
dot = Sign(650, 520, ".")

sign_instances = [equal, plus, minus, multiplication, division, dot]


class Number:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

num1 = Number(10, 410, '1')
num2 = Number(90, 410, '2')
num3 = Number(170, 410, '3')
num4 = Number(10, 480, '4')
num5 = Number(90, 480, '5')
num6 = Number(170, 480, '6')
num7 = Number(10, 550, '7')
num8 = Number(90, 550, '8')
num9 = Number(170, 550, '9')

num_instances = [num1, num2, num3, num4, num5, num6, num7, num8, num9]


def button_pressed(selection):
    if (selection[0] > num1.x and selection[1] > num1.y) and (selection[0] < num1.x + 65 and selection[1] < num1.y + 65):
        return(1)
    elif (selection[0] > num2.x and selection[1] > num2.y) and (selection[0] < num2.x + 65 and selection[1] < num2.y + 65):
        return(2)
    elif (selection[0] > num3.x and selection[1] > num3.y) and (selection[0] < num3.x + 65 and selection[1] < num3.y + 65):
        return(3)
    elif (selection[0] > num4.x and selection[1] > num4.y) and (selection[0] < num4.x + 65 and selection[1] < num4.y + 65):
        return(4)
    elif (selection[0] > num5.x and selection[1] > num5.y) and (selection[0] < num5.x + 65 and selection[1] < num5.y + 65):
        return(5)
    elif (selection[0] > num6.x and selection[1] > num6.y) and (selection[0] < num6.x + 65 and selection[1] < num6.y + 65):
        return(6)
    elif (selection[0] > num7.x and selection[1] > num7.y) and (selection[0] < num7.x + 65 and selection[1] < num7.y + 65):
        return(7)
    elif (selection[0] > num8.x and selection[1] > num8.y) and (selection[0] < num8.x + 65 and selection[1] < num8.y + 65):
        return(8)
    elif (selection[0] > num9.x and selection[1] > num9.y) and (selection[0] < num9.x + 65 and selection[1] < num9.y + 65):
        return(9)
    elif(selection[0] > plus.x and selection[1] > plus.y) and (selection[0] < plus.x + 65 and selection [1] < plus.y + 65):
        return('+')
    elif (selection[0] > minus.x and selection[1] > minus.y) and (selection[0] < minus.x + 65 and selection[1] < minus.y + 65):
        return ('-')
    elif (selection[0] > multiplication.x and selection[1] > multiplication.y) and (selection[0] < multiplication.x + 65 and selection[1] < multiplication.y + 65):
        return ('*')
    elif (selection[0] > division.x and selection[1] > division.y) and (
            selection[0] < division.x + 65 and selection[1] < division.y + 65):
        return ('/')
    elif (selection[0] > dot.x - 15 and selection[1] > dot.y - 15) and (selection[0] < dot.x + 65 and selection[1] < dot.y + 65):
        return ('.')
    elif (selection[0] > equal.x - 10 and selection[1] > equal.y - 10) and (selection[0] < equal.x + 65 and selection[1] < equal.y + 65):
        return ('=')

def operation(num1, operator, num2):
    if operator == '+':
        total = num1 + num2
        return total
    elif operator == '-':
        total = num1 - num2
        return total
    elif operator == '*':
        total = num1 * num2
        return total
    elif operator == '/':
        total = num1 / num2
        return total
    else:
        total = "Error"
        return(total)


def draw_digits(value):
     count_display = font.render(value, True, (20,20,20))
     window.blit(count_display, (200, 200))
     pygame.display.update()


def draw_instructions(instruction):
    count_display = font.render(instruction, True, (20, 20, 20))
    window.blit(count_display, (100, 100))
    pygame.display.update()

exit = False
start_calculation = True
program = True
run = True
while program == True:

    #Proti loopa gia ekatharisi othonis
    while start_calculation == False:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                program = False
                start_calculation = True
                exit = True

        keys = pygame.key.get_pressed()
        draw_instructions("Press SPACE")

        #Otan patithei to SPACE key katharizei i othoni kai arxizei i epomeni loopa
        if keys[pygame.K_SPACE]:
            pygame.draw.rect(window, grey, (80, 80, 800, 400))
            start_calculation = True
            run = True

    calculator_screen = ""
    value = ""
    selecting_num2 = False

    #An den exei patithei to X gia kleisimo programatos, we validate the condition for the previous loop
    if exit == False:
        start_calculation = False

    #Defteri loopa -  Main loop
    while run == True:
        fps.tick(10)
        #Using for loop to create the numbers on the screen
        for i in range(0,9):
           window.blit(number_pics[i], (num_instances[i].x, num_instances[i].y))

        for i in range(0,6):
            window.blit(sign_pics[i], (sign_instances[i].x, sign_instances[i].y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                program = False

        if pygame.mouse.get_pressed()[0]:
            selection = pygame.mouse.get_pos()
            icon_selected = button_pressed(selection)


            if icon_selected == 1:
                value = value + str(icon_selected)
                calculator_screen = calculator_screen + str(icon_selected)
                print(value)
            elif icon_selected == 2:
                value = value + str(icon_selected)
                calculator_screen = calculator_screen + str(icon_selected)
                print(value)
            elif icon_selected == 3:
                value = value + str(icon_selected)
                calculator_screen = calculator_screen + str(icon_selected)
                print(value)
            elif icon_selected == 4:
                value = value + str(icon_selected)
                calculator_screen = calculator_screen + str(icon_selected)
                print(value)
            elif icon_selected == 5:
                value = value + str(icon_selected)
                calculator_screen = calculator_screen + str(icon_selected)
                print(value)
            elif icon_selected == 6:
                value = value + str(icon_selected)
                calculator_screen = calculator_screen + str(icon_selected)
                print(value)
            elif icon_selected == 7:
                value = value + str(icon_selected)
                calculator_screen = calculator_screen + str(icon_selected)
                print(value)
            elif icon_selected == 8:
                value = value + str(icon_selected)
                calculator_screen = calculator_screen + str(icon_selected)
                print(value)
            elif icon_selected == 9:
                value = value + str(icon_selected)
                calculator_screen = calculator_screen + str(icon_selected)
                print(value)
            elif icon_selected == '.':
                time.sleep(0.4)
                value = value + icon_selected
                calculator_screen = calculator_screen + str(icon_selected)
                print(value)
            elif icon_selected == '+':
                number1 = float(value)
                operator = icon_selected
                print(operator)
                calculator_screen = calculator_screen + str(icon_selected)
                value = ""
            elif icon_selected == '-':
                number1 = float(value)
                operator = icon_selected
                print(operator)
                value = ""
                calculator_screen = calculator_screen + str(icon_selected)
            elif icon_selected == '*':
                number1 = float(value)
                operator = icon_selected
                print(operator)
                value = ""
                calculator_screen = calculator_screen + str(icon_selected)
            elif icon_selected == '/':
                number1 = float(value)
                operator = icon_selected
                print(operator)
                value = ""
                calculator_screen = calculator_screen + str(icon_selected)
            elif icon_selected == '=':
                number2 = float(value)
                value = operation(number1, operator, number2)
                calculator_screen = calculator_screen + str(icon_selected) + str(value)
                print(value)
                value = ''
                selecting_num2 = False
                run = False

        draw_digits(calculator_screen)
        pygame.display.update()

pygame.quit()
