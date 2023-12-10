from operator import itemgetter

def selection_sort(data):
    n=len(data)

    for i in range(n-1):
        minindex=i
        for j in range(i+1,n):
            if(data[j]['First name'],data[j]['Last name']) < (data[minindex]['First name'],data[minindex]['Last name']):
                minindex=j
                print(data[j]['First name'],data[j]['Last name'])

                data[i],data[minindex]=data[minindex],data[i]



data=[
            {'First name': 'Raj' , 'Last name': 'Nayyar' },
            {'First name': 'Suraj' , 'Last name': 'Sharma' },
            {'First name': 'Karan' , 'Last name': 'Kumar' },
            {'First name': 'Jade' , 'Last name': 'Canary' },
            {'First name': 'Raj' , 'Last name': 'Thakur' },
            {'First name': 'Raj' , 'Last name': 'Sharma' },
            {'First name': 'Kiran' , 'Last name': 'Kamla' },
            {'First name': 'Armaan' , 'Last name': 'Kumar' },
            {'First name': 'Jaya' , 'Last name': 'Sharma' },
            {'First name': 'Ingrid' , 'Last name': 'Galore' },
            {'First name': 'Jaya' , 'Last name': 'Seth' },
            {'First name': 'Armaan' , 'Last name': 'Dadra' },
            {'First name': 'Ingrid' , 'Last name': 'Maverick' },
            {'First name': 'Aahana' , 'Last name': 'Arora' },
]

selection_sort(data)
print(data)
