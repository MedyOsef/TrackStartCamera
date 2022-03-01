import cv2
from time import asctime  # asctime renvoie la date et l'heure avec se format (Sun Jun 20 23:21:05 1993)


def videoCapture():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    out = cv2.VideoWriter("videos/" + "-".join(("-".join(asctime().split()) + ".mp4").split(":")), fourcc, 30.0,
                          (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # write the flipped frame
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
