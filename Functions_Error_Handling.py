def validate_product(product_name,product_price,product_category):
    if not validate_product_name(product_name):
        raise ValueError("Wrong Product name")
    
    if not validate_product_price(product_price):
        raise ValueError("Wrong Price")
    
    if not validate_product_category(product_category):
        raise ValueError("Wrong Cat")
    
    return True

def register_product(product_name,product_price,product_category):
    if validate_product(product_name,product_price,product_category):
        product={"Product Name":product_name,"Product Price":product_price,"Product Category":product_category}
        return product
    else:
        return False
    
    
    #--------------------------------------------------------
    
    
    
    
def validate_student(student_name,student_age,student_grade):
    if not validate_student_name(student_name):
        raise ValueError("Student name error")
    if not validate_student_age(student_age):
        raise ValueError("sTUDENT AGE WRONG")
    if not validate_student_grade(student_grade):
        raise ValueError("Student grade wrong")
    
    return True


def register_student(student_name,student_age,student_grade):
    try:
        validate_student(student_name,student_age,student_grade)
        return {"Name":student_name,"Age":student_age,"Grade":student_grade}
        
    except ValueError as e:
        print(f"Error:{e}")
        return False
        
        #--------------------------------------------
        
        
        
ALLOWED_DEPARTMENTS = ["HR", "Engineering", "Marketing", "Sales", "Finance"]

def validate_employee_name(name):
    """Ensures the employee's name is at least 3 characters long."""
    return isinstance(name, str) and len(name) >= 3

def validate_employee_age(age):
    """Ensures the employee's age is between 18 and 65."""
    return isinstance(age, int) and 18 <= age <= 65

def validate_employee_department(department):
    """Ensures the employee's department is in the allowed list."""
    return department in ALLOWED_DEPARTMENTS
        
        
        
def validate_employee(employee_name,employee_age,employee_department):
    if not validate_employee_name(employee_name):
        raise ValueError("Wrong Name INPUT")
    if not validate_employee_age(employee_age):
        raise ValueError("Wrong AGE INPUT")    
    if not validate_employee_department(employee_department):
        raise ValueError("WRONG DEPARTMENT INPUT")
    
    return True

def register_employee(employee_name,employee_age,employee_department):
    try:
        validate_employee(employee_name,employee_age,employee_department)
        return {"name":employee_name,"age":employee_age,"department":employee_department}
    
    except ValueError as e:
        print(f"Error:{e}")
        return False#11
        