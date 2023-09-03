import cv2
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

DATA_DIR = "/Users/weijiang/Data/20181029_D10_0900_0930"
OUTPUTP_DIR = "/Users/weijiang/Data"

COLORS = {
    'Bus': (228, 201, 248), 
    'Car': (177, 238, 197), 
    'Heavy Vehicle': (236, 16, 91), 
    'Medium Vehicle': (25, 84, 87), 
    'Motorcycle': (243, 138, 41), 
    'Taxi': (87, 126, 91)
    }
ARROW_LENGTH = 30
ARROW_THICKNESS = 5

def draw_frame(frame_num, show_img=False):

    # read the csv file
    frame_annos = pd.read_csv("{}/Annotations/{:05d}.csv".format(DATA_DIR, frame_num))
    # frame_annos.columns 
    # Index(['Time [s]', 'ID', 'Type', 'x_img [px]', 'y_img [px]',
    #        'Angle_img [rad]'],
    #       dtype='object')



    veh_type = frame_annos['Type'].tolist()
    veh_color = frame_annos['Type'].apply(lambda x: COLORS.get(x, "Car"))

    veh_x = frame_annos['x_img [px]'].to_numpy()
    veh_y = frame_annos['y_img [px]'].to_numpy()
    veh_xy = np.concatenate((veh_x[:, np.newaxis], veh_y[:,np.newaxis]), axis=1)
    # Unit: rad, valued from 0 to 2pi, with 0 being the x-axis, and the value increases counter-clockwise
    veh_ang = frame_annos['Angle_img [rad]'].to_numpy() 
    arrow_dx, arrow_dy = np.cos(veh_ang), np.sin(veh_ang)
    arrow_end_xy = veh_xy + ARROW_LENGTH * np.concatenate((arrow_dx[:, np.newaxis], arrow_dy[:, np.newaxis]), axis=1)
    arrow_end_xy = arrow_end_xy.astype(np.int32)

    image = cv2.imread("{}/Frames/{:05d}.jpg".format(DATA_DIR, frame_num))
    for start, end, t in zip(veh_xy, arrow_end_xy, veh_type):
        cv2.arrowedLine(image, start.tolist(), end.tolist(), color=COLORS[t], thickness=ARROW_THICKNESS, tipLength=0.3)

    if show_img:
        cv2.imshow("new", image)
        cv2.waitKey(0) 
    # resize accepts (width, height)
    cv2.imwrite("{}/annotated_{}.jpg".format(OUTPUTP_DIR, frame_num), img=cv2.resize(image, dsize=(image.shape[1]//2, image.shape[0]//2)))


if __name__ == "__main__":
    from glob import glob 
    all_images = glob("{}/Frames/*.jpg".format(DATA_DIR))
    for frame in all_images:
        frame_num = int(frame.split("/")[-1].rstrip(".jpg"))
        draw_frame(frame_num)
    