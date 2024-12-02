import sys
import typing

DEBUG = False

with open(sys.argv[1]) as f:
    lines = f.readlines()
    a = int(lines[0].split(":")[1])
    b = int(lines[1].split(":")[1])
    c = int(lines[2].split(":")[1])
    program = [int(i) for i in lines[4].split(":")[1].strip().split(",")]


def combo(a, b, c, operand):
    debug = "combo: "
    result = operand
    if operand == 4:
        result = a
        debug += "(4: from a) "
    elif operand == 5:
        result = b
        debug += "(5: from b) "
    elif operand == 6:
        result = c
        debug += "(6: from c) "
    elif operand == 7:
        raise RuntimeError
    debug += f"{result}"
    if DEBUG:
        print(debug)
    return result


def run(
    a: int, b: int, c: int, program: list[int]
) -> typing.Generator[int, None, None]:
    pointer = 0
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]
        if DEBUG:
            print(f"a: {a}")
        if DEBUG:
            print(f"b: {b}")
        if DEBUG:
            print(f"c: {c}")

        if opcode == 0:  # adv
            result = int(a / (2 ** combo(a, b, c, operand)))
            if DEBUG:
                print(f"adv: {a} / {2**combo(a,b,c,operand)} -> {result}")
            a = result
        if opcode == 1:  # bxl
            result = b ^ operand
            if DEBUG:
                print(f"bxl: {b} ^ {operand} -> {result}")
            b = result
        if opcode == 2:  # bst
            result = combo(a, b, c, operand) % 8
            if DEBUG:
                print(f"bst: {combo(a, b,c,operand)} % 8 -> {result}")
            b = result
        if opcode == 3:  # jnz
            if a != 0:
                pointer = operand
                if DEBUG:
                    print(f"jnz: {a} -> {operand}")
                continue
            if DEBUG:
                print("jnz: noop")
        if opcode == 4:  # bxc
            result = b ^ c
            if DEBUG:
                print(f"bxc: {b} ^ {c} -< {result}")
            b = result
        if opcode == 5:  # out
            result = combo(a, b, c, operand) % 8
            if DEBUG:
                print(f"out: {combo(a, b, c, operand)} % 8 -> {result}")
            yield result
        if opcode == 6:  # bdv
            result = int(a / (2 ** combo(a, b, c, operand)))
            if DEBUG:
                print(f"adv: {b} / {2**combo(a,b,c,operand)} -> {result}")
            b = result
        if opcode == 7:  # cdv
            result = int(a / (2 ** combo(a, b, c, operand)))
            if DEBUG:
                print(f"cdv: {a} / {2**combo(a,b,c,operand)} -> {result}")
            c = result

        if DEBUG:
            print()

        pointer += 2


def find_a(b: int, c: int, program: list[int]) -> int:
    potential_numbers: list[list[int]] = [[]]
    solutions: list[int] = []
    while potential_numbers:
        vals = potential_numbers.pop(0)
        for v in range(0, 8):
            next_vals = vals + [v]
            next_a = sum(v << (it * 3) for it, v in enumerate(reversed(next_vals)))
            out = list(run(next_a, b, c, program))
            if out == program:
                solutions.append(next_a)
            elif out == program[-len(out) :] and len(next_vals) < len(program):
                potential_numbers.append(next_vals)
    return min(solutions)


part1 = list(run(a, b, c, program))
print(f"Part 1: {','.join([str(it) for it in part1])}")

print(f"Part 2: {find_a(b, c, program)}")
