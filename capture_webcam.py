from webcam_class import WebcamCapture

webcam = WebcamCapture()

folder_name="frames"
webcam.assign_folder(folder_name)

webcam.start_webcam()

frames_count = 0

while frames_count < 50:
    webcam.read_webcamObj()
    webcam.wait_for_adjustment(8)
    frames_count += 1

webcam.release_webcam_close_windows()
