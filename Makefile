# global constants
SPWNFLAGS=--allow readfile
SZS=(8 32 64 128 256)# available input sizes

# flags for debug and release
DEBUGSZ=32# number of inputs
RELEASESZ=256
DEBUGNAME=CTFCHALL2022DEBUG#level name
RELEASENAME=CTFCHALL2022

release: genexp main_circuit.spwn
	echo gates_conv_$(RELEASESZ).txt | spwn build main_circuit.spwn $(SPWNFLAGS) --level-name=$(RELEASENAME)

debug: genexp main_circuit.spwn
	echo gates_conv_$(DEBUGSZ).txt | spwn build main_circuit.spwn $(SPWNFLAGS) --level-name=$(DEBUGNAME)

dry: genexp main_circuit.spwn
	cd
	echo gates_conv_$(DEBUGSZ).txt | spwn build main_circuit.spwn $(SPWNFLAGS) --no-level --level-name=$(DEBUGNAME)

# batch script
genexp: convert_circuit.py gates_*.txt
	FOR %%s IN $(SZS) DO python convert_circuit.py gates_%%s.txt gates_conv_%%s.txt

# batch script
.PHONY: clean
clean:
	del gates_conv.txt "gates_conv_*.txt"