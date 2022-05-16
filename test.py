from json import loads

# from time import asctime, sleep
# from time import asctime
# i = 0
# var = "-".join(("-".join(asctime().split())+".mp4").split(":"))
# print(var)

"""cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Initialisation de la webcam
vid_cod = cv2.VideoWriter_fourcc(*'mp4v')
var = "-".join(asctime().split())+".mp4"
dill = var
output = cv2.VideoWriter(dill, vid_cod, 20.0, (640, 480))
# la boucle de capture
while True:
    # capture chaque image de la video de la webcam
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    output.write(frame)

    if cv2.waitKey(1) == ord('q'):
        break

output.release()  # fermer le fichier de sorti
cap.release()  # fermer la capture
cv2.destroyAllWindows()"""

eleves = '{"MEDY": 19, "Willi": 18, "Ange": "18"}'


dictionaire = loads(eleves)
print(dictionaire)
