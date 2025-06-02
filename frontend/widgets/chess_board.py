from PySide6.QtWidgets import (
    QGraphicsRectItem, QGraphicsView, QGraphicsScene, QGraphicsItem
)

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QBrush, QColor, QPen

from frontend.other.types import TrackingDict

from backend.princess import Princess



class ChessSquare(QGraphicsRectItem):
    def __init__(self, board, x, y, size, color):
        super().__init__(0, 0, size, size)
        self.board = board
        self.x = x
        self.y = y
        self.default_color = color

        self.setPos(self.x * size, self.y * size)
        self.setBrush(QBrush(self.default_color))
        self.setPen(QPen(Qt.NoPen))
        
        self.setClickable(True)

     
    def setClickable(self, enabled):
        self._clickable = enabled
        self.setAcceptHoverEvents(enabled)
        self.setFlag(QGraphicsItem.ItemIsSelectable, enabled)


    def _handle_left_button(self):
        self.board.princesses[(self.x,self.y)] = Princess(self.board, self.x, self.y)
        self.board.set_moves()
        self.board.values["K"] += 1
        self.setBrush(QBrush(QColor("lime")))


    def _handle_right_button(self):
        if (self.x, self.y) in self.board.princesses.keys():
            self.board.princesses.pop((self.x,self.y))
            self.board.unset_moves()
            self.board.values["K"] -= 1
        self.setBrush(QBrush(self.default_color))


    def mousePressEvent(self, event):
        """ Обработка клика по клетке """
        if not self._clickable:
            event.ignore()
            return

        if event.button() == Qt.LeftButton:
            self._handle_left_button()
            event.accept()

        elif event.button() == Qt.RightButton:
            self._handle_right_button()
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
    def __init__(self, values, config=None):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        
        self.values = values
        self.config = config

        self.N = self.values["N"]
        self.square_size = 30

        self.setFixedSize((self.N+1)*self.square_size, (self.N+1)*self.square_size)
        self.setSceneRect(0, 0, self.N*self.square_size, self.N*self.square_size)
        

        self.moves = set()
        self.princesses = TrackingDict()

        self.create_board()

        if not self.config is None:
            self._apply_config()


    def _apply_config(self):
        princesses_coords, moves_coords = self.config
        
        for princess_coords in princesses_coords:
            x = princess_coords[0]
            y = princess_coords[1]
            self.princesses[(x,y)] = Princess(self, x, y) 

        self.moves = moves_coords
        self.set_princesses()
        self.set_moves()
    

    def create_board(self):
        self.squares = []
        
        for y in range(self.N):
            for x in range(self.N):
                color = QColor(240, 217, 181) if (x+y) % 2 else QColor(181, 136, 99)
                square = ChessSquare(self, x, y, self.square_size, color)
                self.scene.addItem(square)
                self.squares.append(square)


    def fetch_moves(self):
        """ Собирает ходы фигур """
        for princess in self.princesses.values():
            self.moves |= princess.moves


    def set_princesses(self):
        for princess_coords in self.princesses.keys():
            square = self.squares[princess_coords[0] + princess_coords[1]*self.N]
            square.setBrush(QBrush(QColor("lime")))
            


    def set_moves(self):
        for move in self.moves:
            square = self.squares[move[0] + move[1]*self.N]
            square.setBrush(QBrush(QColor(255, 51, 51)))
            square.setClickable(False)

    
    def unset_moves(self):
        for square in self.squares:
            if (square.x, square.y) not in self.moves and (square.x, square.y) not in self.princesses.keys():
                square.setBrush(QBrush(square.default_color))
                square.setClickable(True)


    def get_moves_coords(self):
        return tuple(self.moves)


    def get_princesses_coords(self):
        return tuple(self.princesses.keys())
