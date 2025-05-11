from dataclasses import dataclass


@dataclass()
class Confine:
    dyad: int
    state1no: int
    state1ab: str
    state2no: int
    state2ab: str
    year: int
    conttype: int
    version: float

    def __hash__(self):
        return hash(self.dyad)

    def __eq__(self, other):
        return self.dyad == other.dyad

    def __str__(self):
        return f"{self.year}: {self.state1ab} - {self.state2ab}"

