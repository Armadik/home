l = (1, 5, 7, 1, 4, 6, 9)
def find_more(l):
    event_list = []
    for i in range(len(l)-1):
        b = i + 1
        if l[i] < l[b]:
            event_list.append(l[b])
    return event_list
print(find_more(l))
