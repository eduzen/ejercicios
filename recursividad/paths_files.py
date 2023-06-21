from rich import print


def create_file_path(file_path, filesystem):
    # split the file path into parts
    parts = file_path.strip('/').split('/')
    current_dir = filesystem
    for part in parts:
        if part not in current_dir:
            current_dir[part] = {}
        current_dir = current_dir[part]
    return filesystem


def create_file_path_recursively(file_path, dir_dict):
    # split the file path into parts
    parts = file_path.strip('/').split('/')
    # Base case: if parts is empty, return the directory dictionary
    if not parts:
        return dir_dict
    # Recursive case: create the current directory and call the function on the subdirectory
    else:
        current_dir = parts[0]
        sub_path = '/'.join(parts[1:])
        if current_dir not in dir_dict:
            dir_dict[current_dir] = {}
        dir_dict[current_dir] = create_file_path(sub_path, dir_dict[current_dir])
        return dir_dict

def print_files(dir_dict, indent=0):
    # print each file/directory in the directory structure
    for name, sub_dir in dir_dict.items():
        print('  ' * indent + '- ' + name)
        if sub_dir:
            print_files(sub_dir, indent + 1)

def process_command(commands: list[str]) -> dict[str, dict]:
    filesystem = {}
    for command in commands:
        _, _, file_path = command.split(' ', 2)
        filesystem = create_file_path(file_path, filesystem)
    return filesystem

def main():
    commands = ["create file /home/jack/Downloads/1.txt",
                "create file /home/jack/Downloads/pics/2.jpg",
                "create file /home/jack/3.txt",
                "create folder /home/jack/tmp/",
                "create file /home/jack/1.txt",
    ]
    filesystem = process_command(commands)
    print_files(filesystem)

if __name__ == "__main__":
    main()
