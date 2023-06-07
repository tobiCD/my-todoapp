Filepath='py.txt'
def toto(filepath=Filepath):
    """Read a text file and return líst of to-do item """

    with open(filepath,'r')as file:
        todo_1=file.readlines()
    return todo_1
def write(todo, filepath=Filepath):
    """ write to do item list in a text file """
    with open(filepath,'w')as file:
         file.writelines(todo)

if __name__=="__main__":
    print(toto())
    print("heel0")
    """ câu lệnh if trên để thực thi nếu chạy file này chúng sẽ được thực thi 
    còn nếu import file này sang file khác câu lệnh if trên sẽ k đc thực thi """