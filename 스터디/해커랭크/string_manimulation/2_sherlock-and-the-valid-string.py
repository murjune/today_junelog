def isValid(s):
    d1 = [0]*26 ;
    d2 = defaultdict(int);
    for c in s:
        d1[ord(c) - 97] += 1 ;

    for i in range(26):
        if d1[i]:
            d2[d1[i]]+=1;

    n = len(d2);

    if n == 1: return "YES"
    elif n == 2:
        st = []
        for i in d2:
            st.append((i,d2[i]));
        st.sort()
        if st[1][0]-st[0][0] == 1 and st[1][1] == 1:
            return "YES"
        elif st[0] == (1,1): return "YES"
        else: return "NO"
            
    else:
        return "NO"
