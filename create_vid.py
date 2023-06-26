import cv2
import numpy as np
import glob
import os

framesize = (640, 480)

out = cv2.VideoWriter('outvideo.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 15, framesize)

relative_file_list = os.listdir('out_vid/reconstruction')
relative_file_list.sort()

for filename in relative_file_list:
    filename = os.path.join('out_vid/reconstruction', filename)
    img = cv2.imread(filename)
    print(filename)
    out.write(img)
out.release()

#python run_reconstruction.py -c pretrained/E2VID_lightweight.pth.tar -i data/MyFile.zip --auto_hdr --display --show_events --output_folder out_vid
