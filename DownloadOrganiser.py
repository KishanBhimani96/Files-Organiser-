#!/usr/bin/env python3

import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DownloadOrganizerHandler(FileSystemEventHandler):
	def on_modified(self, event):
		for filename in os.listdir(folder_to_track):
			src = f"{folder_to_track}/{filename}"
			if os.path.isdir(src):
				continue  # Skip directories
			file_extension = filename.split(".")[-1].lower()
			dest_folder = folder_destinations.get(file_extension, folder_to_track + "/Others")
			dest = f"{dest_folder}/{filename}"
			os.makedirs(dest_folder, exist_ok=True)
			shutil.move(src, dest)
			print(f"Moved: {src} -> {dest}")
			
folder_to_track = '/path/to/your/downloads'  
folder_destinations = {
	'jpeg': '/path/to/your/images',  
	'jpg': '/path/to/your/images',
	'png': '/path/to/your/images',
	'gif': '/path/to/your/images',
	'heic': '/path/to/your/images',
	'pdf': '/path/to/your/documents',
	'docx': '/path/to/your/documents',
	'xlsx': '/path/to/your/documents',
	# Add more file types and destinations as needed
}

event_handler = DownloadOrganizerHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
	while True:
		pass
except KeyboardInterrupt:
	observer.stop()
observer.join()
