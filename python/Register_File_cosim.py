import os
from myhdl import Simulation, Cosimulation, Signal, traceSignals, intbv, instances
from helpers.Paths import *
from helpers.Clock_Generator import clock_generator
from helpers.Pulse_Generator import pulse_generator
from helpers.Random_Signal import random_signal
from helpers.Match_Test import match_test_report
from Register_File import RegisterFile


def v_rf(readA, readB, write, rAddrA, rAddrB, wAddr, writeSignal, clock, reset, registers):
    cmd = 'iverilog -o %s %s %s' % (RF_cosim_o, RF_cosim_v, RF_v)
    os.system(cmd)
    return Cosimulation('vvp -m %s %s' % (myhdl_vpi, RF_cosim_o),
                        readA=readA, readB=readB, write=write, rAddrA=rAddrA, rAddrB=rAddrB,
                        wAddr=wAddr, writeSignal=writeSignal, clock=clock, reset=reset,
                        regOut0=registers[0], regOut1=registers[1], regOut2=registers[2], regOut3=registers[3],
                        regOut4=registers[4], regOut5=registers[5], regOut6=registers[6], regOut7=registers[7],
                        regOut8=registers[8], regOut9=registers[9], regOut10=registers[10], regOut11=registers[11],
                        regOut12=registers[12], regOut13=registers[13], regOut14=registers[14], regOut15=registers[15],
                        regOut16=registers[16], regOut17=registers[17], regOut18=registers[18], regOut19=registers[19],
                        regOut20=registers[20], regOut21=registers[21], regOut22=registers[22], regOut23=registers[23],
                        regOut24=registers[24], regOut25=registers[25], regOut26=registers[26], regOut27=registers[27],
                        regOut28=registers[28], regOut29=registers[29], regOut30=registers[30], regOut31=registers[31]
                        )

def run_RF_cosim():
    # Initiate signals
    MAX_TIME = 10000
    clock = Signal(0)
    reset = Signal(0, delay=10)
    writeSignal = Signal(0, delay=10)
    pyReadA = Signal(intbv(0, 0, 2**32))
    pyReadB = Signal(intbv(0, 0, 2**32))
    vReadA = Signal(intbv(0, 0, 2**32))
    vReadB = Signal(intbv(0, 0, 2**32))
    write = Signal(intbv(0, 0, 2**32), delay=10)
    rAddrA = Signal(intbv(0, 0, 2**5))
    rAddrB = Signal(intbv(0, 0, 2**5))
    wAddr = Signal(intbv(0, 0, 2**5), delay=10)
    pyregs = []
    vregs  = []
    for i in range(0, 32):
        pyregs.append(Signal(intbv(0, 0, 2**32)))
        pyregs[i].driven = not pyregs[i].driven
        vregs.append(Signal(intbv(0, 0, 2**32)))
        vregs[i].driven = not vregs[i].driven

    # Build driver instances
    clock_driver = clock_generator(clock, period=20)
    reset_driver = pulse_generator(clock, reset, delay=30)
    write_driver = pulse_generator(clock, writeSignal, delay=2)
    wd_rand = random_signal(clock, write, seed=1)
    rdAddrA_rand = random_signal(clock, rAddrA, seed=2)
    rdAddrB_rand = random_signal(clock, rAddrB, seed=3)
    wAddr_rand = random_signal(clock, wAddr, seed=4)
    py_cosim = traceSignals(RegisterFile(pyReadA, pyReadB, write, rAddrA, rAddrB, wAddr, writeSignal, clock, reset, pyregs))
    v_cosim = v_rf(vReadA, vReadB, write, rAddrA, rAddrB, wAddr, writeSignal, clock, reset, vregs)
    read_test = match_test_report(clock, (vReadA, vReadB), (pyReadA, pyReadB), a_name="v:", b_name="py:")
    reg_test = match_test_report(clock, vregs, pyregs, a_name="verilog", b_name="python")

    sim = Simulation(instances())

    inp = ""
    help = 'Enter "run <cycles>" to run the simulation "print" to show the register files, or "quit" to exit.'
    prompt = "command: "
    print(help)
    while (inp != "quit"):
        inp = input(prompt)
        if inp == "show":
            for x, reg in enumerate(pyregs):
                print("py[%d]=%#x" % (x, reg.val), end=' ')
            print()
            for x, reg in enumerate(vregs):
                print(" v[%d]=%#x" % (x, reg.val), end=' ')
            print()
            if (pyregs == vregs):
                print("They match")
            else:
                print("They don't match")
            continue
        elif inp.startswith("run "):
            try:
                cycles = int(inp.split()[1].strip())
                sim.run(cycles)
                continue
            except ValueError:
                pass
        elif inp != "quit":
            print(help)


run_RF_cosim()
