import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from math import floor

kivy.require("1.0.9")


class CombatCalculator(GridLayout):
    def __init__(self, **kwargs):
        super(CombatCalculator, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Hitpoints"))
        self.hp = TextInput(multiline=False)
        self.add_widget(self.hp)

        self.add_widget(Label(text="Attack"))
        self.attack = TextInput(multiline=False)
        self.add_widget(self.attack)

        self.add_widget(Label(text="Strength"))
        self.strength = TextInput(multiline=False)
        self.add_widget(self.strength)

        self.add_widget(Label(text="Defence"))
        self.defence = TextInput(multiline=False)
        self.add_widget(self.defence)

        self.add_widget(Label(text="Ranged"))
        self.ranged = TextInput(multiline=False)
        self.add_widget(self.ranged)

        self.add_widget(Label(text="Prayer"))
        self.prayer = TextInput(multiline=False)
        self.add_widget(self.prayer)

        self.add_widget(Label(text="Magic"))
        self.magic = TextInput(multiline=False)
        self.add_widget(self.magic)

        self.calculate = Button(text="Calculate")
        self.calculate.bind(on_press=self.calculate_combat)
        self.add_widget(self.calculate)

        self.output = Label(text="")
        self.add_widget(self.output)

    def calculate_combat(self, instance):
        hitpoints = int(self.hp.text)
        attack = int(self.attack.text)
        strength = int(self.strength.text)
        defence = int(self.defence.text)
        ranged = int(self.ranged.text)
        prayer = int(self.prayer.text)
        magic = int(self.magic.text)

        base = 0.25 * (defence + hitpoints + floor(prayer / 2))
        melee = 0.325 * (attack + strength)
        mage = 0.325 * (floor(magic / 2) + magic)
        range_ = 0.325 * (floor(ranged / 2) + ranged)
        combat = floor(base + max(melee, mage, range_))

        self.output.text = f"Combat Level: {combat:.2f}"


class MyApp(App):
    def build(self):
        return CombatCalculator()


if __name__ == "__main__":
    MyApp().run()
