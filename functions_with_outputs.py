# Functions with Outputs

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You did not provide valid inputs"
  title_case_f_name = f_name.title()
  title_case_l_name = l_name.title()
  return f"Result: {title_case_f_name} {title_case_l_name}"

print(format_name(input("what is your first name? "), input("What is your last name? ")))
