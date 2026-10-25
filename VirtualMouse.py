import cv2
import numpy as np
import elMouse as htm 
import pyautogui
import math

pyautogui.PAUSE = 0 
wCam, hCam = 640, 480
wScr, hScr = pyautogui.size()
frameR = 150 
smoothening = 3 

plocX, plocY = 0, 0
clocX, clocY = 0, 0

sol_basili_mi = False
sag_basili_mi = False
onceki_y_scroll = 0 

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.HandDetector(max_hands=1)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1) 
    
    img = detector.find_hands(img)
    lmList = detector.find_position(img, draw=False)

    if len(lmList) != 0:
        x_isaret, y_isaret = lmList[8][1], lmList[8][2]   
        x_bas, y_bas = lmList[4][1], lmList[4][2]         
        x_orta, y_orta = lmList[12][1], lmList[12][2]
        x_yuzuk, y_yuzuk = lmList[16][1], lmList[16][2] 
        x_avuc, y_avuc = lmList[9][1], lmList[9][2] 

        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        # --- 1. ÖNCE MESAFELERİ HESAPLA ---
        mesafe_sol = math.hypot(x_bas - x_isaret, y_bas - y_isaret)
        mesafe_sag = math.hypot(x_bas - x_orta, y_bas - y_orta)
        mesafe_isaret_orta = math.hypot(x_isaret - x_orta, y_isaret - y_orta)
        mesafe_orta_yuzuk = math.hypot(x_orta - x_yuzuk, y_orta - y_yuzuk)

        # Kaydırma (Scroll) modunda olup olmadığımızı belirle
        kaydirma_modu = (mesafe_isaret_orta < 25 and mesafe_orta_yuzuk < 25)

        # --- 2. HAREKET VE KAYDIRMA KONTROLÜ ---
        if kaydirma_modu:
            # KAYDIRMA MODU AKTİF (İmleç sabit kalır)
            cv2.circle(img, (x_orta, y_orta), 20, (0, 255, 255), cv2.FILLED) 
            
            if onceki_y_scroll != 0:
                y_fark = y_orta - onceki_y_scroll
                if y_fark > 5: 
                    pyautogui.scroll(-60) 
                elif y_fark < -5: 
                    pyautogui.scroll(60) 
            onceki_y_scroll = y_orta
            
        else:
            # NORMAL MOD (İmleç hareket eder ve kaydırma sıfırlanır)
            onceki_y_scroll = 0
            
            # Koordinatları oranla ve yumuşat
            x3 = np.interp(x_avuc, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y_avuc, (frameR, hCam - frameR), (0, hScr))

            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            pyautogui.moveTo(clocX, clocY)
            cv2.circle(img, (x_avuc, y_avuc), 15, (255, 0, 0), cv2.FILLED)
            plocX, plocY = clocX, clocY

            # --- 3. TIKLAMA KONTROLLERİ ---
            # Sadece kaydırma yapmıyorsak tıklamaya izin ver
            
            # Sol Tık
            if mesafe_sol < 20:
                cv2.circle(img, (x_isaret, y_isaret), 15, (0, 255, 0), cv2.FILLED) 
                if not sol_basili_mi: 
                    pyautogui.mouseDown(button='left')
                    sol_basili_mi = True
            else:
                if sol_basili_mi: 
                    pyautogui.mouseUp(button='left')
                    sol_basili_mi = False

            # Sağ Tık
            if mesafe_sag < 20:
                cv2.circle(img, (x_orta, y_orta), 15, (0, 0, 255), cv2.FILLED) 
                if not sag_basili_mi:
                    pyautogui.mouseDown(button='right')
                    sag_basili_mi = True
            else:
                if sag_basili_mi:
                    pyautogui.mouseUp(button='right')
                    sag_basili_mi = False

    cv2.imshow("Sanal Fare", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break