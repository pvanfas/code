# convert media files
ffmpeg -i python.mov -codec copy python.mkv

# merge video files
mkvmerge -o output.mkv 'python 1.mkv' \+ python.mkv

# Delete empty folders
find . -empty -type d -delete

#Remove all *.pyc files and __pycache__ directories recursively
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
