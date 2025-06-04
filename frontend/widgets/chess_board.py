from PySide6.QtWidgets import (
    QGraphicsRectItem, QGraphicsView, QGraphicsScene, QGraphicsItem
)

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QBrush, QColor, QPen

from backend.other.types import TrackingDict

from backend.princess import UserPrincess, BotPrincess



class ChessSquare(QGraphicsRectItem):
    def __init__(self, board, x, y, size, default_color, clickable_enabled):
        super().__init__(0, 0, size, size)
        self.board = board
        self.x = x
        self.y = y
        self._set_colors(default_color)

        self.setPos(self.x * size, self.y * size)
        self.setBrush(QBrush(self.default_color))
        self.setPen(QPen(Qt.NoPen))
        
        self.setClickable(clickable_enabled)

    
    def _set_colors(self, default_color):
        self.default_color = default_color

        self.user_princess_color = QColor("lime")
        self.user_moves_color = QColor("red")

        self.bot_princess_color = QColor("cyan")
        self.bot_moves_color = QColor("magenta")

     
    def setClickable(self, enabled):
        self._clickable = enabled
        self.setAcceptHoverEvents(enabled)
        self.setFlag(QGraphicsItem.ItemIsSelectable, enabled)


    def _handle_left_button(self, event):
        if (self.x,self.y) in self.board.user_princesses.keys():
            event.ignore()
            return

        user_princess = UserPrincess(self.board, self.x, self.y)
        self.board.user_princesses[(self.x,self.y)] = user_princess 
        self.board.set_moves()

        self.setBrush(QBrush(self.user_princess_color))


    def _handle_right_button(self):
        if (self.x, self.y) in self.board.user_princesses.keys():
            self.board.user_princesses.pop((self.x,self.y))
            self.board.unset_moves_and_princesses()
        self.setBrush(QBrush(self.default_color))


    def mousePressEvent(self, event):
        """ Обработка клика по клетке """
        if not self._clickable:
            event.ignore()
            return

        if event.button() == Qt.LeftButton:
            self._handle_left_button(event)
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
    def __init__(self, config, clickable_enabled):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        
        self.clickable_enabled = clickable_enabled

        self.user_princesses = TrackingDict()
        self.bot_princesses = TrackingDict()

        self.user_moves = set()
        self.bot_moves = set()

        config_applied = self._apply_config(config)

        self.N = self.params["N"]
        self.square_size = self._calculate_square_size()

        self.setSceneRect(0, 0, self.N*self.square_size, self.N*self.square_size)

        self.create_board()

        if config_applied:
            self.set_moves()
            self.set_princesses()



    def create_board(self):
        self.squares = []
        
        for y in range(self.N):
            for x in range(self.N):
                color = QColor(240, 217, 181) if (x+y) % 2 else QColor(181, 136, 99)
                square = ChessSquare(self, x, y, self.square_size, color, self.clickable_enabled)
                self.scene.addItem(square)
                self.squares.append(square)


    def _calculate_square_size(self):
        return self.width()//(self.N+1)


    def _apply_config(self, config):
        self.params = config["params"]
        princesses = config["princesses"]
        moves = config["moves"]
        
        if princesses["user_princesses_coords"] is not None and moves["user_moves"] is not None:
            for user_princess_coords in princesses["user_princesses_coords"]:
                x = user_princess_coords[0]
                y = user_princess_coords[1]
                self.user_princesses[(x,y)] = UserPrincess(self, x, y) 

            for bot_princess_coords in princesses["bot_princesses_coords"]:
                x = bot_princess_coords[0]
                y = bot_princess_coords[1]
                self.bot_princesses[(x,y)] = BotPrincess(self, x, y) 

            self.user_moves = moves["user_moves"]
            self.bot_moves = moves["bot_moves"]

            return 1
        return 0


    def save_princesses_count(self):
        self.params["K"] = len(self.user_princesses)


    def fetch_moves(self):
        """ Собирает ходы фигур """
        for user_princess in self.user_princesses.values():
            self.user_moves |= user_princess.moves

        for bot_princess in self.bot_princesses.values():
            self.bot_moves |= bot_princess.moves


    def set_princesses(self):
        for user_princess_coords, user_princess in self.user_princesses.items():
            square = self.squares[user_princess_coords[0] + user_princess_coords[1]*self.N]
            square.setBrush(QBrush(square.user_princess_color))
            
        for bot_princess_coords, bot_princess in self.bot_princesses.items():
            square = self.squares[bot_princess_coords[0] + bot_princess_coords[1]*self.N]
            square.setBrush(QBrush(square.bot_princess_color))


    def set_moves(self):
        for user_move in self.user_moves:
            square = self.squares[user_move[0] + user_move[1]*self.N]
            square.setBrush(QBrush(square.user_moves_color))
            square.setClickable(False)

        for bot_move in self.bot_moves:
            square = self.squares[bot_move[0] + bot_move[1]*self.N]
            square.setBrush(QBrush(square.bot_moves_color))
            square.setClickable(False)
    

    def unset_moves_and_princesses(self):
        free_squares = self.get_free_squares()
        for square in free_squares:
            square.setClickable(True)
            square.setBrush(QBrush(square.default_color))


    def get_params(self):
        return self.params


    def get_princesses_coords(self):
        return {
            "user_princesses_coords": tuple(self.user_princesses.keys()),
            "bot_princesses_coords": tuple(self.bot_princesses.keys())
        }


    def get_moves_coords(self):
        return {
            "user_moves": tuple(self.user_moves),
            "bot_moves": tuple(self.bot_moves)
        }


    def get_free_squares(self):
        free_squares = set()
        for square in self.squares:
            if (square.x, square.y) not in (self.user_moves | self.bot_moves) and (square.x, square.y) not in (self.user_princesses.keys() | self.bot_princesses.keys()):
                free_squares.add(square)
        return free_squares
                

    def get_free_squares_coords(self):
        free_squares_coords = set()
        free_squares = self.get_free_squares()
        for square in free_squares:
            free_squares_coords.add((square.x,square.y))
        return tuple(free_squares_coords)
