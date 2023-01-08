import numpy as np
import os
import cv2
import pandas as pd
import json


vid = cv2.VideoCapture('your_video.mp4')

def get_vid_properties(): 
    width = int(vid.get(3))  # float
    height = int(vid.get(4)) # float
    vid.release()
    return width,height
  
print('Video Properties: ',get_vid_properties())


column_names = ['x', 'y', 'acc']


path_to_json = "output"


json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
print('Found: ',len(json_files),'json keypoint frame files')
count = 0

width,height = get_vid_properties()


body_keypoints_df = pd.DataFrame()
left_knee_df = pd.DataFrame()

print('json files: ',json_files[0])   


for file in json_files:

    temp_df = json.load(open(path_to_json+file))
    temp = []
    for k,v in temp_df['part_candidates'][0].items():
        
       
        if len(v) < 4:
            temp.append(v)
            
            
      
        elif len(v) > 4: 
            near_middle = width
            np_v = np.array(v)
            
            
            np_v_reshape = np_v.reshape(int(len(np_v)/3),3)
            np_v_temp = []
            
            for pt in np_v_reshape:
                if(np.absolute(pt[0]-width/2)<near_middle):
                    near_middle = np.absolute(pt[0]-width/2)
                    np_v_temp = list(pt)
         
            temp.append(np_v_temp)
            
        else:
            
            temp.append([0,0,0])
            
    temp_df = pd.DataFrame(temp)
    temp_df = temp_df.fillna(0)
    

    try:
        prev_temp_df = temp_df
        body_keypoints_df= body_keypoints_df.append(temp_df)
        left_knee_df = left_knee_df.append(temp_df.iloc[13].astype(int))

    except:
        print('errorr', file)
        
body_keypoints_df.columns = column_names
left_knee_df.columns = column_names

body_keypoints_df.reset_index()
left_knee_df = left_knee_df.reset_index(drop = True)

##adjacent keypoint angles

angle = atan2(keypoint2_y - keypoint1_y, keypoint2_x - keypoint1_x) * 180 / pi

## Mahalanobis distance shit
prev_keypoints = []

movements = []

while True:
   
    success, frame = video.read()
    if not success:
        break

    
    greyed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    keypoints, output = opWrapper.emplaceAndPop([greyed])
    keypoints = keypoints[0]

if not prev_keypoints:
        prev_keypoints = keypoints


    
distance = 0
for i in range(len(keypoints)):
        distance += np.sqrt(np.sum((keypoints[i] - prev_keypoints[i])**2))

   
movements.append(distance)

    
prev_keypoints = keypoints


avg_movement = sum(movements) / len(movements)


movement_per_sec = avg_movement * fps


