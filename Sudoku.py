from graphics import *
import random
#Importing from the random library allows us to properly randomly generate the random game each time the program runs

def generate_sudoku():
    base = 3
    side = base * base
    nums = random.sample(range(1, side + 1), side)
    #These 3 work together to create the range of what numbers can be randomly generated.
    #Since side always equals 9 the nums function can only produce numbers from 1-9
    board = [[nums[(base * (r % base) + r // base + c) % side] for c in range(side)] for r in range(side)]
    #Board function is used to determine which row and column each generated number is placed in.
    squares = side * side
    #This makes sure only 9 boxes are generated for each row/column
    empties = squares * 3 // 4
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0

    return board

def draw_board(win, board, inputs):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = Text(Point(50*j + 25, 50*i + 25), str(board[i][j]))
                text.setSize(25)
                text.draw(win)
            else:
                inputs[i][j].draw(win)

def check_solution(board, user_board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != user_board[i][j]:
                return False
    return True

def main():
    board = generate_sudoku()
    user_board = [[0 for _ in range(9)] for _ in range(9)]

    win = GraphWin("Sudoku", 500, 700)
    win.setBackground("white")

    inputs = [[Entry(Point(50*j + 25, 50*i + 25), 1) for j in range(9)] for i in range(9)]
    draw_board(win, board, inputs)

    message = Text(Point(250, 650), "")
    message.setSize(20)
    message.draw(win)

    submit_button = Rectangle(Point(200, 450), Point(300, 490))
    submit_button.setFill("gray")
    submit_button.draw(win)
    submit_text = Text(Point(250, 470), "Submit")
    submit_text.setSize(16)
    submit_text.draw(win)

    while True:
        click_point = win.getMouse()
        if 200 < click_point.getX() < 300 and 450 < click_point.getY() < 490:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        try:
                            num = int(inputs[i][j].getText())
                            if 1 <= num <= 9:
                                user_board[i][j] = num
                            else:
                                message.setText("Please enter numbers from 1 to 9")
                                break
                        except ValueError:
                            message.setText("Please enter numbers from 1 to 9")
                            break
            else:
                break

    if check_solution(board, user_board):
        message.setText("Good job!")
    else:
        message.setText("Game Over. Try again.")

    win.getMouse()
    win.close()

main()