import zlib 
import base64
import re

from pystyle import Colors , Write

from banner import vivod_logo

vivod_logo()

file_code = Write.Input("Введи путь файла с хэш говна:", Colors.yellow_to_red, interval=0)
name_file =  Write.Input("Также введи куда сохранить код :", Colors.yellow_to_red, interval=0)
def func(code):
    return zlib.decompress(base64.b64decode(code[::-1]))

with open(file_code,'r',encoding='utf-8') as file:
    hex_code =  eval(file.read())

res = func(hex_code)

regex = re.compile(rb"^exec\(\(_\)\(b'(.+)'\)\)$")


while True:
    result = regex.search(res)
    
    if not result:
        break
    
    res = func(result.group(1))


source_code = res.decode('utf-8')
with open(name_file,'w+',encoding='utf-8') as file:
    file.write(source_code)
Write.Print(f"Код сохранен в {name_file}. Не пишите говнокод)", Colors.yellow_to_red, interval=0)
