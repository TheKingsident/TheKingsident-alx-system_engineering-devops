## Uploading Files to My Sandbox Online

I followed these steps to upload files to my sandbox online using the SFTP command-line tool:

1. **Open Terminal**: Start by opening a terminal or command prompt on my local machine.

2. **Connect to Sandbox**: Use the `sftp` command to connect to my sandbox server. Replace `<username>` and `<hostname>` with my actual credentials.

   ```bash
   sftp <username>@<hostname>

3. **Navigate to Destination Directory**: After connecting, I navigated to the directory on the server where I wanted to upload the file. I used the cd command, replacing <destination_directory> with the actual path.

   ```bash
   cd /root/alx-system_engineering-devops/command_line_for_the_win/

4. **Upload File**: To upload the PNG file from my local machine to the server, I used the put command. I replaced <local_file_path> with the actual path of my PNG file on my local machine.

   ```bash
   put put /mnt/c/Users/ACER\ NITRO/Dropbox/PC/Downloads/0-first_9_tasks.jpg

5. **Verify Upload**: I double-checked to ensure the file was successfully uploaded by using the ls command to list the files in the current directory on the server.

   ```bash
   ls

By following these steps and using the provided commands, I was able to upload files to my sandbox online using SFTP.
