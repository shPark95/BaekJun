def matrix_chain(p):
    n = len(p) - 1
    m=[[0]*n for _ in range(n)]
    s=[[0]*n for _ in range(n)]

    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            m[i][j]=float('inf')
            for k in range(i,j):
                q= m[i][k]+m[k+1][j]+p[i]*p[k+1]*p[j+1]

                if q<m[i][j]:
                    m[i][j]=q
                    s[i][j]=k


    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            m[i][j]= float('inf')
            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]

                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

arr= [10,10,20,50,40]

matrix_chain(arr)

