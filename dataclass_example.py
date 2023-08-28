from dataclasses import dataclass, field
from itertools import count

"""
Dataclasses
-----------

-   Reduce the amount of boilerplate code to write.
-   Easier to manage if the object is mainly used to manage state.
"""


@dataclass(frozen=True, order=True)
class Comment:
    text: str
    id: int = field(default_factory=count().__next__)


def main():
    comment_1 = Comment("Hey")
    comment_2 = Comment("Test")
    print(sorted([comment_2, comment_1]))


if __name__ == "__main__":
    main()
