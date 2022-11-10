from __future__ import annotations


class Stack:
    def __init__(self) -> None:
        self.items: list[int] = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: int) -> int:
        if isinstance(item, int):
            self.items.append(item)
            return len(self.items)
        else:
            print("Only integers are allowed")
            return -1

    def pop(self) -> int | None:
        if not self.is_empty():
            return self.items.pop()
        print("Nothing to pop. Stack is empty!")
        return None

    def __str__(self) -> str:
        return " ".join([str(x) for x in self.items])

    def get_length(self) -> int:
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    while True:
        print("")
        print("Select an option: ")
        print("    Push")
        print("    Pop")
        print("    Quit")
        print()
        choice = input("Type your choice here: ").split()
        print()

        if choice[0].strip().lower() == "push":
            try:
                print(f"Stack length: {stack.push(int(choice[1]))}")
                print(f"Stack: {stack}")
            except ValueError:
                print("Only integers are allowed")
            except IndexError:
                print("Please supply a value to push")
        elif choice[0].strip().lower() == "pop":
            print(f"Popped: {stack.pop()}")
            print(f"Stack length: {stack.get_length()}")
            print(f"Stack: {stack}")
        elif choice[0].strip().lower() == "quit":
            break
        else:
            print(f"Not implemented choice: {choice[0]}")
