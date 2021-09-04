# Python에서 json 파일 다루기 (읽기, 쓰기, 수정)


# json 파일 읽기
import json

with open('test.json', 'r') as f:
    json_data = json.load(f)
print(json.dumps(json_data))
print(json.dumps(json_data, indent = '\t'))


# json 파일 출력하기
k5_price = json_data['K5']['price']
print(k5_price)


# json 파일 수정하기
json_data['K5']['price'] = "7000"
print(json_data['K5']['price'])


with open('test.json', 'w', encoding = 'utf-8') as make_file:
          json.dump(json_data, make_file, indent = "\t")
          
      
with open('test.json', 'r') as f:
    json_data = json.load(f)
print(json.dumps(json_data, indent = '\t'))
