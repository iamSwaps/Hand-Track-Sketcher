import cv2
import mediapipe as mp
 
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)



def gethan(camwidth, camheight, camera):
        success,frame = camera.read()
        if not success:
            print("Alert ! Camera disconnected")
            exit()
        else:

            frame=cv2.flip(frame, 1)
            #cv2.imshow('image',frame)
            results = hands.process(frame)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks( frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                ind=hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                pixel=mp_drawing._normalized_to_pixel_coordinates(ind.x, ind.y, camwidth, camheight)
                return pixel
            else:
                return (0, 0)
            
    
