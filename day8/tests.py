from unittest import TestCase

from day8.solution import Instruction, CMD, CPU, RETURN_CODE


class TestDay8(TestCase):
    def test_parse_opcode(self):
        ops = [
            "acc +1",
            "nop -5",
            "jmp +2"
        ]

        acc, nop, jmp = [Instruction(opcode) for opcode in ops]

        self.assertEqual(acc.cmd, CMD.ACC)
        self.assertEqual(acc.operand, 1)

        self.assertEqual(nop.cmd, CMD.NOP)
        self.assertEqual(nop.operand, -5)

        self.assertEqual(jmp.cmd, CMD.JMP)
        self.assertEqual(jmp.operand, 2)

    def test_cpu_acc_nops_step(self):
        commands = """acc +1
nop +1
nop +2
nop +3
acc +5
acc -6
nop +1
nop +2"""
        cpu = CPU(commands)
        cpu.step()
        self.assertEqual(cpu.acc,1)
        self.assertEqual(cpu.PC, 1)  # PC starts at 0

    def test_cpu_multiple_nojump(self):
        commands = """acc +1
nop +1
nop +2
nop +3
acc +5
acc -6
nop +1
nop +2"""
        cpu = CPU(commands)
        cpu.run()
        self.assertEqual(cpu.acc,0)
        self.assertEqual(cpu.PC, 8)  # PC starts at 0
        self.assertEqual(cpu.IC, 9)  # next step would be 9

        visited = cpu.visits
        for i in range(8):
            self.assertEqual(1, len(visited[i]))
            self.assertIn(i+1, visited[i])

    def test_jmp(self):
        commands = """jmp +1
acc +1
jmp +2
acc +100
nop +5"""
        cpu = CPU(commands)
        cpu.run()
        self.assertEqual(1, cpu.acc)  # if jump was not taken acc is 101

        self.assertEqual(0, len(cpu.visits[3]))  # acc +100 was skipped

    def test_jmp_backwards(self):
        commands = """jmp +4
nop +1
acc -999
jmp +3
acc +5
jmp -2
acc +5"""
        cpu = CPU(commands)
        cpu.run()
        self.assertEqual(10, cpu.acc)
        self.assertEqual(0, len(cpu.visits[1]))
        self.assertEqual(0, len(cpu.visits[2]))
        self.assertEqual(1, len(cpu.visits[0]))
        self.assertEqual(1, len(cpu.visits[-1]))

    def test_loop_detection(self):
        commands = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
        cpu = CPU(commands)
        cpu.run()
        self.assertEqual(5, cpu.acc)
        self.assertEqual(2, len(cpu.visits[1]))

    def test_annotate_code(self):
        commands = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
        cpu = CPU(commands)
        cpu.run()

        annotated = cpu.trace()
        lines = annotated.split("\n")
        self.assertEqual("nop +0   | 1", lines[0])
        self.assertEqual("acc +1   | 2, 8(!)",lines[1])

        print(annotated)

    def test_return_code_loop(self):
        commands = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
        cpu = CPU(commands)
        cpu.run()

        self.assertEqual(RETURN_CODE.LOOP, cpu.return_code)

    def test_return_code_normal(self):
        commands = "nop +1"
        cpu = CPU(commands)
        cpu.run()

        self.assertEqual(RETURN_CODE.SUCCESS, cpu.return_code)

    def test_patch(self):
        commands = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
        cpu = CPU(commands)
        cpu.use_patch = True
        cpu.patch_index = 7
        cpu.patch_instruction = CMD.NOP
        cpu.run()

        self.assertEqual(RETURN_CODE.SUCCESS, cpu.return_code)
        self.assertEqual(8, cpu.acc)

    def test_find_patch(self):
        commands = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
        cpu = CPU(commands)
        cpu.find_patch()  # Find and enable patch to exit without loops
        self.assertEqual(CMD.NOP, cpu.patch_instruction)
        self.assertEqual(7, cpu.patch_index)
        self.assertEqual(8, cpu.acc)

    def test_print_patch(self):
        commands = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
        cpu = CPU(commands)
        cpu.find_patch()  # Find and enable patch to exit without loops
        self.assertEqual("Line 7: jmp -4", cpu.print_patch())