import convert_circuit
import convert_sat

print('--- Generating Circuit File ---')
convert_circuit.main()
print('--- Generating SAT File ---')
convert_sat.main()