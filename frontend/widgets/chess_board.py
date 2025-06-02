from PySide6.QtWidgets import (
    QGraphicsRectItem, QGraphicsView, QGraphicsScene, QGraphicsItem
)

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QBrush, QColor, QPen

from frontend.other.types import TrackingDict

from backend.princess import Princess



class ChessSquare(QGraphicsRectItem):
    def __init__(self, board, y, x, size, color):
        super().__init__(0, 0, size, size)
        self.board = board
        self.y = y
        self.x = x
        self.default_color = color

        self.setPos(y * size, x * size)
        self.setBrush(QBrush(self.default_color))
        self.setPen(QPen(Qt.NoPen))
        
        self.set_clickable(True)

     
    def set_clickable(self, enabled):
        self._clickable = enabled
        self.setAcceptHoverEvents(enabled)
        self.setFlag(QGraphicsItem.ItemIsSelectable, enabled)


    def mousePressEvent(self, event):
        """ Обработка клика по клетке """
        if not self._clickable:
            event.ignore()
            return

        if event.button() == Qt.LeftButton:
            self.board.princesses[(self.y,self.x)] = Princess(self.board, self.y, self.x)
            self.board.set_moves()
            self.setBrush(QBrush(QColor("lime")))
            event.accept()

        elif event.button() == Qt.RightButton:
            if (self.y, self.x) in self.board.princesses.keys():
                self.board.princesses.pop((self.y,self.x))
                self.board.unset_moves()
            self.setBrush(QBrush(self.default_color))
            event.accept()

        else:
            super().mousePressEvent(event)
    
    
    def hoverEnterEvent(self, event):
        """ При наведении курсора """
        self.setPen(QPen(QColor(255, 255, 0), 2)) # Желтая рамка
        super().hoverEnterEvent(event)
    

    def hoverLeaveEvent(self, event):
        """ При убирании курсора """
        self.setPen(QPen(Qt.NoPen))
        super().hoverLeaveEvent(event)


class ChessBoard(QGraphicsView):
    def __init__(self, N):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.N = N
        self.square_size = 30

        self.setFixedSize((self.N+1)*self.square_size, (self.N+1)*self.square_size)
        self.setSceneRect(0, 0, self.N*self.square_size, self.N*self.square_size)

        self.moves = set()
        self.princesses = TrackingDict()

        self.create_board()
    

    def create_board(self):
        self.squares = []
        
        for y in range(self.N):
            for x in range(self.N):
                color = QColor(240, 217, 181) if (y + x) % 2 else QColor(181, 136, 99)
                square = ChessSquare(self, y, x, self.square_size, color)
                self.scene.addItem(square)
                self.squares.append(square)


    def fetch_moves(self):
        """ Собирает ходы фигур """
        for princess in self.princesses.values():
            self.moves |= princess.moves


    def set_moves(self):
        for move in self.moves:
            square = self.squares[move[0]*self.N + move[1]]
            square.setBrush(QBrush(QColor(255, 51, 51)))
            square.set_clickable(False)

    
    def unset_moves(self):
        for square in self.squares:
            if (square.y, square.x) not in self.moves and (square.y, square.x) not in self.princesses.keys():
                square.setBrush(QBrush(square.default_color))
                square.set_clickable(True)
