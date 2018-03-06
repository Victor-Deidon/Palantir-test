input = ['Alice;START','Bob;START','Bob;1','Carson;START','Alice;15','Carson;6','David;START','David;24','Evil;START','Evil;4','Alice;START','Bob;START','Bob;1','Carson;START','Alice;15','Carson;6','David;START','David;24','Evil;START','Evil;4'];
start = [];
for i in range(0, len(input)):
    if 'START' in input[i] :
        a,b = input[i].split(";");      ##start[[name,nb of line],[]]
        start.append([a,i+1]);
    else :        
        a,b = input[i].split(";");
        for k in range(0, len(start)):
            if start[k][0] == a :         
                c = b.count(',');
                start[k].append(c+1);   ##start[[name,nb of line start,nb of work completed,[work id,(work id)],line nb end of work],[]]
                start[k].append(b.split(','));
                start[k].append(i+1);
        
        
            
        

        

for e in range(0, len(start)):

    print(start[e]);
    print('\n');

##for f in range(len(start)):
##    for g in range (len(start)-f-1):        
##        if start[f][4]  < start[g][1] and start[f][3][0]  > start[g][3][0]:
##            print (start[f][4],';',start[f][0],';','SHORTENED_JOB');
