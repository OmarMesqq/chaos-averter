import os 
import re
import chardet
from termcolor import colored

# Array of matching files and user given keywords
matches = []
keywords =[]
  


root = input("Enter root dir of restored data (eg. sort/PY): ")
ui =input("What keywords are you looking for in your files? (Press q to exit)\n")


def choice(ui):

    if ui == 'q':
        pass

    else:
        keywords.append(ui)
        ui =input("What keywords are you looking for in your files? (Press q to exit)\n")
        choice(ui)





def lineReader(arr): 

    # Counts number of folders in root dir
    for i in range(len(os.listdir(root))):

        # Walks the array containing each of these folders i.e enter each and every one of them
        for folder in os.listdir(root):

            # Access each and every file in the folder
            for filename in os.listdir(os.path.join(root, folder)):
                
                # Open the file in binary mode, detects its encoding and return to the user
                # This can be commented out if you only want to use the program for its main purpose
                f = open(os.path.join(root,folder ,f'{filename}') , 'rb') 
                x = chardet.detect(f.read()).get("encoding")
                print(os.path.join(root, folder,filename), "has encoding:", x)

                # Open file in read mode, ignoring possible errors of non UTF-8 standard encoding
                # Note: this will skip these "different" bytes, not detecting its text   
                file_lines = open(os.path.join(root,folder ,f'{filename}') , 'r', errors='ignore')

                # Read every single line of the file in search of a keyword 
                 
                print("Array is", arr)    
                text = colored("File has keyword in it!", color="red")
                for line in file_lines.readlines():

                    for word in arr:
                        
                        if re.search(word, line): 
                            print(text)
                            matches.append(os.path.join(root, folder, f'{filename}'))
                            print("Keyword", word, "found in:", os.path.join(root, folder, f'{filename}'))
                        else:
                            continue 
                
                        
        # Returns the number of the folder 
        # the algorithm is currently at 
        # Remember: arrays in Python start at zero
        print("Number of folder iteration:", i)


choice(ui)
lineReader(keywords)
final = colored(("Found matching files", matches), color='red')
print(final)
        