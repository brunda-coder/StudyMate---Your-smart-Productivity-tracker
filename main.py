from tracker import ProgressTracker

def main():
    tracker = ProgressTracker()

    while True:
        print("\n--- Python Progress Tracker ---")
        print("1. View Progress")
        print("2. Add New Topic")
        print("3. Mark Topic as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            tracker.view_progress()
        elif choice == '2':
             topic = input("Enter topic name:")                         
             tracker.add_topic(topic)
        elif choice == '3':
            topic = input("Enter topic name to mark as completed")
            tracker.mark_completed(topic)
        elif choice == '4':
            print("Exiting tracker. Keep learning and coding!")
            break
        else:
            print("Invalid choice. Please try again! ") 
if__name_ == "__main__":
    main()

    


                                                              
                                                                                                                                   
                                                                                                                                                
                                                                                                                                                   
                                                                                                                                                                 
                                                                                                                                                                                  
                                                                                                                                                                

                                                                                                                                                                                           
                                                                                                                                                                             