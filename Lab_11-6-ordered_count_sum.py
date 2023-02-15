def ordered_count(inp):
    count= {}
    for char in inp:
        if char is not count:
            count[char]=1
        else:
            count += 1 
        
        sorted_counts = sorted(count.items())
        return count


#No matter what I did I couldn't get it to work

