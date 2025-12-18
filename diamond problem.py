
        A
       / \
      B   C
       \ /
        D

from abc import ABC, abstractmethod

# ---------- Base Class ----------
class A(ABC):
    def __init__(self):
        print("initializing A")

    @abstractmethod
    def foo(self):
        pass


# ---------- Class C ----------
class C(A):
    def __init__(self):
        super().__init__()
        print("initializing C")

    def foo(self):
        return "[Implementation of C]"


# ---------- Class B ----------
class B(A):
    def __init__(self):
        super().__init__()
        print("initializing B")

    def foo(self):
        return "[Implementation of B]"


# ---------- Class D ----------
class D(B, C):
    def __init__(self):
        super().__init__()   # follows MRO
        print("initialising D")

    def foo(self):
        # Explicit ambiguity resolution
        b_impl = B.foo(self)
        c_impl = C.foo(self)
        print(f"D resolves diamond by using: {b_impl} AND {c_impl}")


# ---------- Execution ----------
if __name__ == "__main__":
    d = D()
    d.foo()


