# convert media files
ffmpeg -i python.mov -codec copy python.mkv

# merge video files
mkvmerge -o output.mkv 'python 1.mkv' \+ python.mkv

# Delete all pyc files
find . -path "*.pyc"  -delete

# Delete empty folders
find . -empty -type d -delete