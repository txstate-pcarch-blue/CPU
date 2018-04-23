from myhdl import block, always


# Provides an equality testing platform to compare values
#   In the report version, incorrect matches are reported to stdout
@block
def match_test_report(clock, a, b, a_name="a", b_name="b"):
    @always(clock.negedge)
    def match_t():
        if a != b:
            print("No Match: %s %s, %s %s" % (a_name, a, b_name, b))
        else:
            print("Match: %s %s, %s %s" % (a_name, a, b_name, b))
    return match_t


# Provides an equality testing platform to compare values
#   In the assert version, incorrect matches end execution
@block
def match_test_assert(clock, a, b):
    @always(clock.negedge)
    def match_t():
        assert(a == b)
    return match_t
