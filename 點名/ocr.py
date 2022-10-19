''''''  
import easyocr


reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(r'./6.png', detail=0)


member_list = []


with open(r'./member_list.txt', 'w') as f:    
    for m in result:
        if len(m)>=4:
            f.write(f'{m}\n')
      
with open(r'./人員名單.txt', 'r')  as f:
    data = f.read().splitlines()
 
final = [] 
for d in data:
    for m in result:
        if d not in m:
            final.append(d)

print(f'未出席清單：{final}')

        


