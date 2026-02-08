d = {"name": "Ram", "age": 20}

#add
d["city"] = "Delhi" 
print(d)
    
#update
d.update({"age": 21})  
print(d.update)

#get name
print(d.get("name"))     

#all keys
print(d.keys())       

#all values
print(d.values())        

#key-value pairs
print(d.items())        

#remove key
d.pop("age")  
print(d)
   

#clear dict
d.clear()              
print(d)
