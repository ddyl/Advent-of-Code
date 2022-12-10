"""My solution for year 200 day 10."""
from dataclasses import dataclass
from os import linesep

from advent_of_code import advent_of_code_requests as aoc_requests


@dataclass
class Signal:
    """Represents a signal in the instruction set."""

    ins: str
    add: int


@dataclass
class Cpu:
    """Represents the cpu that is modified by the instruction set."""

    cycle: int
    register: int


@dataclass
class Crt:
    """Represents the cathode ray tube (crt)."""

    cycle: int
    display: list


def get_input() -> list[Signal]:
    """Returns the challenge input as a list of Signal dataclass objects.

    Returns:
        list[Signal]: The challenge instructions.
    """
    return [
        Signal(ins=line.split(" ")[0], add=0)
        if len(line.split(" ")) == 1
        else Signal(ins=line.split(" ")[0], add=int(line.split(" ")[1]))
        for line in aoc_requests.get_input(year="2022", day="10").split("\n")
    ]


def part_1_solution(signal_cycles: list) -> int:
    """Applies instructions to the CPU and returns the sum of signal strengths at\
         the cycles included in `signal_cycles`.

    Each signal strength is the resulting value of `cycle number * register value`.

    Args:
        signal_cycles (list): The cycles at which the signal strength should be\
             considered.

    Returns:
        int: The sum of all signal strengths.
    """
    instructions = get_input()
    cpu = Cpu(cycle=0, register=1)
    signal_strengths = []
    s_index = 0

    for instruction in instructions:
        local_instruction = (
            [instruction]
            if instruction.ins == "noop"
            else [Signal(ins="noop", add=0), instruction]
        )
        for ins in local_instruction:
            cpu.cycle += 1

            if s_index < len(signal_cycles) and cpu.cycle == signal_cycles[s_index]:
                signal_strengths.append(cpu.cycle * cpu.register)
                s_index += 1

            cpu.register += ins.add

    return sum(signal_strengths)


def part_2_solution() -> str:
    """Prints out challenge instructions on the cathode ray tube (dataclass object)\
         and returns a string representing the screen.

    Returns:
        str: The display on as seen on the cathode ray tube.
    """
    instructions = get_input()
    cpu = Cpu(cycle=0, register=1)
    crt = Crt(cycle=0, display=[])

    for instruction in instructions:
        local_instruction = (
            [instruction]
            if instruction.ins == "noop"
            else [Signal(ins="noop", add=0), instruction]
        )
        for ins in local_instruction:
            if crt.cycle % 40 == 0:
                crt.display.append([])
                crt.cycle = 0

            if crt.cycle in (cpu.register - 1, cpu.register, cpu.register + 1):
                crt.display[-1].append("%")
            else:
                crt.display[-1].append(" ")

            cpu.cycle += 1
            crt.cycle += 1

            cpu.register += ins.add

    return linesep + linesep.join(["".join(line) for line in crt.display])


def main() -> tuple:
    """Returns the answer for parts 1 and 2 as a tuple."""
    return (
        part_1_solution(signal_cycles=[20, 60, 100, 140, 180, 220]),
        part_2_solution(),
    )
