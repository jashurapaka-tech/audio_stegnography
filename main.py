"""Application entry point."""
import sys
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import QApplication, QGraphicsOpacityEffect
from app.config import load_settings
from app.gui.main_window import MainWindow
from app.gui.splash_screen import SplashScreen
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Advanced Audio Steganography")
    window = MainWindow(load_settings()["theme"])
    window.hide()
    splash = SplashScreen()
    def show_main_window():
        window.show()
        effect = QGraphicsOpacityEffect(window)
        window.setGraphicsEffect(effect)
        animation = QPropertyAnimation(effect, b"opacity", window)
        animation.setDuration(350)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.start()
        window._startup_fade_animation = animation
    splash.finished.connect(show_main_window)
    splash.start()
    return app.exec()
if __name__ == "__main__":
    raise SystemExit(main())
