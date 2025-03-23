# ** kwargs: it is a param that will pack all args into a dict
def hello(**kwargs):
    '''print("Hello "+kwargs["first"]+" "+kwargs["middle"]+" "+kwargs["last"])
hello(first="Vemparala",middle="lakshmi",last="sirisha")'''
    print("hello ",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
print(title="Ms. ",first="sowmya",middle="Kumari",last="maha")
