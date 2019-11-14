# Submit initial value(changeble) into form by default
# Pass initial into GET section of form [form = CustomerForm()]
# The dictionary key must be a form field 
form = CustomerForm(initial={
        "name" : "Default Name",
        "email" : "Default Email"
    })