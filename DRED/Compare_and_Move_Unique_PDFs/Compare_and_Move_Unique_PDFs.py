"""
Program: PDF File Deduplication and Organization Script
Author: John Akujobi
Date: Oct 17, 2024
Description:
    This program is designed to compare PDF files across two directories (source and comparison directory) to identify duplicates.
    It moves unique files from the source directory to a target directory while preserving the directory structure. The program:
    
    - Traverses both the source and comparison directories (including subdirectories) to find all files.
    - Uses file size as an initial filter and then compares file content using SHA-256 hashes.
    - Moves unique files from the source directory to the target directory.
    - Ensures the original directory structure is preserved when moving files.
    - Implements parallel processing for faster execution with large sets of files.
    - Logs operations such as moved files, duplicates found, and errors encountered.
    
    This version integrates Tkinter to allow users to select source, comparison, and target directories using a GUI.

Dependencies:
    - PyPDF2 (for optional PDF text extraction, not currently used in the main process)
    - hashlib (for SHA-256 hashing)
    - concurrent.futures (for parallel processing)
    - os, shutil (for file and directory operations)
    - logging (for logging file operations and errors)
    - tkinter (for file and directory selection)
"""

import os
import shutil
import hashlib
import PyPDF2
from concurrent.futures import ProcessPoolExecutor
import logging
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Set up logging
logging.basicConfig(filename='file_operations.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PDFDeduplicationTool:
    def __init__(self):
        # Variables for directories
        self.source_directory = ""
        self.compare_directory = ""
        self.target_directory = ""

        # Initialize the GUI
        self.init_gui()

    def init_gui(self):
        """Initialize the Tkinter GUI for selecting directories."""
        self.root = tk.Tk()
        self.root.title("PDF Deduplication Tool")

        # Source directory selection
        tk.Label(self.root, text="Select Source Directory:").grid(row=0, column=0, padx=10, pady=10)
        self.source_dir_button = tk.Button(self.root, text="Browse...", command=self.select_source_directory)
        self.source_dir_button.grid(row=0, column=1)

        # Compare directory selection
        tk.Label(self.root, text="Select Compare Directory:").grid(row=1, column=0, padx=10, pady=10)
        self.compare_dir_button = tk.Button(self.root, text="Browse...", command=self.select_compare_directory)
        self.compare_dir_button.grid(row=1, column=1)

        # Target directory selection
        tk.Label(self.root, text="Select Target Directory:").grid(row=2, column=0, padx=10, pady=10)
        self.target_dir_button = tk.Button(self.root, text="Browse...", command=self.select_target_directory)
        self.target_dir_button.grid(row=2, column=1)

        # Start button to begin the process
        self.start_button = tk.Button(self.root, text="Start Deduplication", command=self.start_deduplication)
        self.start_button.grid(row=3, column=0, columnspan=2, pady=20)

        self.root.mainloop()

    def select_source_directory(self):
        """Open file explorer to select the source directory."""
        self.source_directory = filedialog.askdirectory()
        logging.info(f"Selected source directory: {self.source_directory}")

    def select_compare_directory(self):
        """Open file explorer to select the comparison directory."""
        self.compare_directory = filedialog.askdirectory()
        logging.info(f"Selected comparison directory: {self.compare_directory}")

    def select_target_directory(self):
        """Open file explorer to select the target directory."""
        self.target_directory = filedialog.askdirectory()
        logging.info(f"Selected target directory: {self.target_directory}")

    def start_deduplication(self):
        """Start the deduplication process."""
        if not self.source_directory or not self.compare_directory or not self.target_directory:
            messagebox.showerror("Error", "Please select all three directories before starting.")
            return
        
        # Confirm the action with the user
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to start the deduplication?")
        if confirmation:
            self.parallel_move_unique_or_similar_files()
            messagebox.showinfo("Success", "Deduplication process completed.")
        else:
            logging.info("Deduplication process cancelled.")

    def calculate_file_hash(self, file_path):
        """Calculate the SHA-256 hash of the file content."""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
        except Exception as e:
            logging.error(f"Error calculating hash for {file_path}: {e}")
            return None
        return sha256_hash.hexdigest()

    def are_file_sizes_similar(self, size1, size2, tolerance=1024 * 50):
        """Compares the file sizes of two files within a specified tolerance."""
        return abs(size1 - size2) <= tolerance

    def move_file_preserving_structure(self, source_file_path, source_dir, target_dir):
        """Move a file from the source directory to the target directory, preserving directory structure."""
        try:
            relative_path = os.path.relpath(source_file_path, source_dir)
            target_file_path = os.path.join(target_dir, relative_path)
            target_subdir = os.path.dirname(target_file_path)

            if not os.path.exists(target_subdir):
                os.makedirs(target_subdir)

            shutil.move(source_file_path, target_file_path)
            logging.info(f"Moved: {source_file_path} to {target_file_path}")
        except Exception as e:
            logging.error(f"Error moving {source_file_path} to {target_file_path}: {e}")

    def process_file(self, source_file, compare_dir, target_dir, source_dir):
        """Process a single file: compare to files in the comparison directory, move if unique."""
        source_size = os.path.getsize(source_file)
        source_hash = self.calculate_file_hash(source_file)
        if not source_hash:
            return

        # Check for duplicates in the comparison directory
        for root, _, files in os.walk(compare_dir):
            for comp_file in files:
                comp_file_path = os.path.join(root, comp_file)
                comp_size = os.path.getsize(comp_file_path)

                if self.are_file_sizes_similar(source_size, comp_size):
                    comp_hash = self.calculate_file_hash(comp_file_path)
                    if not comp_hash:
                        continue

                    if source_hash == comp_hash:
                        logging.info(f"Duplicate found: {source_file} (same as {comp_file_path})")
                        return  # Skip moving if duplicate found

        # No duplicate found, move the file
        self.move_file_preserving_structure(source_file, source_dir, target_dir)

    def parallel_move_unique_or_similar_files(self):
        """Traverse source directory, compare files, and move unique ones."""
        source_files = []
        for root, _, files in os.walk(self.source_directory):
            for file in files:
                source_files.append(os.path.join(root, file))

        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)

        with ProcessPoolExecutor() as executor:
            executor.map(lambda file: self.process_file(file, self.compare_directory, self.target_directory, self.source_directory), source_files)


if __name__ == "__main__":
    # Run the PDF deduplication tool with GUI
    PDFDeduplicationTool()
