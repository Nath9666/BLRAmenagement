import os

if __name__ == '__main__':
    
    pathTest = "./assets/vrac"
    PathLego = "./assets/Lego"

    #list all files in the directory
    files = os.listdir(pathTest)
    print(files)