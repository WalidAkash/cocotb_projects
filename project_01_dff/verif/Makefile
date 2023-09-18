TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(shell pwd)/../src/d_ff.sv
TOPLEVEL = d_ff
MODULE = test_d_ff
SIM = verilator

CT +=	__pycache__
CT +=	results.xml
CT +=	sim_build

include $(shell cocotb-config --makefiles)/Makefile.sim

clean::
	@rm -rf $(CT)
