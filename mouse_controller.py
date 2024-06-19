import cv2
import mediapipe as mp
import pyautogui as pya

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

capture_hands = mp_hands.Hands()

# Get screen parameters
screen_width, screen_height = pya.size()

# Capture the video using webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror the capture
    rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output_hands = capture_hands.process(rgb_img)
    all_hands = output_hands.multi_hand_landmarks

    if all_hands:
        for hand in all_hands:
            mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
            for id, lm in enumerate(hand.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)

                # Get the tumb tip and index tip 
                if id == 8:
                    # Getting x,y for Tumb tip as cx1 & cy1
                    cx1 = cx
                    cy1 = cy

                    cv2.circle(frame,(cx,cy),10,(255,0,0),2)
                    
                if id == 12:
                    # Getting x,y for middle tip as cx2 & cy2
                    cx2 = cx
                    cy2 = cy
                    cv2.circle(frame,(cx,cy),10,(255,0,0),2)
                    mouse_x = int(screen_width/w * cx)
                    mouse_y = int(screen_height/h * cy)
                    # Move mouse
                    pya.moveTo(mouse_x, mouse_y)

                if id == 7:
                    # Getting x,y for Idenx 2 as cx3 & cy3
                    cx3 = cx
                    cy3 = cy
                    cv2.circle(frame,(cx,cy),10,(255,0,0),2)

                if id == 4:
                    # Getting x,y for Idenx 2 as cx3 & cy3
                    cx4 = cx
                    cy4 = cy
                    cv2.circle(frame,(cx,cy),10,(255,0,0),2)
                
                if id == 6:
                    # Getting x,y for Idenx 2 as cx3 & cy3
                    cx5 = cx
                    cy5 = cy
                    cv2.circle(frame,(cx,cy),10,(255,0,0),2)
                   

        # Mouse Click
        click_val = cy3-cy1
        print(click_val)
        if (click_val<15):
            pya.click()

        # Mouse Right Click
        right_click = cy4-cy5
        print(right_click)
        if (right_click<10):
            pya.rightClick()
        

    cv2.imshow("Hand Movements", frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
