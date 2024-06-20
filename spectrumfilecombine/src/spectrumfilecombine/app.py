"""
combines the txt files provided by spectrum for Hyla boxes
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .combine import SpectrumCombiner


class SpectrumFileCombine(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        # job number 
        job_number_label = toga.Label(
            "Job Number: ",
            style=Pack(padding=(0, 5))
        )
        self.job_number_input = toga.TextInput(style=Pack(flex=1))
        job_number_box = toga.Box(style=Pack(direction=ROW, padding=5))
        job_number_box.add(job_number_label)
        job_number_box.add(self.job_number_input)

        # date
        date_label = toga.Label(
            "Date (mmddx): ",
            style=Pack(padding=(0,5))
        )
        self.date_input = toga.TextInput(style=Pack(flex=1))
        date_box = toga.Box(style=Pack(direction=ROW, padding=5))
        date_box.add(date_label)
        date_box.add(self.date_input)

        # Button
        button = toga.Button(
            "Process files",
            on_press=self.process_files,
            style=Pack(padding=5)
        )

        main_box.add(job_number_box)
        main_box.add(date_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(
            title=self.formal_name,
            size=(500,50)
        )
        self.main_window.content = main_box
        self.main_window.show()

    def process_files(self, widget):
        """combines all files into one file"""
        job_number = self.job_number_input.value
        date = self.date_input.value
        combiner = SpectrumCombiner(job_number, date)
        self.main_window.info_dialog(
            "Processing status",
            "Jobs Done!"
        )


def main():
    return SpectrumFileCombine()
