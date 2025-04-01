# \r \n => CRLF
# \n => LF
print(12, 34, 1011, sep="-", end='##\r\n') # Quebra de linha com ## antes da quebra, resultando ## no final da linha ou antes da quebra
print(56, 78, sep='~', end='\n##') # Quebra de linha com ## no final, resultando o ## na proxima linha
print(9, 10, sep='~', end='\n')