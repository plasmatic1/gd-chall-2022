SPWNFLAGS=--level-name CTFCHALL2022 --allow readfile

release: genexp main_circuit.spwn
	spwn build main_circuit.spwn $(SPWNFLAGS) < gates_conv.txt

debug: genexp main_circuit.spwn
	spwn build main_circuit.spwn $(SPWNFLAGS) < gates_conv_example.txt

dry: genexp main_circuit.spwn
	spwn build main_circuit.spwn $(SPWNFLAGS) -l < gates_conv_example.txt

genexp: convert_circuit.py gates.txt gates_example.txt
	python convert_circuit.py gates_example.txt gates_conv_example.txt
	python convert_circuit.py gates.txt gates_conv.txt