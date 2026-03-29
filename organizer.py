import os
import shutil

def get_file_type(filename):
    import os
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    if ext in [".jpg", ".jpeg", ".png", ".gif"]:
        return "Images"
    elif ext in [".pdf", ".docx", ".txt"]:
        return "Documents"
    elif ext in [".mp3", ".wav"]:
        return "Music"
    elif ext in [".mp4", ".mkv"]:
        return "Videos"
    else:
        return "Others"


def create_folder_if_not_exists(folder_name):
    import os
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Created folder: {folder_name}")

def get_file_size_readable(size_bytes):
    """Convert bytes to readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"


def move_file(file, destination):
    import shutil
    import os
    try:
        # Check if file exists in source
        if not os.path.exists(file):
            print(f"Source file not found: {file}")
            return
        
        # Create full destination path
        dest_path = os.path.join(destination, os.path.basename(file))
        
        # Check if file already exists at destination
        if os.path.exists(dest_path):
            print(f"File already exists at destination: {dest_path}")
            return
        
        # Move the file
        shutil.move(file, dest_path)
        print(f"Moved {file} to {dest_path}")
    except Exception as e:
        print(f"Error moving {file}: {e}")
        
def organize(file):
    folder = get_file_type(file)
    create_folder_if_not_exists(folder)
    move_file(file, folder)

organize("example.pdf")


if __name__ == "__main__":
    print("File Organizer starting...")

    # Example test
    file_type = get_file_type("example.pdf")
    create_folder_if_not_exists(file_type)
    move_file("example.pdf", file_type)

