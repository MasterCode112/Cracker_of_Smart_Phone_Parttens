import itertools
from tkinter import Tk, Canvas, Button, Label, simpledialog, font
import itertools

DOT_POSITIONS_TEMPLATE = {
    1: (1 / 6, 1 / 6),
    2: (3 / 6, 1 / 6),
    3: (5 / 6, 1 / 6),
    4: (1 / 6, 3 / 6),
    5: (3 / 6, 3 / 6),
    6: (5 / 6, 3 / 6),
    7: (1 / 6, 5 / 6),
    8: (3 / 6, 5 / 6),
    9: (5 / 6, 5 / 6)
}

class LockPatternViewer:
    def __init__(self, root, canvas_size):
        self.root = root
        self.root.title("MasterCode Hacking Tool")
        self.canvas_size = canvas_size
        self.dot_radius = canvas_size // 30

        title_font = font.Font(size=20, weight="bold")
        self.title_label = Label(root, text="MasterCode Hacking Tool", font=title_font)
        self.title_label.pack()
        
        self.colors = ["red", "green", "blue"]
        self.current_color_index = 0
        self.cycle_title_color()

        self.canvas = Canvas(root, width=canvas_size, height=canvas_size, bg="white")
        self.canvas.pack()

        self.previous_button = Button(root, text="Previous", command=self.display_previous_pattern)
        self.previous_button.pack(side="left")

        self.next_button = Button(root, text="Next", command=self.display_next_pattern)
        self.next_button.pack(side="right")

        self.pattern_label = Label(root, text="")
        self.pattern_label.pack()

        self.dots_positions = {k: (int(x * canvas_size), int(y * canvas_size))
                               for k, (x, y) in DOT_POSITIONS_TEMPLATE.items()}

        self.patterns = list(self.generate_patterns())
        self.current_index = 0
        self.display_pattern(self.current_index)

    def cycle_title_color(self):
        self.title_label.config(fg=self.colors[self.current_color_index])
        self.current_color_index = (self.current_color_index + 1) % len(self.colors)
        self.root.after(500, self.cycle_title_color)

    def draw_pattern(self, pattern):
        self.canvas.delete("all")

        for pos in self.dots_positions.values():
            self.canvas.create_oval(pos[0] - self.dot_radius, pos[1] - self.dot_radius,
                                    pos[0] + self.dot_radius, pos[1] + self.dot_radius,
                                    fill="black")

        for i in range(len(pattern) - 1):
            start_pos = self.dots_positions[pattern[i]]
            end_pos = self.dots_positions[pattern[i + 1]]
            self.canvas.create_line(start_pos[0], start_pos[1],
                                    end_pos[0], end_pos[1],
                                    fill="blue", width=5)

    def display_pattern(self, index):
        pattern = self.patterns[index]
        self.draw_pattern(pattern)
        self.update_pattern_label()
        self.update_buttons_state()
        self.log_pattern(index)

    def display_next_pattern(self):
        if self.current_index < len(self.patterns) - 1:
            self.current_index += 1
            self.display_pattern(self.current_index)

    def display_previous_pattern(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.display_pattern(self.current_index)

    def update_buttons_state(self):
        self.previous_button.config(state="normal" if self.current_index > 0 else "disabled")
        self.next_button.config(state="normal" if self.current_index < len(self.patterns) - 1 else "disabled")

    def update_pattern_label(self):
        self.pattern_label.config(text=f"Pattern {self.current_index + 1} of {len(self.patterns)}")

    def log_pattern(self, index):
        # Log the current pattern view to a file
        with open("patterns_log.txt", "a") as log_file:
            pattern = self.patterns[index]
            log_file.write(f"Viewed Pattern {index + 1}: {pattern}\n")

    def generate_patterns(self):
        for length in range(4, 10): 
            for pattern in itertools.permutations(range(1, 10), length):
                yield pattern

root = Tk()
canvas_size = simpledialog.askinteger("Canvas Size", "Enter canvas size (e.g., 600 for 600x600):", minvalue=300, maxvalue=1000)
if canvas_size:
    viewer = LockPatternViewer(root, canvas_size)
    root.mainloop()
