# #КРЕСТИКИ-НОЛИКИ
# board = list(range(1, 10))
# victory_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), 
# (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

# def game_board():
#     print('-'*5)
#     for i in range(3):
#         print(board[0 + i * 3],
#          board[1 + i * 3], 
#          board[2 + i * 3])
#     print('-'*5)

# def take_input(player_select):
#     while True:
#         value = input('Куда ходят' + player_select + '? ->')
#         if not (value in '123456789'):
#             print('Таких клеток нет!!! Повтори заново, только будь внимательней ')
#             continue
#         value = int(value)
#         if str(board[value - 1]) in 'XO':
#             print('Эта клетка уже занята')
#             continue
#         board[value - 1] = player_select
#         break

# def check_win():
#     for each in victory_coord:
#         if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
#             return board[each[0]-1]
#     else:
#         return False

# def runner():
#     counter = 0
#     while True:
#         game_board()
#         if counter % 2 == 0:
#             take_input('X')
#         else:
#             take_input('O')
#         if counter > 3:
#             winner = check_win()
#             if winner:
#                 game_board()
#                 print(winner, 'Победили!')
#                 break
#         counter += 1
#         if counter > 8:
#             game_board()
#             print('Ничья!')
#             break

# runner()

# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
    
# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count +=1
#         else:
#             res = res +str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res

# s = input('Введите текст для кодировки: ')
# print(f'Текст после кодировки: {coding(s)}')
# print(f'Текст после декодировки: {decoding(coding(s))}')


