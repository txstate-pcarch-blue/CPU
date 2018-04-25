import os
import sys
from myhdl import *

base_d = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(base_d, "python/"))

from python.helpers.Clock_Generator import clock_generator
from python.helpers.Paths import *
from python.helpers.Match_Test import match_test_assert, match_test_report
from CPU import CPU as py_cpu
from helpers.CPU_Reset_Generator import CPU_Reset_Generator


def v_cpu(clock, reset, vregisters):
    cmd = "iverilog -o %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s" %\
            (CPU_cosim_o, PC_v, IM_v, RF_v, ALU_v, DM_v, Control_v, ALU_control_v,
             BJ_calc, FU_v, HD_v, MUX_v, IF_ID_v, ID_EX_v, EX_MEM_v, MEM_WB_v, CPU_v, CPU_cosim_v)
    os.system(cmd)
    return Cosimulation("vvp -m %s %s" % (myhdl_vpi, CPU_cosim_o), clock=clock, reset=reset,
                    regOut0=vregisters[0], regOut1=vregisters[1], regOut2=vregisters[2], regOut3=vregisters[3],
                    regOut4=vregisters[4], regOut5=vregisters[5], regOut6=vregisters[6], regOut7=vregisters[7],
                    regOut8=vregisters[8], regOut9=vregisters[9], regOut10=vregisters[10], regOut11=vregisters[11],
                    regOut12=vregisters[12], regOut13=vregisters[13], regOut14=vregisters[14], regOut15=vregisters[15],
                    regOut16=vregisters[16], regOut17=vregisters[17], regOut18=vregisters[18], regOut19=vregisters[19],
                    regOut20=vregisters[20], regOut21=vregisters[21], regOut22=vregisters[22], regOut23=vregisters[23],
                    regOut24=vregisters[24], regOut25=vregisters[25], regOut26=vregisters[26], regOut27=vregisters[27],
                    regOut28=vregisters[28], regOut29=vregisters[29], regOut30=vregisters[30], regOut31=vregisters[31])


def run_MIPS_cosim():
    MAX_TIME = 1000000
    clock = Signal(0)
    reset = Signal(0)

    # Make output register files for comparison
    pyregs = []
    vregs = []
    for i in range(0, 32):
        pyregs.append(Signal(intbv(0, 0, 2**32)))
        pyregs[i].driven = not pyregs[i].driven
        vregs.append(Signal(intbv(0, 0, 2**32)))
        vregs[i].driven = not vregs[i].driven

    # Create the simulations and run
    clock_driver = clock_generator(clock)
    reset_driver = CPU_Reset_Generator(clock, reset)
    py_cosim = traceSignals(py_cpu(clock, reset, pyregs))
    v_cosim = v_cpu(clock, reset, vregs)
    match_t = match_test_report(clock, vregs, pyregs)
    sim = Simulation(instances())

    # Enter the read / execute / display cycle
    inp = ""
    help = 'Enter "run <cycles>" to run the simulation "print" to show the register files, or "quit" to exit.'
    prompt = "command: "
    print(help)
    while inp != "quit":
        inp = input(prompt)
        if inp == "show":
            for x, reg in enumerate(pyregs):
                print("py[%d]=%#x" % (x, reg.val), end=' ')
            print()
            for x, reg in enumerate(vregs):
                print(" v[%d]=%#x" % (x, reg.val), end=' ')
            print()
            if pyregs == vregs:
                print("They match")
            else:
                print("They don't match")
            continue
        elif inp.startswith("run "):
            try:
                cycles = int(inp.split()[1].strip())
                sim.run(cycles*20)
                continue
            except ValueError:
                pass
        elif inp != "quit":
            print(help)


if __name__ == '__main__':
    from argparse import ArgumentParser
    from shutil import copy
    from os import remove
    parser = ArgumentParser(description="MIPS CPU Verilog and Python cosimulation.")
    parser.add_argument('instructions_hex')
    args = parser.parse_args()
    infile = args.instructions_hex
    copy(infile, IM_in_file)
    run_MIPS_cosim()
    remove(IM_in_file)
