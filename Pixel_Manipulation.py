import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import numpy as np

def swap_pixels(image):
    data = np.array(image)
    width, height = data.shape[1], data.shape[0]
    swapped_data = np.copy(data)
    for y in range(height):
        for x in range(0, width, 2):  # Swap every pair of adjacent pixels
            if x < width - 1:
                swapped_data[y, x], swapped_data[y, x + 1] = data[y, x + 1], data[y, x]
    return Image.fromarray(swapped_data)

def apply_operation(image, operation):
    data = np.array(image)
    if operation == "Invert":
        processed_data = np.bitwise_not(data)
    elif operation == "Add 50":
        processed_data = np.clip(data + 50, 0, 255)
    elif operation == "Subtract 50":
        processed_data = np.clip(data - 50, 0, 255)
    else:
        return image
    return Image.fromarray(processed_data)

def reverse_operation(image, operation):
    data = np.array(image)
    if operation == "Invert":
        processed_data = np.bitwise_not(data)
    elif operation == "Add 50":
        processed_data = np.clip(data - 50, 0, 255)
    elif operation == "Subtract 50":
        processed_data = np.clip(data + 50, 0, 255)
    else:
        return image
    return Image.fromarray(processed_data)

def encrypt_image():
    global image, encrypted_image, last_operation
    if image is None:
        messagebox.showerror("Error", "No image loaded")
        return
    
    operation = simpledialog.askstring("Input", "Enter operation (Swap, Invert, Add 50, Subtract 50):")
    if operation == "Swap":
        encrypted_image = swap_pixels(image)
    else:
        encrypted_image = apply_operation(image, operation)
    
    last_operation = operation
    display_images(image, encrypted_image)

def decrypt_image():
    global encrypted_image, decrypted_image, last_operation
    if encrypted_image is None:
        messagebox.showerror("Error", "No encrypted image to decrypt")
        return
    
    if last_operation == "Swap":
        decrypted_image = swap_pixels(encrypted_image)
    else:
        decrypted_image = reverse_operation(encrypted_image, last_operation)
    
    display_images(encrypted_image, decrypted_image)

def open_image():
    global image, encrypted_image, decrypted_image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image = Image.open(file_path).convert("RGB")
        encrypted_image = None
        decrypted_image = None
        display_images(image, None)

def save_image():
    global image, encrypted_image, decrypted_image
    
    # Determine which image to save
    if encrypted_image is not None:
        image_to_save = encrypted_image
    elif decrypted_image is not None:
        image_to_save = decrypted_image
    else:
        image_to_save = image
    
    if image_to_save is None:
        messagebox.showerror("Error", "No image to save")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg;*.jpeg")])
    if file_path:
        image_to_save.save(file_path)
        messagebox.showinfo("Success", f"Image saved to {file_path}")

def resize_image(img, size=(400, 400)):
    return img.resize(size, Image.Resampling.LANCZOS)

def display_images(img1, img2):
    # Clear existing widgets
    for widget in image_frame.winfo_children():
        widget.destroy()

    # Create a frame for each image and its label
    img1_frame = tk.Frame(image_frame, bg='light gray')
    img1_frame.pack(side="left", padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    img2_frame = tk.Frame(image_frame, bg='light gray')
    img2_frame.pack(side="right", padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Display original image
    if img1 is not None:
        img1_resized = resize_image(img1)
        tk_image1 = ImageTk.PhotoImage(img1_resized)
        label1 = tk.Label(img1_frame, image=tk_image1, bg='light gray')
        label1.image = tk_image1
        label1.pack(fill=tk.BOTH, expand=True)
        label1_text = tk.Label(img1_frame, text="Original Image", bg='light gray')
        label1_text.pack(side="bottom")

    # Display encrypted/decrypted image
    if img2 is not None:
        img2_resized = resize_image(img2)
        tk_image2 = ImageTk.PhotoImage(img2_resized)
        label2 = tk.Label(img2_frame, image=tk_image2, bg='light gray')
        label2.image = tk_image2
        label2.pack(fill=tk.BOTH, expand=True)
        label2_text = tk.Label(img2_frame, text="Processed Image", bg='light gray')
        label2_text.pack(side="bottom")

# Initialize the GUI
root = tk.Tk()
root.title("Image Encryption Tool")

# Set the size of the main window
root.geometry("600x300")  # Adjusted Width x Height

# Set background color for the main window
root.configure(bg='light gray')

# Define GUI elements
button_width = 25  # Width of the buttons
button_height = 3  # Height of the buttons

upload_button = tk.Button(root, text="Upload Your Image", width=button_width, height=button_height, command=open_image, bg='light blue')
upload_button.pack(pady=10, padx=10, fill=tk.X, expand=True)

encrypt_button = tk.Button(root, text="Encrypt Image", width=button_width, height=button_height, command=encrypt_image, bg='light green')
encrypt_button.pack(pady=10, padx=10, fill=tk.X, expand=True)

decrypt_button = tk.Button(root, text="Decrypt Image", width=button_width, height=button_height, command=decrypt_image, bg='light coral')
decrypt_button.pack(pady=10, padx=10, fill=tk.X, expand=True)

save_button = tk.Button(root, text="Save Image", width=button_width, height=button_height, command=save_image, bg='light yellow')
save_button.pack(pady=10, padx=10, fill=tk.X, expand=True)

# Create a frame for displaying images side by side
image_frame = tk.Frame(root, bg='light gray')
image_frame.pack(pady=20, fill=tk.BOTH, expand=True)

# Initialize global variables
image = None
encrypted_image = None
decrypted_image = None
last_operation = None

root.mainloop()
