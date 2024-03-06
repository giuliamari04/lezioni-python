#slicing --> crea una sottostringa estraendo elementi da un' altra stringa
#   indexing[] or slice()
#   [start:stop:step]
#   start: indice da dove parte
#   stop: indice dove si ferma
#   step: ogni quanto 

name= "name surname"
first_name = name[0] #---> n
first_name = name[0:2] #-->na
first_name = name[:4] #-->name

last_name = name[::7] #-->nr
last_name = name[::2] #-->nm unm
last_name = name[::3] #-->neua
reverse_name = name[::-1] #-->emanrus eman


print(first_name)
print(last_name)
print(reverse_name)


website = "https://google.com"
website2 = "https://wikipedia.com"
slice = slice(8,-4)

print(website[slice])
print(website2[slice])