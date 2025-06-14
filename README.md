# 🖐️ Mouse Control Using Hand Gestures

Control your computer's mouse using just your **hand gestures** with the help of your webcam!  
Perform actions like **left click**, **right click**, **double click**, **scroll**, **adjust volume**, and **brightness** — all without touching your mouse.

---

## 🚀 Features

- 👉 Left Click, Right Click, and Double Click  
- 🔼🔽 Scroll Up / Scroll Down  
- 🔊 Volume Control  
- 💡 Screen Brightness Adjustment  
- 📷 Works in Real-Time via Webcam  
- 🧠 Built with Computer Vision & Gesture Recognition  

---

## 🧰 Requirements

Install the necessary dependencies with:

```bash
pip install flask cvzone opencv-python pyautogui comtypes pycaw screen_brightness_control

```

## 📸 How It Works

The system captures live video through your webcam, detects hand landmarks using **OpenCV** and **CVZone**, and maps finger positions to specific mouse or system control actions using **PyAutoGUI**, **Pycaw**, and **screen\_brightness\_control**.

---

## 📷 Screenshots / Demo

| Menu Interface                                                                        | Hand Detection                                                                        |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| ![1](https://github.com/user-attachments/assets/9d5b3630-c586-46e1-b39d-b6f3776abfe8) | ![1](https://github.com/user-attachments/assets/f147a599-fbbf-4d63-be4c-f16265ebe392) |

| Scroll Up                                                                             | Sroll Down                                                                            |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| ![2](https://github.com/user-attachments/assets/a1bd7150-1877-40ca-ab2f-d77dcc750a1c) | ![3](https://github.com/user-attachments/assets/326b3ac2-a053-4b59-92f4-01972ebe0b74) |

| Brightness Control                                                                    | Volume Control                                                                        |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| ![4](https://github.com/user-attachments/assets/ea13212e-0807-4e3e-93b0-d98c3a646716) | ![5](https://github.com/user-attachments/assets/99cc1a38-45bf-41d6-a548-2760ab204394) |

---

## 📂 Folder Structure (Suggested)

```
project-root/
│
├── main.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── hand_module.py
├── README.md
└── requirements.txt
```

---

## 📌 Future Improvements

* Add custom gesture training
* Introduce drag & drop support
* Multi-hand gesture detection
* GUI for configuration and sensitivity

---

## 🤝 Contributors

* **Your Name** — [GitHub](https://github.com/Tejas9523)
* Add more if team project...

---

## 💡 Inspiration

This project was built as part of a **Software Engineering PBL** (Project-Based Learning) to integrate **AI**, **Computer Vision**, and **Human-Computer Interaction** in a practical, engaging application.

---

