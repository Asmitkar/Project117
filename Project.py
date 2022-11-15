import os
import cv2


path = r"Friends\Images"

friends = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        friends.append(file_name)
        
print(len(friends))
count = len(friends)

frame = cv2.imread(friends[0])
height,width,channels= frame.shape
print(height,width,channels)

output = cv2.VideoWriter('FriendVideo.mp4',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))


for x in range(0,count-1,1):
    frame = cv2.imread(friends[x])
    output.write(frame)


output.release()
print('Video Created')