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