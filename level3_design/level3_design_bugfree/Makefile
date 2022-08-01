# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/sync_fifo_bugfree.v             # provide your design path

TOPLEVEL := sync_fifo_bugfree      # design file
MODULE   := test_sync_fifo_bugfree # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
