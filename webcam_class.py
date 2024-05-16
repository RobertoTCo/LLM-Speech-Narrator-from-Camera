import cv2
import time
import numpy as np
import os
from PIL import Image

# initialise a class called webcam_capture
class WebcamCapture():
    
    def __init__(self):
        pass 

    def assign_folder(self, folder_name):
        self.folder_name = folder_name
        self.frames_dir = os.path.join(os.getcwd(), self.folder_name)
        os.makedirs(self.frames_dir, exist_ok=True) # exist_ok already handles if path exists
    
    def start_webcam(self):
        self.webcamObj = cv2.VideoCapture(0)
        self.check_webcamObj_isOpened()
        print("--> Webcam has been started and is working")
        self.wait_for_adjustment(2)
    
    def check_webcamObj_isOpened(self):
        if not self.webcamObj.isOpened():
            raise IOError("Cannot open webcam")
    
    def wait_for_adjustment(self, seconds):
        time.sleep(seconds)

    def read_webcamObj(self):
        self.success, self.frame = self.webcamObj.read()
        if self.success:
            self.process_frame()
            self.saveframe()
        else:
            print("--> Error: Failed to capture image")

    def process_frame(self):
        self.max_frame_size = 250
        pil_img = self.convert_OpenCVimg_to_PIL()
        resized_pil_img = self.resize_PIL(pil_img)
        self.frame = self.convert_PIL_to_OpenCVimg(resized_pil_img)
            
    def convert_OpenCVimg_to_PIL(self):
        return Image.fromarray(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
    
    def resize_PIL(self, pil_img):
        ratio_to_resize = self.max_frame_size / max(pil_img.size)
        new_size = tuple([int(pixel*ratio_to_resize) for pixel in pil_img.size])
        resized_img = pil_img.resize(new_size, Image.LANCZOS)
        return resized_img

    def convert_PIL_to_OpenCVimg(self, pil_img):
        return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    
    def saveframe(self):
        print("📸 --> Say cheese! Saving frame.")
        path = f"{self.folder_name}/frame.jpg"
        cv2.imwrite(path, self.frame)
    
    def release_webcam_close_windows(self):
        print("\n --> Releasing webcam and closing all windows")
        self.webcamObj.release()
        cv2.destroyAllWindows()
