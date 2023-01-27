import difflib
import filecmp
import os.path
from pathlib import Path
import sys


def dir_atributes(path):  # get atributes of dir
    for (root, dirs, file) in os.walk(path):
        return root, dirs, file


def make_diff(path1, path2, n_diff):  # creates diff file
    file1 = open(path1).readlines()
    file2 = open(path2).readlines()
    delta = difflib.HtmlDiff().make_file(file1, file2, Path(path1).name, Path(path2).name)
    with open(n_diff, 'w') as f:
        f.write(delta)


def compare_two_files(folder_name1, folder_name2, filename, f1, f2):  # compares 2 files
    a = filecmp.cmp(f1, f2, shallow=True)
    if a:
        return f"{filename.upper()} in {folder_name1.upper()} is the same as {filename.upper()} in {folder_name2.upper()}"
    make_diff(f1, f2, Path(f'C:/Users/Arina/Desktop/Main/{filename[:-4]}.html'))
    diffs.append(Path(f'C:/Users/Arina/Desktop/Main/{filename[:-4]}.html'))
    return f"{filename.upper()} in {folder_name1.upper()} is NOT the same as {filename.upper()} in {folder_name2.upper()}"


def walk_in_dir(path1, path2, dir_name1, dir_name2, files1, files2):  # iterating in directory
    for file_name1 in files1:
        for file_name2 in files2:
            if file_name1 == file_name2:
                report.add(compare_two_files(dir_name1, dir_name2, file_name1, Path(f'{path1}/{file_name1}'),
                                             Path(f'{path2}/{file_name2}')))
            elif file_name1 not in files2:
                report.add(f"{file_name1.upper()} is not in {dir_name2.upper()} directory")
            elif file_name2 not in files1:
                report.add(f"{file_name2.upper()} is not in {dir_name1.upper()} directory")


def html_report(path):
    html_content = f"<b>Here is the report</b> <br/>{'<br/>'.join(sorted(report))}<br/>"
    with open(Path(f"{path}/report.html"), "w") as f:
        f.write(html_content)
        for i in diffs:
            f.write(f"<a href='{i}'>Link</a><br/>")
        f.write(f"<b>Thank You</b>")


def start(folder_name1: str, folder_name2: str, path1, path2):
    root1, dirs1, files1 = dir_atributes(path1)
    root2, dirs2, files2 = dir_atributes(path2)
    walk_in_dir(path1, path2, folder_name1, folder_name2, files1, files2)
    if dirs1:
        for d1 in dirs1:
            for d2 in dirs2:
                if d1:
                    start(d1, d2, Path(f'{root1}/{d1}'), Path(f'{root2}/{d2}'))


def main(path1, path2):
    start(folder_name1='golden', folder_name2='out', path1=path1, path2=path2)
    html_report(os.path.abspath(os.path.join(path1, os.pardir)))  # parent dir


diffs = []
report = set()
path1, path2 = Path(sys.argv[1]), Path(sys.argv[2])
main(path1, path2)
print(f"{'--'.join(sorted(report))}")
# C:/Users/Arina/Desktop/Main/out C:/Users/Arina/Desktop/Main/golden
