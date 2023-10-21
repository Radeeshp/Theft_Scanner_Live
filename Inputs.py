class Address_locations:
    def __init__(self):
        self.Destination_T='D:\\EDUCATION\\PROJECTS\\Theft_Scanner_Live\\Detected'
        self.Destination_F="D:\\EDUCATION\\PROJECTS\\Theft_Scanner_Live\\Not Detected"
        self.KNOWN_FACES_DIR = "D:\\EDUCATION\\PROJECTS\\Theft_Scanner_Live\\known_faces"
        self.UNKNOWN_FACES_DIR = "D:\\EDUCATION\\PROJECTS\\Theft_Scanner_Live\\unknown_faces"
        self.Face_Not_Clear="D:\\EDUCATION\\PROJECTS\\Theft_Scanner_Live\\Face_not_clear"
        self.Face_train_vid="D:\\EDUCATION\\PROJECTS\\Theft_Scanner_Live\\Input_vid_known_face"
        self.motion_detected="D:\\EDUCATION\\PROJECTS\\Theft_Scanner_Live\\Motion_Detected"
        self.Input_video_location="D:\\Education\\PROJECTS\\Theft_Scanner_Live\\Inputs.py"
        
    def Locations_input(self):
        print("Do you need to change any of the address locations of files and folders??")
        print("\nYes-1\nNo-2\n")
        if input()==1:
            print("If the address is E:\EDUCATION\PROJECTS\Theft_Scanner\Detected\nEnter it as E:\\EDUCATION\\PROJECTS\\Theft_Scanner\\Detected")
            self.Destination_T=input("\nDestination_T:")
            self.Destination_F=input("\nDestination_F:")
            self.KNOWN_FACES_DIR = input("\nknown_faces")
            self.UNKNOWN_FACES_DIR =input("\nunknown_faces:")
            self.Face_Not_Clear=input("\nFace_not_clear:")
            self.Face_train_vid=input("\nInput_vid_known_face:")
            self.motion_detected=input("\nMotion_detected:")
            self.Input_video_location=input("\nInput_video_location:")
            
            