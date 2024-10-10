import customtkinter as ctk  # Using customtkinter for a modern look
from datetime import datetime, timedelta

class StopwatchApp:
    def __init__(self, root: ctk.CTk) -> None:
        """
        Initializes StopwatchApp with the main window and components.
        """
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("400x200")
        self.root.attributes("-topmost", True, "-alpha", 0.90)  # Keeps window on top and sets transparency
        self.root.configure(fg_color="black")  # Background color

        self.running = False
        self.start_time = None
        self.elapsed_time = timedelta(0)

        # Grid weight configuration (for centering elements)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        # Label to display the time
        self.label = ctk.CTkLabel(self.root, text="00:00:00", fg_color="black", text_color="#D3D3D3", font=("Digital-7 Mono", 72))
        self.label.grid(row=0, column=0, columnspan=3, pady=20, sticky="nsew")

        # Buttons
        self.start_button = ctk.CTkButton(self.root, text='Start', command=self.start, font=("Geneva", 15, "bold"), fg_color="green", text_color="white")
        self.start_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        self.stop_button = ctk.CTkButton(self.root, text='Stop', command=self.stop, font=("Geneva", 15, "bold"), fg_color="red", text_color="white", state="disabled")
        self.stop_button.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        self.reset_button = ctk.CTkButton(self.root, text='Reset', command=self.reset, font=("Geneva", 15, "bold"), fg_color="grey", text_color="white", state="disabled")
        self.reset_button.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")

    def start(self) -> None:
        """
        Starts the stopwatch.
        """
        if not self.running:
            self.running = True
            self.start_time = datetime.now() - self.elapsed_time  # Adjust start time to account for pause
            self.start_button.configure(state='disabled')
            self.stop_button.configure(state='normal')
            self.reset_button.configure(state='normal')
            self.update_timer()

    def update_timer(self) -> None:
        """
        Updates the stopwatch display every second.
        """
        if self.running:
            now = datetime.now()
            self.elapsed_time = now - self.start_time  # Calculates elapsed time
            total_seconds = int(self.elapsed_time.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Format time with leading zeros
            time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.label.configure(text=time_str)
            self.root.after(1000, self.update_timer)  # Re-run update_timer every second

    def stop(self) -> None:
        """
        Stops the stopwatch.
        """
        self.running = False
        self.start_button.configure(state='normal')
        self.stop_button.configure(state='disabled')

    def reset(self) -> None:
        """
        Resets the stopwatch to 00:00:00.
        """
        self.running = False
        self.elapsed_time = timedelta(0)  # Reset elapsed time
        self.label.configure(text="00:00:00")  # Reset display
        self.start_button.configure(state='normal')
        self.stop_button.configure(state='disabled')
        self.reset_button.configure(state='disabled')

if __name__ == "__main__":
    ctk.set_appearance_mode("#D3D3D3")  # Sets the theme appearance
    root = ctk.CTk()
    app = StopwatchApp(root)
    root.mainloop()