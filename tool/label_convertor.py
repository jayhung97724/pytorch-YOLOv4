import os
import glob

# hyper parameters
label_path = 'D:/Code/yolo/pytorch-YOLOv4/data/train_origin.txt'
output_path = 'D:/Code/yolo/pytorch-YOLOv4/data/train.txt'
width = 1920
height = 1080

with open(output_path, "a") as outfile:
    with open(label_path, "r") as infile:
        lines = infile.readlines()
        for line in lines:
            li = line.split()
            pth = li[0]
            rest = li[1].split(',')
            x_c = float(rest[0])
            y_c = float(rest[1])
            wi = float(rest[2])/2
            hi = float(rest[3])/2

            x1 = str(int(width * (x_c - wi)))
            y1 = str(int(height * (y_c - hi)))
            x2 = str(int(width * (x_c + wi)))
            y2 = str(int(height * (y_c + hi)))

            outline = pth + ' ' + x1 + ',' + y1 + ',' + x2 + ',' + y2 + ',0\n'
            print(outline)
            outfile.write(outline)
        