from myhdl import block, always

# Program Counter
# Adds 4 to the current instruction address each clock cycle
# Changes the current instruction address to addr_in if given a branch signal
@block
def program_counter(clock, reset, addr_out, addr_in, PCwrite):
    @always(clock.posedge)
    def program_counter():
      if (reset):
        addr_out.next = 0
      elif (PCWrite):
        addr_out.next = addr_in + 4

    return program_counter
