import textwrap
fillpara = textwrap.fill("the quick brown fox jumped over the lazy dogs",20)
indent = textwrap.indent("the quick brown fox jumped over the lazy dogs",'   ')
short = textwrap.shorten("the quick brown fox jumped over the lazy dogs",20)
wrapped = textwrap.wrap("the quick brown fox jumped over the lazy dogs",width=10)
for part in wrapped:
    print(part)

print()
print(fillpara)
print()
print(indent)
print()
print(short)


import random,statistics

def sample(population: int, k: int):
    random.sample(range(population),k)


def mode(data:list):
    statistics.mode(data)

def fill(text:str,width:int):
    textwrap.fill(text,width)


