from myhdl import block, always


@block
def CPU_Reset_Generator(clock, reset):
    @always(clock.posedge)
    def generator():
        if generator.count in range(2, 5):
            reset.next = 1
        else:
            reset.next = 0
        generator.count += 1
    generator.count = 0
    return generator
