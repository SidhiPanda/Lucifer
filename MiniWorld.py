import subprocess as sp
import pymysql
import pymysql.cursors


def selectionFromCharacters():
    try:
        query = "SELECT * FROM Characters"

        print(query)
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return


def projectionByEntity():

    print()
    try:
        row = {}
        row["TName"] = input("Table Name: ")
        row["AName"] = input("Attribute Name: ")
        row["AType"] = input("{Char/Int}: ")
        if row["AType"] == "Char":
            row["Search"] = input("Search for: ")
            query = "SELECT * FROM '%s' WHERE '%s'='%s'" % (
                row["TName"], row["AName"], row["Search"])
        elif row["AType"] == "Int":
            row["Search"] = int(input("Search for: "))
            query = "SELECT * FROM '%s' WHERE '%s'='%f'" % (
                row["TName"], row["AName"], row["Search"])

        print(query)
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return


def projectionOverall():

    print()
    try:
        row = {}
        row["TName"] = input("Table Name: ")
        row["AName"] = input("Attribute Name: ")
        row["AType"] = input("{Char/Int}: ")
        if row["AType"] == "Char":
            row["Search"] = input("Search for: ")
            query = "SELECT * FROM Characters JOIN Cases JOIN Abilities JOIN Character_Age JOIN Dependent_Family WHERE '%s'.'%s'='%s'" % (
                row["TName"], row["AName"], row["Search"])
        elif row["AType"] == "Int":
            row["Search"] = int(input("Search for: "))
            query = "SELECT * FROM Characters JOIN Cases JOIN Abilities JOIN Character_Age JOIN Dependent_Family WHERE '%s'.'%s'='%f'" % (
                row["TName"], row["AName"], row["Search"])

        print(query)
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return


def noOfCasesBy():

    print()
    try:
        row = {}
        row["Name"] = input("Enter Name: ")
        query = "SELECT COUNT(*) FROM Team WHERE Detective1='%s' OR Detective2='%s'" % (
            row["Name"], row["Name"])

        print(query)
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return


def costliestDrug():

    print()
    try:
        query = "SELECT Common_Name, Scientific_Name, Price_per_Kilo FROM Illegal_Substance ORDER BY Price_per_Kilo DESC LIMIT 1"

        print(query)
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return


def netWorth():

    print()
    try:
        row = {}
        row["Name"] = input("Enter Name: ")
        query = "SELECT SUM(Share), Owned_By FROM Individual_Shares GROUP BY Owned_By HAVING Owned_By='%s'" % (
            row["Name"])

        print(query)
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return


def searchName():

    print()
    try:
        row = {}
        row["Name"] = input("Enter Name: ")
        query = "SELECT Name, BeingType FROM Characters WHERE Name LIKE '%'%s'%'" % (
            row["Name"])

        print(query)
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return


def insertCharacter():

    print()
    try:
        row = {}
        row["Name"] = input("Enter Name of Character: ")
        row["DOB"] = input("Enter DOB(YYYY-MM-DD): ")
        row["Parent1"] = input("Enter name of Parent 1: ")
        row["Parent2"] = input("Enter name of Parent 2: ")
        row["Beingtype"] = input("Enter Type of Being: ")
        row["Rel_Status"] = input("Enter Relationship Status: ")
        row["Rel_Partner"] = input("Enter Relationship Partner's Name: ")
        row["Place_of_Origin"] = input("Enter the Place of Origin: ")
        query = "INSERT INTO Characters VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            row["Name"], row["DOB"], row["Parent1"], row["Parent2"], row["Beingtype"], row["Rel_Status"], row["Rel_Partner"], row["Place_of_Origin"])

        print(query)
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def updateCharacter():

    print()
    try:
        row = {}
        row["Name"] = input("Enter Name: ")
        row["Attribute"] = input("Enter the Attribute to be Updated: ")
        row["Value"] = input("Enter New Value: ")
        query = "UPDATE Characters SET '%s'='%s' WHERE Name='%s'" % (
            row["Attribute"], row["Value"], row["Name"])

        print(query)
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return


def deleteCharacter():

    print()
    try:
        row = {}
        row["Name"] = input("Enter Name to be Deleted: ")
        query = "DELETE FROM Characters WHERE Name='%s'" % (row["Name"])
        print(query)
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)

    except Exception as e:
        con.rollback()
        print("Failed to delete in database")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):

    if(ch == 1):
        selectionFromCharacters()
    elif(ch == 2):
        projectionByEntity()
    elif(ch == 3):
        projectionOverall()
    elif(ch == 4):
        noOfCasesBy()
    elif(ch == 5):
        costliestDrug()
    elif(ch == 6):
        netWorth()
    elif(ch == 7):
        searchName()
    elif(ch == 8):
        insertCharacter()
    elif(ch == 9):
        updateCharacter()
    elif(ch == 10):
        deleteCharacter()
    else:
        print("Error: Invalid Option")


while(1):
    tmp = sp.call('clear', shell=True)

    username = input("Username: ")
    pwd = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user=username,
                              password=pwd,
                              db='Lucifer',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                print("1. Selection of data from Characters")
                print("2. Projection_by_Entity")
                print("3. Projection_Overall")
                print("4. No_of_Cases_By")
                print("5. Costliest Drug")
                print("6. Net Worth")
                print("7. Search Name")
                print("8. Inserting into Characters")
                print("9. Updating Characters")
                print("10. Deleting Characters")
                print("Enter ANY other number to EXIT.\n")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 11:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
