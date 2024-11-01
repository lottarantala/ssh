
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
            return "#Circular"
        self._evaluating.add(cell)
        try:
            value = self._cells.get(cell, '')
            if value.startswith("'") and value.endswith("'"):
                return value[1:-1]
            elif value.startswith("="):
                if value[1:].isidentifier():
                    referenced_value = self.evaluate(value[1:])
                    if referenced_value == "#Error" or referenced_value == "#Circular":
                        return referenced_value
                    return int(referenced_value)
                elif value[1:].isdigit():
                    return int(value[1:])
                elif value[1:].startswith("'") and value[1:].endswith("'"):
                    return value[2:-1]
                else:
                    try:
                        # Evaluate arithmetic expressions
                        expression = value[1:]
                        result = eval(expression, {}, {})
                        if isinstance(result, float) and not result.is_integer():
                            return "#Error"
                        return int(result)
                    except:
                        return "#Error"
            try:
                return int(value)
            except ValueError:
                return "#Error"
        finally:
            self._evaluating.remove(cell)

