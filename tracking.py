import cv2
import sys

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

if __name__ == '__main__':
    i = 1
    while (i <= 61):
        # Set up tracker.
        # Instead of MIL, you can also use

        tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
        tracker_type = tracker_types[1]

        if int(minor_ver) < 3:
            tracker = cv2.Tracker_create(tracker_type)
        else:
            if tracker_type == 'BOOSTING':
                tracker = cv2.TrackerBoosting_create()
            if tracker_type == 'MIL':
                tracker = cv2.TrackerMIL_create()
            if tracker_type == 'KCF':
                tracker = cv2.TrackerKCF_create()
            if tracker_type == 'TLD':
                tracker = cv2.TrackerTLD_create()
            if tracker_type == 'MEDIANFLOW':
                tracker = cv2.TrackerMedianFlow_create()
            if tracker_type == 'GOTURN':
                tracker = cv2.TrackerGOTURN_create()

        # Read video
        if (i < 10):
            vidName = "00000_Sub_0" + str(i) + ".mp4"
        else:
            vidName = "00000_Sub_" + str(i) + ".mp4"
        video = cv2.VideoCapture(vidName)

        # Exit if video not opened.
        if not video.isOpened():
            print
            "Could not open video"
            sys.exit()

        # Read first frame.
        ok, frame = video.read()
        if not ok:
            print
            'Cannot read video file'
            sys.exit()

        # Define an initial bounding box
        bbox = (287, 23, 86, 320)

        # Uncomment the line below to select a different bounding box
        bbox = cv2.selectROI(frame, False)

        # Initialize tracker with first frame and bounding box
        ok = tracker.init(frame, bbox)

        # # Initializing position of origin
        # # print(bbox[0],bbox[1],bbox[2],bbox[3])
        # x0 = bbox[0] + bbox[2] / 2
        # y0 = bbox[1] + bbox[3] / 2

        # Creating text file to be written in
        if (i < 10):
            filename = "00000_Sub_0" + str(i) + "_data.txt"
        else:
            filename = "00000_Sub_" + str(i) + "_data.txt"

        file = open(filename, "w")

        file.write("x" + "\t" + "y" + "\t" + "Frame" + "\t" + "Time-Stamp" + "\n") #"x co-ordinate" + "\t" + "y co-ordinate" + "\t" + "Frame Nos." + "\t" + "Time-Stamp" + "\n"

        while True:
            # Read a new frame
            ok, frame = video.read()
            if not ok:
                break

            # Start timer
            timer = cv2.getTickCount()

            # Update tracker
            ok, bbox = tracker.update(frame)

            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

            # Initializing Co-ordinate variables
            coordinate = ()
            x = 0
            y = 0

            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))

                # Noting Co-ordinates
                coordinate = (((p1[0] + p2[0]) / 2), ((p1[1] + p2[1]) / 2))
                x = coordinate[0]
                y = coordinate[1]

                cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

                # Printing co-ordinate in console


                x/=8.05 # As 11.85 pixels = 1cm

                y/=8.05 # As 11.85 pixels = 1cm
                print(x)
                print(y)

                # Printing Frame Number
                frameNo = video.get(1)
                print(frameNo)

                # Printing Time Stamp
                timeStamp = video.get(0)
                print(timeStamp)

                # Storing the data in the text file
                # Co-ordinates are being stored in cms. rounded down to 2 decimal places
                file.write(str(round(x, 2)) + " " + str(round(y, 2)) + " " + str(frameNo) + " " + str(timeStamp) + "\n")





            else:
                # Tracking failure
                cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255),
                            2)

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

            # Exit if ESC pressed
            k = cv2.waitKey(1) & 0xff
            if k == 27: break

        file.close()
        i += 1
