print("Welcome to the Prudent Healthcare Hospital")
print("Lets start with users login process:-")


def Secretarylogin():
    email=input("Enter your username:")
    passw=input("Enter your password:")
    while True:
        if (email, passw) == ("secretary", "admin"):
            print("username and password matched")
            print("\nyou are login as a secretary\n")
            break

        else:
            print("wrong email and password\ntry again")
            last()


def physicianlogin():
    email=input("Enter your username:")
    passw=input("Enter your password:")
    while True:
        if (email, passw) == ("physician", "admin"):
            print("username and password matched")
            print("\nyou are login as a physician\n")
            break
        else:
            print("wrong email and password\ntry again")
            last()


def accountantlogin():
    email=input("Enter your username:")
    passw=input("Enter your password:")
    while True:
        if (email, passw) == ("accountant", "admin"):
            print("username and password matched")
            break
        else:
            print("wrong email and password\ntry again")
            last()

#textfile="dic.txt"  for record patient information

def writes(patient_id, first_name, last_name, address, gender,Age, contact):
    fw = open('dic.txt', "a")
    fw.write("%1s%20s%20s%20s%20s%20s%20s\n" % (patient_id, first_name, last_name, address, gender,Age, contact))
    fw.close()

def registration():



    print("You are a physian\n")
    users = input("now registration of patient press Enter")
    patient_id = input("Enter patient_id:")
    first_name = input("Enter your first_name:")
    last_name = input("Enter your last name:")
    address = input("Enter your address:")
    gender = input("Enter your gender: ")
    Age=input("Enter your Age")
    contact = input("Enter your contact number:")
    writes(patient_id, first_name, last_name, address, gender,Age, contact)
    print("THANK YOU!!!")
    print("\nUser created!\n")
    print("information saved in text file")


def read():
    users = open("dic.txt",'r')
    extract = input("Please input patient ID")
    for each_line in users:
        (patient_id, first_name, last_name, address, gender,Age, contact) = each_line.split()

        if (patient_id == extract):
            print(patient_id, first_name, last_name, address, gender,Age, contact)
    users.close()

#textfile="appointment.txt"  for record appointment information

def appointment2w(patientID,AppointmentID,status,Doctor):
    fw = open('appointment.txt', "a")
    fw.write("%1s%20s%20s%20s\n" % (patientID,AppointmentID,status,Doctor))
    fw.close()


def readappointment():
    users = open("appointment.txt",'r')
    extract = input("Please input appointment ID")
    for each_line in users:
        (patientID,AppointmentID,status,Doctor) = each_line.split()

        if (AppointmentID == extract):
            print(patientID,AppointmentID,status,Doctor)
        else:
            print("Appointment Id not matched")
    users.close()

def appointment2():

    patientID=input(" Enter your patientID")
    AppointmentID=input("Enter your AppointmentID")
    Doctor=input("Choose your doctor\n Dr.kelvin\n Dr.Scott \n Dr.Nitesh \n Dr.Richard")
    status = input("Complete or Appointment")
    appointment2w(patientID, AppointmentID, status,Doctor)


#textfile="treatmentplan.txt"  for record treatment plan

def Treatmentwrite(TreatmentID,patientID,Complaint,Treatment):
    fw = open('treatmentplan.txt', "a")
    fw.write("%1s%20s%20s%20s\n" % (TreatmentID,patientID,Complaint,Treatment))
    fw.close()

def patientTreatmentPlan():

    TreatmentID=input("Enter your Treatment ID:")
    patientID=input("Enter your patientID:")
    Complaint=input("Enter your complaint:")
    Treatment=input("Enter given Treatment:")
    Treatmentwrite(TreatmentID,patientID,Complaint,Treatment)

#textfile="invoice.txt" for record invoicing record

def invoicingw(extract,invoiceID,TreatmentID,name,recebill):
        fw = open('invoicing.txt', "a")
        fw.write("%1s%20s%20s%20s%20s\n" % (extract,invoiceID,TreatmentID,name,recebill))
        fw.close()

def invoicing():

    extract = input("Please input patient ID")
    invoiceID=input("Enter your invoiceID:")
    TreatmentID=input("Enter your TreatmentId:")
    name=input("Enter your name")
    recebill = input("Please enter the bill amount in Rs.:-")
    print(recebill)
    invoicingw(extract,invoiceID,TreatmentID,name,recebill)
    print("Thank you")

def readinvoiceID():
    users = open("invoicing.txt",'r')
    extract = input("Please input invoice ID")
    for each_line in users:
        (extract,invoiceID,TreatmentID,name,recebill) = each_line.split()

        if (invoiceID == extract):
            print(extract,invoiceID,TreatmentID,name,recebill)
        else:
            print("Invoice ID not found")
    users.close()

def searchinvoice():
        readinvoiceID()
        print("Thank you")

#textfile="receipt.txt" for record receipt payemnt

def receiptw(extract,TreatmentID, name, amount):
    fw = open('receipt.txt', "a")
    fw.write("%1s%20s%20s%20s\n" % (extract,TreatmentID,name,amount))
    fw.close()

def receipt():

    extract = input("Please input patient ID")
    TreatmentID=input("Enter your TreatmentId:")
    name=input("Enter your name")
    recebill = input("Please enter the bill amount in Rs.:-")
    print(recebill)
    receiptw(extract,TreatmentID,name,recebill)
    print("Thank you")

def logout():
    print("logout")


def last():
    while True:
        print("Are you \n1.Secretary\n2.Physician\n3.Accountant\n4.logout\n")
        choose = input("Enter Choice?")
        number = int(choose)
        if (number == 1):
            print("Only Secretary can login\n")
            Secretarylogin()
            users=input("now for your menu press Enter")
            while True:
                print("1.Register Patient\n2.View Patient\n3.Exit")
                choose = input("Enter Choice?")
                number = int(choose)

                if (number == 1):
                    registration()
                elif (number == 2):
                    read()

                elif(number==3):
                    break
                    print("exit")
                else:
                    print("wrong choice")


        elif(number==2):
            post = input("only physician can login")
            print(post)
            physicianlogin()
            while True:
                print("1.Appointment\n2.View Appointment\n3.Treatment Plan\n4.Exit")
                choose = input("Enter Choice?")
                number = int(choose)
                if (number == 1):
                    appointment2()
                elif (number == 2):
                    readappointment()

                elif (number == 3):
                    patientTreatmentPlan()

                elif (number == 4):
                    break
                    print("exit")
                else:
                    print("wrong choice")

        elif (number == 3):
            post = input("only accountant can login")
            print(post)
            accountantlogin()
            print("you are login as a accountant\n")
            while True:
                users = input("1.Invoicing\n2.View Record\n3.Receipt Payment\n4.exit\n")
                number = int(users)
                if (number == 1):
                    invoicing()
                elif (number == 2):
                    searchinvoice()
                elif(number==3):
                    receipt()
                elif(number==4):
                    break
                    print("Exit")
                else:
                    print("wrong choice")

        elif(number==4):
            logout()
            break

        else:
            print("wrong choice")

#main part or module
last()
