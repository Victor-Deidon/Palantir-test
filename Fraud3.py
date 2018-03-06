#input = ['Alice;START','Bob;START','Bob;1','Carson;START','Alice;15','Carson;6','David;START','David;24','Evil;START','Evil;START','Evil;4,5'];
datafeed = ['Alice;START','Bob;START','Bob;1','Carson;START','Alice;15','Carson;6','David;START','David;24','Evil;START','Evil;4'];
#input = ['Nick;START','Jeremy;START','Leah;START','Nick;10','Jeremy;START','Jeremy;START','Leah;15','Jeremy;8,14,9'];
start = [];
for i in range(0, len(datafeed)):
    if 'START' in datafeed[i] :
        a,b = datafeed[i].split(";");      ##start[[name,nb of line],[]]
        start.append([a,i+1]);
    else :        
        a,b = datafeed[i].split(";");
        k =len(start);
        c = b.count(',');
        while k > 0:
            k = k-1;
            if start[k][0] == a :         
##                start[k].append(c+1);   ##start[[name,nb of line start,[work id],line nb end of work],[]]
                start[k].append(b.split(','));

                start[k].append(i+1);
                if c == 0 :
                    break 
                c=c-1;


for l in range (len(start)):
    for m in range (len(start[l][2])):
        start[l][2][m]=int(start[l][2][m]);
            


print(start);


resultats = []

for f in range(len(start)):
    for g in range (len(start)):      
        if start[g][3] != start[f][3] : #on ne compare pas les memes evenements
            #for t in range (len(start[f][2])):
             #       for y in range (len(start[g][2])):
              #          if start[f][2][t]  < start[g][2][y] and start[f][1] > start[g][3] : 
               #             print (start[f][1],';',start[f][0],';','SHORTENED_JOB');
                #        break;
                        
            nbIdInf = 0;#nb id de f inférieur à l'id de g
            nbStartAvant = 0;#nb de start pour f avant la fin de g
            for t in range (len(start[f][2])):
                if start[f][2][t] < start[g][2][0]:
                   nbIdInf += 1;
            for h in range(len(start)):
                if start[h][3] == start[f][3] and start[h][1] < start[g][3] :
                    nbStartAvant += 1;
            if(nbStartAvant < nbIdInf):
                
                
                if(nbIdInf == len(start[f][2])):
                    for h2 in range(len(start)):
                        if start[h2][3] == start[f][3]:

                            cptR = 0;
                            for res in range(len(resultats)):
                                if(resultats[res][0]!=start[h2][1]):
                                    cptR += 1;
                            if(cptR == len(resultats)):
                                resultats.append([start[h2][1],start[h2][0],'SHORTENED_JOB']);
                else:
                    cptR = 0;
                    for res2 in range(len(resultats)):
                        if(resultats[res2][0]!=start[f][3]):
                            cptR += 1;
                    if(cptR == len(resultats)):
                        resultats.append([start[f][3],start[f][0],'SUSPICIOUS_BATCH']);
                   
for j in range (len(resultats)):
    h = [str(resultats[j][0]),';',str(resultats[j][1]),';',str(resultats[j][2])];
    p = ''.join(h);
    return (p);
           # Pour shortened jobs
           #     if start[f][2][0]  < start[g][2][0] and start[f][1] > start[g][3] : 
            #        print (start[f][1],';',start[f][0],';','SHORTENED_JOB');
           #         break;
           # 