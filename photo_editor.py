import cv2 as cv
 
img=cv.imread('input.png')
if img is None:
    print("Error: Image not found!")
    exit()

edited_img=img.copy()

while True:
    print("\n----Photo Editor----")
    print("1.Convert to Grayscale")
    print("2.Resize Image")
    print("3.Crop Image")
    print("4.Rotate Image")
    print("5.Flip Image")
    print("6.Show edited image")
    print("7.Save Image")
    print("8.Reset Image")
    print("9.Exit")

    choice=input("enter ur choice: ")

    if choice=="1":
        edited_img=cv.cvtColor(edited_img,cv.COLOR_BGR2GRAY)
        print("Image converted to grayscale")
    
    elif choice=="2":
        width=int(input("enter new width: "))
        height=int(input("enter new height: "))
        edited_img=cv.resize(edited_img,(width,height))
        print("Image resized")
        
    elif choice=="3":
        x=int(input("enter x coordinate: "))
        y=int(input("enter y coordinate: "))
        width=int(input("enter width: "))
        height=int(input("enter height: "))
        edited_img=edited_img[y:y+height, x:x+width]
        print("Image cropped")
        
    elif choice=="4":
        angle=float(input("enter rotation angle (degrees): "))
        h,w=edited_img.shape[:2]
        center=(w//2,h//2)

        matriax=cv.getRotationMatrix2D(center,angle,1.0)
        edited_img=cv.warpAffine(edited_img,matriax,(w,h))
        print("Image rotated")

    elif choice=="5":
        print("\nFilp Options")
        print("0 -vertical")
        print("1 -horizontal")
        print("-1 -both")
        flip_code=int(input("enter flip code: "))
        edited_img=cv.flip(edited_img,flip_code)
        print("Image flipped")

    elif choice=="6":
        cv.imshow("Edited Image",edited_img)
        print("Press any key while the image window is selected to return to the menu.")
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif choice=="7":
        filename=input("enter output file name(e.g.,output.jpg): ")
        cv.imwrite(filename,edited_img)
        print(f"Image saved as {filename}")

    elif choice == "8":
        edited_img = img.copy()
        print("Image reset to original")

    elif choice=="9":
        cv.destroyAllWindows()
        print("exiting..")
        break
    
    else:
        print("invalid choice! please try again.")