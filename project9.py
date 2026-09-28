total_homework  = 4
original_count = total_homework
print("You have {original_count} homeworks to finish!")
completed_count = 0
task_num = 1
while task_num <= total_homework:
    if task_num == 1:
        next_task = "Maths worksheet"
    elif task_num == 2:
        next_task = "Science reading"
    elif task_num == 3:
        next_task = "English writing"
    else: 
        next_task = "Coding homework"

    answer = input("Have you finished {next_task}? (yes/no)")
    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("Great job, Homework task completed")
    else: 
        print("Okay, go finish the homework")
    print("Homeworks left: ", total_homework - completed_count)
    print()

print("===== ALL HOMEWORK COMPLETED =====")
print("Great work finishing your homework today")

print("Now let's safely peek at an infinte loop...")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("(Stopping here on purpose - a real infinte loop never stops on its own!)")
        break

print("\n===== HOMEWORK SUMMARY =====")
print("Homework Completed: ", completed_count)
print("Homework Assigned: ", original_count)
print("Homework Left: ", total_homework)
print("==============================")


