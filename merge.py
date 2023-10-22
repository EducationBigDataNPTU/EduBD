for i in range(1,6):
    f=open("這裡放檔案路徑/edu_bigdata_imp"+str(i)+".csv",encoding="big5")
    temp=f.readlines()
    if i==1:
        data=temp
    else:
        for j in range(1,len(temp)):
            tempstring=temp[j]
            tempstring=tempstring.replace('""',"暫")
            tempstring=tempstring.replace('"',"")
            tempstring=tempstring.replace("暫",'""')
            templist=tempstring.split(",")
            templist[0]=str(int(templist[0])+(287137)*(i-1))
            tempstring=",".join(templist)
            data.append(tempstring)
    f.close()
f2=open("./輸出檔案.csv",mode="w")
f2.writelines(data)
f2.close()
print(data[int(input("請輸入查詢筆數:"))])
