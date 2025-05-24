import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('top50.csv')

print("Available columns:")
print(df.columns.tolist())

# 1. Python Basics
def mood_score(valence, danceability):
    """Calculate mood score based on valence and danceability."""
    return 0.6 * valence + 0.4 * danceability

# Basic statistics
total_tracks = len(df)

average_tempo = df['Beats.Per.Minute'].mean()

print(f"\nDataset Summary:")
print(f"Total number of tracks: {total_tracks}")
print(f"Average tempo (BPM): {average_tempo:.2f}")

# Energy
def classify_energy(energy):
    if energy >= 0.8:
        return "High Energy"
    elif energy >= 0.5:
        return "Moderate Energy"
    else:
        return "Low Energy"

df['Energy Class'] = df['Energy'].apply(classify_energy)

# 2. NumPy Operations
bpm_array = df['Beats.Per.Minute'].to_numpy()
first_10_bpm = bpm_array[:10]
high_bpm = bpm_array[bpm_array > 120]

bpm_stats = {
    'Average BPM': np.mean(bpm_array),
    'BPM Std Dev': np.std(bpm_array)
}

high_energy_indices = np.where(df['Energy'].to_numpy() > 0.7)[0]

# 3. Matplotlib
plt.rcParams['figure.figsize'] = [15, 12]  # Set figure size
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

# Energy by Genre
genre_energy = df.groupby('Genre')['Energy'].mean().sort_values(ascending=False)
ax1.plot(range(len(genre_energy)), genre_energy.values, marker='o')
ax1.set_title('Average Energy by Genre')
ax1.set_xlabel('Genre')
ax1.set_ylabel('Average Energy')
ax1.set_xticks(range(len(genre_energy)))
ax1.set_xticklabels(genre_energy.index, rotation=45, ha='right')

# Loudness 
genres = df['Genre'].unique()
loudness_data = [df[df['Genre'] == genre]['Loudness..dB..'] for genre in genres]
ax2.boxplot(loudness_data, tick_labels=genres)
ax2.set_title('Loudness Distribution by Genre')
ax2.set_xlabel('Genre')
ax2.set_ylabel('Loudness (dB)')
ax2.tick_params(axis='x', rotation=45)

# BPM 
ax3.hist(df['Beats.Per.Minute'], bins=20, edgecolor='black', color='skyblue')
ax3.set_title('Distribution of Beats Per Minute')
ax3.set_xlabel('BPM')
ax3.set_ylabel('Count')

# Valence vs Danceability
ax4.scatter(df['Valence.'], df['Danceability'], color='darkblue', alpha=0.5)
ax4.set_title('Valence vs Danceability')
ax4.set_xlabel('Valence')
ax4.set_ylabel('Danceability')

plt.tight_layout()

# 4. Pandas Series Operations
energy_series = pd.Series(df['Energy'].values, index=df['Track.Name'])
liveness_classification = df['Liveness'].apply(lambda x: 'Lively' if x > 0.6 else 'Not Lively')

# 5. Pandas DataFrame
# Filter high energy and danceability tracks
energetic_danceable = df[(df['Energy'] > 0.8) & (df['Danceability'] > 0.7)]

# Sort by BPM
df_sorted = df.sort_values('Beats.Per.Minute')

# Add mood score
df['Mood Score'] = df.apply(lambda row: mood_score(row['Valence.'], row['Danceability']), axis=1)

genre_stats = df.groupby('Genre').agg({
    'Energy': 'mean',
    'Danceability': 'mean'
}).round(3)

# Save processed data
df.to_csv('spotify_track_analysis.csv', index=False)

# Display
print("\nGenre Statistics:")
print(genre_stats)
print("\nBPM Statistics:")
print(bpm_stats)

plt.show()
