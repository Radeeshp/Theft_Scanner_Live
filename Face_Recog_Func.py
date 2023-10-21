from imports import *
def Face_Recognition_func(Destination_T,
                          Destination_F,
                          KNOWN_FACES_DIR,
                          UNKNOWN_FACES_DIR,
                          Face_Not_Clear):
    
    #This variable is used to set the tolerance level for comparing the faces and 
    #Lower the number higher the accuracy(Lower false positive,higher false negative)
    TOLERANCE = 0.5
    MODEL = 'cnn'  
    
    
    #To find which name has the most positive results.
    def find_results(known_names,results_T_F,no_faces):
             
            #We are converting the  results which are in the form of a list containing True/False to 1/0  
            results_1_0 = list(map(lambda x: 1 if x else 0, results_T_F))
            
            #Flag is used to indicate if the number of matchs of the unknown faces with the given database 
            #is less than threshold
            flag=True
            current=0
            Matches_betw_kn_and_un=known_names.copy()
            
            
            for K in  known_names.keys():
                    j = known_names[K]
                    Matches_betw_kn_and_un[K]=sum(results_1_0[current:current+j+1])
                    current=current+j    
          
        
            Matches_betw_kn_and_un_copy=dict(Matches_betw_kn_and_un)
            for key,values in Matches_betw_kn_and_un_copy.items():
                if Matches_betw_kn_and_un[key]<20:
                     Matches_betw_kn_and_un.pop(key)    
            
            if len(Matches_betw_kn_and_un)==0 : flag=False    
            
            
            
            sorted_dict = sorted(Matches_betw_kn_and_un.items(), key=lambda x: x[1], reverse=True)
            top_n_salaries = sorted_dict[:no_faces] 
            # Extract the names from the top N entries
            top_n_names = [entry[0] for entry in top_n_salaries]
            return(top_n_names,flag)

            
            
    # Returns (R, G, B) from name
    def name_to_color(name):
        # Take 3 first letters, tolower()
        # lowercased character ord() value rage is 97 to 122, substract 97, multiply by 8
        color = [(ord(c.lower())-97)*8 for c in name[:3]]
        return color


    with open("known_faces.pkl", "rb") as file:
        known_faces, known_names = pickle.load(file)

    #Have to change it to live stream and add boxes to the output image.
    print('\n\n\nProcessing unknown faces...')
    # Now let's loop over a folder of faces we want to label
    cap = cv2.VideoCapture(r"D:\Education\PROJECTS\Theft_Scanner_Live\Input_Video\WhatsApp Video 2023-10-21 at 21.33.22_b7620aaa.mp4")

    while True:
        ret, image = cap.read()
        if not ret:
            break
        
        # This time we first grab face locations - we'll need them to draw boxes
        locations = face_recognition.face_locations(image)
        
        # Now since we know loctions, we can pass them to face_encodings as second argument
        # Without that it will search for faces once again slowing down whole process
        encodings = face_recognition.face_encodings(image, locations)

        # We passed our image through face_locations and face_encodings, so we can modify it
        # First we need to convert it from RGB to BGR as we are going to work with cv2
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # But this time we assume that there might be more faces in an image - we can find faces of dirrerent people
        print(f', found {len(encodings)} face(s)')
        no_faces=len(encodings)
        if no_faces==0:
            continue
        
        for face_encoding, face_location in zip(encodings, locations):

            # We use compare_faces (but might use face_distance as well)
            # Returns array of True/False values in order of passed known_faces
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
            # Since order is being preserved, we check if any face was found then grab index
            # then label (name) of first matching known face withing a tolerance
            match=None
            match,flag = find_results(known_names,results,no_faces)
            
            if flag:  # If at least one is true, get a name of first of found labels
              #  change_location(UNKNOWN_FACES_DIR+'\\'+filename ,Destination_T+name)
                             
                match = ', '.join(match)
                top, right, bottom, left=face_location
                cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(image, match, (left + 6, bottom - 6), font, 0.5, (0, 0, 255), 1)
                    
        cv2.imshow('Face Recognition', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
        
        # Show image
        #cv2.imshow(filename, image)
        #cv2.waitKey(0)
        #cv2.destroyWindow(filename)