from PyQt6.QtWidgets import QLabel
from core.widgets.base import BaseWidget
from core.validation.widgets.yasb.separator import VALIDATION_SCHEMA


class SeparatorWidget(BaseWidget):
    validation_schema = VALIDATION_SCHEMA

    def __init__(
            self,
            label: str,
            label_max_length: int,
            class_name: str
    ):
        super().__init__(class_name=f"separator-widget {class_name}")
        self._label_max_length = label_max_length

        self._label_content = label

        self._label = QLabel()
        self._label.setProperty("class", "label")
        self.widget_layout.addWidget(self._label)

        self._label.show()
        self._update_label()

    def _truncate_label(self, label):
        if self._label_max_length and len(label) > self._label_max_length:
            return label[:self._label_max_length] + "..."

        return label

    def _update_label(self):
        active_label = self._label
        active_label_content = self._label_content

        active_label.setText(self._truncate_label(active_label_content))
        active_label.setStyleSheet('')
