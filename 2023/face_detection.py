import cv2
import dlib
from imutils import *
import time


class Face_utilities():

    def __init__(self, face_width=200):
        self.detector = None
        self.predictor = None
        self.age_net = None
        self.gender_net = None
        self.path=str(input('shape_predictor: '))

    def face_detection(self, frame):

        if self.detector is None:
            self.detector = dlib.get_frontal_face_detector()

        if frame is None:
            return

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = self.detector(gray, 0)

        return rects

    def get_landmarks(self, frame, t0):
        if self.predictor is None:
            self.predictor = dlib.shape_predictor(self.path)
            print("Load_model-->!SUCCESS!")

        if frame is None:
            return None

        # face must be gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = self.face_detection(frame)

        if len(rects) <= 0:
            return None, None, None
        else:
            shape = self.predictor(gray, rects[0])
            shape = face_utils.shape_to_np(shape)
            time_face = time.perf_counter() - t0
            return rects, shape, time_face

    def no_age_gender_face_process(self, frame, start_time):
        t0 = start_time
        rects, shape, time_face = self.get_landmarks(frame, t0)

        if shape is None:
            return shape, rects, time_face
        else:
            (x, y, w, h) = face_utils.rect_to_bb(rects[0])
            # face = frame[y:y+h,x:x+w]
        return rects, shape, time_face







