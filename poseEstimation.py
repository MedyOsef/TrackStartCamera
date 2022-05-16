import cv2
import mediapipe as mp
from time import asctime
from threading import Thread


def pose_estimation():
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

        while cap.isOpened():
            ret, frame = cap.read()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')

            results = pose.process(image)
            if not results.pose_landmarks:  # https://mlhieve.com/2021/11/person-pose-landmarks-detection-using-mediapipe
                print("no result")
            else:
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                # out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
                out = cv2.VideoWriter("videos/" + "-".join(("-".join(asctime().split()) + ".mp4").split(":")), fourcc, 30.0, (640, 480))

            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


pose_estimation()
