import cv2
import mediapipe as mp
import math

def detect_gesture(hand_landmarks):
    index_extended = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y
    middle_extended = hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y
    ring_extended = hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y
    pinky_extended = hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y

    thumb_tip = hand_landmarks.landmark[4]
    pinky_base = hand_landmarks.landmark[17]
    distance = math.sqrt((thumb_tip.x - pinky_base.x)**2 + (thumb_tip.y - pinky_base.y)**2)
    thumb_extended = distance > 0.22

    if index_extended and middle_extended and ring_extended and pinky_extended and thumb_extended:
        return "open palm"
    elif not index_extended and not middle_extended and not ring_extended and not pinky_extended and not thumb_extended:
        return "closed fist"
    elif index_extended and middle_extended and not ring_extended and not pinky_extended and not thumb_extended:
        return "peace sign"
    elif not index_extended and not middle_extended and not ring_extended and not pinky_extended and thumb_extended:
        return "thumbs up"
    elif not index_extended and not middle_extended and not ring_extended and pinky_extended and not thumb_extended:
        return "washroom please"
    else:
        return "unknown"

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

while True:
    success, frame = cap.read()
    if not success:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = detect_gesture(hand_landmarks)
            print(gesture)
            cv2.putText(frame,gesture,(15,55),cv2.FONT_HERSHEY_PLAIN,3,(158,100,170),3)

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

