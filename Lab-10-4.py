#Lab_10-4

def indexed_names(list):
    list2=[]
    for i, v in enumerate(list):
        list2[i]=v.list()
        print(list2)

#TEST CASES
indexed_names(['max','will','zaza'])
indexed_names(['MAX','WILL','ZAZA'])
