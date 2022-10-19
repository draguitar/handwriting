  
import easyocr


reader = easyocr.Reader(['en'], gpu=False)
ocr_result = reader.readtext(r'./6.png', detail=0)


member_list = []
attendance_list = []

with open(r'./attendance.txt', 'w') as f:    
    for m in ocr_result:
        if len(m)>=4:
            attendance_list.append(m)
            f.write(f'{m}\n')

with open(r'./人員名單.txt', 'r')  as f:
    data = f.read().splitlines()

final_list = []
  
#final = [] 
# m 出席者 - 長字串
# d      名單 - 短字串
for d in data:
    for m in attendance_list:
        if m.lower().find(d.lower())!=-1:
            final_list.append(d)
            break
print(f'缺席者 {set(data) - set(final_list)}')
        
