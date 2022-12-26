SPWNFLAGS=--level-name CTFCHALL2022 --allow readfile

release: genexp main_circuit.spwn
	echo gates_conv.txt | spwn build main_circuit.spwn $(SPWNFLAGS)

debug: genexp main_circuit.spwn
	echo gates_conv_example.txt | spwn build main_circuit.spwn $(SPWNFLAGS) 

dry: genexp main_circuit.spwn
	cd
	echo gates_conv_example.txt | spwn build main_circuit.spwn $(SPWNFLAGS) --no-level

genexp: convert_circuit.py gates.txt gates_example.txt
	python convert_circuit.py gates_example.txt gates_conv_example.txt
	python convert_circuit.py gates.txt gates_conv.txt