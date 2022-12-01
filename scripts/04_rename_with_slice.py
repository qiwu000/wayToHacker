import os
import glob

# change dir
os.chdir("/home/zhguo/test/")
for file in glob.glob("*.json"):
    # get name
    file_name = os.path.splitext(file)[0]
    # get type of extension
    extension = os.path.splitext(file)[1]
    # rename the file
    new_file_name = file_name[:-6] + extension
    try:
        os.rename(file, new_file_name)
    except OSError as e:
        print(e)
    # print result if no exception raised
    else:
        print("Renamed {} to {}".format(file, new_file_name))
