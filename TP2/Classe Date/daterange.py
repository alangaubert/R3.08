from __future__ import annotations
from datex import Date
from errors import InvalidDateError

class DateRange:
    __slots__ = ("start", "end")

    def __init__(self, start: Date, end: Date):
        # TODO: valider start &lt;= end
        if start > end:
            raise InvalidDateError("Date de début doit être inférieur ou égale à la date de fin")
        self.start = start
        self.end = end 

    def duration(self) -> int:
        # TODO
        return 0

    def contains(self, d: Date) -> bool:
        # TODO
        return False

    def overlaps(self, other: "DateRange") -> bool:
        # TODO
        return False

    def intersection(self, other: "DateRange") -> "DateRange | None":
        # TODO
        return None

# --- Tests rapides ---
if __name__ == "__main__":
    a = DateRange(Date(2025, 9, 1), Date(2025, 9, 10))
    b = DateRange(Date(2025, 9, 5), Date(2025, 9, 15))
    c = a.intersection(b)
    assert c is not None and c.start.to_iso() == "2025-09-05" and c.end.to_iso() == "2025-09-10"
    assert a.duration() == 10
    assert a.contains(Date(2025, 9, 1)) and a.contains(Date(2025, 9, 10))
    print("Tests Ex2 OK")