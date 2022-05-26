from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox


class CheckableComboBox(QComboBox):
    def __init__(self, parent=None):
        super(CheckableComboBox, self).__init__(parent)

        self._changed = False

        self.view().pressed.connect(self.handleItemPressed)

    def setItemChecked(self, index, checked=False):
        """
        Función para comprobar si el campo del combobox está con el tick de check
        :param index:
        :param checked:
        """
        item = self.model().item(index, self.modelColumn())

        if checked:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)

    def handleItemPressed(self, index):
        """
        Función para activar el check o desactivarlo cuando le damos con el ratón
        :param index:
        """
        item = self.model().itemFromIndex(index)

        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)
        self._changed = True
    
    def hidePopup(self):
        if not self._changed:
            super().hidePopup()
        self._changed = False

    def itemChecked(self, index):
        item = self.model().item(index, self.modelColumn())
        return item.checkState() == Qt.Checked

    def get_checked_items(self) -> list[int]:
        checkedItems = []
        for i in range(self.count()):
            if self.itemChecked(i):
                checkedItems.append(i)
        return checkedItems
