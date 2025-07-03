import functools
import sys
import typing

Register = str
Operation = typing.Literal["AND", "OR", "XOR"]
Result = int


if __name__ == "__main__":
    input: dict[Register, tuple[Register, Operation, Register] | Result] = {}
    with open(sys.argv[1], "r") as f:
        for line in f.readlines():
            if ":" in line:
                t = line.strip().split(": ")
                input[t[0]] = int(t[1])
            if "->" in line:
                t = line.strip().split(" ")
                input[t[4]] = (t[0], typing.cast(Operation, t[1]), t[2])

    @functools.cache
    def _eval(reg: Register) -> Result:
        result = input[reg]
        if isinstance(result, Result):
            return result
        r1, op, r2 = result
        if op == "AND":
            return _eval(r1) & _eval(r2)
        elif op == "OR":
            return _eval(r1) | _eval(r2)
        else:
            return _eval(r1) ^ _eval(r2)

    def _expand(reg: Register) -> str:
        result = input[reg]
        if isinstance(result, Result):
            return reg
        r1, op, r2 = result
        return f"({_expand(r1)} {op} {_expand(r2)})"

    part1 = input.copy()
    z_registers = sorted(k for k in part1.keys() if k.startswith("z"))
    result = 0
    for index, z in enumerate(z_registers):
        result += _eval(z) << index
    print(result)

    for z in z_registers:
        print(f"{z}: {len(_expand(z))}\n")
