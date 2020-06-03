from move_file import Move_file

def move_file():
    move_file = Move_file()
    move_file.move_file(1)
    move_file.move_file(2)

def mkdir(file_name):
    move_file = Move_file()
    move_file.mkdir(file_name)


mkdir("爱音麻里亚")
move_file()


