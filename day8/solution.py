from collections import defaultdict
from copy import copy

from day8.puzzleinput import PUZZLEINPUT

class RETURN_CODE:
    RUNNING = -1
    SUCCESS = 0
    LOOP = 1


class CMD:
    ACC = "acc"
    JMP = "jmp"
    NOP = "nop"

class EndReachedException(Exception):
    pass

class InfiniteLoopException(Exception):
    pass


class Instruction:
    def __init__(self, opcode: str):
        self.cmd, operand = opcode.split(" ")
        self.operand = int(operand)

    def __str__(self):
        prefix = "+" if self.operand >= 0 else ""
        return f"{self.cmd} {prefix}{self.operand}"

class CPU:
    def __init__(self, code: str):
        self.opcodes = code.split("\n")
        self.reset_cpu()

    def reset_cpu(self):
        opcodes = self.opcodes
        self.program = [Instruction(op) for op in opcodes]
        self.PC = 0
        self.IC = 1  # instruction counter; how many instructions have been issued?
        self.acc = 0  # accumulator starts at 0
        self.visits = [[] for i in range(len(self.program))]  # index -> [PC values]
        self.return_code = RETURN_CODE.RUNNING
        # Patching system
        self.use_patch = False  # for clarity
        self.patch_index = -1
        self.patch_instruction = CMD.NOP

    def fetch_instruction(self):
        if self.PC >= len(self.program):
            raise EndReachedException()
        original_instruction = self.program[self.PC]
        if self.use_patch and self.PC == self.patch_index:
            patched = copy(original_instruction)
            patched.cmd = self.patch_instruction
            return patched
        else:
            return original_instruction

    def visit(self):
        self.visits[self.PC].append(self.IC)
        if len(self.visits[self.PC]) >= 2:
            raise InfiniteLoopException()

    def exec(self, instruction):
        """
        Method that defines the behaviour of the instructions

        :param instruction: Instruction to execute
        :return: Nothing
        """
        if instruction.cmd == CMD.NOP:
            self.PC += 1
            return

        if instruction.cmd == CMD.ACC:
            self.acc += instruction.operand
            self.PC += 1
            return

        if instruction.cmd == CMD.JMP:
            self.PC += instruction.operand
            return

    def step(self):
        # get instruction
        instruction = self.fetch_instruction()

        # mark as visited
        self.visit()

        # execute instruction
        self.exec(instruction)

        # update IC
        self.IC += 1

    def run(self):
        while True:
            try:
                self.step()
            except EndReachedException:
                self.return_code = RETURN_CODE.SUCCESS
                return
            except InfiniteLoopException:
                self.return_code = RETURN_CODE.LOOP
                return

    def trace(self):
        out = ""
        for i,instruction in enumerate(self.program):
            value_len = len(str(abs(instruction.operand)))
            padding = 4 - value_len
            prefix = "+" if instruction.operand >= 0 else ""
            visits = ", ".join([str(j) for j in self.visits[i]])
            if len(self.visits[i]) > 1:
                visits += "(!)"
            out += f"{instruction}{padding*' '}| {visits}\n"
        return out

    def find_patch(self):
        for i, instruction in enumerate(self.program):
            if instruction.cmd == CMD.JMP:
                # This instruction could be patched out
                self.reset_cpu()  # reset cpu
                self.use_patch = True
                self.patch_index = i
                self.patch_instruction = CMD.NOP
                # Run code and check
                self.run()
                if self.return_code == RETURN_CODE.SUCCESS:
                    return True  # patch found

    def print_patch(self):
        return f"Line {self.patch_index}: {self.program[self.patch_index]}"



def find_solution_a():  # pragma: nocover
    cpu = CPU(PUZZLEINPUT)
    cpu.run()
    return cpu.acc


def find_solution_b():  # pragma: nocover
    cpu = CPU(PUZZLEINPUT)
    cpu.find_patch()
    cpu.run()
    return cpu.acc