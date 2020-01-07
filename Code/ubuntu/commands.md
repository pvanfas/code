convert media files
```
ffmpeg -i media.mov -codec copy media.mkv
```

Merge video files
```
mkvmerge -o output.mkv 'media 1.mkv' \+ media.mkv
```

Delete empty folders
```
find . -empty -type d -delete
```

Remove all *.pyc files and __pycache__ directories recursively
```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```
