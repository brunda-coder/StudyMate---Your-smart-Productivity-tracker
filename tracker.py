import json
from utilis import save_data, load_data

class ProgressTracker:
    def__init__(self, file_path='data/progress.json'):
        self.file_path = file_path
        self.progress = load_data(file_path)
     
    def add_topic(self, topic):
        if topic not in self.progress:
            self.progress[topic] = "Not completed"
            save_data(self.file_path, self.progress)
            print(f"Added topic: {topic} )
        else:
            print(f"Topic {topic} already exists.")
          
 def mark_completed(self, topic):
    if topic in self.progress:

        self.progress[topic] = "Completed"
        save_data(self.file_path, self.progress)
        print(f"Marked {topic} as completed.")
    else:
        print("Topic not found.")

  def view_progress(self):
      if not self.progress:
        print("No topics added yet.")
        else:
            for topic, status in self.progress.items():
                print(f"{topic} - {status}")

    

      





















































































































































































   if topic in self.progress:
                        self.progress[topic] = "Completed"
                                    save_data(self.file_path, self.progress)
                                                print(f"Marked {topic} as completed.")
                                                        else:
                                                                    print("Topic not found.")

                                                                        def view_progress(self):
                                                                                if not self.progress:
                                                                                            print("No topics added yet.")
                                                                                                    else:
                                                                                                                for topic, status in self.progress.items():
                                                                                                                                print(f"{topic} - {status}")




