import cv2
from time import asctime, time  # asctime renvoie la date et l'heure avec se format (Sun Jun 20 23:21:05 1993)


def video_capture():
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    pTime = 0
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    out = cv2.VideoWriter("videos/" + "-".join(("-".join(asctime().split()) + ".mp4").split(":")), fourcc, 30.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # write the flipped frame
            out.write(frame)
            cTime = time()  # Current millisecond (epoch linux)
            fps = 1 / (cTime - pTime)

            pTime = cTime  # updates the previous second each time an image is displayed
            cv2.putText(frame, f'FPS: {int(fps)}', (0, 40), cv2.FONT_HERSHEY_PLAIN, 2, (94, 252, 141), 3)  # affiche les FPS
            cv2.putText(frame, f'{str(asctime())}', (0, 475), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 1)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


video_capture()
