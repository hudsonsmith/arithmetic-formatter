def arithmetic_arranger(problems, show_answers=False):
    tops = []
    bottoms = []
    banners = []
    answers = []
    
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        problem = problem.split(" ")

        # Validating
        if problem[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Size validation.
        elif len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Type Validation. Can only be integer.
        try:
            problem[0] = int(problem[0])
            problem[2] = int(problem[2])
            
        except ValueError:
            return "Error: Numbers must only contain digits."

        # If the interpreter is still parsing, the problem must be valid.

        # Step 1: Find the biggest number.
        both = "both"
        biggest = None
        
        if problem[0] > problem[2]:
            biggest = 0

        else:
            biggest = 2

        # Step 2: render each line and append to the array.
        
        # If the biggest is equal to the first item in the array, put two spaces before it.
        if biggest == 0:
            tops.append(f"  {problem[0]}")


        # If the first item is not the biggest, we need to subtract the length of the first from the second and add two (because there is no operator sign) to get the number of spaces.
        
        # NOTE: I am turning the integer into a string and getting the length of it in order to see how many digits long it is.
        else:
            spaces = 2 + (len(str(problem[2])) - len(str(problem[0])))
            tops.append(f"{' ' * spaces}{problem[0]}")


        # Rendering bottoms.
        # NOTE: Problem[1] is the operator.
        if biggest == 2:
            bottoms.append(problem[1] + " " + str(problem[2]))

        else:
            spaces = 1 + (len(str(problem[0])) - len(str(problem[2])))
            bottoms.append(f"{problem[1]}{spaces * ' '}{problem[2]}")

        
        # Render the banners.
        banner = f"{'-' * (2 + len(str(problem[biggest])))}"
        banners.append(banner)


        # Render show answer, optional.
        if show_answers == True:
            digits = len(str(problem[biggest])) + 2

            answer = None

            if problem[1] == "+":
                answer = problem[0] + problem[2]
            
            else:
                answer = problem[0] - problem[2]
            
            print(answer)
            spaces = digits - len(str(answer))
            
            answers.append(f"{spaces * ' '}{answer}")
            
        
    # Finally, loop through all the arrays and print out the ouput side by side.
    formatted_questions = ""
    
    for line in tops:
        formatted_questions += f"{line}    "

    formatted_questions += "\n"
    
    for line in bottoms:
        formatted_questions += f"{line}    "
    
    formatted_questions += "\n"
    
    for line in banners:
        formatted_questions += f"{line}    "
    
    if show_answers == True:
        formatted_questions += "\n"

        for line in answers:
            formatted_questions += f"{line}    "

    return formatted_questions
