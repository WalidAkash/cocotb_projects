import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge

@cocotb.test()
async def test_d_ff_simple(dut):
    """Test that d propagates to q"""

    # Create a 10us period clock on the port
    clock = Clock(dut.clk, 10, units="us")
    # Start the clock. Start it low to avoid issues on the first positive edge
    cocotb.start_soon(clock.start())

    for i in range(10):
        val = random.randint(0, 1)
        dut.d.value = val  # Assign the random value val to the input port d
        await FallingEdge(dut.clk)
        assert dut.q.value == val, f"output q was incorrect on the {i}th cycle"
