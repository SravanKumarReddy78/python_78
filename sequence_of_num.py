def seq_of_num(st,end,up):
    out=[]
    while st<end:
        out+=[st]
        st+=up
    print(out)
seq_of_num(1,10,2)