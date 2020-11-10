# from collections import defaultdict
# from tqdm import tqdm
import os
import glob

# hyper parameters
images_dir_path = 'D:/Code/yolo/pytorch-YOLOv4/data/back_val/'
output_path = './val.txt'
# testfile = 'D:/Code/yolo/pytorch-YOLOv4/data/back\\740.txt'


read_files = glob.glob(os.path.join(images_dir_path, '*.txt'))
print('hi')

with open(output_path, "a") as outfile:
    for f in read_files:
        with open(f, "r") as infile:
            # outfile.write(infile.read())
            words = infile.read().split()
            outline = f + ' ' + ','.join(words[1:]) + ',0\n' #remember to replace '.txt' with '.png'
            outfile.write(outline)