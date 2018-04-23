import os
from myhdl import Simulation, Cosimulation, Signal, traceSignals, intbv, instances
from helpers.Paths import *
from helpers.Clock_Generator import clock_generator
from helpers.Pulse_Generator import pulse_generator
from helpers.Random_Signal import random_signal
from helpers.Match_Test import match_test_report
from ALU import alu as py_alu


def v_alu(clock, reset, ALUcontrol, A, B, R, zero):
    cmd = "iverilog -o %s %s %s" % (ALU_cosim_o, ALU_cosim_v, ALU_v)
    os.system(cmd)
    return Cosimulation("vvp -m %s %s" % (myhdl_vpi, ALU_cosim_o),
                        clock=clock, reset=reset, ALUcontrol=ALUcontrol, A=A, B=B, R=R, zero=zero)

def run_ALU_cosim():
    # Initiate signals
    MAX_TIME = 1000000
    clock = Signal(0)
    reset = Signal(0)
    inA = Signal(intbv(0, 0, 2**32), delay=10)
    inB = Signal(intbv(0, 0, 2**32), delay=10)
    ALU_control = Signal(intbv(0, 0, 2**3), delay=10)
    pyData = Signal(intbv(0, 0, 2**32))
    pyZero = Signal(intbv(0, 0, 2**32))
    vData = Signal(intbv(0, 0, 2**32))
    vZero = Signal(intbv(0, 0, 2**32))

    # Build driver instances
    clock_driver = clock_generator(clock, period=20)
    control_driver = random_signal(ALU_control, clock, seed=1)
    A_rand = random_signal(inA, clock, seed=2)
    B_rand = random_signal(inB, clock, seed=3)
    reset_driver = pulse_generator(clock, reset)
    py_cosim = traceSignals(py_alu(clock, reset, inA, inB, ALU_control, pyData, pyZero))
    v_cosim = v_alu(clock, reset, ALU_control, inA, inB, vData, vZero)
    read_test = match_test_report(clock, (vData, vZero), (pyData, pyZero), a_name="v:", b_name="py:")

    sim = Simulation(instances())
    sim.run(MAX_TIME)

run_ALU_cosim()
