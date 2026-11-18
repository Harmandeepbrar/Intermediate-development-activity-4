"""The module defines the ContactListWindow class."""
from PySide6.QtCore import Slot
from ui.base.main_window import MainWindow
from PySide6.QtWidgets import QMessageBox


__author__ = "Harmandeep Brar"
__version__ = "1.0.0"

class ContactListWindow(MainWindow):
    """Represents the main window of the application."""

    def __init__(self) -> None:
        """Initializes instance of ContactListWindow class."""

        super().__init__()

        self.setWindowTitle("Contact Manager")
        self.__initialize_widgets()


    def __initialize_widgets(self) -> None:
        """Initializes the widgets of the window."""

        # Widget Initialization
        self._name_line_edit.setPlaceholderText("Contact Name")
        self._phone_line_edit.setInputmask("(000) 000-0000;_")
        self._add_button.setDefault(True)
        self._add_button.setEnabled(False)
        self._remove_button.setEnabled(False)

        self._name_line_edit.textChanged.connect(self.__on_input_changed)
        self._phone_line_edit.textChanged.connect(self.__on_input_changed)
        
        
    @Slot()
    def __on_input_changed(self) -> None:
        """Represents the text states of the line edit widgets change."""

        name = self._name_line_edit.text().strip()
        digit_count = 0
        for character in self._phone_line_edit.text():
            if character.isdigit():
                digit_count += 1

        self._add_button.setEnabled(name != "" and digit_count == 10)