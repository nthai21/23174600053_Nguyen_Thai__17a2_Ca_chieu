import tkinter as tk
from tkinter import messagebox  # Import messagebox
import random
import csv
from collections import defaultdict

class DiceGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Dự Đoán Tổng Xúc Xắc")
        self.play_count = 0
        self.results = []  # List to store the result of each dice roll
        self.unique_totals = set()  # Set to store unique totals
        self.roll_counts = defaultdict(int)  # Dictionary to store count of each total

        # Create the UI structure
        self.create_ui()

    def create_ui(self):
        # Main title
        title = tk.Label(self.root, text="Game Dự Đoán Tổng Xúc Xắc", font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, columnspan=3, pady=10)

        # Dice frame
        self.dice_frame = tk.Frame(self.root)
        self.dice_frame.grid(row=1, column=0, columnspan=3, pady=10)

        self.dice_canvases = [tk.Canvas(self.dice_frame, width=100, height=100, bg='white') for _ in range(3)]
        for i, canvas in enumerate(self.dice_canvases):
            canvas.grid(row=0, column=i, padx=10)

        # Prediction and result frame
        input_frame = tk.Frame(self.root)
        input_frame.grid(row=2, column=0, columnspan=3, pady=10)

        self.label = tk.Label(input_frame, text="Dự đoán tổng của ba xúc xắc:", font=("Arial", 14))
        self.label.grid(row=0, column=0, padx=10)

        self.entry = tk.Entry(input_frame, font=("Arial", 14))
        self.entry.grid(row=0, column=1, padx=10)

        self.roll_button = tk.Button(input_frame, text="Roll Dice", command=self.roll_dice, font=("Arial", 14))
        self.roll_button.grid(row=0, column=2, padx=10)

        self.result_label = tk.Label(input_frame, text="", font=("Arial", 14))
        self.result_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.previous_result_label = tk.Label(input_frame, text="Kết quả dự đoán trước:", font=("Arial", 14))
        self.previous_result_label.grid(row=2, column=0, columnspan=3, pady=10)

        # Stats frame
        stats_frame = tk.Frame(self.root)
        stats_frame.grid(row=3, column=0, columnspan=3, pady=10)

        self.stats_label = tk.Label(stats_frame, text="Thống kê số lần xuất hiện:", font=("Arial", 14))
        self.stats_label.grid(row=0, column=0, pady=10)

        self.stats_text = tk.Text(stats_frame, height=10, width=40, font=("Arial", 12))
        self.stats_text.grid(row=1, column=0, pady=10)

        self.play_count_label = tk.Label(self.root, text=f"Số lần chơi: {self.play_count}", font=("Arial", 14))
        self.play_count_label.grid(row=4, column=0, columnspan=3, pady=10)

        # Open CSV file to write results
        with open("dice_game_results.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Lần tung", "Tổng", "Kết quả"])

    def draw_dice(self, values):
        for canvas in self.dice_canvases:
            canvas.delete("all")
        
        dot_coords = {
            1: [(50, 50)],
            2: [(20, 20), (80, 80)],
            3: [(20, 20), (50, 50), (80, 80)],
            4: [(20, 20), (20, 80), (80, 20), (80, 80)],
            5: [(20, 20), (20, 80), (50, 50), (80, 20), (80, 80)],
            6: [(20, 20), (20, 50), (20, 80), (80, 20), (80, 50), (80, 80)]
        }

        for i, value in enumerate(values):
            for (x, y) in dot_coords[value]:
                self.dice_canvases[i].create_oval(x-10, y-10, x+10, y+10, fill='black')

    def roll_dice(self):
        try:
            guess = int(self.entry.get())
            if guess < 3 or guess > 18:
                messagebox.showerror("Lỗi", "Dự đoán phải nằm trong khoảng từ 3 đến 18")
                return
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ")
            return

        self.play_count += 1
        self.play_count_label.config(text=f"Số lần chơi: {self.play_count}")

        dice_values = [random.randint(1, 6) for _ in range(3)]
        self.draw_dice(dice_values)

        total = sum(dice_values)
        self.unique_totals.add(total)  # Add new total to the set of unique totals
        self.roll_counts[total] += 1

        result = "Đúng" if guess == total else "Sai"
        self.results.append((self.play_count, total, result))  # Save the result of the current dice roll

        self.update_stats()

        if len(self.results) > 1:
            prev_result = self.results[-2]
            self.previous_result_label.config(text=f"Kết quả dự đoán trước: {prev_result[1]} ({prev_result[2]})")

        if guess == total:
            self.result_label.config(text=f"Kết quả: {total} (Đúng)", fg="green")
        else:
            self.result_label.config(text=f"Kết quả: {total} (Sai)", fg="red")

        # Write the result to the CSV file
        with open("dice_game_results.csv", "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self.play_count, total, result])

    def update_stats(self):
        total_rolls = sum(self.roll_counts.values())
        self.stats_text.delete(1.0, tk.END)
        for total in sorted(self.unique_totals):  # Iterate through the unique totals and calculate the probability
            count = self.roll_counts[total]
            probability = count / total_rolls * 100 if total_rolls > 0 else 0
            self.stats_text.insert(tk.END, f"Tổng {total}: {count} lần | Xác suất: {probability:.2f}%\n")

if __name__ == "__main__":
    root = tk.Tk()
    game = DiceGame(root)
    root.mainloop()
