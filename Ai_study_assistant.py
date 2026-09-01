print("🤖 AI STUDY ASSISTANT")
print("--------------------")

name = input("Enter your name: ")

while True:

    topic = input("\nEnter the topic you want to study: ")
    
    if topic.lower() == "exit":
       print("\nThank you for using AI Study Assistant! 👋")
       break

    print("\nWelcome! Choose an option:")
    print("[1] Explain a topic")
    print("[2] Make a summary")
    print("[3] Generate quiz questions")

    choice = input("\nYour choice: ")

    # =========================
    # EXPLAIN
    # =========================

    if choice == "1" or choice.lower() == "explain":

        print("\nYou selected: Explain a topic")
        print("Your topic is:", topic)

        if topic.lower() == "python":
            print("Python is a programming language used to build software, analyze data, and develop AI applications.")

        elif topic.lower() == "ai":
            print("AI is the field of computer science that enables machines to perform tasks that normally require human intelligence.")

        elif topic.lower() == "machine learning" or topic.lower() == "ml":
            print("Machine Learning is a branch of AI where computers learn patterns from data to make predictions or decisions.")

        elif topic.lower() == "data science" or topic.lower() == "ds":
            print("Data Science uses data, statistics, programming, and machine learning to find useful insights and solve problems.")

        else:
            print("Sorry, I don't have an explanation for this topic yet.")


    # =========================
    # SUMMARY
    # =========================

    elif choice == "2" or choice.lower() == "summary":

        print("\nYou selected: Make a summary")

        if topic.lower() == "python":
            print("Python is a simple and powerful programming language used in data science, AI, automation, and software development.")

        elif topic.lower() == "ai":
            print("Artificial Intelligence is a field of computer science that focuses on creating systems that can perform tasks requiring human-like intelligence.")

        elif topic.lower() == "machine learning" or topic.lower() == "ml":
            print("Machine Learning is a part of AI that allows computers to learn patterns from data and use them to make predictions or decisions.")

        elif topic.lower() == "data science" or topic.lower() == "ds":
            print("Data Science combines programming, statistics, and data analysis to discover useful patterns and insights from data.")

        else:
            print("Sorry, I don't have a summary for this topic yet.")


    # =========================
    # QUIZ
    # =========================

    elif choice == "3" or choice.lower() == "quiz":

        print("\nYou selected: Generate quiz questions")

        # -------------------------
        # PYTHON QUIZ
        # -------------------------

        if topic.lower() == "python":

            score = 0

            print("\nQuestion 1: What is Python?")
            print("[1] A programming language")
            print("[2] A database")
            print("[3] An operating system")
            print("[4] A web browser")

            answer = input("\nYour answer: ")

            if answer == "1":
                print("Correct! 🎉")
                score = score + 1
            elif answer in ["2", "3", "4"]:
                print("Incorrect.")
            else:
                print("Invalid answer.")

            print("\nQuestion 2: Which symbol is used for comments in Python?")
            print("[1] //")
            print("[2] #")
            print("[3] <!-- -->")
            print("[4] **")

            answer = input("\nYour answer: ")

            if answer == "2":
                print("Correct! 🎉")
                score = score + 1
            elif answer in ["1", "3", "4"]:
                print("Incorrect.")
            else:
                print("Invalid answer.")

            print("\nQuestion 3: Which function is used to display output in Python?")
            print("[1] input()")
            print("[2] output()")
            print("[3] print()")
            print("[4] display()")

            answer = input("\nYour answer: ")

            if answer == "3":
                print("Correct! 🎉")
                score = score + 1
            elif answer in ["1", "2", "4"]:
                print("Incorrect.")
            else:
                print("Invalid answer.")

            print("\nQuiz Completed! 🎉")
            print("Your Score:", score, "/ 3")


        # -------------------------
        # AI QUIZ
        # -------------------------

        elif topic.lower() == "ai":

            score = 0

            print("\nQuestion 1: What does AI stand for?")
            print("[1] Artificial Intelligence")
            print("[2] Automated Internet")
            print("[3] Advanced Information")
            print("[4] Applied Innovation")

            answer = input("\nYour answer: ")

            if answer == "1":
                print("Correct! 🎉")
                score = score + 1
            elif answer in ["2", "3", "4"]:
                print("Incorrect.")
            else:
                print("Invalid answer.")

            print("\nQuestion 2: Which is an example of AI?")
            print("[1] Calculator")
            print("[2] Voice assistant")
            print("[3] Keyboard")
            print("[4] USB cable")

            answer = input("\nYour answer: ")

            if answer == "2":
                print("Correct! 🎉")
                score = score + 1
            elif answer in ["1", "3", "4"]:
                print("Incorrect.")
            else:
                print("Invalid answer.")

            print("\nQuestion 3: AI systems can learn from?")
            print("[1] Data")
            print("[2] Electricity only")
            print("[3] Keyboard buttons")
            print("[4] Computer screen")

            answer = input("\nYour answer: ")

            if answer == "1":
                print("Correct! 🎉")
                score = score + 1
            elif answer in ["2", "3", "4"]:
                print("Incorrect.")
            else:
                print("Invalid answer.")

            print("\nQuiz Completed! 🎉")
            print("Your Score:", score, "/ 3")


        # -------------------------
        # MACHINE LEARNING QUIZ
        # -------------------------

        elif topic.lower() == "machine learning" or topic.lower() == "ml":

            score = 0

            print("\nQuestion 1: What is Machine Learning?")
            print("[1] A type of database")
            print("[2] A branch of AI that learns from data")
            print("[3] A programming language")
            print("[4] An operating system")

            answer = input("\nYour answer: ")

            if answer == "2":
                print("Correct! 🎉")
                score = score + 1
            elif answer in ["1", "3", "4"]:
                print("Incorrect.")
            else:
                print("Invalid answer.")

            print("\nQuestion 2: Machine Learning mainly uses?")
            print("[1] Data")
            print("[2] Paint")
            print("[3] Music")
            print("[4] Keyboard")

            answer = input("\nYour answer: ")

            if answer == "1":
                print("Correct! 🎉")
                score = score + 1
            elif answer in ["2", "3", "4"]:
                print("Incorrect.")
            else:
                print("Invalid answer.")

            print("\nQuestion 3: Which is a type of Machine Learning?")
            print("[1] Supervised Learning")
            print("[2] Manual Learning")
            print("[3] Screen Learning")
            print("[4] Keyboard Learning")

            answer = input("\nYour answer: ")

            if answer == "1":
                print("Correct! 🎉")
                score = score + 1
            elif answer in ["2", "3", "4"]:
                print("Incorrect.")
            else:
                print("Invalid answer.")

            print("\nQuiz Completed! 🎉")
            print("Your Score:", score, "/ 3")


        # -------------------------
        # DATA SCIENCE QUIZ
        # -------------------------

        elif topic.lower() == "data science" or topic.lower() == "ds":

            score = 0

            print("\nQuestion 1: What is the main purpose of Data Science?")
            print("[1] To design computer hardware")
            print("[2] To create mobile applications")
            print("[3] To extract useful insights from data")
            print("[4] To manage computer networks")

            answer = input("\nYour answer: ")

            if answer == "3":
                print("Correct! 🎉")
                score = score + 1
            elif answer in ["1", "2", "4"]:
                print("Incorrect.")
            else:
                print("Invalid answer.")

            print("\nQuestion 2: Which language is widely used in Data Science?")
            print("[1] Python")
            print("[2] HTML")
            print("[3] CSS")
            print("[4] XML")

            answer = input("\nYour answer: ")

            if answer == "1":
                print("Correct! 🎉")
                score = score + 1
            elif answer in ["2", "3", "4"]:
                print("Incorrect.")
            else:
                print("Invalid answer.")

            print("\nQuestion 3: Data Science works mainly with?")
            print("[1] Data")
            print("[2] Paintings")
            print("[3] Music instruments")
            print("[4] Electricity")

            answer = input("\nYour answer: ")

            if answer == "1":
                print("Correct! 🎉")
                score = score + 1
            elif answer in ["2", "3", "4"]:
                print("Incorrect.")
            else:
                print("Invalid answer.")

            print("\nQuiz Completed! 🎉")
            print("Your Score:", score, "/ 3")


        else:
            print("\nSorry, I don't have a quiz for this topic yet.")


    # =========================
    # INVALID OPTION
    # =========================

    else:

        print("\nInvalid choice.")
        print("Please choose 1, 2, or 3.")


    # =========================
    # ASK FOR ANOTHER TOPIC
    # =========================

    again = input("\nDo you want to study another topic? (yes/no): ")

    if again.lower() != "yes":

        print("\nThank you for using AI Study Assistant! 👋")
        print("Keep learning, " + name + "! 🚀")
        break

    