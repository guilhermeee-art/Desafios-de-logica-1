'''Murilo foi passar as férias nos estados unidos, ao chegar na cidade de Boston achou a temperatura muito fria e foi olhar no termômetro de rua quantos graus estava fazendo. 
Para sua surpresa o termômetro estava em Fahrenheit.
Desenvolva um sistema que recebe a temperatura em Fahrenheit e responda a quantos graus equivale em Celsius.
Fórmula de conversão: ºC = (ºF-32)/1.8
'''


fahrenheit = int (input ("Digite a temperatura em fahrenheit: "))
divisao = fahrenheit-32
print (f"A Temperatura em Celsius é:{divisao/1.8}")
