from PySide6.QtWidgets import (
    QGraphicsRectItem, QGraphicsView, QGraphicsScene, QGraphicsItem
)

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QBrush, QColor, QPen


class ChessSquare(QGraphicsRectItem):
    def __init__(self, row, col, size, color):
        super().__init__(0, 0, size, size)
        self.row = row
        self.col = col
        self.default_color = color
        self.setPos(col * size, row * size)
        self.setBrush(QBrush(color))
        self.setPen(QPen(Qt.NoPen))
        
        
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
    
    def mousePressEvent(self, event):
        """Обработка клика на клетке"""

        if event.button() == Qt.LeftButton:
            self.setBrush(QBrush(QColor("lime")))  
            event.accept()

        elif event.button() == Qt.RightButton:
            self.setBrush(QBrush(self.default_color))
            event.accept()

        else:
            super().mousePressEvent(event)
    
    def hoverEnterEvent(self, event):
        """При наведении курсора"""
        self.setPen(QPen(QColor(255, 255, 0), 2))  
        super().hoverEnterEvent(event)
    
    def hoverLeaveEvent(self, event):
        """Когда курсор уходит"""
        self.setPen(QPen(Qt.NoPen))
        super().hoverLeaveEvent(event)


class ChessBoard(QGraphicsView):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.square_size = 50
        self.setFixedSize((self.n+1)*self.square_size, (self.n+1)*self.square_size)
        self.setSceneRect(0, 0, self.n*self.square_size, self.n*self.square_size)
        self.princesses_coords = []


        self.create_board()
    
    def create_board(self):
        self.squares = []
        
        for row in range(self.n):
            for col in range(self.n):
                color = QColor(240, 217, 181) if (row + col) % 2 else QColor(181, 136, 99)
                square = ChessSquare(row, col, self.square_size, color)
                self.scene.addItem(square)
                self.squares.append(square)
