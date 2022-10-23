import cv2
import sys

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    tracker = cv2.TrackerKCF_create()
    ok, frame = cap.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
    bbox = cv2.selectROI(frame, False)
    ok = tracker.init(frame, bbox)

    while True:
        timer = cv2.getTickCount()
        ok, frame = cap.read()
        # Update tracker
        ok, bbox = tracker.update(frame)

        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        else:
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # Display FPS on frame
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
        cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

        # Display result
        cv2.imshow("Tracking", frame)

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff

        if k == 27:
            break

    cap.release()