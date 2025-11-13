import time
n = int(input("Saisir un entier positif n : "))
print("Compte à rebours avec for :")
for i in range(n, -1, -1):
    print(i)
    time.sleep(1)

print("Compte à rebours avec while :")
m = n
while m >= 0:
    print(m)
    time.sleep(1)
