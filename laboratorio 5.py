import simpy
import random

#
# el carro se conduce un tiempo y tiene que llegar a cargarse de energia
# luego puede continuar conduciendo
# Debe hacer cola (FIFO) en el cargador
 
global tiempoProceso
    

def programa(env, name, memory, driving_time, process, cont):
    global val
    global tiempoTotal
    # Simulate driving to the BCS
    yield env.timeout(driving_time)
    print('%s entra el segundo %s' % (name, env.now))
    tiempoInicial = env.now
    val = 3
    # Request one of its charging spots
    memoria.get(memory)
    print('%s solicita entrada al CPU en el segundo %s' % (name, env.now))
    print('%s memoria utilizada %s' % (name, memory))
    print('%s procesos del programa %s' % (name, process))
    while process > 3 :
        with CPU.request() as req:  #pedimos utilizar el CPU
            yield req
        yield env.timeout(val)
        process = process - 3
        rand3 = random.randint(1,2)
        if rand3 == 1:
            yield env.timeout(5)
    if process <= 3:
        with CPU.request() as req:  #pedimos utilizar el CPU
            yield req
        yield env.timeout(process)
        process = 0
    memoria.put(memory)
    print('%s termina %s' % (name, env.now))
    tiempoFinal = env.now
    tiempoProm= tiempoFinal - tiempoInicial
    print('%s tiempo del programa: %s' % (name, tiempoProm))
    tiempoTotal = tiempoTotal + tiempoProm
    #creacion de objetos
env = simpy.Environment()  #crear ambiente de simulacion
CPU = simpy.Resource(env, capacity=1) #velocidad de CPU, cantidad de instrucciones por unidad de tiempo
memoria = simpy.Container(env, init=100, capacity=100)#Capacidad de memoria



req = 3
tiempoInicial = 0
tiempoTotal = 0.0
tiempoFinal = 0
tiempoProm = 0
totalPromedio = 0
variable = 0
nprogramas = 25
interval = 10
# crear los carros
for i in range(nprogramas):
    t = random.expovariate(1.0 / interval)
    rand = random.randint(1,10)
    rand2 = random.randint(1,10)
    env.process(programa(env, 'programa %d' % i, rand, t, rand2, i))


# correr la simulacion
env.run()
tiempoTotal = tiempoTotal / nprogramas
print('tiempo promedio total: %s' % (tiempoTotal))
