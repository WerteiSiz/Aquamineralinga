COLORS = {
    "light": {
        "primary": "#0c7054",  # medium_green
        "on_primary": "#ffffff",  # white
        "secondary": "#1da668",  # light_green
        "background": "#feebc8",  # Молочный фон
        "surface": "#ffffff",  # Белый для карточек
        "on_surface": "#0b362c",  # dark_green (текст)
        "accent": "#0f81f1"  # medium_blue
    },
    "dark": {
        "primary": "#1da668",  # light_green
        "on_primary": "#ffffff",  # white
        "secondary": "#0c7054",  # medium_green
        "background": "#0b362c",  # dark_green фон
        "surface": "#0c7054",  # medium_green для карточек
        "on_surface": "#ffffff",  # Белый текст
        "accent": "#0f81f1"  # medium_blue
    }
}
class ThemeManager:
    def __init__(self):
        self.light_theme = {
            "primary": "#0c7054",  # medium_green
            "secondary": "#0b362c",  # dark_green
            "background": "#feebc8",  # молочный
            "surface": "#ffffff",  # white
            "on_primary": "#ffffff",  # white
            "on_surface": "#0b362c",  # dark_green
        }
        self.dark_theme = {
            "primary": "#1da668",  # light_green
            "secondary": "#0c7054",  # medium_green
            "background": "#0b362c",  # dark_green
            "surface": "#1a3a32",  # темнее dark_green
            "on_primary": "#ffffff",  # white
            "on_surface": "#feebc8",  # молочный
        }
        self.is_dark = False
        self.colors = self.light_theme

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.colors = self.dark_theme if self.is_dark else self.light_theme
        return self.colors


