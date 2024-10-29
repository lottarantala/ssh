
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str):
        if cell in self._evaluating:
            raise ValueError("Circular dependency detected")
        self._evaluating.add(cell)
        try:
            value = self._cells.get(cell, '')
            if value.isdigit():
                return int(value)
            else:
                return value
        finally:
            self._evaluating.remove(cell)

