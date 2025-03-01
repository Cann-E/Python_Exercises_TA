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
        