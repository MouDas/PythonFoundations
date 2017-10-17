import os

def rename_files():
#(1) Go to folder

    file_list = os.listdir("/Users/mousumi.das/Tool_Root/Scripts/OOP-Udacity/alphabet")
    print (file_list)
    saved_path = os.getcwd()
    print ("current working directory is"+saved_path)
    os.chdir("/Users/mousumi.das/Tool_Root/Scripts/OOP-Udacity/alphabet")
    new_path = os.getcwd()
    print ("new dir is"+new_path)
#(2) for each file rename without number
    
    for file_name in file_list:
        print ("old name"+file_name)
        os.rename(file_name,file_name.translate(None,"0123456789"))
        print ("new file name"+ file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
rename_files()
