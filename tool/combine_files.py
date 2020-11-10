import os
import glob

# hyper parameters
txt_dir = './predictions/'
output_path = './predictions/result.txt'
# testfile = 'D:/Code/yolo/pytorch-YOLOv4/data/back\\740.txt'


read_files = glob.glob(os.path.join(txt_dir, '*.txt'))
print('hi')

with open(output_path, "w") as outfile:
    for f in read_files:
        with open(f, "r") as infile:
            # outfile.write(infile.read())
            words = infile.read().split()
            print(words)
            if words[0] == '-1':
                outline = f[f.rfind('\\')+1:] + ',0,0,0,0,0\n'
            else:
                outline = f[f.rfind('\\')+1:] + ',' + ','.join(words[1:]) + '\n'
            outfile.write(outline)