from pyscript import document, display

# List of subject IDs used to get input values from HTML
subs = ["sci", "eng", "ict", "math", "fil", "pe"]

# Corresponding number of units (or weight) for each subject
units = (5, 5, 2, 5, 3, 1)

# Main function that runs when the user clicks the "Calculate" button
def do_calc(e):

    # Get student's first and last name from HTML input fields
    f_name = document.getElementById("fname").value
    l_name = document.getElementById("lname").value

    # Get the scores entered for each subject
    sci_score = int(document.getElementById(subs[0]).value)
    eng_score = int(document.getElementById(subs[1]).value)
    ict_score = int(document.getElementById(subs[2]).value)
    math_score = int(document.getElementById(subs[3]).value)
    fil_score = int(document.getElementById(subs[4]).value)
    pe_score = int(document.getElementById(subs[5]).value)

    # Multiply each score by its corresponding unit to get the weighted score
    sci_final = sci_score * units[0]
    eng_final = eng_score * units[1]
    ict_final = ict_score * units[2]
    math_final = math_score * units[3]
    fil_final = fil_score * units[4]
    pe_final = pe_score * units[5]

    # Calculate the total number of units (sum of all subject units)
    total_units = units[0] + units[1] + units[2] + units[3] + units[4] + units[5]

    # Compute the General Weighted Average (GWA)
    # Formula: (sum of all weighted scores) / (total number of units)
    average = (sci_final + eng_final + ict_final + math_final + fil_final + pe_final) / total_units

    # Clear any previous output
    document.getElementById("output").innerHTML = ""

    # Display the student's name
    display(f"Name: {f_name} {l_name}", target="output")

    # Display each subject's raw score
    display("Scores:", target="output")
    display(f"{subs[0]}: {sci_score}", target="output")
    display(f"{subs[1]}: {eng_score}", target="output")
    display(f"{subs[2]}: {ict_score}", target="output")
    display(f"{subs[3]}: {math_score}", target="output")
    display(f"{subs[4]}: {fil_score}", target="output")
    display(f"{subs[5]}: {pe_score}", target="output")

    # Display the computed General Weighted Average
    display(f"General Weighted Average: {average}", target="output")


# More efficient code.
'''
subs = ["sci", "eng", "ict", "math", "fil", "pe"]
units = (5, 5, 2, 5, 3, 1)

def do_calc(e):

    f_name = document.getElementById("fname").value
    l_name = document.getElementById("lname").value


    results_raw = {}
    result_flist = []

    # Getting scores for computation
    index = 0
    for x in subs:
        subject_score = int(document.getElementById(x).value)
        results_raw[x] = subject_score
        score_unit = units[index]

        final_scr = subject_score * score_unit
        result_flist.append(final_scr)
        index += 1
    
    # Average
    average = sum(result_flist)/sum(units)

    # Displaying
    document.getElementById("output").innerHTML = ""

    display(f"Name: {f_name} {l_name}", target="output")

    for subject in results_raw:
        display(f"{subject}: {results_raw[subject]}", target="output")
    
    display(f"General Weighted Average: {average}", target="output")

'''