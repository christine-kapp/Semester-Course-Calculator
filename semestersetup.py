# Student Semester Course Calculator


# major selection

print("Hello. Welcome to Student Semester Course Calculator.")
print("This application version is currently only available for Computer Science majors. Once a later version is available it will be accessible to a larger audience.")
print("To begin you will be prompted to enter your current major.")
print("Enter your entire major using capital letters for the first letter of each word.")
print("Example: Computer Science")
major_selection = input("What is your current major: ")


# version for computer science only

def main():

    if major_selection == "Computer Science":
    
        print("You have selected: Computer Science")

    # other majors are currently available, error message will appear

    else:

        print("Current version of the application only supports the following majors: Computer Science.")
        print("Stay tuned for future version for other options.")

main()


# math


def main():

# computer science

    if major_selection == "Computer Science":

        cs_math = input("Enter the course number of the highest Math course you will have completed before your next semester: ")
        print("You have selected: ",cs_math)

    if cs_math == "0702":

        print("The next reccomended Math course is 1021: College Algebra")

    if cs_math == "1021":

        print("The next reccomended Math course is 1022: Precalculus")

    if cs_math == "1022":

        print("The next reccomended Math course is 1041: Calculis I")

    if cs_math == "1041":

        print("The next reccomended Math course is 1042: Calculus II")

    elif cs_math == "1042":
        
        print("Math credits complete. There are no further reccomended courses.")

main()


# english


print("You will be prompted to enter information regarding your English course completion next.")
print("Remember: This does not include Intellectual Heritage courses.")


def main():

# computer science

    if major_selection == "Computer Science":

        cs_english = input("Enter the course number of the highest English course you will have completed before your next semester: ")
        print("You have selected: ",cs_english)

    if cs_english == "0701":

        print("The next reccomended English course is 0802: Analytical Reading And Writing")

    elif cs_english == "0802":

        print("English credits complete. There are no further reccomended courses.")

main()


# intellectual heritage


def main():

# computer science

    if major_selection == "Computer Science":

        cs_intheritage = input("Enter the course number of the highest Intellectual Heritage course you will have completed before your next semester: ")
        print("You have selected: ",cs_intheritage)

    if cs_intheritage == "0851":

        print("The next reccomended Intellectual Heritage course is 0852: Intellectual Heritage II")

    elif cs_intheritage == "0852":

        print("Intellectual heritage credits complete. There are no further reccomended courses.")

main()


# cis


def main():

# computer science

    if major_selection == "Computer Science":

        cs_cis = input("Enter the course number of the highest Programming course you will have completed before your next semester: ")
        print("You have selected: ",cs_cis)

    if cs_cis == "1051":

        print("The next reccomended CIS courses are 1166 and 1068: Mathematical Concepts In Computing I and Program Design And Abstraction")

    elif cs_cis == "1057":

        print("The next reccomended CIS courses are 1166 and 1068: Mathematical Concepts In Computing I and Program Design And Abstraction")

    elif cs_cis == "1166":

        print("The next reccomended CIS course is 2168: Data Structures")

    elif cs_cis == "1068":

        print("The next reccomended CIS course is 2168: Data Structures")

    elif cs_cis == "2168":

        print("The next reccomended CIS courses are 2166 and 3207: Mathematical Concepts In Computing II and Introduction To Systems Programming And Operating Systems")

    elif cs_cis == "2166":

        print("The next reccomended CIS course is 3223: Data Structures And Algorithms")

    elif cs_cis == "3207":

        print("The next reccomended CIS course is 3223: Data Structures And Algorithms")

    elif cs_cis == "3223":

        print("The next reccomended CIS course is 3296: Software Design")

    elif cs_cis == "3296":

        print("The next reccomended CIS courses are 4397 and 4398: Indepedent Research In Computer Science and Projects In Computer Science")

    elif cs_cis == "4397":

        print("CIS credits complete. There are no further reccomended courses.")

    elif cs_cis == "4398":

        print("CIS credits complete. There are no further reccomended courses.")


main()


# intro to academics in cs


print("You will be prompted to enter information regarding your Intro To Academics In Computer Science course completion next.")
print("Answer with Yes or No.")


def main():

# computer science

    if major_selection == "Computer Science":

        cs_introcs = input("Have you completed 1001: Introduction To Academics In Computer Science: ")
        print("You have selected: ",cs_introcs)
        
    if cs_introcs == "Yes":

        print("Intro To Academica In Computer Science credit complete. There are no further reccomended courses")
        
    if cs_introcs == "No":

        print("The next reccomended course is 1001: Introduction To Academics In Computer Science")


main()


# cst first year seminar


print("You will be prompted to enter information regarding your CST First Year Seminar course completion next.")
print("Answer with Yes or No.")


def main():

# computer science

    if major_selection == "Computer Science":

        cs_introcs = input("Have you completed 1001: CST First Year Seminar: ")
        print("You have selected: ",cs_introcs)
        
    if cs_introcs == "Yes":

        print("CST First Year Seminar credit complete. There are no further reccomended courses")
        
    if cs_introcs == "No":

        print("The next reccomended course is 1001: CST First Year Seminar")

main()



































