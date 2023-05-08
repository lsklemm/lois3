# Лабораторная работа №3 по дисциплине "Логические основы интеллектуальных систем"
# Вариант 9: Требуется расставить на шахматной доске восемь ферзей так, чтобы ни один из ферзей не находился под боем другого ферзя
# Выполнена студенткой группы 021703 БГУИР Склема Елена Дмитриевна
# 01.05.2023


#Проверка на нахождение ферзя на доске под угрозой других ферзей
def is_under_attack(board, row, col):
    for i in range(row):
        #Проверки на вертикальную атаку, на диагональную атаку сверху вниз и диагональную атаку снизу вверх
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return True
    return False


#Рекурсивная расстановка ферзей на шахматной доске
def place_queen(board, row=0):
    if row == len(board):
        return True
    #Начинает расстановку с первой строки и размещает ферзя в каждом столбце, который не находится под боем другого ферзя
    #Если ферзь успешно размещен, то функция переходит к следующей строке
    for col in range(len(board)):
        if not is_under_attack(board, row, col):
            board[row] = col
            if place_queen(board, row + 1):
                return True
    return False

#Создаем пустую шахматную доску
board = [-1] * 8

#Вывод решения на экран
if place_queen(board):
    for row in range(len(board)):
        line = ""
        for col in range(len(board)):
            #Если ферзь установлен верно, он обозначается  симоволом Q(Qeen), а пустые клетки доски точкой(.)
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
else:
    print("Решения не существует.")