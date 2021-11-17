import math
import random
ang = random.randint(0, 90)
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'Âmgulo: {ang} \nO seno do ângulo é {sen:.2f} \nO cosseno do ângulo é {cos:.2f} \nA tangente do ângulo é {tan:.2f}')
