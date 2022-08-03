from typing import NewType

InvalidPlayerActionError = NewType("InvalidPlayerActionError", AssertionError)
