#!/usr/bin/env python3
import os
import subprocess
import sys
import argparse

def get_repo_name(repo_url):
    repo_url = repo_url.rstrip('/')
    name = os.path.basename(repo_url)
    if name.endswith('.git'):
        name = name[:-4]
    return name

def run_command(command, message):
    print(message)
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running: {' '.join(command)}")
        sys.exit(e.returncode)

def main():
    parser = argparse.ArgumentParser(description='Clone specific folders from a Git repository.')
    parser.add_argument('repo_url', help='URL of the Git repository.')
    args = parser.parse_args()
    
    repo_url = args.repo_url
    sub_dirs = input("Enter the subdirectories (or file paths) to clone, separated by commas: ").strip()
    
    sub_dirs_list = [dir.strip() for dir in sub_dirs.split(',')]
    
    local_repo_name = get_repo_name(repo_url)
    print(f"\nThe repository will be cloned into '{local_repo_name}' directory.")
    
    if os.path.exists(local_repo_name):
        print(f"Error: The directory '{local_repo_name}' already exists. Please remove it or choose a different location.")
        sys.exit(1)
    
    os.mkdir(local_repo_name)
    os.chdir(local_repo_name)
    
    print("\n--- Starting Sparse Checkout Process ---")
    
    run_command(["git", "init"], "Making Harambe eat a banana ")

    run_command(["git", "remote", "add", "-f", "origin", repo_url], "looking for the origin of the universe...")

    run_command(["git", "config", "core.sparseCheckout", "true"], "checking for hot moms around you...")

    # Step 4: Specify the subdirectories or files in the sparse-checkout configuration.
    sparse_config_path = os.path.join(".git", "info", "sparse-checkout")
    try:
        with open(sparse_config_path, "w") as f:
            for dir in sub_dirs_list:
                f.write(dir + "\n")
        print(f"Configured sparse checkout with paths: {', '.join(sub_dirs_list)}")
    except IOError as e:
        print("Error writing to sparse-checkout configuration file:", e)
        sys.exit(1)

    try:
        run_command(["git", "pull", "origin", "master"], "Trying to rizz up master")
    except SystemExit:
        print("Master died moving on to his woman")
        run_command(["git", "pull", "origin", "main"], "Pulling the main chick")
    
    print("\nCooked")
    print("The specified folders or files have been cloned into this repository.")

if __name__ == "__main__":
    main()
