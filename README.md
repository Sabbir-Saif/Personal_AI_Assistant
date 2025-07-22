# Personal_AI_Assistant

This repository contains a Python-based personal AI assistant named "Siri," designed to perform various tasks such as web browsing, sending emails, taking screenshots, playing music, and more. The assistant uses voice commands and integrates multiple libraries for functionality.

## Overview

- **Name**: Siri (customizable activation word)
- **Purpose**: A voice-activated personal assistant for daily tasks.
- **Features**: Web automation, email sending, camera access, music playback, location tracking, and more.
- **Dependencies**: `tkinter`, `datetime`, `webbrowser`, `requests`, `speech_recognition`, `pyttsx3`, `wikipedia`, `wolframalpha`, `cv2`, `pywhatkit`, `pyautogui`, and others.
- **Language**: Python

## Features

- Voice command recognition and response using `speech_recognition` and `pyttsx3`.
- Web browsing with Chrome automation (open sites, new tabs, history).
- Email sending via SMTP.
- Camera and screenshot capture.
- Music playback from a local directory.
- Location tracking using IP geolocation.
- Alarm setting and system control (shutdown, restart, sleep).
- Integration with YouTube and other websites for dynamic content access.

## Prerequisites

- **Python 3.8+**
- **Required Libraries**:
  - `tkinter`
  - `datetime`
  - `webbrowser`
  - `requests`
  - `speech_recognition`
  - `pyttsx3`
  - `wikipedia`
  - `wolframalpha`
  - `opencv-python` (for `cv2`)
  - `pywhatkit`
  - `pyautogui`
  - `playsound` (for alarm)
