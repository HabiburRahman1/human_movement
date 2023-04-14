# import cv2

# cap = cv2.VideoCapture('dance.mp4')
# from cvzone.PoseModule import PoseDetector
# detector = PoseDetector()
# counter = 0
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

#     img = detector.findPose(frame)
#     lmList, box_info = detector.findPosition(img, draw=False) 
#     print(lmList)
#     print("habib")
#     # move image boxes in different place 
#     counter += 1
#     if counter == 30:
#         break
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# import cv2
# from cvzone.PoseModule import PoseDetector

# cap = cv2.VideoCapture('dance.mp4')
# detector = PoseDetector()
# counter = 0

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

#     img = detector.findPose(frame)
#     lmList, box_info = detector.findPosition(img, draw=False)
#     if lmList:
#         # move all the landmark coordinates to the right by 100 pixels
#         lmList = [[lm[0], lm[1]+100, lm[2]] for lm in lmList]

#         # draw the landmarks and skeleton
#         detector.findPosition(img, draw=True, lmList=lmList)

#     # move image boxes in different place
#     counter += 1
#     if counter == 30:
#         break

#     cv2.imshow('frame', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# import cv2
# from cvzone.PoseModule import PoseDetector

# cap = cv2.VideoCapture('dance.mp4')
# detector = PoseDetector()
# counter = 0

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

#     img = detector.findPose(frame)
#     lmList, box_info = detector.findPosition(img, draw=False)
#     # get connections between the landmarks
#     print(detector.getConnections())
#     print(box_info)
#     if lmList:
#         # draw the skeleton using the landmark points
#         connections = [[0, 1], [1, 2], [2, 3], [3, 4], [1, 5], [5, 6], [6, 7], [1, 8], [8, 9], [9, 10], [10, 11], [8, 12], [12, 13], [13, 14], [0, 15], [15, 17], [0, 16], [16, 18], [14, 19], [19, 20], [14, 21], [11, 22], [22, 23], [11, 24], [0, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32]]
#         # connections = [[0, 1], [1, 2], [2, 3], [3, 4], [1, 5], [5, 6], [6, 7], [1, 8], [8, 9], [9, 10], [10, 11], [8, 12], [12, 13], [13, 14], [0, 15], [15, 17], [0, 16], [16, 18]]
#         for connection in connections:
#             start_point = (int(lmList[connection[0]][1]), int(lmList[connection[0]][2]))
#             end_point = (int(lmList[connection[1]][1]), int(lmList[connection[1]][2]))
#             cv2.line(img, start_point, end_point, (0, 255, 0), 3)

#     # move image boxes in different place
#     # counter += 1
#     # if counter == 30:
#     #     break

#     cv2.imshow('frame', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


from cvzone.PoseModule import PoseDetector
import cv2

cap = cv2.VideoCapture('dance.mp4')
detector = PoseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
    # if bboxInfo:
    #     center = bboxInfo["center"]
    #     cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()