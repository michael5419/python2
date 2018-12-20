# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2 as cv
# 哈爾級聯人臉定位器
fd = cv.CascadeClassifier('./data/haar/face.xml')
ed = cv.CascadeClassifier('./data/haar/eye.xml')
nd = cv.CascadeClassifier('./data/haar/nose.xml')
vc = cv.VideoCapture(0)
while True:
    frame = vc.read()[1]
    faces = fd.detectMultiScale(frame, 1.3, 5)
    for l, t, w, h in faces:
        a, b = int(w / 2), int(h / 2)
        # cv.ellipse(圖像,橢圓心,半徑,旋轉角,起始角,終止角,顏色,線寬,)
        cv.ellipse(frame, (l + a, t + b), (a, b),
                   0, 0, 360, (255, 0, 255), 2)
        face = frame[t:t + h, l:l + w]
        eyes = ed.detectMultiScale(face, 1.3, 5)
        for l, t, w, h in eyes:
            a, b = int(w / 2), int(h / 2)
            cv.ellipse(face, (l + a, t + b),
                       (a, b), 0, 0, 360,
                       (0, 255, 0), 2)
        noses = nd.detectMultiScale(face, 1.3, 5)
        for l, t, w, h in noses:
            a, b = int(w / 2), int(h / 2)
            cv.ellipse(face, (l + a, t + b),
                       (a, b), 0, 0, 360,
                       (0, 255, 255), 2)
    cv.imshow('VideoCapture', frame)
    if cv.waitKey(33) == 27:
        break
vc.release()
cv.destroyAllWindows()
