# extra

# binary file
# birary file means photos, videos etc.
# it is calculated in bytes.
# the mode of binary file is "b"

# copying a binary file
with open("boss.jpg","rb") as rf:
    file_contents=rf.read()
with open("boss_copy.jpg","wb") as wf:
    wf.write(file_contents)
# or-
with open("boss.jpg","rb") as rf:
    with open("boss_copy.jpg","wb") as wf:
        for line in rf:
            wf.write(line)
# we can do this by chunc tecnic also.
with open("boss.jpg","rb") as rf:
    with open("boss_copy.jpg","wb") as wf:
        chunk_size=4096
        rf_chunk=rf.read(chunk_size)
        while len(rf_chunk) >0:
            wf.write(rf_chunk)
            rf_chunk=rf.read(chunk_size)


# appending to a file

# if a file dont exists and we write a file it will be automatically created.
# if a file exists and we write a file, it will delete previous contents and overwrite it.
# if we dont want to remove old contents of a existed file, we can use append mode.
filename="UserGuest.txt"
accessmode="a"
with open(filename, accessmode) as myfile:
    myfile.write("I am shawki")

# different files with their extensions

# text document             -   .txt
# excel (comma separated)   -   .csv
# excel                     -   .xlxs
# command prompt            -   .cmd
# ms word                   -   .docx
# photo                     -   .jpg
# audio                     -   .mp3
# video                     -   .mp4
# python                    -   .py
# powerpoint                -   .pptx
# zip                       -   .zip
# pdf file                  -   .pdf
# subtitle                  -   .str
# torrent file              -   .torrent
# application               -   .exe