from __future__ import annotations
from functools import total_ordering
from typing import Tuple
from errors import InvalidDateError, DateParseError

@total_ordering
class Date:
    """Date grégorienne minimale, immuable en pratique (méthodes renvoient des copies)."""

    __slots__ = ("_y", "_m", "_d")

    def __init__(self, year: int, month: int, day: int):
        # TODO: valider et affecter _y, _m, _d ; lever InvalidDateError si invalide
        if not (1 <= year <= 9999):
            raise InvalidDateError("Année hors limites")
        if not (1 <= month <= 12):
            raise InvalidDateError("Mois hors limites")
        if not (1 <= day <= self._days_in_month(year, month)):
            raise InvalidDateError("Jour invalide pour ce mois")
        self._y, self._m, self._d = year, month, day

    @property
    def year(self) -> int: return self._y
    @property
    def month(self) -> int: return self._m
    @property
    def day(self) -> int: return self._d

    def __repr__(self) -> str:
        # TODO: format non ambigu
        return f"Date({self._y},{self._m:02},{self._d:02})"

    def __str__(self) -> str:
        # TODO: format lisible YYYY-MM-DD
        return f"{self._y:04}-{self._m:02}-{self._d:02}"

    def to_iso(self) -> str:
        # TODO
        return str(self)

    @classmethod
    def from_iso(cls, s: str) -> "Date":
        # TODO: parser, lever DateParseError si invalide
        try:
            parts = s.split("-")
            if len(parts) != 3:
                raise DateParseError("Format incorrect")
            y, m, d = map(int, parts)
            return cls(y, m, d)
        except Exception:
            raise DateParseError("Impossible de parser la date")

    def is_leap_year(self) -> bool:
        # TODO
        y = self._y
        return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

    def _days_in_month(self, y: int, m: int) -> int:
        # TODO
        if m == 2:
            return 29 if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)) else 28
        return [31,28,31,30,31,30,31,31,30,31,30,31][m-1]

    def day_of_year(self) -> int:
        # TODO
        return sum(self._days_in_month(self._y, m) for m in range(1, self._m)) + self._d

    def add_days(self, n: int) -> "Date":
        # TODO: retourner une nouvelle date, gérer dépassements mois/année
        y, m, d = self._y, self._m, self._d + n
        while True:
            dim = self._days_in_month(y, m)
            if d > dim:
                d -= dim
                m += 1
                if m > 12:
                    m = 1
                    y += 1
            elif d < 1:
                m -= 1
                if m < 1:
                    m = 12
                    y -= 1
                d += self._days_in_month(y, m)
            else:
                break
        return Date(y, m, d)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        # TODO
        return (self._y, self._m, self._d) == (other._y, other._m, other._d)

    def __lt__(self, other: "Date") -> bool:
        # TODO: ordre lexicographique (y,m,d)
        if not isinstance(other, Date):
            return NotImplemented
        return (self._y, self._m, self._d) < (other._y, other._m, other._d)

# --- Tests rapides ---
if __name__ == "__main__":
    d = Date(2024, 2, 29)
    assert d.is_leap_year() is True
    assert str(d) == "2024-02-29"
    assert Date.from_iso("2025-09-22").to_iso() == "2025-09-22"

    try:
        Date(2023, 2, 29)
        assert False, "Devrait lever InvalidDateError"
    except InvalidDateError:
        pass

    try:
        Date.from_iso("2025-13-01")
        assert False, "Devrait lever DateParseError"
    except DateParseError:
        pass

    # add_days et ordre
    d1 = Date(2025, 12, 31).add_days(1)
    assert str(d1) == "2026-01-01"
    assert Date(2025, 1, 1) < Date(2025, 1, 2)

    print("Tests Ex1 OK")