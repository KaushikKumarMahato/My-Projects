##### Smart Expense Management System


### Data storages
dict_main = {}
split_per_item = {}
split_per_person = {}
expense_of_person ={}


### Collect data
def expense_details():

    while True:
        what_expense = input("\n Enter 'expense name' or type 'done' to stop : ")
        if what_expense.lower() == "done":
            break
        who_paid = input(f"Enter name who paid for {what_expense} : ")
        amount = float(input(f"Enter amount paid for {what_expense} : "))

        dict1 = {who_paid.lower() : amount}
        dict_main[what_expense.lower()] = dict1

    if dict_main:
        print("\n")
        split()
    else:
        print("\n Please enter some data!!\n")
        expense_details()
    
    
### Count no. of persons for split  
def person_count():

    n = 0
    name_set = set()

    while True:
                name = input("Enter 'name' or type 'done' to stop : ")
                
                if name.lower() == 'done':
                    break

                name_set.add(name)

                n+=1

                if name not in split_per_person:
                    split_per_person[name] = 0
                    
    name_list = list(name_set)

    return n,name_list


### Calculate expenses per person
def split():
    for k,v in dict_main.items():
        for k1 , v1 in v.items():
            print(f"\n ==>{k1} paid {v1} for {k}.")
            print(f"Enter name of the persons among which {k} will split :- \n")

            

            n,name_list = person_count()

            while n<2 :
                print(n)
                print(name_list)
                print("Enter name of two persons atleast!!")
                n,name_list= person_count()

            expense_of_person[k] = name_list

            split_amount= v1/n
            split_per_item[k] = split_amount

            for i in range(n):
                split_per_person[name_list[i]] += split_amount

    print()
    for k,v in split_per_item.items():
        for k1 in dict_main[k].keys():
            print(f"{k} per person : '{v:.2f}' have to pay to {k1}.")


    print("\n\nExpense per person :-\n")
    for k,v in split_per_person.items():
        expenses = []
        for k1 ,v1 in expense_of_person.items():
            if k in v1:
                expenses.append(k1)
            
        print(f"{k} : total {v:.2f} Rupees for {expenses}")
       



### Start

print(f"{'*'*10}SMART EXPENSE MANAGEMENT SYSTEM{'*'*10} ")
expense_details()
