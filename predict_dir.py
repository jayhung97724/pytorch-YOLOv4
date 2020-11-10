from models import *
import glob

if __name__ == "__main__":
    import sys
    import cv2

    namesfile = None
    # if len(sys.argv) == 6:
    #     n_classes = int(sys.argv[1])
    #     weightfile = sys.argv[2]
    #     imgfile = sys.argv[3]
    #     height = int(sys.argv[4])
    #     width = int(sys.argv[5])
    # elif len(sys.argv) == 7:
    n_classes = 1
    weightfile = '.\checkpoints\Yolov4_epoch100.pth'
    img_dir = './data/mAp/images/'
    height = 608
    width = 608
    namesfile = '.\data\classes.names'
    # else:
    #     print('Usage: ')
    #     print('  python models.py num_classes weightfile imgfile namefile')

    model = Yolov4(yolov4conv137weight=None, n_classes=n_classes, inference=True)

    pretrained_dict = torch.load(weightfile, map_location=torch.device('cuda'))
    model.load_state_dict(pretrained_dict)

    use_cuda = True
    if use_cuda:
        model.cuda()

    img_files = glob.glob(os.path.join(img_dir, '*.png'))
    for imgfile in img_files:
        img = cv2.imread(imgfile)

        # Inference input size is 416*416 does not mean training size is the same
        # Training size could be 608*608 or even other sizes
        # Optional inference sizes:
        #   Hight in {320, 416, 512, 608, ... 320 + 96 * n}
        #   Width in {320, 416, 512, 608, ... 320 + 96 * m}
        sized = cv2.resize(img, (width, height))
        sized = cv2.cvtColor(sized, cv2.COLOR_BGR2RGB)

        from tool.utils import load_class_names, plot_boxes_cv2
        from tool.torch_utils import do_detect

        for i in range(2):  # This 'for' loop is for speed check
                            # Because the first iteration is usually longer
            boxes = do_detect(model, sized, 0.4, 0.6, use_cuda)

        # print(len(boxes))
        # print(boxes)
        # print(len(box))
        # print(box)
        box = boxes[0]
        pred_fname = 'predictions/pred_' + imgfile[imgfile.rfind('\\')+1:]
        output_fname = 'predictions/pred_' + imgfile[imgfile.rfind('\\')+1:imgfile.rfind('.png')] + '.txt'
        with open(output_fname , 'w') as outfile:
            if len(box) >= 1:
                class_names = load_class_names(namesfile)
                plot_boxes_cv2(img, box, pred_fname, class_names)
                cls_conf = box[0][5]
                cls_id = box[0][6]
                print('%s: %f' % (class_names[cls_id], cls_conf))
                blist = map(str, box[0][0:4])
                outline = str(cls_id) + ' ' + ' '.join(blist) + ' ' + str(cls_conf) + '\n'
                outfile.write(outline)
            else:
                print('no result')
                outline = '-1\n'
                outfile.write(outline)
