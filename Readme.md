![alt text]('img/demoImg.png")

## Description
Single audio file with timestamp file this automate and export chopped audio files


## Audio File and Timestamp
This changes you audio source folder and under `song1` should contain only two files.
One is the original audio file another is the timestamp
``` python
import_Folder_Path = "import/song1"
```
### Audio File
The script uses pydub library and is competiable to both common mp3 and wav chopping

### Timestamp File
The timestamp file has to be in txt and in following format  
`//` : Line will be ignored  
Each line will be an track export. And it can be commented out too.  

For each track the format is following:
``` text
// This line is comment
//------------Track Export Format------------------
// export name # start-time # end-time (Optional)
//------------------------------------------------ 
track1 # 0:00
track2 # 1:12 # 1:30
// track3 # 1:45
```
End timestamp is optional and if it is not defined than it will end before the next track starts by default


## Usage
pydub library is required you can install with pip install pydub  
or by using the venv like following
```
source venv/bin/activate
sudo python3 main.py
```


## Lisense
This is a do whatever you want license. Have fun :)







   