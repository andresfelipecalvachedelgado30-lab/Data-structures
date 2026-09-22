print("hello.welcome to data structures class!!!")

number =10
print(f"var number1 is: {type(number)}")
gravity=9.8
print(f"var number1 is: {type(gravity)}")
numberx=8j
print(f"var number1 is: {type(numberx)}")
#String data types
'''
this is a scope comment
'''
my_name = "andres"
fullname = "andres calvache"
description = '''
hello, how's it going?
this is amazing!!!
'''
print(f"var my_name is: {type(my_name)}")
print(f"var full_name is: {type(my_name)}")
print(f"var description is: {type(my_name)}")
week_days=[]
print(week_days)
print(type(week_days))
fruits={}
print(fruits)
print(type(fruits))
months=()
print(months)
print(type(months))

#list Data Types
personal_info=['andres','calvache','23','true','3103495837','pasto',['abril',12]]
print(personal_info)
#print(type(personal_info))
#show father age
print(f"father age:{personal_info[2]}")
#print(type(personal_info))
print("father city:",personal_info[5])
#show dauther name and age
print(f"daugther name:{personal_info[6][0]}")
print(f"daugther age:{personal_info[6][1]}")
#update father age
new_age=input("please,type the new father age: ")
personal_info[2]=new_age
print(f"new father age is:{personal_info[2]}")
#add new information
personal_info.append('malala')
print(personal_info)

#tuple
user_data=('benazir','butto',35,false)
print(user_data)
print(user_data[0])
new_age=40
#user_data[2]=new_age

#dictionaries
countries_info={
    'country_name': 'colombia',
    'capital':'bogota',
    'abrbrev':'co',
    "code": 123456
}
print(countries_info[country_name])








