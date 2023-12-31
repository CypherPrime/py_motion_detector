import cv2
import tkinter as tk
import winsound

def motion_detector():
    vid = cv2.VideoCapture(0);#file path can be added to load video from local disk

    ret, frame1 = vid.read()
    ret, frame2 = vid.read()

    while vid.isOpened():
       diff = cv2.absdiff(frame1, frame2)
       gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
       blur = cv2.GaussianBlur(gray, (5,5), 0)
       _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
       dilated = cv2.dilate(thresh, None, iterations=3)
       contours, _ = cv2.findContours(dilated,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

       for contour in contours:
           (x, y, w, h) = cv2.boundingRect(contour)
           if cv2.contourArea(contour) < 700:
               continue
           cv2.rectangle(frame1,(x,y), (x+w, y+h), (0,255, 0), 2)
           cv2.putText(frame1, "MOTION: {}".format('detects movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,25),3)
           winsound.Beep(1000, 100)  # Beep at 1000 Hz for 100 ms
       cv2.imshow("TAMANJI'S MOTION DETECTOR", frame1)
       frame1 = frame2
       ret, frame2 = vid.read()
       if cv2.waitKey(40) == 27:
           break

    vid.release()
    cv2.destroyAllWindows()
#making a graphical look
def out():
    win.destroy()
    exit()
win = tk.Tk()
win.title("Motion Detector by CYPHER PRIME")
win.geometry("400x400")
l1 = tk.Label(win,text="This program is a motion detector that uses video input.",font=("Times New Roman",12,"bold"),bd=10, fg="blue",bg="darkcyan")
l1.grid(column=0,row=0)
l2 = tk.Label(win,text="Ensure there is a camera connected to your system ",font=("Times New Roman",12,"bold"),bd=10, fg="blue",bg="darkcyan")
l2.grid(column=0,row=1)
l3 = tk.Label(win,text="Click start to begin when you are ready",font=("Times New Roman",12,"bold"),bd=10, fg="blue",bg="darkcyan")
l3.grid(column=0,row=2)
start = tk.Button(win,text=":::START:::",fg="Steel Blue",font=("Times New Roman",12,"bold"),bd=10,command=motion_detector)
start.grid(column=0,row=3,padx=20,pady=20)
l4 = tk.Label(win,text="Press ESC key to exit Camera mode when started",font=("Times New Roman",12,"bold"),bd=10, fg="red",bg="darkcyan")
l4.grid(column=0,row=4)
ex = tk.Button(win,text="::EXIT::",fg="Steel Blue",font=("Times New Roman",12,"bold"),bd=10,command=out)
ex.grid(column=0,row=5,padx=20,pady=20)
me = tk.Label(win,text="TEC_L=labs: TAMANJI COURAGE",font=("Times New Roman",10,"bold"),bd=10, fg="black",bg="cyan")
me.grid(column=0,row=6)

win.configure(background='darkcyan')
win.mainloop()