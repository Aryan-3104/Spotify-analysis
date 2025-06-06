
![Project Banner](https://via.placeholder.com/1000x300.png?text=Spotify+Track+Data+Analysis)

# 🎵 Spotify Track Data Analysis

This project is a Python-based data analysis tool that explores patterns and insights from Spotify's Top 50 tracks dataset. It involves cleaning the dataset, analyzing features like energy and tempo, classifying tracks, and visualizing data for a better understanding of music trends.

## 📌 Features

- Cleans and processes Spotify track data using **Pandas** and **NumPy**
- Calculates key metrics such as:
  - Average tempo of all tracks
  - Classification of songs based on energy (High, Medium, Low)
  - Mood score based on valence and danceability
- Visualizes data trends using **Matplotlib**
- Identifies most and least popular tracks based on available metrics

## 📊 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

## 📁 Files Included

- `main.py` – Main Python script for data processing and visualization
- `top50.csv` – Dataset containing information on Spotify's Top 50 tracks
- `README.md` – Project overview and documentation

## 📂 Dataset Overview

The dataset contains the following columns:
- `Track.Name`, `Artist.Name`
- `Genre`, `Beats.Per.Minute (BPM)`, `Energy`, `Danceability`
- `Loudness`, `Liveness`, `Valence`, `Duration`, `Acousticness`
- `Speechiness`, `Popularity`

## 🚀 How to Run

1. Make sure Python 3.x is installed on your system.
2. Install required packages:
   ```bash
   pip install pandas numpy matplotlib
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## 🎯 Learning Outcomes

This project demonstrates:
- Data preprocessing and cleaning
- Exploratory data analysis (EDA)
- Data classification using custom logic
- Visualization of insights using plots

## 📬 Contact

For questions or suggestions, feel free to reach out!

---

*This project was developed as part of an academic assignment to practice data analysis using real-world music datasets.*
