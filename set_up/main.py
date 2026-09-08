import tkinter as tk
from tkinter import messagebox
import threading

from config import MORNING, NIGHT
from downloader import download_schedule
from csv_loader import load_schedule
from comparator import compare_morning, compare_night
from reporter import write_reports

# ==================================================
# iGame Scheduler Application
# ==================================================


class IGameSchedulerApp:

    def __init__(self, root):

        self.root = root

        # ------------------------------------------
        # Window
        # ------------------------------------------

        self.root.title("iGame Scheduler")

        self.root.geometry("450x350")

        self.root.resizable(False, False)

        # ------------------------------------------
        # Title
        # ------------------------------------------

        title = tk.Label(self.root, text="iGame Scheduler", font=("Arial", 22, "bold"))

        title.pack(pady=(30, 10))

        # ------------------------------------------
        # Description
        # ------------------------------------------

        description = tk.Label(
            self.root, text="Select the schedule run:", font=("Arial", 13)
        )

        description.pack(pady=(0, 20))

        # ------------------------------------------
        # Morning button
        # ------------------------------------------

        self.morning_button = tk.Button(
            self.root,
            text="MORNING RUN",
            font=("Arial", 13, "bold"),
            width=25,
            height=2,
            command=lambda: self.start_run(MORNING),
        )

        self.morning_button.pack(pady=8)

        # ------------------------------------------
        # Night button
        # ------------------------------------------

        self.night_button = tk.Button(
            self.root,
            text="NIGHT RUN",
            font=("Arial", 13, "bold"),
            width=25,
            height=2,
            command=lambda: self.start_run(NIGHT),
        )

        self.night_button.pack(pady=8)

        # ------------------------------------------
        # Status
        # ------------------------------------------

        self.status_label = tk.Label(
            self.root, text="Status: Ready", font=("Arial", 11)
        )

        self.status_label.pack(pady=(25, 5))

        # ------------------------------------------
        # Close button
        # ------------------------------------------

        self.close_button = tk.Button(
            self.root, text="Close", width=12, command=self.root.destroy
        )

        self.close_button.pack(pady=5)

    # ==================================================
    # Window handling
    # ==================================================

    def bring_to_front(self):
        """
        Bring the application window to the front.

        The topmost attribute is only used temporarily
        so that the window does not remain permanently
        above other applications.
        """

        try:

            self.root.lift()

            self.root.focus_force()

            self.root.attributes("-topmost", True)

            self.root.update()

            self.root.after(1500, lambda: self.root.attributes("-topmost", False))

        except tk.TclError:

            pass

    # ==================================================
    # Update status
    # ==================================================

    def update_status(self, message):

        self.root.after(0, lambda: self.status_label.config(text=f"Status: {message}"))

    # ==================================================
    # Enable / disable buttons
    # ==================================================

    def set_buttons_enabled(self, enabled):

        state = tk.NORMAL if enabled else tk.DISABLED

        self.root.after(
            0,
            lambda: (
                self.morning_button.config(state=state),
                self.night_button.config(state=state),
            ),
        )

    # ==================================================
    # Start scheduler
    # ==================================================

    def start_run(self, shift):

        # Make sure the window remains visible
        self.bring_to_front()

        # Prevent the user from starting
        # another run while one is active.
        self.set_buttons_enabled(False)

        # Start scheduler in background
        thread = threading.Thread(target=self.run_schedule, args=(shift,), daemon=True)

        thread.start()

    # ==================================================
    # Run scheduler
    # ==================================================

    def run_schedule(self, shift):

        try:

            # --------------------------------------
            # Start
            # --------------------------------------

            self.update_status(f"Starting {shift} run...")

            # --------------------------------------
            # Download schedules
            # --------------------------------------

            self.update_status("Downloading schedule...")

            files = download_schedule(shift)

            # --------------------------------------
            # Morning
            # --------------------------------------

            if shift == MORNING:

                self.update_status("Loading today's schedule...")

                today_df = load_schedule(files["today"])

                self.update_status("Comparing schedule...")

                result = compare_morning(today_df)

            # --------------------------------------
            # Night
            # --------------------------------------

            elif shift == NIGHT:

                self.update_status("Loading schedules...")

                today_df = load_schedule(files["today"])

                tomorrow_df = load_schedule(files["tomorrow"])

                self.update_status("Comparing schedules...")

                result = compare_night(today_df, tomorrow_df)

            else:

                raise ValueError(f"Unknown shift: {shift}")

            # --------------------------------------
            # Create reports
            # --------------------------------------

            self.update_status("Creating reports...")

            report_paths = write_reports(result)

            # --------------------------------------
            # Calculate results
            # --------------------------------------

            switches = result["Status"].eq("switch").sum()

            checks = result["Status"].eq("check channel").sum()

            # --------------------------------------
            # Completed
            # --------------------------------------

            self.update_status("Completed successfully")

            self.set_buttons_enabled(True)

            # --------------------------------------
            # Show completion message
            # --------------------------------------

            def show_success():

                self.bring_to_front()

                messagebox.showinfo(
                    "Run Completed",
                    f"{shift.title()} run completed.\n\n"
                    f"Rows: {len(result)}\n"
                    f"Switches: {switches}\n"
                    f"Check channel: {checks}\n\n"
                    f"Changes file:\n"
                    f"{report_paths['changes']}",
                )

            self.root.after(0, show_success)

        # ------------------------------------------
        # Error handling
        # ------------------------------------------

        except Exception as error:

            self.set_buttons_enabled(True)

            self.update_status("Error")

            def show_error():

                self.bring_to_front()

                messagebox.showerror(
                    "Run Failed", f"The {shift} run failed.\n\n" f"{error}"
                )

            self.root.after(0, show_error)


# ==================================================
# Main
# ==================================================


def main():

    root = tk.Tk()

    app = IGameSchedulerApp(root)

    # ------------------------------------------
    # Force the window to the front when launched
    # ------------------------------------------

    root.lift()

    root.focus_force()

    root.attributes("-topmost", True)

    root.update()

    # Remove temporary topmost behaviour
    # after the window has appeared.
    root.after(1500, lambda: root.attributes("-topmost", False))

    root.mainloop()


# ==================================================
# Entry point
# ==================================================

if __name__ == "__main__":
    main()
