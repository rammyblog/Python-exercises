"""Kevin is a freelance video producer who makes TV commercials for local businesses. When he makes a
commercial, he usually films several short videos. Later, he puts these short videos together to make the final commercial.
He has asked you to write the following two programs.
1. A program that allows him to enter the running time (in
seconds) of each short video in a project. The running
times are saved to a file.
2. A program that reads the contents of the file, displays
the running times, and then displays the total running
time of all the segments.
Here is the general algorithm for the first program, in
pseudocode:
Get the number of videos in the project.
Open an output file.
For each video in the project:
Get the video's running time.
Write the running time to the file.
Close the file."""


import os


def write_running_time():
    name_of_project = input("What is the name of the Project")
    if not os.path.exists(name_of_project + ".txt"):
        number_of_videos = int(input("How many videos do you have in this project"))
        project_file = open(name_of_project + ".txt", 'w')
        count = 1
        for video in range(number_of_videos):
            # Get Running time
            print("What is the running time for short video in secs", count)
            running_time = float(input())
            project_file.write(str(running_time) + '\n')
            count += 1
    else:
        print("File already Exist! Kindly choose another name for the project")
        write_running_time()
    print("The running time has been stored in", name_of_project + ".txt")
    project_file.close()


def read_running_time():
    filename = input("Enter the name of the file you want to open")
    try:
        project_file = open(filename + ".txt", "r")
        total_running_time = 0.0
        count = 0
        # running_time = project_file.read()
        for line in project_file:
            run_time = float(line)
            count += 1
            print("The running time of Short Video " + str(count) + " in " + filename, str(run_time))
            total_running_time += run_time
        project_file.close()
        print(
            "The Total Running time of All THe Short Video in " + filename + " is " + str(total_running_time) + " secs")
    except FileNotFoundError:
        print("Error! No such file Named:" + filename + ".txt")
        print("Try Again Below")

        read_running_time()


def append_running_time():
    name_of_project = input("What is the name of the Project")
    if os.path.exists(name_of_project + ".txt"):
        number_of_videos = int(input("How many videos do you want to add to this project"))
        project_file = open(name_of_project + ".txt", 'a')
        count = 1
        for video in range(number_of_videos):
            # Get Running time
            print("What is the running time for short video in secs", count)
            running_time = float(input())
            project_file.write(str(running_time) + '\n')
            count += 1
    else:
        print("File does not exist!")
        print("Enter 1 To create a new file \n Enter 2 to try again  ")
        append_option = int(input())
        if append_option == 1:
            write_running_time()
        elif append_option == 2:
            append_running_time()
        else:
            print("Wrong Input")
            main()
    print("The running time has been stored in", name_of_project + ".txt")
    project_file.close()


def main():
    print("Hello Kevin, Trust you are having a wonderful day!")
    print()
    print("What can i do for you today!")
    print("1. Create a new file to store short videos running time of a project")
    print("2. Get the Running time of all short videos in a project")
    print("3. Add to the number of short videos in a project")
    print("Enter your choice below")
    choice = int(input())
    if choice == 1:
        write_running_time()
    if choice == 2:
        read_running_time()
    if choice == 3:
        append_running_time()


main()
