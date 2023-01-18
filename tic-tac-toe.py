game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if not just_display:
            game_map[row][column] = player
        print("   a  b  c")
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error: Make sure you input row/column  as 0, 1 or 2", e)
    except Exception as e:
        print("Something went very wrong!!", e)



game = game_board(game, just_display=True)

game = game_board(game, 1, 2, 2)



# slice and index
# numbers = [1,2,3,4,5]
# # index
# print(numbers[1])
# # last index
# print(numbers[-1])
# # slice
# print(numbers[0:3])
# # slice from to last
# print(numbers[3:])
