import os
import shutil


class Move_file():
    """
    Move_file类用于
    """
    def __init__(self):
        self.FileRecv = "E:\FileRecv"
        self.MobileFile = "E:\FileRecv\MobileFile"
        self.target = "E:\DEC_Sec\sec\\"
        self.init()

    def init(self):
        self.FileRecv_list = []
        for item in os.listdir(self.FileRecv):
            if ".mp4" in item:
                self.FileRecv_list.append(item)
        self.MobileFile_list = []
        for item in os.listdir(self.MobileFile):
            if ".mp4" in item:
                self.MobileFile_list.append(item)
        self.target_list = os.listdir(self.target)

    def mkdir(self, file_name):
        path = os.path.join(self.target, file_name)
        if not os.path.exists(path):
            os.mkdir(path)


    def show_files(self, dir_name):
        print(os.listdir(self.target + dir_name))

    def move_file(self,choice):
        def move(source, target, choice):
            if choice == 1:
                source_path = os.path.join(self.FileRecv,source)
            else:
                source_path = os.path.join(self.MobileFile,source)
            target_path = os.path.join(self.target,target)
            shutil.move(source_path,target_path)
            print("source file : " + source)
            print("target dir : " + target)

        if choice == 1:
            list = self.FileRecv_list
        else:
            list = self.MobileFile_list
        print(list)
        total_count = len(list)
        for item in list:
            flag = True
            for name in self.target_list:
                if len(name) == 1:
                    if name in item:
                        move(item,name,choice)
                        flag = False
                        list.remove(item)
                        break
                else:
                    for i in range((len(name) - 1)):
                        temp = name[i] + name[i+1]
                        if temp in item:
                            move(item,name,choice)
                            flag = False
                            list.remove(item)
                            break
            default = "emm"
            if flag:
                # move(item,default,choice)
                print("Fail to allot : " + item)
            else:
                continue
        print("Total count : " + str(total_count))
        total_count = len(list)
        print("Failed count : " + str(total_count))
        print("------------------------------------------------")