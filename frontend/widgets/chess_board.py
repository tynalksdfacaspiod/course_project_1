from PySide6.QtWidgets import (
    QGraphicsRectItem, QGraphicsView, QGraphicsScene
)

from PySide6.QtGui import QBrush, QColor
 


class ChessBoard(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setFixedSize(500, 500)
        self.setSceneRect(0, 0, 400, 400)
        self.create_board()

    def create_board(self):
        self.squares = []
        for row in range(8):
            for col in range(8):
                square = QGraphicsRectItem(col * 50, row * 50, 50, 50)
                color = QColor(240, 217, 181) if (row + col) % 2 else QColor(181, 136, 99)
                square.setBrush(QBrush(color))
                square.setData(0, (row, col))
                square.setAcceptHoverEvents(True)
                self.scene.addItem(square)
                self.squares.append(square)


        self.scene.selectionChanged.connect(self.on_square_clicked)

    
    def on_square_clicked(self):
        items = self.scene.selectedItems()
        if items:
            item = items[0]
            row, col = item.data(0)
            print(f"{row}, {col}")

