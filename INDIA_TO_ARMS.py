import mysql.connector                                                             
import os                                                                       
mydb=mysql.connector.connect(host="localhost",user="root",passwd="2002")
cursor=mydb.cursor()

#Empty lists which would help for iteration in updation and deletion
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]


#function to create database   d
def crdatab():
    try:
        cursor.execute("Create database Indian_Defence_System")
        print("\nDatabase Has Been Created")
    except:
        print("\nDatabase Already Exists")
        cursor.execute("use Indian_Defence_System")

    
#function to create tables   d
def crtableb():
    try:
        cursor.execute("use Indian_Defence_System")
        cursor.execute("Create table BALLISTIC_MISSILES( SNo int(9) primary Key,NAME varchar(100),TYPE varchar(100),NUMBERS_in_TELs int(9), ORIGIN varchar(100), MIN_RANGE int(90),MAX_RANGE int(90),STATUS varchar(100))")
        cursor.execute("Create table AIRCRAFTS( SNo int(9) primary Key,AIRCRAFTS varchar(100), ORIGIN varchar(100), ROLE varchar(100),VERSION varchar(100), NUMBERS int(9), STATUS varchar(100))")
        cursor.execute("Create table MARINE_DEFENCE_SYSTEM( SNo int(9) primary Key,CLASS varchar(100),TYPE varchar(100),SHIPS varchar(100), ORIGIN varchar(100), DISPLACEMENT_in_Tonnes int(9),STATUS varchar(100))")
        cursor.execute("Create table ARTILLERY( SNo int(9) primary Key,NAME varchar(100),TYPE varchar(100),QUANTITY int(9), ORIGIN varchar(100),STATUS varchar(100))")
        cursor.execute("Create table INFANTRY_WEAPONS( SNo int(9) primary Key,NAME varchar(100),TYPE varchar(100),CALIBER_in_mm int(9), ORIGIN varchar(100),STATUS varchar(100))")
        cursor.execute("Create table POINTS_TABLE(NAME varchar(100) primary Key, SCORE int(9),REMARKS varchar(100))")
        mydb.commit()
        print("\nTables are ready for use!!!")
    except:
        print("\nTables are already existing")
        cursor.execute("use Indian_Defence_System")

        
#fuction to insert records into table BALLISTIC_MISSILES   d
def insertrec1():
    cursor.execute("use Indian_Defence_System")
    n=eval(input("Enter how many records you want to input:"))

    #
    global sno1
    global bname
    global type1
    global ori1
    global Mirange
    global Maxrange
    global Sta1
    #
    
    for i in range(0,n):
        sno1=eval(input("Enter the Sno:"))
        bname=input("Enter the Name of Missile:")
        type1=input("Enter the Type of Missile:")
        num1=eval(input("Enter the Number of Missiles (TELs):"))
        ori1=input("Enter the Name of Origin:")
        Mirange=eval(input("Enter Min Range of Missile (TELs):"))
        Maxrange=eval(input("Enter Max Range of Missile (TELs):"))
        Sta1=input("Enter the Status of Missile (In Service/ Phased out/Ordered):")
        sql1="insert into BALLISTIC_MISSILES(SNo, NAME, TYPE, NUMBERS_in_TELs, ORIGIN, MIN_RANGE, MAX_RANGE, STATUS) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql1,(sno1,bname,type1,num1,ori1,Mirange,Maxrange,Sta1))
        print("\nData has been stored!!\n")
        sql="select * from BALLISTIC_MISSILES"
        cursor.execute(sql)
        result=cursor.fetchall()
        from tabulate import tabulate
        print(tabulate(result,headers=['SNo','NAME','TYPE','NUMBERS_in_TELs','ORIGIN','MIN_RANGE','MAX_RANGE','STATUS'],tablefmt='psql'))
        mydb.commit()
        l1.append(sno1)
        l1.append(bname)
        l1.append(type1)
        l1.append(num1)
        l1.append(ori1)
        l1.append(Mirange)
        l1.append(Maxrange)
        l1.append(Sta1)
        

        
#fuction to insert records into table AIRCRAFTS
def insertrec2():
    cursor.execute("use Indian_Defence_System")
    n=eval(input("Enter how many records you want to input:"))
    
    global sno2
    global aname
    global ori2
    global role1
    global ver1
    global Sta2
    for i in range(0,n):
        sno2=eval(input("Enter the Sno:"))
        aname=input("Enter the Name of Aircraft:")
        ori2=input("Enter the Name of Country of Origin:")
        role1=input("Enter the Role of Aircraft:")
        ver1=input("Enter the Version of Aircraft:")
        num2=eval(input("Enter the Number of Aircrafts:"))
        Sta2=input("Enter the Status of Aircrafts (In Service/ Phased out/Ordered):")
        sql2="insert into AIRCRAFTS(SNo, AIRCRAFTS,ORIGIN, ROLE, VERSION, NUMBERS, STATUS) values(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql2,(sno2,aname,ori2,role1,ver1,num2,Sta2))
        print("\nData has been stored!!\n")
        sql="select * from AIRCRAFTS"
        cursor.execute(sql)
        result=cursor.fetchall()
        from tabulate import tabulate
        print(tabulate(result,headers=['SNo','AIRCRAFTS','ORIGIN','ROLE','VERSION','NUMBERS','STATUS'],tablefmt='psql'))
        mydb.commit()
        l2.append(sno2)
        l2.append(aname)
        l2.append(num2)
        l2.append(ori2)
        l2.append(role1)
        l2.append(ver1)
        l2.append(Sta2)

        
#fuction to insert records into table MARINE_DEFENCE_SYSTEM
def insertrec3():
    cursor.execute("use Indian_Defence_System")
    n=eval(input("Enter how many records you want to input:"))
    global sno3
    global cname
    global ori2
    global type2
    global ship
    global ori3
    global disp
    global sta5
    for i in range(0,n):
        sno3=eval(input("Enter the Sno:"))
        cname=input("Enter the Class of Destroyer or Aircraft Carrier:")
        type2=input("Enter the Type of Destroyer or Aircraft Carrier:")
        Ship=input("Enter the Ships:")
        ori3=input("Enter the Name of Origin:")
        disp=eval(input("Enter The Displacement (Tonnes):"))
        sta5=input("Enter the Status of Destroyer or Aircraft Carrier (In Service/ Phased out/Ordered):")
        sql3="insert into MARINE_DEFENCE_SYSTEM(SNo, CLASS, TYPE, SHIPS, ORIGIN,DISPLACEMENT_in_tonnes,STATUS) values(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql3,(sno3,cname,type2,Ship,ori3,disp,sta5))
        print("\nData has been stored!!\n")
        sql="select * from MARINE_DEFENCE_SYSTEM"
        cursor.execute(sql)
        result=cursor.fetchall()
        from tabulate import tabulate
        print(tabulate(result,headers=['SNo','CLASS','TYPE','SHIPS','ORIGIN','DISPLACEMENT_in_tonnes','STATUS'],tablefmt='psql'))
        mydb.commit()
        l3.append(sno3)
        l3.append(cname)
        l3.append(ori2)
        l3.append(type2)
        l3.append(ship)
        l3.append(ori3)
        l3.append(disp)
        l3.append(sta5)


        
#fuction to insert records into table ARTILLERY
def insertrec4():
    cursor.execute("use Indian_Defence_System")
    n=eval(input("Enter how many records you want to input:"))
    global sno4
    global arname
    global type3
    global quant
    global ori4
    global Sta3
    for i in range(0,n):
        sno4=eval(input("Enter the Sno:"))
        arname=input("Enter the Name of Artillery:")
        type3=input("Enter the Type of Artillery:")
        quant=eval(input("Enter the Quantity of Artillery:"))
        ori4=input("Enter the Name of Origin:")
        Sta3=input("Enter the Status of Artillery (In Service/ Phased out/Ordered):")
        sql4="insert into ARTILLERY(SNo, NAME, TYPE, QUANTITY, ORIGIN, STATUS) values(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql4,(sno4,arname,type3,quant,ori4,Sta3))
        print("\nData has been stored!!\n")
        sql="select * from ARTILLERY"
        cursor.execute(sql)
        result=cursor.fetchall()
        from tabulate import tabulate
        print(tabulate(result,headers=['SNo','NAME','TYPE','QUANTITY','ORIGIN','STATUS'],tablefmt='psql'))
        mydb.commit()
        l4.append(sno4)
        l4.append(arname)
        l4.append(type3)
        l4.append(quant)
        l4.append(ori4)
        l4.append(Sta3)

        
#fuction to insert records into table INFANTRY_WEAPONS
def insertrec5():
    cursor.execute("use Indian_Defence_System")
    n=eval(input("Enter how many records you want to input:"))
    global sno5
    global irname
    global type4
    global cal
    global ori5
    global sta4
    for i in range(0,n):
        sno5=eval(input("Enter the Sno:"))
        irname=input("Enter the Name of Infantry Weapon:")
        type4=input("Enter the Type of Infantry Weapon:")
        cal=eval(input("Enter the Caliber of Infantry Weapon:"))
        ori5=input("Enter the Name of Origin:")
        Sta4=input("Enter the Status of Infantry Weapon(In Service/ Phased out/Ordered):")
        sql5="insert into INFANTRY_WEAPONS(SNo, NAME, TYPE, CALIBER_in_mm, ORIGIN, STATUS) values(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql5,(sno5,irname,type4,cal,ori5,Sta4))
        print("\nData has been stored!!\n")
        sql="select * from INFANTRY_WEAPONS"
        cursor.execute(sql)
        result=cursor.fetchall()
        from tabulate import tabulate
        print(tabulate(result,headers=['SNo','NAME','TYPE','CALIBER_in_mm','ORIGIN','STATUS'],tablefmt='psql'))
        mydb.commit()
        l5.append(sno5)
        l5.append(irname)
        l5.append(type4)
        l5.append(cal)
        l5.append(ori5)
        l5.append(sta4)
        

#function to insert records into tables
def insertrec():
    while True :
        print("In which table you want to input records:")
        print("\n\t\t\t1.BALLISTIC_MISSILES \n\t\t\t2.AIRCRAFTS \n\t\t\t3.MARINE_DEFENCE_SYSTEM \n\t\t\t4.ARTILLERY  \n\t\t\t5.INFANTRY_WEAPONS \n\t\t\t6.ALL TABLES \n\t\t\t7.Back To Main Menu")
        a=eval(input("Enter Your Choice:"))
        if a==1:
            insertrec1()
        elif a==2:
            insertrec2()
        elif a==3:
            insertrec3()
        elif a==4:
            insertrec4()
        elif a==5:
            insertrec5()
        elif a==6:
            print("\nTable 1: BALLISTIC_MISSILES\n")
            insertrec1()
            print("\nTable 2: AIRCRAFTS\n")
            insertrec2()
            print("\nTable 3: MARINE_DEFENCE_SYSTEM\n")
            insertrec3()
            print("\nTable 4: ARTILLERY\n")
            insertrec4()
            print("\nTable 5: INFANTRY_WEAPONS\n")
            insertrec5()
        elif a==7:
            break
        else:
            print("\nInvalid Input")


# function to display table

from tabulate import tabulate 

def ballisticmissiledisplay():
    cursor.execute("use Indian_Defence_System")
    sql="select * from BALLISTIC_MISSILES"
    cursor.execute(sql)
    result=cursor.fetchall()
    l1.append(result)#table values are appended in the list for iteration
    ####
    print("\nBALLISTIC MISSILES AND AUTOMATED WEAPONS")
    print(tabulate(result , headers=['SNo', 'NAME', 'TYPE', 'NUMBERS_in_TELs', 'ORIGIN, MIN_RANGE', 'MAX_RANGE', 'STATUS'], tablefmt='psql'))
    mydb.commit()
                   
def aircraftdisplay():
    cursor.execute("use Indian_Defence_System")
    sql="select * from AIRCRAFTS"
    cursor.execute(sql)
    result1=cursor.fetchall()
    l2.append(result1)
    ####
    print("\nINDIAN AIR FORCE : AIRCRAFTS")
    print(tabulate(result1 , headers=['SNo', 'AIRCRAFTS','ORIGIN', 'ROLE', 'VERSION', 'NUMBERS', 'STATUS'], tablefmt='psql'))
    mydb.commit()
    
def marinedisplay():
    cursor.execute("use Indian_Defence_System")
    sql="select * from MARINE_DEFENCE_SYSTEM"
    cursor.execute(sql)
    result2=cursor.fetchall()
    l3.append(result2)
    print("\nINDIAN NAVAL SHIPS")
    print(tabulate(result2 , headers=['SNo', 'CLASS', 'TYPE', 'SHIPS', 'ORIGIN','DISPLACEMENT_in_tonnes','STATUS'], tablefmt='psql'))
    mydb.commit()
    
def artillerydisplay():
    cursor.execute("use Indian_Defence_System")
    sql="select * from ARTILLERY"
    cursor.execute(sql)
    result3=cursor.fetchall()
    l4.append(result3)
    print("\nARTILLERY GUNS AND HOWITZERS")
    print(tabulate(result3 , headers=['SNo', 'NAME', 'TYPE', 'QUANTITY', 'ORIGIN', 'STATUS'], tablefmt='psql'))
    
    mydb.commit()    
def infantrydisplay():
    cursor.execute("use Indian_Defence_System")
    sql="select * from INFANTRY_WEAPONS"
    cursor.execute(sql)
    result4=cursor.fetchall()
    l5.append(result4)
    print("\nINFANTRY_WEAPONS")
    print(tabulate(result4 , headers=['SNo', 'NAME', 'TYPE', 'CALIBER_in_mm', 'ORIGIN', 'STATUS'], tablefmt='psql'))
    
    mydb.commit()
    
def pointtbdisplay():
    print("\nPOINTS TABLE")
    show_points()  
 




#Function To View Tables
def viewtable():
    print("\nWhich table you want to See:")
    print("\n\t\t\t1.BALLISTIC_MISSILES \n\t\t\t2.AIRCRAFTS \n\t\t\t3.MARINE_DEFENCE_SYSTEM \n\t\t\t4.ARTILLERY  \n\t\t\t5.INFANTRY_WEAPONS  \n\t\t\t6.POINTS_TABLE\n\t\t\t7.ALL TABLES")
    a=eval(input("Enter Your Choice:"))
    if a==1:
        ballisticmissiledisplay()
    elif a==2:
        aircraftdisplay()
    elif a==3:
        marinedisplay()
    elif a==4:
        artillerydisplay()
    elif a==5:
        infantrydisplay()
    elif a==6:
        pointtbdisplay()
    elif a==7:
        ballisticmissiledisplay()
        aircraftdisplay()
        marinedisplay()
        artillerydisplay()
        infantrydisplay()
        pointtbdisplay()
    else:
        print("\nInvalid Input")
    
# function to update table 

def update_BALLISTIC_MISSILES():
    ballisticmissiledisplay()
    cursor.execute("use Indian_Defence_System")
    column=int(input("Choose the column to be updated \nenter \n1 for NUMBERS_in_TELs \n2 for MAX_RANGE \n3 for MIN_RANGE \n>"))
    namu=input("Enter name of missile for the entity you want change in (ENTER NAME AMONG THE CONTENTS OF TABLE ONLY):")
    op=eval(input("enter \n1 TO ADD A VALUE \n2 TO MULTIPLY A VALUE \n3 TO DIVIDE A VALUE \n4 TO SUBTRACT A VALUE\n>"))
    if op==1:
        vfop=eval(input("Enter the value to be added::"))
    elif op==2:
        vfop=eval(input("Enter the value to be multiplied::"))
    elif op==3:
        vfop=eval(input("Enter the value to be divided::"))
    elif op==4:
        vfop=eval(input("Enter the value to be subtracted::"))
    invalid=0 #Loop for iteration and checking validity of inputs
    for i in l1:
        for j in i:
            if namu in j:
                invalid=0
            if namu not in j:
                invalid=invalid+1
    print("False value(s) which (has/have) been input :",namu)    
    print("No of wrong inputs:",invalid)
    if invalid>0:
        print("Invalid Input !!!")
    elif invalid==0:    
        if op==1 and column==1:
            sqlubn="UPDATE BALLISTIC_MISSILES SET NUMBERS_in_TELs = NUMBERS_in_TELs + %s WHERE NAME= %s"
            cursor.execute(sqlubn,(vfop,namu,))
            xb=cursor.fetchall()
            for i in xb:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            ballisticmissiledisplay()
        elif op==2 and column==1:
            sqlubn="UPDATE BALLISTIC_MISSILES SET NUMBERS_in_TELs = NUMBERS_in_TELs * %s WHERE NAME= %s"
            cursor.execute(sqlubn,(vfop,namu,))
            xb=cursor.fetchall()
            for i in xb:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            ballisticmissiledisplay()
        elif op==3 and column==1:
            sqlubn="UPDATE BALLISTIC_MISSILES SET NUMBERS_in_TELs = NUMBERS_in_TELs / %s WHERE NAME= %s"
            cursor.execute(sqlubn,(vfop,namu,))
            xb=cursor.fetchall()
            for i in xb:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            ballisticmissiledisplay()
        elif op==4 and column==1:
            sqlubn="UPDATE BALLISTIC_MISSILES SET NUMBERS_in_TELs = NUMBERS_in_TELs - %s WHERE NAME= %s"
            cursor.execute(sqlubn,(vfop,namu,))
            xb=cursor.fetchall()
            for i in xb:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            ballisticmissiledisplay()
        elif op==1 and column==2:   #############################
            sqlubn="UPDATE BALLISTIC_MISSILES SET MAX_RANGE = MAX_RANGE + %s WHERE NAME= %s"
            cursor.execute(sqlubn,(vfop,namu,))
            xb=cursor.fetchall()
            for i in xb:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            ballisticmissiledisplay()
        elif op==2 and column==2:
            sqlubn="UPDATE BALLISTIC_MISSILES SET MAX_RANGE = MAX_RANGE * %s WHERE NAME= %s"
            cursor.execute(sqlubn,(vfop,namu,))
            xb=cursor.fetchall()
            for i in xb:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            ballisticmissiledisplay()
        elif op==3 and column==2:
            sqlubn="UPDATE BALLISTIC_MISSILES SET MAX_RANGE = MAX_RANGE / %s WHERE NAME= %s"
            cursor.execute(sqlubn,(vfop,namu,))
            xb=cursor.fetchall()
            for i in xb:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            ballisticmissiledisplay()
        elif op==4 and column==2:
            sqlubn="UPDATE BALLISTIC_MISSILES SET MAX_RANGE = MAX_RANGE - %s WHERE NAME= %s"
            cursor.execute(sqlubn,(vfop,namu,))
            xb=cursor.fetchall()
            for i in xb:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            ballisticmissiledisplay()
        elif op==1 and column==3:   #############################
            sqlubn="UPDATE BALLISTIC_MISSILES SET MIN_RANGE = MIN_RANGE + %s WHERE NAME= %s"
            cursor.execute(sqlubn,(vfop,namu,))
            xb=cursor.fetchall()
            for i in xb:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            ballisticmissiledisplay()
        elif op==2 and column==3:
            sqlubn="UPDATE BALLISTIC_MISSILES SET MIN_RANGE = MIN_RANGE * %s WHERE NAME= %s"
            cursor.execute(sqlubn,(vfop,namu,))
            xb=cursor.fetchall()
            for i in xb:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            ballisticmissiledisplay()
        elif op==3 and column==3:
            sqlubn="UPDATE BALLISTIC_MISSILES SET MIN_RANGE = MIN_RANGE / %s WHERE NAME= %s"
            cursor.execute(sqlubn,(vfop,namu,))
            xb=cursor.fetchall()
            for i in xb:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            ballisticmissiledisplay()
        elif op==4 and column==3:
            sqlubn="UPDATE BALLISTIC_MISSILES SET MIN_RANGE = MIN_RANGE - %s WHERE NAME= %s"
            cursor.execute(sqlubn,(vfop,namu,))
            xb=cursor.fetchall()
            for i in xb:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            ballisticmissiledisplay()
        else:
            print("INVALID INPUT HAS BEEN DETECTED!! PLEASE TRY AGAIN.")
            update_BALLISTIC_MISSILES()
    
    
    
def update_AIRCRAFTS():
    cursor.execute("use Indian_Defence_System")
    aircraftdisplay()
    print("Updating column for NUMBERS BUILT")
    namu1=input("Enter name of AIRCRAFTS (ENTER NAME AMONG THE CONTENTS OF TABLE ONLY):")
    op1=eval(input("enter \n1 TO ADD A VALUE \n2 TO MULTIPLY A VALUE \n3 TO DIVIDE A VALUE \n4 TO SUBTRACT A VALUE\n>"))
    if op1==1:
        vfop1=eval(input("Enter the value to be added::"))
    elif op1==2:
        vfop1=eval(input("Enter the value to be multiplied::"))
    elif op1==3:
        vfop1=eval(input("Enter the value to be divided::"))
    elif op1==4:
        vfop1=eval(input("Enter the value to be subtracted::"))
        
    '''
    invalid1=0 #Loop for iteration and checking validity of inputs
    for i in l2:
        for j in i:
            if namu1 in j:
                invalid1=0
            else:
                invalid1=invalid1+1
                break
    print("False value(s) which (has/have) been input :",namu1)    
    print("No of wrong inputs:",invalid1)
    if invalid1>0:
        print("Invalid Input !!!")
    elif invalid1==0:    
    '''
    if op1==1:
        sqlubn1="UPDATE AIRCRAFTS SET NUMBERS = NUMBERS + %s WHERE AIRCRAFTS= %s"
        cursor.execute(sqlubn1,(vfop1,namu1,))
        xair=cursor.fetchall()
        for i in xair:
            print(i)
        mydb.commit()
        print("column has been updated !!")
        aircraftdisplay()
    elif op1==2:
        sqlubn1="UPDATE AIRCRAFTS SET NUMBERS = NUMBERS * %s WHERE AIRCRAFTS= %s"
        cursor.execute(sqlubn1,(vfop1,namu1,))
        xair=cursor.fetchall()
        for i in xair:
            print(i)
        mydb.commit()
        print("column has been updated !!")
        aircraftdisplay()
    elif op1==3:
        sqlubn1="UPDATE AIRCRAFTS SET NUMBERS = NUMBERS / %s WHERE AIRCRAFTS= %s"
        cursor.execute(sqlubn1,(vfop1,namu1,))
        xair=cursor.fetchall()
        for i in xair:
            print(i)
        mydb.commit()
        print("column has been updated !!")
        aircraftdisplay()
    elif op1==4:
        sqlubn1="UPDATE AIRCRAFTS SET NUMBERS = NUMBERS - %s WHERE AIRCRAFTS= %s"
        cursor.execute(sqlubn1,(vfop1,namu1,))
        xair=cursor.fetchall()
        for i in xair:
            print(i)
        mydb.commit()
        print("column has been updated !!")
        aircraftdisplay()
    else:
        print("INVALID INPUT HAS BEEN DETECTED!! PLEASE TRY AGAIN.")
        update_AIRCRAFTS()
        


def update_MARINE_DEFENCE_SYSTEM():
    cursor.execute("use Indian_Defence_System")
    marinedisplay()
    namu2=input("Enter name of INS (ENTER NAME AMONG THE CONTENTS OF TABLE ONLY):")
    print("Updating column for DISPLACEMENT OF MARINE CRAFT") 
    op2=eval(input("enter \n1 TO ADD A VALUE \n2 TO MULTIPLY A VALUE \n3 TO DIVIDE A VALUE \n4 TO SUBTRACT A VALUE\n>"))
    if op2==1:
        vfop2=eval(input("Enter the value to be added::"))
    elif op2==2:
        vfop2=eval(input("Enter the value to be multiplied::"))
    elif op2==3:
        vfop2=eval(input("Enter the value to be divided::"))
    elif op2==4:
        vfop2=eval(input("Enter the value to be subtracted::"))
        vfop=eval(input("Enter the value to be subtracted::"))
    invalid2=0 #Loop for iteration and checking validity of inputs
    for i in l3:
        for j in i:
            if namu2 in j:
                invalid2=0
            if namu2 not in j:
                invalid2=invalid2+1
    print("False value(s) which (has/have) been input :",namu2)    
    print("No of wrong inputs:",invalid2)
    if invalid2>0:
        print("Invalid Input !!!")    
    elif invalid2==0:    
        if op2==1:
            sqlubn2="UPDATE MARINE_DEFENCE_SYSTEM SET DISPLACEMENT_in_Tonnes = DISPLACEMENT_in_Tonnes + %s WHERE SHIPS= %s"
            cursor.execute(sqlubn2,(vfop2,namu2,))
            xm=cursor.fetchall()
            for i in xm:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            marinedisplay()
        elif op2==2:
            sqlubn2="UPDATE MARINE_DEFENCE_SYSTEM SET DISPLACEMENT_in_Tonnes = DISPLACEMENT_in_Tonnes * %s WHERE SHIPS= %s"
            cursor.execute(sqlubn2,(vfop2,namu2,))
            xm=cursor.fetchall()
            for i in xm:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            marinedisplay()
        elif op2==3:
            sqlubn2="UPDATE MARINE_DEFENCE_SYSTEM SET DISPLACEMENT_in_Tonnes = DISPLACEMENT_in_Tonnes / %s WHERE SHIPS= %s"
            cursor.execute(sqlubn2,(vfop2,namu2,))
            xm=cursor.fetchall()
            for i in xm:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            marinedisplay()
        elif op2==4:
            sqlubn2="UPDATE MARINE_DEFENCE_SYSTEM SET DISPLACEMENT_in_Tonnes = DISPLACEMENT_in_Tonnes - %s WHERE SHIPS= %s"
            cursor.execute(sqlubn2,(vfop2,namu2,))
            xm=cursor.fetchall()
            for i in xm:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            marinedisplay()
        else:
            print("INVALID INPUT HAS BEEN DETECTED!! PLEASE TRY AGAIN.")
            update_MARINE_DEFENCE_SYSTEM()


def update_ARTILLERY():
    cursor.execute("use Indian_Defence_System")
    artillerydisplay()
    namu3=input("Enter name of ARTILLERY PIECE (ENTER NAME AMONG THE CONTENTS OF TABLE ONLY):")
    print("Updating column for QUANTITY")
    op3=eval(input("enter \n1 TO ADD A VALUE \n2 TO MULTIPLY A VALUE \n3 TO DIVIDE A VALUE \n4 TO SUBTRACT A VALUE\n>"))
    if op3==1:
        vfop3=eval(input("Enter the value to be added::"))
    elif op3==2:
        vfop3=eval(input("Enter the value to be multiplied::"))
    elif op3==3:
        vfop3=eval(input("Enter the value to be divided::"))
    elif op3==4:
        vfop3=eval(input("Enter the value to be subtracted::"))
    invalid3=0 #Loop for iteration and checking validity of inputs
    for i in l4:
        for j in i:
            if namu3 in j:
                invalid3=0
            if namu3 not in j:
                invalid3=invalid3+1
    print("False value(s) which (has/have) been input :",namu3)    
    print("No of wrong inputs:",invalid3)
    if invalid3>0:
        print("Invalid Input !!!")
    elif invalid3==0:    
        if op3==1:
            sqlubn3="UPDATE ARTILLERY SET QUANTITY = QUANTITY + %s WHERE NAME= %s"
            cursor.execute(sqlubn3,(vfop3,namu3,))
            xar=cursor.fetchall()
            for i in xar:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            artillerydisplay()
        elif op3==2:
            sqlubn3="UPDATE ARTILLERY SET QUANTITY = QUANTITY * %s WHERE NAME= %s"
            cursor.execute(sqlubn3,(vfop3,namu3,))
            xar=cursor.fetchall()
            for i in xar:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            artillerydisplay()
        elif op3==3:
            sqlubn3="UPDATE ARTILLERY SET QUANTITY = QUANTITY / %s WHERE NAME= %s"
            cursor.execute(sqlubn3,(vfop3,namu3,))
            xar=cursor.fetchall()
            for i in xar:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            artillerydisplay()
        elif op3==4:
            sqlubn3="UPDATE ARTILLERY SET QUANTITY = QUANTITY - %s WHERE NAME= %s"
            cursor.execute(sqlubn3,(vfop3,namu3,))
            xar=cursor.fetchall()
            for i in xar:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            artillerydisplay()
        else:
            print("INVALID INPUT HAS BEEN DETECTED!! PLEASE TRY AGAIN.")
            update_ARTILLERY()
    
    

def update_INFANTRY_WEAPONS():
    cursor.execute("use Indian_Defence_System")
    infantrydisplay()
    namu4=input("Enter name of INFANTRY WEAPON (ENTER NAME AMONG THE CONTENTS OF TABLE ONLY):")
    print("Updating column for CALIBER of arms")
    op4=eval(input("enter \n1 TO ADD A VALUE \n2 TO MULTIPLY A VALUE \n3 TO DIVIDE A VALUE \n4 TO SUBTRACT A VALUE\n>"))
    if op4==1:
        vfop4=eval(input("Enter the value to be added::"))
    elif op4==2:
        vfop4=eval(input("Enter the value to be multiplied::"))
    elif op4==3:
        vfop4=eval(input("Enter the value to be divided::"))
    elif op4==4:
        vfop4=eval(input("Enter the value to be subtracted::"))
    invalid4=0 #Loop for iteration and checking validity of inputs
    invalid3=0 #Loop for iteration and checking validity of inputs
    for i in l5:
        for j in i:
            if namu4 in j:
                invalid4=0
            if namu4 not in j:
                invalid4=invalid4+1
    print("False value(s) which (has/have) been input :",namu3)    
    print("No of wrong inputs:",invalid3)
    if invalid4>0:
        print("Invalid Input !!!")
    elif invalid4==0:    
        if op4==1:
            sqlubn4="UPDATE INFANTRY_WEAPONS SET CALIBER_in_mm = CALIBER_in_mm + %s WHERE NAME= %s"
            cursor.execute(sqlubn4,(vfop4,namu4,))
            xiw=cursor.fetchall()
            for i in xiw:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            infantrydisplay()
        elif op4==2:
            sqlubn4="UPDATE INFANTRY_WEAPONS SET CALIBER_in_mm = CALIBER_in_mm * %s WHERE NAME= %s"
            cursor.execute(sqlubn4,(vfop4,namu4,))
            xiw=cursor.fetchall()
            for i in xiw:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            infantrydisplay()
        elif op4==3:
            sqlubn4="UPDATE INFANTRY_WEAPONS SET CALIBER_in_mm = CALIBER_in_mm / %s WHERE NAME= %s"
            cursor.execute(sqlubn4,(vfop4,namu4,))
            xiw=cursor.fetchall()
            for i in xiw:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            infantrydisplay()
        elif op4==4:
            sqlubn4="UPDATE INFANTRY_WEAPONS SET CALIBER_in_mm = CALIBER_in_mm - %s WHERE NAME= %s"
            cursor.execute(sqlubn4,(vfop4,namu4,))
            xiw=cursor.fetchall()
            for i in xiw:
                print(i)
            mydb.commit()
            print("column has been updated !!")
            infantrydisplay()
        else:
            print("INVALID INPUT HAS BEEN DETECTED!! PLEASE TRY AGAIN.")
            update_INFANTRY_WEAPONS()
    
    
# CALLING THE UPDATE TABLE

def updatetable():
    wttu=eval(input("\nEnter number indicated before the table you want to update \n\t\t\t1.BALLISTIC_MISSILE  \n\t\t\t2.AIRCRAFTS  \n\t\t\t3.ARTILLERY  \n\t\t\t4.MARINE_DEFENCE_SYSTEM \n\t\t\t5.INFANTRY_WEAOPONS \n>"))
    if wttu==1:
        update_BALLISTIC_MISSILES()
    elif wttu==2:
        update_AIRCRAFTS()
    elif wttu==3:
        update_ARTILLERY()
    elif wttu==4:
        update_MARINE_DEFENCE_SYSTEM()
    elif wttu==5:
        update_INFANTRY_WEAPONS()
    else:
        print("Please Try Again")
        updatetable()
    mydb.commit()

#FUNCTION TO DELETE A TABLE
    
def delete_ballistic_missiles():
    cursor.execute("use Indian_Defence_System")
    ballisticmissiledisplay()
    pdel=eval(input("enter the code indicated against each column to specify parameter for deleting entities from table \n1.SNO \n2.NAME OF MISSILE \n3.TYPE OF MISSILE \n4.NUMBER OF MISSILES \n5.ORIGIN COUNTRY \n6.MINIMUM RANGE OF MISSILE \n7.MAXIMUM RANGE OF MISSILE \n8.STATUS OF MISSILE( IN SERVICE , PHASED OUT , ORDERED) \n>"))
    no=0
    if pdel==1:
        parv=eval(input("enter value of SNO(ENTER SNO VALUE AMONG THE ABOVE TABLE CONTENTS ONLY):"))
        for i in l1:
            for j in i:
                count=len(i)
                if parv not in j:#To check validity of input
                    no=no+1
                    if no==count:
                        print("Invalid Input!!!\n")
                        break
                if parv in j:
                    sqldel="DELETE FROM BALLISTIC_MISSILES WHERE SNo = %s"
                    cursor.execute(sqldel,(parv,))
                    xdb=cursor.fetchall()
                    for i in xdb:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")    
    elif pdel==2:
        parv=input("enter NAME OF MISSILE (ENTER NAME AMONG THE ABOVE TABLE CONTENTS ONLY):")
        for i in l1:
            for j in i:
                count=len(i)
                if parv not in j:#To check validity of input
                    no=no+1
                    if no==count:
                        print("Invalid Input!!!\n")
                        break
                if parv in j:
                    sqldel="DELETE FROM BALLISTIC_MISSILES WHERE NAME = %s"
                    cursor.execute(sqldel,(parv,))
                    xdb=cursor.fetchall()
                    for i in xdb:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif pdel==3:
        parv=input("enter TYPE OF MISSILE (ENTER TYPE FROM ABOVE TABLE CONTENTS ONLY):")
        for i in l1:
            for j in i:
                count=len(i)
                if parv not in j:#To check validity of input
                    no=no+1
                    if no==count:
                        print("Invalid Input!!!\n")
                        break
                if parv in j:
                    sqldel="DELETE FROM BALLISTIC_MISSILES WHERE TYPE = %s"
                    cursor.execute(sqldel,(parv,))
                    xdb=cursor.fetchall()
                    for i in xdb:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif pdel==4:
        parv=eval(input("enter NUMBER OF MISSILES (ENTER VALUE FROM THE ABOVE TABLE CONTENTS ONLY):"))
        for i in l1:
            for j in i:
                count=len(i)
                if parv not in j:#To check validity of input
                    no=no+1
                    if no==count:
                        print("Invalid Input!!!\n")
                        break
                if parv in j:
                    sqldel="DELETE FROM BALLISTIC_MISSILES WHERE NUMBERS_in_TELs = %s"
                    cursor.execute(sqldel,(parv,))
                    xdb=cursor.fetchall()
                    for i in xdb:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif pdel==5:
        parv=input("enter ORIGIN COUNTRY (ENTER ORIGIN FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l1:
            for j in i:
                count=len(i)
                if parv not in j:#To check validity of input
                    no=no+1
                    if no==count:
                        print("Invalid Input!!!\n")
                        break
                if parv in j:
                    sqldel="DELETE FROM BALLISTIC_MISSILES WHERE ORIGIN = %s"
                    cursor.execute(sqldel,(parv,))
                    xdb=cursor.fetchall()
                    for i in xdb:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif pdel==6:
        parv=eval(input("enter MINIMUM RANGE OF MISSILE (ENTER VALUE FROM THE ABOVE TABLE CONTENTS ONLY):"))
        for i in l1:
            for j in i:
                count=len(i)
                if parv not in j:#To check validity of input
                    no=no+1
                    if no==count:
                        print("Invalid Input!!!\n")
                        break
                if parv in j:    
                    sqldel="DELETE FROM BALLISTIC_MISSILES WHERE MIN_RANGE = %s"
                    cursor.execute(sqldel,(parv,))
                    xdb=cursor.fetchall()
                    for i in xdb:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif pdel==7:
        parv=eval(input("enter MAXIMUM RANGE OF MISSILE (ENTER VALUE FROM THE ABOVE TABLE CONTENTS ONLY):"))
        for i in l1:
            for j in i:
                count=len(i)
                if parv not in j:#To check validity of input
                    no=no+1
                    if no==count:
                        print("Invalid Input!!!\n")
                        break
                if parv in j:
                    sqldel="DELETE FROM BALLISTIC_MISSILES WHERE MAX_RANGE = %s"
                    cursor.execute(sqldel,(parv,))
                    xdb=cursor.fetchall()
                    for i in xdb:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif pdel==8:
        parv=input("enter STATUS OF MISSILE (ENTER STATUS FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l1:
            for j in i:
                count=len(i)
                if parv not in j:#To check validity of input
                    no=no+1
                    if no==count:
                        print("Invalid Input!!!\n")
                        break
                if parv in j:    
                    sqldel="DELETE FROM BALLISTIC_MISSILES WHERE STATUS = %s"
                    cursor.execute(sqldel,(parv,))
                    xdb=cursor.fetchall()
                    for i in xdb:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    else:
        print("please try again")
        delete_ballistic_missiles()
    ballisticmissiledisplay()

##############################################################

def delete_AIRCRAFTS():
    cursor.execute("use Indian_Defence_System")
    aircraftdisplay()
    print(l2)
    adel=eval(input("enter the code indicated against each column to specify parameter for deleting entities from table \n1.SNO \n2.NAME OF AIRCRAFT \n3.ORIGIN OF AIRCRAFT \n4.ROLE OF AIRCRAFT \n5.VERSION OF AIRCRAFT \n6.NUMBER OF AIRCRAFT \n7.STATUS OF AIRCRAFT( IN SERVICE , PHASED OUT , ORDERED) \n> "))
    no1=0
    if adel==1:
        aarv=eval(input("enter value of SNO (ENTER VALUE FROM THE ABOVE TABLE CONTENTS ONLY):"))
        for i in l2:
            for j in i:
                count=len(i)
                if aarv not in j:#To check validity of input
                    no1=no1+1
                    if no1==count:
                        print("Invalid Input!!!\n")
                        break
                if aarv in j:
                    sqldel2="DELETE FROM AIRCRAFTS WHERE SNo = %s"
                    cursor.execute(sqldel2,(aarv,))
                    x1=cursor.fetchall()
                    for i in x1:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif adel==2:
        aarv=input("enter NAME OF AIRCRAFT (ENTER NAME FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l2:
            for j in i:
                count=len(i)
                if aarv not in j:#To check validity of input
                    no1=no1+1
                    if no1==count:
                        print("Invalid Input!!!\n")
                        break
                if aarv in j:            
                    sqldel2="DELETE FROM AIRCRAFTS WHERE AIRCRAFTS = %s"
                    cursor.execute(sqldel2,(aarv,))
                    x1=cursor.fetchall()
                    for i in x1:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif adel==3:
        aarv=input("enter ORIGIN (ENTER ORIGIN FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l2:
            for j in i:
                count=len(i)
                if aarv not in j:#To check validity of input
                    no1=no1+1
                    if no1==count:
                        print("Invalid Input!!!\n")
                        break
                if aarv in j:
                    sqldel2="DELETE FROM AIRCRAFTS WHERE ORIGIN = %s"
                    cursor.execute(sqldel2,(aarv,))
                    x1=cursor.fetchall()
                    for i in x1:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif adel==4:
        aarv=input("enter ROLE (ENTER ROLE FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l2:
            for j in i:
                count=len(i)
                if aarv not in j:#To check validity of input
                    no1=no1+1
                    if no1==count:
                        print("Invalid Input!!!\n")
                        break
                if aarv in j:
                    sqldel2="DELETE FROM AIRCRAFTS WHERE ROLE = %s"
                    cursor.execute(sqldel2,(aarv,))
                    x1=cursor.fetchall()
                    for i in x1:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif adel==5:
        aarv=input("enter VERSION (ENTER VERSION FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l2:
            for j in i:
                count=len(i)
                if aarv not in j:#To check validity of input
                    no1=no1+1
                    if no1==count:
                        print("Invalid Input!!!\n")
                        break
                if aarv in j:
                    sqldel2="DELETE FROM AIRCRAFTS WHERE VERSION = %s"
                    cursor.execute(sqldel2,(aarv,))
                    x1=cursor.fetchall()
                    for i in x1:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif adel==6:
        aarv=eval(input("enter NUMBERS BUILT (ENTER VALUE FROM THE ABOVE TABLE CONTENTS ONLY):"))
        for i in l2:
            for j in i:
                count=len(i)
                if aarv not in j:#To check validity of input
                    no1=no1+1
                    if no1==count:
                        print("Invalid Input!!!\n")
                        break
                if aarv in j:
                    sqldel2="DELETE FROM AIRCRAFTS WHERE NUMBERS = %s"
                    cursor.execute(sqldel2,(aarv,))
                    x1=cursor.fetchall()
                    for i in x1:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif adel==7:
        aarv=input("enter STATUS (ENTER STATUS FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l2:
            for j in i:
                count=len(i)
                if aarv not in j:#To check validity of input
                    no1=no1+1
                    if no1==count:
                        print("Invalid Input!!!\n")
                        break
                if aarv in j:         
                    sqldel2="DELETE FROM AIRCRAFTS WHERE STATUS = %s"
                    cursor.execute(sqldel2,(aarv,))
                    x1=cursor.fetchall()
                    for i in x1:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    else:
        print("please try again")
        delete_AIRCRAFTS()
    aircraftdisplay()


#######################################################


def delete_ARTILLERY():
    cursor.execute("use Indian_Defence_System")
    artillerydisplay()
    ardel=eval(input("enter the code indicated against each column to specify parameter for deleting entities from table \n1.SNO \n2.NAME OF ARTILLERY \n3.TYPE \n4.QUANTITY \n5.ORIGIN  \n6.STATUS ( IN SERVICE , PHASED OUT , ORDERED) \n>"))
    no3=0
    if ardel==1:
        ararv=eval(input("enter value of SNO (ENTER VALUE FROM THE ABOVE TABLE CONTENTS ONLY):"))
        for i in l4:
            for j in i:
                count=len(i)
                if ararv not in j:#To check validity of input
                    no3=no3+1
                    if no3==count:
                        print("Invalid Input!!!\n")
                        break
                if ararv in j:
                    sqldel3="DELETE FROM ARTILLERY WHERE SNo = %s"
                    cursor.execute(sqldel3,(ararv,))
                    x2=cursor.fetchall()
                    for i in x2:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif ardel==2:
        ararv=input("enter NAME (ENTER NAME FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l4:
            for j in i:
                count=len(i)
                if ararv not in j:#To check validity of input
                    no3=no3+1
                    if no3==count:
                        print("Invalid Input!!!\n")
                        break
                if ararv in j:
                    sqldel3="DELETE FROM ARTILLERY WHERE NAME = %s"
                    cursor.execute(sqldel3,(ararv,))
                    x2=cursor.fetchall()
                    for i in x2:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif ardel==3:
        ararv=input("enter TYPE (ENTER TYPE FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l4:
            for j in i:
                count=len(i)
                if ararv not in j:#To check validity of input
                    no3=no3+1
                    if no3==count:
                        print("Invalid Input!!!\n")
                        break
                if ararv in j:
                    sqldel3="DELETE FROM ARTILLERY WHERE TYPE = %s"
                    cursor.execute(sqldel3,(ararv,))
                    x2=cursor.fetchall()
                    for i in x2:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif ardel==4:
        ararv=eval(input("enter QUANTITY (ENTER VALUE FROM THE ABOVE TABLE CONTENTS ONLY):"))
        for i in l4:
            for j in i:
                count=len(i)
                if ararv not in j:#To check validity of input
                    no3=no3+1
                    if no3==count:
                        print("Invalid Input!!!\n")
                        break
                if ararv in j:
                    sqldel3="DELETE FROM ARTILLERY WHERE QUANTITY = %s"
                    cursor.execute(sqldel3,(ararv,))
                    x2=cursor.fetchall()
                    for i in x2:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif ardel==5:
        ararv=input("enter ORIGIN (ENTER ORIGIN FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l4:
            for j in i:
                count=len(i)
                if ararv not in j:#To check validity of input
                    no3=no3+1
                    if no3==count:
                        print("Invalid Input!!!\n")
                        break
                if ararv in j:
                    sqldel3="DELETE FROM ARTILLERY WHERE ORIGIN = %s"
                    cursor.execute(sqldel3,(ararv,))
                    x2=cursor.fetchall()
                    for i in x2:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif ardel==6:
        ararv=input("enter STATUS (ENTER STATUS FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l4:
            for j in i:
                count=len(i)
                if ararv not in j:#To check validity of input
                    no3=no3+1
                    if no3==count:
                        print("Invalid Input!!!\n")
                        break
                if ararv in j:
                    sqldel3="DELETE FROM ARTILLERY WHERE STATUS = %s"
                    cursor.execute(sqldel3,(ararv,))
                    x2=cursor.fetchall()
                    for i in x2:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    else:
        print("please try again")
        delete_ARTILLERY()
    artillerydisplay()


#######################################################



def delete_MARINE_DEFENCE_SYSTEM():
    cursor.execute("use Indian_Defence_System")
    marinedisplay()
    mdel=eval(input("enter the code indicated against each column to specify parameter for deleting entities from table \n1.SNO \n2.CLASS \n3.TYPE \n4.NAME \n5.ORIGIN \n6.DISPLACEMENT \n7.STATUS ( IN SERVICE , PHASED OUT , ORDERED) \n>"))
    no2=0
    if mdel==1:
        marv=eval(input("enter value of SNO (ENTER VALUE FROM THE ABOVE TABLE CONTENTS ONLY):"))
        for i in l3:
            for j in i:
                count=len(i)
                if marv not in j:#To check validity of input
                    no2=no2+1
                    if no2==count:
                        print("Invalid Input!!!\n")
                        break
                if marv in j:
                    sqldel4="DELETE FROM MARINE_DEFENCE_SYSTEM WHERE SNo = %s"
                    cursor.execute(sqldel4,(marv,))
                    x3=cursor.fetchall()
                    for i in x3:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif mdel==2:
        marv=input("enter CLASS (ENTER CLASS FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l3:
            for j in i:
                count=len(i)
                if marv not in j:#To check validity of input
                    no2=no2+1
                    if no2==count:
                        print("Invalid Input!!!\n")
                        break
                if marv in j:
                    sqldel4="DELETE FROM MARINE_DEFENCE_SYSTEM WHERE CLASS = %s"
                    cursor.execute(sqldel4,(marv,))
                    x3=cursor.fetchall()
                    for i in x3:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif mdel==3:
        marv=input("enter TYPE (ENTER TYPE FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l3:
            for j in i:
                count=len(i)
                if marv not in j:#To check validity of input
                    no2=no2+1
                    if no2==count:
                        print("Invalid Input!!!\n")
                        break
                if marv in j:
                    sqldel4="DELETE FROM MARINE_DEFENCE_SYSTEM WHERE TYPE = %s"
                    cursor.execute(sqldel4,(marv,))
                    x3=cursor.fetchall()
                    for i in x3:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif mdel==4:
        marv=input("enter NAME (ENTER NAME FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l3:
            for j in i:
                count=len(i)
                if marv not in j:#To check validity of input
                    no2=no2+1
                    if no2==count:
                        print("Invalid Input!!!\n")
                        break
                if marv in j:
                    sqldel4="DELETE FROM MARINE_DEFENCE_SYSTEM WHERE SHIPS = %s"
                    cursor.execute(sqldel4,(marv,))
                    x3=cursor.fetchall()
                    for i in x3:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif mdel==5:
        marv=input("enter ORIGIN (ENTER ORIGIN FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l3:
            for j in i:
                count=len(i)
                if marv not in j:#To check validity of input
                    no2=no2+1
                    if no2==count:
                        print("Invalid Input!!!\n")
                        break
                if marv in j:
                    sqldel4="DELETE FROM MARINE_DEFENCE_SYSTEM WHERE ORIGIN = %s"
                    cursor.execute(sqldel4,(marv,))
                    x3=cursor.fetchall()
                    for i in x3:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif mdel==6:
        marv=input("enter DISPLACEMENT (ENTER VALUE FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l3:
            for j in i:
                count=len(i)
                if marv not in j:#To check validity of input
                    no2=no2+1
                    if no2==count:
                        print("Invalid Input!!!\n")
                        break
                if marv in j:
                    sqldel4="DELETE FROM MARINE_DEFENCE_SYSTEM WHERE DISPLACEMENT_in_Tonnes = %s"
                    cursor.execute(sqldel4,(marv,))
                    x3=cursor.fetchall()
                    for i in x3:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif mdel==7:
        marv=input("enter STATUS (ENTER STATUS FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l3:
            for j in i:
                count=len(i)
                if marv not in j:#To check validity of input
                    no2=no2+1
                    if no2==count:
                        print("Invalid Input!!!\n")
                        break
                if marv in j:
                    sqldel4="DELETE FROM MARINE_DEFENCE_SYSTEM WHERE STATUS = %s"
                    cursor.execute(sqldel4,(marv,))
                    x3=cursor.fetchall()
                    for i in x3:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    else:
        print("please try again")
        delete_MARINE_DEFENCE_SYSTEM()
    marinedisplay()

 

############################################################


def delete_INFANTRY_WEAPONS():
    cursor.execute("use Indian_Defence_System")
    infantrydisplay()
    wdel=eval(input("enter the code indicated against each column to specify parameter for deleting entities from table \n1.SNO \n2.NAME \n3.TYPE \n4.CALIBER \n5.ORIGIN  \n6.STATUS ( IN SERVICE , PHASED OUT , ORDERED) \n>"))
    no4=0
    if wdel==1:
        warv=eval(input("enter value of SNO (ENTER VALUE FROM THE ABOVE TABLE CONTENTS ONLY):"))
        for i in l5:
            for j in i:
                count=len(i)
                if warv not in j:#To check validity of input
                    no4=no4+1
                    if no4==count:
                        print("Invalid Input!!!\n")
                        break
                if warv in j:
                    sqldel5="DELETE FROM INFANTRY_WEAPONS WHERE SNo = %s"
                    cursor.execute(sqldel5,(warv,))
                    x4=cursor.fetchall()
                    for i in x4:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif wdel==2:
        warv=input("enter NAME (ENTER NAME FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l5:
            for j in i:
                count=len(i)
                if warv not in j:#To check validity of input
                    no4=no4+1
                    if no4==count:
                        print("Invalid Input!!!\n")
                        break
                if warv in j:
                    sqldel5="DELETE FROM INFANTRY_WEAPONS WHERE NAME = %s"
                    cursor.execute(sqldel5,(warv,))
                    x4=cursor.fetchall()
                    for i in x4:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif wdel==3:
        warv=input("enter TYPE (ENTER TYPE FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l5:
            for j in i:
                count=len(i)
                if warv not in j:#To check validity of input
                    no4=no4+1
                    if no4==count:
                        print("Invalid Input!!!\n")
                        break
                if warv in j:
                    sqldel5="DELETE FROM INFANTRY_WEAPONS WHERE TYPE = %s"
                    cursor.execute(sqldel5,(warv,))
                    x4=cursor.fetchall()
                    for i in x4:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif wdel==4:
        warv=eval(input("enter CALIBER (ENTER CALIBER FROM THE ABOVE TABLE CONTENTS ONLY):"))
        for i in l5:
            for j in i:
                count=len(i)
                if warv not in j:#To check validity of input
                    no4=no4+1
                    if no4==count:
                        print("Invalid Input!!!\n")
                        break
                if warv in j:
                    sqldel5="DELETE FROM INFANTRY_WEAPONS WHERE CALIBER_in_mm = %s"
                    cursor.execute(sqldel5,(warv,))
                    x4=cursor.fetchall()
                    for i in x4:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif wdel==5:
        warv=input("enter ORIGIN (ENTER ORIGIN FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l5:
            for j in i:
                count=len(i)
                if warv not in j:#To check validity of input
                    no4=no4+1
                    if no4==count:
                        print("Invalid Input!!!\n")
                        break
                if warv in j:
                    sqldel5="DELETE FROM INFANTRY_WEAPONS WHERE ORIGIN = %s"
                    cursor.execute(sqldel5,(warv,))
                    x4=cursor.fetchall()
                    for i in x4:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    elif wdel==6:
        warv=input("enter STATUS (ENTER STATUS FROM THE ABOVE TABLE CONTENTS ONLY):")
        for i in l5:
            for j in i:
                count=len(i)
                if warv not in j:#To check validity of input
                    no4=no4+1
                    if no4==count:
                        print("Invalid Input!!!\n")
                        break
                if warv in j:
                    sqldel5="DELETE FROM INFANTRY_WEAPONS WHERE STATUS = %s"
                    cursor.execute(sqldel5,(warv,))
                    x4=cursor.fetchall()
                    for i in x4:
                        print(i)
                    mydb.commit()
                    print("Entity deleted!!")
    else:
        print("please try again")
        delete_INFANTRY_WEAPONS()
    infantrydisplay()
######################################################

# CALLING THE DELETE FUNCTION

def delete_table():
    cursor.execute("use Indian_Defence_System")
    wttd=eval(input("enter number indicated before the table you want to delete \n\t\t\t1.BALLISTIC_MISSILE  \n\t\t\t2.AIRCRAFTS  \n\t\t\t3.ARTILLERY  \n\t\t\t4.MARINE_DEFENCE_SYSTEM \n\t\t\t5.INFANTRY_WEAOPONS \n>"))
    if wttd==1:
        delete_ballistic_missiles()
    elif wttd==2:
        delete_AIRCRAFTS()
    elif wttd==3:
        delete_ARTILLERY()
    elif wttd==4:
        delete_MARINE_DEFENCE_SYSTEM()
    elif wttd==5:
        delete_INFANTRY_WEAPONS()
    else:
        print("please try again")
    mydb.commit()

# FUNCTION TO SEARCH STATUS OF AMMUNITIONS
def searcher():
    cursor.execute("use Indian_Defence_System")
    search=eval(input("To search for phased out, in service or ordered arms and ammunitions \nenter the code displayed against the tables \nBALLISTIC_MISSILES:1  \nAIRCRAFTS:2  \nARTILLERY:3  \nMARINE_DEFENCE_SYSTEM:4 \nINFANTRY_WEAOPONS:5 \n>"))
    
    if search==1:                           ##################### 
        element=eval(input("To search for \nIn Service arms enter 1 \n2 for Phased out \n3 for Ordered arms \n>"))
        if element==1:
            sqlsearchB1="SELECT * FROM BALLISTIC_MISSILES WHERE STATUS='In_Service' or STATUS='in service'"
            cursor.execute(sqlsearchB1)
            recsrchB1=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchB1 , headers=['SNo', 'NAME', 'TYPE', 'NUMBERS_in_TELs', 'ORIGIN, MIN_RANGE', 'MAX_RANGE', 'STATUS'], tablefmt='sqlsearchB1'))
            mydb.commit()
        elif element==2:
            sqlsearchB2="SELECT * FROM BALLISTIC_MISSILES WHERE STATUS='Phased_out' or STATUS='phased out'"
            cursor.execute(sqlsearchB2)
            recsrchB2=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchB2 , headers=['SNo', 'NAME', 'TYPE', 'NUMBERS_in_TELs', 'ORIGIN, MIN_RANGE', 'MAX_RANGE', 'STATUS'], tablefmt='sqlsearchB2'))
            mydb.commit()
        elif element==3:
            sqlsearchB3="SELECT * FROM BALLISTIC_MISSILES WHERE STATUS='Ordered'"
            cursor.execute(sqlsearchB3)
            recsrchB3=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchB3 , headers=['SNo', 'NAME', 'TYPE', 'NUMBERS_in_TELs', 'ORIGIN, MIN_RANGE', 'MAX_RANGE', 'STATUS'], tablefmt='sqlsearchB3'))
            mydb.commit()
        else:
            print("INVALID INPUT!! PLEASE TRY AGAIN.")
            searcher()


    elif search==2:                          #####################
        element1=eval(input("To search for \nIn Service arms enter 1 \n2 for Phased out \n3 for Ordered arms \n>"))
        if element1==1:
            sqlsearchA1="SELECT * FROM AIRCRAFTS WHERE STATUS = 'In_Service' or STATUS='in service'"
            cursor.execute(sqlsearchA1)
            recsrchA1=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchA1 , headers=['SNo', 'AIRCRAFTS','ORIGIN', 'ROLE', 'VERSION', 'NUMBERS', 'STATUS'], tablefmt='sqlsearchA1'))
            mydb.commit()
            
        elif element1==2:
            sqlsearchA2="SELECT * FROM AIRCRAFTS WHERE STATUS='Phased_out' or STATUS='phased out'"
            cursor.execute(sqlsearchA2)
            recsrchA2=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchA2 , headers=['SNo', 'AIRCRAFTS','ORIGIN', 'ROLE', 'VERSION', 'NUMBERS', 'STATUS'], tablefmt='sqlsearchA2'))
            mydb.commit()
            
        elif element1==3:
            sqlsearchA3="SELECT * FROM AIRCRAFTS WHERE STATUS='Ordered'"
            cursor.execute(sqlsearchA3)
            recsrchA3=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchA3 , headers=['SNo', 'AIRCRAFTS','ORIGIN', 'ROLE', 'VERSION', 'NUMBERS', 'STATUS'], tablefmt='sqlsearchA3'))
            mydb.commit()
        else:
            print("INVALID INPUT!! PLEASE TRY AGAIN.")
            searcher()
        

    elif search==3:                             ######################
        element2=eval(input("To search for \nIn Service arms enter 1 \n2 for Phased out \n3 for Ordered arms \n>"))
        if element2==1:
            sqlsearchAR1="SELECT * FROM ARTILLERY WHERE STATUS='In_Service' or STATUS='in service'"
            cursor.execute(sqlsearchAR1)
            recsrchAR1=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchAR1 , headers=['SNo', 'NAME', 'TYPE', 'QUANTITY', 'ORIGIN', 'STATUS'], tablefmt='sqlsearchAR1'))
            mydb.commit()
        elif element2==2:
            sqlsearchAR2="SELECT * FROM ARTILLERY WHERE STATUS='Phased_out' or STATUS='phased out'"
            cursor.execute(sqlsearchAR2)
            recsrchAR2=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchAR2 , headers=['SNo', 'NAME', 'TYPE', 'QUANTITY', 'ORIGIN', 'STATUS'], tablefmt='sqlsearchAR2'))
            mydb.commit()
        elif element2==3:
            sqlsearchAR3="SELECT * FROM ARTILLERY WHERE STATUS='Ordered'"
            cursor.execute(sqlsearchAR3)
            recsrchAR3=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchAR3 , headers=['SNo', 'NAME', 'TYPE', 'QUANTITY', 'ORIGIN', 'STATUS'], tablefmt='sqlsearchA3'))
            mydb.commit()
        else:
            print("INVALID INPUT!! PLEASE TRY AGAIN.")
            searcher()
        



    elif search==4:                           #####################
        element3=eval(input("To search for \nIn Service arms enter 1 \n2 for Phased out \n3 for Ordered arms \n>"))
        if element3==1:
            sqlsearchM1="SELECT * FROM MARINE_DEFENCE_SYSTEM WHERE STATUS='In_Service' or STATUS='in service'"
            cursor.execute(sqlsearchM1)
            recsrchM1=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchM1 , headers=['SNo', 'CLASS', 'TYPE', 'SHIPS', 'ORIGIN','DISPLACEMENT_in_tonnes','STATUS'], tablefmt='sqlsearchM1'))
            mydb.commit()
        elif element3==2:
            sqlsearchM2="SELECT * FROM MARINE_DEFENCE_SYSTEM WHERE STATUS='Phased_out' or STATUS='phased out'"
            cursor.execute(sqlsearchM2)
            recsrch3=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchM2 , headers=['SNo', 'CLASS', 'TYPE', 'SHIPS', 'ORIGIN','DISPLACEMENT_in_tonnes','STATUS'], tablefmt='sqlsearchM2'))
            mydb.commit()
        elif element3==3:
            sqlsearchM3="SELECT * FROM MARINE_DEFENCE_SYSTEM WHERE STATUS='Ordered'"
            cursor.execute(sqlsearchM3)
            recsrchM3=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchM3 , headers=['SNo', 'CLASS', 'TYPE', 'SHIPS', 'ORIGIN','DISPLACEMENT_in_tonnes','STATUS'], tablefmt='sqlsearchM3'))
            mydb.commit()
        else:
            print("INVALID INPUT!! PLEASE TRY AGAIN.")
            searcher()
        



    elif search==5:
        element4=eval(input("To search for \nIn Service arms enter 1 \n2 for Phased out \n3 for Ordered arms \n>"))
        if element4==1:
            sqlsearchI1="SELECT * FROM INFANTRY_WEAPONS WHERE STATUS='In_Service' or STATUS='in service'"
            cursor.execute(sqlsearchI1)
            recsrchI1=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchI1 , headers=['SNo', 'NAME', 'TYPE', 'CALIBER_in_mm', 'ORIGIN', 'STATUS'], tablefmt='sqlsearchI1'))
            mydb.commit()
        elif element4==2:
            sqlsearchI2="SELECT * FROM INFANTRY_WEAPONS WHERE STATUS='Phased_out' or STATUS='phased out'"
            cursor.execute(sqlsearchI2)
            recsrchI2=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchI2 , headers=['SNo', 'NAME', 'TYPE', 'CALIBER_in_mm', 'ORIGIN', 'STATUS'], tablefmt='sqlsearchI2'))
            mydb.commit()
        elif element4==3:
            sqlsearchI3="SELECT * FROM INFANTRY_WEAPONS WHERE STATUS='Ordered'"
            cursor.execute(sqlsearchI3)
            recsrchI3=cursor.fetchall()
            from tabulate import tabulate
            print(tabulate(recsrchI3 , headers=['SNo', 'NAME', 'TYPE', 'CALIBER_in_mm', 'ORIGIN', 'STATUS'], tablefmt='sqlsearchI3'))
            mydb.commit()
        else:
            print("INVALID INPUT!! PLEASE TRY AGAIN.")
            searcher()
        
    else:
        print("Try again")
        searcher()

    
#Function for the quiz
def Quiz():
    Score=0
    cand=input("\nEnter Your Name:")
    print("\nREAD THE FOLLOWING INSTRUCTIONS CAREFULLY!!!!")
    print("\n1.Each question carries 4 points")
    print("2. 1 point would be deducted for wrong answer")
    print("3.If any question is not answered then you will be awarded with 0")
    print("\nSo,let's start the quiz")
    print("\nQues.1\nIn which year Indian army was established? \n\nA. 1895 \nB. 1900 \nC. 1905 \nD. 1947\nE.Dont Want To Answer")
    ans1=input("\nPlease Choose From One Of The Above Options:")
    if ans1=="A":
        Score2=Score+4
    elif ans1=="B":
        Score2=Score-1
    elif ans1=="C":
        Score2=Score-1
    elif ans1=="D":
        Score2=Score-1
    elif ans1=="E":
        Score2=Score
    else:
        print("\nInvalid Input!!")
        Score2=0
    
    print("\nQues.2\nSmallest unit of Indian Army called:\nA. Battalion\nB. Company\nC. Platoon\nD. Section\nE.Dont Want To Answer")
    ans2=input("\nPlease Choose From One Of The Above Options:")
    if ans2=="D":
        Score3=Score2+4
    elif ans2=="B":
        Score3=Score2-1
    elif ans2=="C":
        Score3=Score2-1
    elif ans2=="A":
        Score3=Score2-1
    elif ans2=="E":
        Score3=Score2
    else:
        print("\nInvalid Input!!")
        Score3=Score2
  
    print("\nQues.3\nWho is the present Chief of Indian Army?\nA. Manoj Mukund Naravane\nB. R. K. Dhowan\nC. Dalbir Singh Suhag\nD. Bipin Rawat\nE.Dont Want To Answer")
    ans3=input("\nPlease Choose From One Of The Above Options:")
    if ans3=="A":
        Score4=Score3+4
    elif ans3=="B":
        Score4=Score3-1
    elif ans3=="C":
        Score4=Score3-1
    elif ans3=="D":
        Score4=Score3-1
    elif ans3=="E":
        Score4=Score3
    else:
        print("\nInvalid Input!!")
        Score4=Score3
  
    print("\nQues.4\nWhich of the following organizations has Sarvatra Sarvottam Suraksha as its slogan?\nA.Border Security Force\nB.Sikh Light Infantry\nC.Indian Air Force\nD.National Security Guard\nE.Dont Want To Answer")
    ans4=input("\nPlease Choose From One Of The Above Options:")
    if ans4=="D":
        Score5=Score4+4
    elif ans4=="B":
        Score5=Score4-1
    elif ans4=="C":
        Score5=Score4-1
    elif ans4=="A":
        Score5=Score4-1
    elif ans4=="E":
        Score5=Score4
    else:
        print("\nInvalid Input!!")
        Score5=Score4
  
    print("\nQues.5\nAt which of the following places is the College of Defence Management located?\nA.Dehradun\nB.Pune\nC.Secunderabad\nD.Chennai\nE.Dont Want To Answer")
    ans5=input("\nPlease Choose From One Of The Above Options:")
    if ans5=="C":
        Score6=Score5+4
    elif ans5=="B":
        Score6=Score5-1
    elif ans5=="A":
        Score6=Score5-1
    elif ans5=="D":
        Score6=Score5-1
    elif ans2=="E":
        Score6=Score5
    else:
        print("\nInvalid Input!!")
        Score6=Score5
  
    print("\nQues.6\nWhat was the name given to the operation conducted by National Security Guard in 2008 against terrorist attack in Taj hotel, Mumbai?\nA.Operation Black Tornado\nB.Operation Black Thunder\nC.Operation Safed Sagar\nD.Operation Vijay\nE.Dont Want To Answer")
    ans6=input("\nPlease Choose From One Of The Above Options:")
    if ans6=="A":
        Score7=Score6+4
    elif ans6=="B":
        Score7=Score6-1
    elif ans6=="C":
        Score7=Score6-1
    elif ans1=="D":
        Score7=Score6-1
    elif ans2=="E":
        Score7=Score6
    else:
        print("\nInvalid Input!!")
        Score7=Score6
        
    print("\nQues.7\n On which of the following dates is the Navy Day celebrated in India?\nA.January 15\nB.October 8\nC.December 4\nD.February 1\nE.Dont Want To Answer")
    ans7=input("\nPlease Choose From One Of The Above Options:")
    if ans7=="C":
        Score8=Score7+4
    elif ans7=="B":
        Score8=Score7-1
    elif ans7=="A":
        Score8=Score7-1
    elif ans7=="D":
        Score8=Score7-1
    elif ans7=="E":
        Score8=Score7
    else:
        print("\nInvalid Input!!")
        Score8=Score7
  
    print("\nQues.8\nThe commando unit of the Indian Air Force is named\nA.Baaz\nB.Garud\nC.MARCOS\nD.Ghatak\nE.Dont Want To Answer")
    ans8=input("\nPlease Choose From One Of The Above Options:")
    if ans8=="B":
        Score9=Score8+4
    elif ans8=="A":
        Score9=Score8-1
    elif ans8=="C":
        Score9=Score8-1
    elif ans8=="D":
        Score9=Score8-1
    elif ans8=="E":
        Score9=Score8
    else:
        print("\nInvalid Input!!")
        Score9=Score8
  
    print("\nQues.9\nHow many wars did India has fought and won respectively since Independence?\nA.4,4\nB.4,3\nC.3,2\nD.5,4\nE.Dont Want To Answer")
    ans9=input("\nPlease Choose From One Of The Above Options:")
    if ans9=="B":
        Score10=Score9+4
    elif ans9=="A":
        Score10=Score9-1
    elif ans9=="C":
        Score10=Score9-1
    elif ans9=="D":
        Score10=Score9-1
    elif ans9=="E":
        Score10=Score9
    else:
        print("\nInvalid Input!!")
        Score10=Score9
  
    print("\nQues.10\nWho is the Chief of Defence Staff (India)\nA.Mr.Narendra Modi\nB. R. K. Dhowan\nC. Bipin Rawat\nD. Dalbir Singh Suhag\nE.Dont Want To Answer")
    ans10=input("\nPlease Choose From One Of The Above Options:")
    if ans10=="C":
        Score11=Score10+4
    elif ans10=="B":
        Score11=Score10-1
    elif ans10=="A":
        Score11=Score10-1
    elif ans10=="D":
        Score11=Score10-1
    elif ans10=="E":
        Score11=Score10
    else:
        print("\nInvalid Input!!")
        Score11=Score10
  
    print("Ques.11\n Who is the Defence Minister of India \nA.Rajnath Singh.\nB.Arun Jately\nC.Amit Shah\nD.Mr.Narendra Modi\nE.Dont Want To Answer")
    ans11=input("\nPlease Choose From One Of The Above Options:")
    if ans11=="A":
        Score12=Score11+4
    elif ans11=="B":
        Score12=Score11-1
    elif ans11=="C":
        Score12=Score11-1
    elif ans11=="D":
        Score12=Score11-1
    elif ans11=="E":
        Score12=Score11
    else:
        print("\nInvalid Input!!")
        Score12=Score11
  
    print("Ques.12\n Name an Indian Air Force fighter pilot who, during the 2019 India–Pakistan standoff, was held captive in Pakistan for 60 hours after his aircraft was shot down in an aerial dogfight\nA.Abhinandan Kumar\nA.Abhinandan Singh Rajput\nC.Abhinandan Rathore\nD.Abhinandan Varthaman\nE.Dont Want To Answer")
    ans12=input("\nPlease Choose From One Of The Above Options:")
    if ans12=="D":
        Score13=Score12+4
    elif ans12=="B":
        Score13=Score12-1
    elif ans12=="C":
        Score13=Score12-1
    elif ans12=="A":
        Score13=Score12-1
    elif ans12=="E":
        Score13=Score12
    else:
        print("\nInvalid Input!!")
        Score13=Score12
    if Score13==48:
        rem="Perfect_You_Are_A_True_Soldier_and_Patriot___Country_Needs_People_like_You"
    elif Score13>=40 and Score13<48:
        rem="You_Are_A_True_Patriot"
    elif Score13>=25 and Score13<40:
        rem="This_Proves_That_You_are_a_Good__Citizen_and_Can_Become_A_Patriot"
    elif Score13>=15 and Score13<25:
        rem="You_are_on_right_path_just_focus_more_and_you_will_fly"
    elif Score13>=-12 and Score13<15:
        rem="Dont_Worry_Just_try_to_inculcate_more_Information_and_knowledge"
    Final_score=Score13
    print(cand,"You Have Scored",Final_score,"points",rem)
    cursor.execute("use Indian_Defence_System")
    sql6="insert into POINTS_TABLE(NAME,SCORE,REMARKS) values(%s,%s,%s)"#To insert Values into Points table
    cursor.execute(sql6,(cand,Final_score,rem))
    print("\nYou Score Has Been Recorded \nYou Can Now,Compare Your Score With Others")
    sqlpoints="Select* from POINTS_TABLE"
    cursor.execute(sqlpoints)
    points=cursor.fetchall()
    from tabulate import tabulate
    print(tabulate(points,headers=['NAME','SCORE','REMARKS'],tablefmt='psql'))
    mydb.commit()

#Function to drop Database    
def Drop():
    cursor.execute("use Indian_Defence_System")
    sqldrop="Drop database Indian_Defence_System"
    cursor.execute(sqldrop)
    print("\nDatabase has been Dropped!!!!!")

#Function to show points table according to rank    
def show_points():
    cursor.execute("use Indian_Defence_System")
    sqlpoints="Select* from POINTS_TABLE  order by SCORE desc"
    cursor.execute(sqlpoints)
    points=cursor.fetchall()
    from tabulate import tabulate
    print(tabulate(points,headers=['NAME','SCORE','REMARKS'],tablefmt='psql'))
    mydb.commit()
    

#Function for The Indian Defence Management System
def Menu():
    while True:
        greet=eval(input("\nPLEASE ENTER TIME IN {0-24} FORMAT:"))
        if (greet>=0 and greet <12):
            print("\n\t\t\tGood Morning To One And All!!!")
            break
        elif greet>=12 and greet<16:
            print("\n\t\t\tGood Afternoon To One And All!!!")
            break
        elif greet>=16 and greet<=24:
            print("\n\t\t\tGood Evening To One And All!!!")
            break
        else:
            print("\n\t\t\tPlease Input Carefully!!!")
    print("\n\tINTRODUCTION")        
    print("\n\n\tThis project has been developed to increase the fascination of people for the armed forces \t\t\tof India.")
    print("\n\tOne will be able deploy his own system of weapons combination and strategies to tackle \t\t\t\tsituations.")
    print("\n\tThrough this you'll be able to select your own choice of weapons and make changes in them.")
    print("\tYou can search for the weapons which are in service and ordered or phased out so as to plan the future \tdeployements.")
    print("\n\tAt last a very interesting Quiz is there ,it will surely increase yor fascination for the forces.")
    print("\n\tMoreover,you can also see the leaderboard and could compare where you stand among others.")
    while True:
        print("\n\n\n\t\t\t\t WELCOME TO INDIAN DEFENCE SYSTEM \n\t\t\t\t\tSEVA PARMO DHARMA\n\t\t\t\t\tDEATH BEFORE DISHONOUR")          
        print("\n\t\t\t1: Create Database")
        print("\t\t\t2: Create Tables")
        print("\t\t\t3: To Add Equipments")
        print("\t\t\t4: To View Tables")
        print("\t\t\t5: To Update Tables")
        print("\t\t\t6: To Delete from Tables")
        print("\t\t\t7: Search for status of weapons")
        print("\t\t\t8: Quiz (How much you Know About Indian Army)")
        print("\t\t\t9: To See Quiz Leader board")
        print("\t\t\t10:Drop Database")
        print("\t\t\t11: Exit")
        userinput=eval(input("\nPlease Select An Above Option:")) #Take input from user
        if (userinput==1):
            crdatab()
        elif (userinput==2):
            crtableb()
        elif (userinput==3):
            insertrec()
        elif (userinput==4):
            viewtable()
        elif (userinput==5):
            updatetable()
        elif (userinput==6):
            delete_table()    
        elif(userinput==7):
            searcher()
        elif (userinput==8):
            Quiz()
        elif (userinput==9):
            show_points()
        elif (userinput==10):
            Drop()
        elif (userinput==11):
            print("\n\n\nBye \n\nHope you would serve your motherland to the fullest\n\nJAI HIND!!!!! \n\nBalidan Parmo Dharma!!!! \n------x-------------x-------------x-----------x-----------x--------- ")
            input("")
            break
        else:
            print("\nInvalid Input!!!")
Menu()
