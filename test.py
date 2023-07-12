from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFormLayout, QLineEdit, QDoubleSpinBox
from PyQt5.QtCore import Qt
import sys
import math

class CombatLevelCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # Create layout
        self.layout = QFormLayout()

        # Create and add widgets to layout
        self.attack_input = self.create_input_field('Attack:')
        self.strength_input = self.create_input_field('Strength:')
        self.defence_input = self.create_input_field('Defence:')
        self.hitpoints_input = self.create_input_field('Hitpoints:')
        self.ranged_input = self.create_input_field('Ranged:')
        self.prayer_input = self.create_input_field('Prayer:')
        self.magic_input = self.create_input_field('Magic:')

        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.clicked.connect(self.calculate_combat_level)
        self.layout.addRow(self.calculate_button)

        self.combat_level_label = QLabel('')
        self.layout.addRow('Combat Level:', self.combat_level_label)

        # Set layout on widget
        self.setLayout(self.layout)

    def create_input_field(self, label_text):
        input_field = QDoubleSpinBox()
        input_field.setRange(1, 99)
        input_field.setDecimals(0)
        self.layout.addRow(QLabel(label_text), input_field)
        return input_field

    def calculate_combat_level(self):
        attack = self.attack_input.value()
        strength = self.strength_input.value()
        defence = self.defence_input.value()
        hitpoints = self.hitpoints_input.value()
        ranged = self.ranged_input.value()
        prayer = self.prayer_input.value()
        magic = self.magic_input.value()

        base = 0.25 * (defence + hitpoints + math.floor(prayer / 2))
        melee = 0.325 * (attack + strength)
        ranger = 0.325 * (math.floor(ranged / 2) + ranged)
        mage = 0.325 * (math.floor(magic / 2) + magic)
        combat_level = base + max(melee, ranger, mage)
        combat_level = round(combat_level, 2)

        self.combat_level_label.setText(str(combat_level))

app = QApplication(sys.argv)

calculator = CombatLevelCalculator()
calculator.show()

sys.exit(app.exec_())
