
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
            if value.startswith("'") and value.endswith("'"):
                return value[1:-1]
            try:
                return int(value)
            except ValueError:
                return "#Error"
        finally:
            self._evaluating.remove(cell)

