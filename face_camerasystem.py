import cv2
from datetime import datetime
import os

class FaceDetect:
    def __init__(self, cascade_path):
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return self.face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=6, flags=0, minSize=(50, 50))

class FaceRecognition:
    def __init__(self, model_path):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read(model_path)

    def recognize_faces(self, frame, faces):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        results = []
        for (x, y, w, h) in faces:
            face = gray[y:y + h, x:x + w]
            label, confidence = self.recognizer.predict(face)
            results.append({
                "coordinates": (x, y, w, h),
                "label": label if confidence < 60 else "Unknown",
                "confidence": confidence
            })
        return results

class FFmpegRecorder:
    def __init__(self, webcam_name="Logi C270 HD WebCam"):
        import subprocess
        self.subprocess = subprocess
        self.webcam_name = webcam_name

    def record_video_with_audio(self, output_file_path, duration):
        command = [
            "ffmpeg",
            "-y",
            "-f", "dshow",
            "-i", f"video={self.webcam_name}:audio=Mikrofon ({self.webcam_name})",
            "-t", str(duration),
            "-c:v", "libx264",
            "-preset", "veryfast",
            "-c:a", "aac",
            "-b:a", "128k",
            output_file_path
        ]
        
        self.subprocess.run(command, check=True)

def run():
    cascade_path = "haarcascade_frontalface_default.xml"
    model_path = "akmodel.yml"
    recording_duration = 30
    output_dir = "database/output"

    os.makedirs(output_dir, exist_ok=True)

    face_detector = FaceDetect(cascade_path)
    face_recognizer = FaceRecognition(model_path)
    recorder = FFmpegRecorder()
    camera = cv2.VideoCapture(0)

    unknown_frame_count = 0  
    unknown_threshold = 20

    print("Tryk på 'q' for at afslutte programmet.")

    while True:
        frame = camera.read()

        faces = face_detector.detect_faces(frame)
        if len(faces) > 0:
            results = face_recognizer.recognize_faces(frame, faces)

            for result in results:
                label = str(result["label"])
                confidence = result["confidence"]
                print(f"Label: {label}, Confidence: {confidence:.2f}%")

                if label == "Unknown":
                    unknown_frame_count += 1
                    print(f"Ukendt ansigt detekteret i {unknown_frame_count}/{unknown_threshold} frames.")
                else:
                    unknown_frame_count = 0

            if unknown_frame_count >= unknown_threshold:
                print("Starter optagelse på grund af vedvarende ukendt ansigt.")
                output_file = os.path.join(output_dir, f"recording_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.mp4")
                camera.release()
                recorder.record_video_with_audio(output_file, recording_duration)
                camera = cv2.VideoCapture(0)
                unknown_frame_count = 0

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
    print("Program afsluttet.")

if __name__ == "__main__":
    run()