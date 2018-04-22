import os
from myhdl import Simulation, Cosimulation, Signal, traceSignals, intbv
from helpers.Paths import *
from helpers.Clock_Generator import clock_generator
from helpers.Pulse_Generator import pulse_generator
from helpers.Random_Signal import random_signal
from helpers.Match_Test import match_test_report
from Register_File import RegisterFile


def v_rf(readA, readB, write, rAddrA, rAddrB, wAddr, writeSignal, clock, reset, registers):
    cmd = "iverilog -o %s %s %s" % (RF_cosim_o, RF_cosim_v, RF_v)
    os.system(cmd)
    return Cosimulation("vvp -m %s %s" % (myhdl_vpi, RF_cosim_o),
                        readA=readA, readB=readB, write=write, rAddra=rAddrA, rAddrB=rAddrB,
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
    MAX_TIME = 1000000
    clock = Signal(0)
    reset = Signal(0)
    writeSignal = Signal(0)
    pyReadA = Signal(intbv(0, 0, 2**32))
    pyReadB = Signal(intbv(0, 0, 2**32))
    vReadA = Signal(intbv(0, 0, 2**32))
    vReadB = Signal(intbv(0, 0, 2**32))
    write = Signal(intbv(0, 0, 2**32))
    rAddrA = Signal(intbv(0, 0, 2**5))
    rAddrB = Signal(intbv(0, 0, 2**5))
    wAddr = Signal(intbv(0, 0, 2**5))
    pyregs = []
    vregs  = []
    for i in range(0, 32):
        pyregs.append(Signal(intbv(0, 0, 2**32)))
        pyregs[i].driven = not pyregs[i].driven
        vregs.append(Signal(intbv(0, 0, 2**32)))
        vregs[i].driven = not vregs[i].driven

    # Build driver instances
    clock_driver = clock_generator(clock)
    reset_driver = pulse_generator(clock, reset)
    write_driver = pulse_generator(writeSignal, reset, delay=3)
    wd_rand = random_signal(write, clock, seed=1)
    rdAddrA_rand = random_signal(rAddrA, clock, seed=2)
    rdAddrB_rand = random_signal(rAddrB, clock, seed=3)
    wAddr_rand = random_signal(wAddr, clock, seed=4)
    py_cosim = traceSignals(RegisterFile(pyReadA, pyReadB, write, rAddrA, rAddrB, wAddr, writeSignal, clock, reset, pyregs))
    v_cosim = traceSignals(v_rf(vReadA, vReadB, write, rAddrA, rAddrB, wAddr, writeSignal, clock, reset, vregs))
    read_test = match_test_report(clock, (vReadA, vReadB), (pyReadA, pyReadB))
    reg_test = match_test_report(clock, vregs, pyregs)

    sim = Simulation(clock_driver, reset_driver, write_driver, wd_rand, rdAddrA_rand, rdAddrB_rand, wAddr_rand,
                      py_cosim, v_cosim, read_test, reg_test)
    sim.run(MAX_TIME)

run_RF_cosim()
