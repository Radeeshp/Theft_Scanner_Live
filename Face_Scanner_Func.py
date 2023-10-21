#This code is used to generate the known face database from a video input of the user which 
#contains the video of a known face


from imports import *
import pickle
# Provide the location path
def create_folder(location):
    name=input("Enter your name: ")
# Define the path for the new folder
    try:
        # Create the folder in the given path
        os.mkdir(location+"\\"+name)
        
    except OSError:
        print ("Creation of the directory %s failed" % location+name)
    else:
        print ("Successfully created the directory %s " % location+name)
    return location+"\\"+name,name
#To create a database of photos of a person from the video the input.
def create_known_face(database_location,video_location):
    #path to the input video
    
    name=input("\nEnter the file name with its extension:")
    video_capture = cv2.VideoCapture(video_location+"\\"+name)
    frame_count=0
    no_saved_frame=0
    check = True
    while no_saved_frame<100 and check is True:
        frame_count+=1
        #read the video
        check,frame=video_capture.read()
        if check is True and frame_count%5==0:
        #writing the video as frames in the video as frame in the folder 
            cv2.imwrite(database_location+"\\"+str(frame_count)+".jpg",frame)
            no_saved_frame+=1
    print("Extracted")   
def train(KNOWN_FACES_DIR,name):
    known_faces = []
    known_names = {}
    
    # We oranize known faces as subfolders of KNOWN_FACES_DIR
    # Each subfolder's name becomes our label (name)
    it=1
    intial=0
    for filename in os.listdir(KNOWN_FACES_DIR):

            # Load an image
            
            image = face_recognition.load_image_file(KNOWN_FACES_DIR+"\\"+filename)

            # Get 128-dimension face encoding
            # Always returns a list of found faces, for this purpose we take first face only (assuming one face per image as you can't be twice on one image)
            encodings = face_recognition.face_encodings(image)
            if len(encodings) > 0:
                encoding = encodings[0]
            else:
               
                continue
            # Append encodings and name
            known_faces.append(encoding)
            intial+=1
        
    known_names[name]=intial
    #Check if file exists
    #if it does exist then read it and append the known_faces and known_names to and then write it 
    with open("known_faces.pkl", "wb") as file:
        
        pickle.dump((known_faces, known_names), file)
        

    
            