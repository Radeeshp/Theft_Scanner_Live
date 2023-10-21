
# imports has all the common required imports 
from imports import *
from Face_Recog_Func import Face_Recognition_func
from Face_Detect_Func import detectfaces
from Face_Scanner_Func import create_folder
from Face_Scanner_Func import create_known_face
from Face_Scanner_Func import train
from Inputs import Address_locations
    
def face_database():

    while True:
        if input("Enter 1 to create database for new person:")=='1':
        
            location,name=create_folder(address.KNOWN_FACES_DIR)
            create_known_face(location,address.Face_train_vid)
            train(location,name)
            print("/nFace database has been created for the given input")

        else:break
    print("\nFace and motion detection is starting\n")


#Call's the Face_Recognition_func 
def face_recog():
    Face_Recognition_func(address.Destination_T,
                          address.Destination_F,
                          address.KNOWN_FACES_DIR,
                          address.UNKNOWN_FACES_DIR,
                          address.Face_Not_Clear)
    
    
if __name__=="__main__":
    
    os.system('cls')
   
    print("**********************Welcome to Theft_Scanner*******************************\n\n")
    
    print("**********************You Have Accessed The Facial And Motion Scannner and Detector*******************************\n\n")
    address=Address_locations()

    print("Do you need to change any of the address locations of files and folders??")
    print("\nYes-1\nNo-2\n")
    if input()==1:
        address.Locations_input()
    else:
        pass
    

    #Function called to create face database for new people or strangers.
    face_database()

    face_recog()

print("\n*******************Program Has Ended********************")
#video_capture.release()
cv2.destroyAllWindows()
