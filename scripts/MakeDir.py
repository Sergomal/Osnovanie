import os

# checking if the directory demo_folder
# exist or not.
if os.path.exists(r"D:\My_Py\OSNOVANIE\Study"):
    # if the demo_folder directory is not present
    # then create it.
    for i in range(12):
        folder_name = "M" + str(i)
        path_folder = ()
        os.makedirs(r"D:\My_Py\OSNOVANIE\Study\\" + folder_name)
