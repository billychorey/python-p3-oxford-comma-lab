def oxford_comma(items):  
    if len(items) == 1:
        return(''.join(items))
    elif len(items) == 2:
        return(' and '.join(items))
    elif len(items) >= 3:
        return(f"{', '.join(items[:-1])}, and {items[-1]}")
 
        
        
print(oxford_comma(["kiwi"]))
print(oxford_comma(["kiwi", "durian"]))
print(oxford_comma(['kiwi', 'durian', 'starfruit']))