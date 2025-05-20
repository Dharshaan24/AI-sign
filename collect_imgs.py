import os
import cv2

# Ask the user for number of classes and dataset size
try:
    number_of_classes = int(input("Enter the number of classes to collect: "))
    dataset_size = int(input("Enter number of images per class: "))
except ValueError:
    print("Please enter valid integers.")
    exit()

# Create main data directory
DATA_DIR = './data'
os.makedirs(DATA_DIR, exist_ok=True)

# Initialize camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Loop through each class
for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    os.makedirs(class_dir, exist_ok=True)

    print(f"\nCollecting data for Class {j}")
    print("Press 'q' when you're ready to start capturing images...")

    # Wait for user to press 'q' before starting image capture
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
        cv2.putText(frame, f"Class {j}: Press 'Q' to start", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1.2, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Start capturing images
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        cv2.imshow('frame', frame)
        cv2.imwrite(os.path.join(class_dir, f'{counter}.jpg'), frame)
        counter += 1
        if cv2.waitKey(1) & 0xFF == ord('x'):  # Optional: press 'x' to skip
            break

    print(f"Collected {counter} images for Class {j}")

print("\n✅ Data collection completed.")
cap.release()
cv2.destroyAllWindows()
