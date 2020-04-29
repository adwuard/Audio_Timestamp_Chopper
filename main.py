import os
from os.path import basename, join
from pydub import AudioSegment

import_Folder_Path = "import/song2"

class ProjectFolder:
    time_Stamp = ""
    audio_Path = ""
    import_Folder_Path = ""
    time_Stamp_Data = []
    fileType = ""

    def parseTimeToMill(self, strTime):
        res = 0
        t = [1, 60, 60 * 60]  # s, m, h
        if ':' in str(strTime):
            time = strTime.split(":")
            time.reverse()
            for ele in time:
                res += int(ele) * t[0] * 1000
                t.remove(t[0])
            return res
        else:
            return strTime

    def read_Txt_File(self):
        print("Parsing:", self.time_Stamp)
        file1 = open(self.time_Stamp, 'r')
        Lines = file1.readlines()
        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            if not line.startswith("//"):
                line = line.replace("\n", "")
                params = line.split("#")
                self.time_Stamp_Data.append(params)
        # self.time_Stamp_Data.sort(key=lambda x: x[1])

    def exportChop(self, Audio, name, start, end):
        exportFolderPath = join("export", basename(import_Folder_Path))
        if not os.path.exists(exportFolderPath):
            os.mkdir(exportFolderPath)
        file_Export_Path = join(exportFolderPath, name)
        extract = Audio[self.parseTimeToMill(start):self.parseTimeToMill(end)]
        print("Exporting Track :  " + file_Export_Path, "Start: " + str(start), "\tEnd: " + str(end))
        extract.export(file_Export_Path + "."+self.fileType, format=self.fileType)

    def chopSamples(self):
        audio = AudioSegment.from_file(self.audio_Path)
        audio_source_end = int(audio.duration_seconds * 1000)

        for i in range(0, len(self.time_Stamp_Data)):
            filename, start_time_mill, end_time_mill = (list(self.time_Stamp_Data[i]) + [None] * 3)[:3]
            if start_time_mill and end_time_mill:
                self.exportChop(audio, filename, start_time_mill, end_time_mill)
            elif start_time_mill and not end_time_mill:
                if i + 1 < len(self.time_Stamp_Data):
                    _, s2, _ = (list(self.time_Stamp_Data[i + 1]) + [None] * 3)[:3]
                    self.exportChop(audio, filename, start_time_mill, s2)
                else:
                    print(audio_source_end)
                    self.exportChop(audio, filename, start_time_mill, audio_source_end)

    def run(self):
        self.read_Txt_File()
        self.chopSamples()


if __name__ == '__main__':
    p = ProjectFolder()
    dir = os.listdir(import_Folder_Path)
    isTxtFile = False
    isAudioFile = False
    print("Import Files Found: ", dir)
    p.import_Folder_Path = import_Folder_Path
    for i in dir:
        if i.lower().endswith("txt"):
            isTxtFile = True
            p.time_Stamp = os.path.join(import_Folder_Path, i)
        elif i.lower().endswith("mp3"):
            isAudioFile = True
            p.fileType = "mp3"
            p.audio_Path = os.path.join(import_Folder_Path, i)
        elif i.lower().endswith("wav"):
            isAudioFile = True
            p.fileType = "mp3"
            p.audio_Path = os.path.join(import_Folder_Path, i)
    if not isAudioFile and isTxtFile:
        if isAudioFile:
            print("Missing (.MP3/.WAV) Audio File")
        else:
            print("Missing Time Stamp .txt File")
    p.run()
    print("Done!")

