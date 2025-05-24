from abc import ABC, abstractmethod



class AbstractLineEditController(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def on_text_changed(self, text):
        pass

    def connect_to_line_edit(self, line_edit):
        self.line_edit = line_edit
        self.line_edit.textChanged.connect(self.on_text_changed)



class IntLineEditController(AbstractLineEditController):
    def __init__(self):
        super().__init__()

    def on_text_changed(self, text):
        if text:
            self.line_edit.is_empty = False
        else:
            self.line_edit.is_empty = True
        print(self.line_edit.is_empty)
