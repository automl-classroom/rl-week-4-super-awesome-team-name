# vibe coded :')
import os
import re

import matplotlib.pyplot as plt

# Set the directory containing the log files
log_dir = "txt_logs"  # Replace with your directory path

# Regular expression to match the data
pattern = re.compile(r"Frame (\d+), AvgReward\(10\): ([\d.]+)")

# Create output directory for plots
output_dir = os.path.join(log_dir, "plots")
os.makedirs(output_dir, exist_ok=True)

# Process each .txt file in the directory
for filename in os.listdir(log_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(log_dir, filename)
        base_name = os.path.splitext(filename)[0]  # Remove .txt

        frames = []
        avg_rewards = []

        with open(file_path, "r") as file:
            for line in file:
                match = pattern.search(line)
                if match:
                    frames.append(int(match.group(1)))
                    avg_rewards.append(float(match.group(2)))

        # Skip if no valid data
        if not frames:
            continue

        # Plot and save
        plt.figure(figsize=(10, 5))
        plt.plot(frames, avg_rewards, marker="o", linestyle="-")
        plt.xlabel("Frame")
        plt.ylabel("Average Reward (10)")
        plt.title(f"Avg Reward Over Time: {base_name}")
        plt.grid(True)
        plt.tight_layout()

        output_path = os.path.join(output_dir, f"{base_name}.png")
        plt.savefig(output_path)
        plt.close()

print("Plots saved to:", output_dir)
