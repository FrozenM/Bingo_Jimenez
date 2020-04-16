mi_carton = (
    (1,1,1,1,1,1,1,1,1),
    (1,1,1,1,1,1,1,1,1),
    (1,1,1,1,1,1,1,1,1)
)
mi_carton1=mi_carton[0]
mi_carton2=mi_carton[1]
mi_carton3=mi_carton[2]
i=0
for x, y, z  in zip(mi_carton1,mi_carton2,mi_carton3):
    if (x==1 or y==1 or z==1):
        i += 1
print (i)
