# Beetle Navigation Tracking

This repository is for the Project "Optimal Intermittent Navigation" at [Dr. Orit Peleg's laboratory](https://www.peleglab.com/optimal-intermittent-navigation).

<img src="https://static.wixstatic.com/media/cb8b73_b15dafc59b90493593cfdb770924436c~mv2.png/v1/crop/x_234,y_0,w_525,h_523/fill/w_550,h_550,al_c,lg_1/cb8b73_b15dafc59b90493593cfdb770924436c~mv2.png" alt="The Beetle!" height="200px">

This readme explains how to use each file in the repository.



## tracking.py

This program has been written to track the beetle in the videos recorded during live experiments. We use the [OpenCV](https://opencv.org/) library for tracking. This program provisions the use of multiple trackers. However, from results obtained after several trials, the 'MIL' tracker has been adopted for this project.

```python
tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
        tracker_type = tracker_types[1]
```

The **index 1** selects the MIL tracker.

---

The entire code is packed into a while loop.

```python
 i = 1
    while (i <= 61):
    .
    .
    .
```

The **i=1** designates the index of the first video and **i<=61** designates the index of the last video in the set being processed. These values can be tweaked depending on the set of videos being processed.

---

```python
# Read video
        if (i < 10):
            vidName = "00000_Sub_0" + str(i) + ".mp4"
        else:
            vidName = "00000_Sub_" + str(i) + ".mp4"
        video = cv2.VideoCapture(vidName)
```

The "**vidName**" variable caters to the various naming schemes of experimental subsets. In this particular case as the videos were batch exported from subsequences of video 00000.mp4 in Adobe Premiere Pro the prefix is "00000_Sub_0". This can easily be tweaked. The **i** as shown here takes care of the incremental name change depending on the batch size.

---

```python
if (i < 10):
            filename = "00000_Sub_0" + str(i) + "_data.txt"
        else:
            filename = "00000_Sub_" + str(i) + "_data.txt"

        file = open(filename, "w")
```

The file name for the text files containing the data is similarly labeled as the video files.

---

The central section of the code handles the tracking, this is properly documented with comments. You will have to press **Enter** after selecting the tracking are on the video for tracking to begin. While tracking is on, you can press **ESC** at any point to terminate the program.

---

```python
# Display tracker type on frame
            cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

            # Display FPS on frame
            cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

            # Displaying video number
            cv2.putText(frame, " Video : " + str(i), (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

            # Display Co-ordinates on frame
            cv2.putText(frame, "Co-ordinates : " + str(x) + " , " + str(y), (100, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);



            # Display result
            cv2.imshow("Tracking", frame)
```

This section handles what is displayed when the tracking is on. We have decided to make the **Tracker Type**, **FPS**, **Video Number** and **Co-ordinates** visible on-screen.

---





## recordObstacle.py

We record all the obstacles on the arena with this program.

```python
for image_path in glob.glob("Arena Snap.png"):
    img = misc.imread(image_path)
    print (img.shape)
    print (img.dtype)
```

The picture of the Arena is provided as a png file as shown in the code fragment above. The picture provided here is, **Arena Snap.png**. By double clicking on each obstacle a red circle demarcates that the obstacle has been marked. Now pressing **a** ensures that obstacle has been recorded and we can move on to click on another obstacle.

```python
def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),10,(0,0,255),-1)
        ix,iy = x,y
```

We can change how the selected circles look by modifying the draw_circle method. Moreover, the reason we have adopted a **select one, commit one** approach, is to ensure that if an obstacle is selected by mistake it can be erased before it is committed to memory. This makes the task easier but a little laborious.

---

