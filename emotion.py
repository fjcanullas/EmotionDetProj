from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import cv2
import os
import sys
from deepface import DeepFace

def initialize_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    return cap


def detect_faces(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces


def analyze_face(face, action):
    results = DeepFace.analyze(face, actions=[action], enforce_detection=False)
    return results[0][action]


def draw_emotions(frame, faces, action):
    font = cv2.FONT_HERSHEY_SIMPLEX
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        face = frame[y:y + h, x:x + w]
        results = analyze_face(face, action)
        print(type(results), results)
        if isinstance(results, int):
            result_str = str(results)
            cv2.putText(frame, result_str, (x, y + h + 20), font, 1, (0, 0, 255), 2, cv2.LINE_4)
        else:
            dominant_result = max(results, key=results.get)
            cv2.putText(frame, dominant_result, (x, y + h + 20), font, 1, (0, 0, 255), 2, cv2.LINE_4)
    return frame


class EmotionApp(App):
    def build(self):

        # Check if we're running as a PyInstaller bundle
        if getattr(sys, 'frozen', False):
            # We're running in a PyInstaller bundle
            base_path = sys._MEIPASS
        else:
            # We're running in a normal Python environment
            base_path = os.path.dirname(os.path.abspath(__file__))

        cascade_path = os.path.join(base_path, 'haarcascade_frontalface_default.xml')
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        self.cap = initialize_webcam()
        self.action = 'emotion'  # default action

        layout = BoxLayout(orientation='vertical')

        emotion_button = Button(text="Emotion")
        emotion_button.bind(on_press=self.set_emotion)
        layout.add_widget(emotion_button)

        age_button = Button(text="Age")
        age_button.bind(on_press=self.set_age)
        layout.add_widget(age_button)

        gender_button = Button(text="Gender")
        gender_button.bind(on_press=self.set_gender)
        layout.add_widget(gender_button)

        race_button = Button(text="Race")
        race_button.bind(on_press=self.set_race)
        layout.add_widget(race_button)

        Clock.schedule_interval(self.update, 1.0/33.0)

        return layout

    def set_emotion(self, instance):
        self.action = 'emotion'

    def set_age(self, instance):
        self.action = 'age'

    def set_gender(self, instance):
        self.action = 'gender'

    def set_race(self, instance):
        self.action = 'race'

    def update(self, dt):
        ret, frame = self.cap.read()
        faces = detect_faces(frame, self.face_cascade)
        frame = draw_emotions(frame, faces, self.action)
        cv2.imshow('My Emotion Detection Project', frame)
        key = cv2.waitKey(2) & 0xFF
        if key == ord('q'):
            self.cap.release()
            cv2.destroyAllWindows()
            App.get_running_app().stop()


if __name__ == "__main__":
    EmotionApp().run()
