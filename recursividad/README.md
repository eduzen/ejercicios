# Directory Structure Creation - Exercise

Create a Python program that simulates the creation of directories and files based on user commands, and prints the directory structure in a hierarchical format.

The commands will be provided in a list, where each command is a string in the following formats:

    "create file /path/to/the/file.txt"
    "create folder /path/to/the/folder/"

Your program should read these commands and create a representation of the directory structure.

Finally, it should print out the directory structure in a hierarchical format. For example, given the following input:

```python
commands = ["create file /home/jack/Downloads/1.txt",
            "create file /home/jack/Downloads/pics/2.jpg",
            "create file /home/jack/3.txt",
            "create folder /home/jack/tmp/",
            "create file /home/jack/1.txt",
]
```

The output of your program should look like this:

```yaml
- home
  - jack
    - Downloads
      - 1.txt
      - pics
        - 2.jpg
    - 3.txt
    - tmp
    - 1.txt
```

Note: The program should work with any number and combination of commands, and it should handle both file and folder creation commands. Be sure to consider edge cases and potentially incorrect command formats.
