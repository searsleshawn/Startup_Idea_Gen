# 🚀 Startup Idea Generator

This is an interactive Streamlit app to generate startup ideas based on industry and audience filters — or get a random idea with the "Inspire Me" button.

## 📖 Libraries used
```python
import streamlit as st
import pandas as pd
```
These libraries were used in a custom conda environement that uses python 3.9

## ▶️ How to Run
1. Clone the repo
    ```bash
    git clone https://github.com/searsleshawn/Startup_Idea_Gen.git
    
2. Environment
   - You should be able to run this anywhere that you can use `streamlit` and `pandas`.
   - If you are unsure where, download and create a conda python environment and `pip install` the `streamlit` and `pandas` libraries
     to your new environment.
     
3. Launch the app
   ```bash
   streamlit run main.py
**This will open your browser and run it locally

## 🎬 App Demo

![Startup Idea Generator Demo](GIF/startup_idea_generator.gif)

## 📁 Project Structure
```kotlin
├── app.py
├── requirements.txt
├── README.md
└── data/
    └── startup_idea_generator.csv
