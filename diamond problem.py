
        A
       / \
      B   C
       \ /
        D

from abc import ABC, abstractmethod

# ---------- Step 1: Abstract Base Class A ----------
class A(ABC):
    def __init__(self):
        self.value = 100  # shared state (should exist only once)

    @abstractmethod
    def foo(self):
        pass


# ---------- Step 2: Class B ----------
class B:
    def __init__(self, a: A):
        self.a = a  # reference to shared A

    def foo(self):
        return f"B::foo -> value = {self.a.value}"


# ---------- Step 3: Class C ----------
class C:
    def __init__(self, a: A):
        self.a = a  # reference to same shared A

    def foo(self):
        return f"C::foo -> value = {self.a.value}"


# ---------- Step 4: Class D (Diamond Resolver) ----------
class D(A):
    def __init__(self):
        super().__init__()   # creates ONE A instance
        self.b = B(self)    # share A with B
        self.c = C(self)    # share A with C

    def foo(self):
        b_result = self.b.foo()
        c_result = self.c.foo()

        return (
            "D::foo resolving diamond problem\n"
            f"{b_result}\n"
            f"{c_result}\n"
            f"Final shared value = {self.value}"
        )


if __name__ == "__main__":
    d = D()
    print(d.foo())

