#!/usr/bin/python3

class signature:

    sigs = {
        'pcap' : ['D4 C3 B2 A1','A1 B2 C3 D4','4D 3C B2 A1','A1 B2 3C 4D'],
        'pcapng' : ['0A 0D 0D 0A'],
        'sqlite/ sqlitedb' : ['53 51 4C 69 74 65 20 66','6F 72 6D 61 74 20 33 00'],
        'ico' : ['00 00 01 00'],
        '3gp' : ['66 74 79 70 33 67'],
        'tar.z' : ['1F 9D'],
        'bz2' : ['42 5A 68'],
        'gif' : ['47 49 46 38 37 61','47 49 46 38 39 61'],
        'tif/tiff' : ['49 49 2A 00','4D 4D 00 2A'],
        'jpg/ jpeg' : ['FF D8 FF DB','FF D8 FF E0 00 10 4A 46 49 46 00 01','FF D8 FF EE','FF D8 FF E1 ?? ?? 45 78 69 66 00 00'],
        'lz' : ['4C 5A 49 50'],
        'exe/ dll/ sys' : ['4D 5A','5A 4D'],
        'docx/ pptx/ xlsx' : ['50 4B 03 04 14'],
        'zip/ apk/ jar/' : ['50 4B 03 04'],
        'zip/ apk (empty)' : ['50 4B 05 06'],
        'winzip' : ['57 69 6E 5A 69 70'],
        'doc/ ppt/ xls' : ['D0 CF 11 E0 A1 B1 1A E1'],
        'elf' : ['7F 45 4C 46'],
        'rar' : ['52 61 72 21 1A 07 00','52 61 72 21 1A 07 01 00'],
        'png' : ['89 50 4E 47 0D 0A 1A 0A'],
        'class' : ['CA FE BA BE'],
        'txt/ others' : ['EF BB BF','FF FE','FE EE','FF FE 00 00','00 00 FE FF'],
        'pdf' : ['25 50 44 46 2D'],
        'wma/ wmv' : ['30 26 B2 75 8E 66 CF 11','A6 D9 00 AA 00 62 CE 6C'],
        'ogg/ ogv' : ['4F 67 67 53'],
        'psd' : ['38 42 50 53'],
        'wav' : ['38 42 50 53','57 41 56 45'],
        'avi' : ['52 49 46 46','41 56 49 20'],
        'mp3' : ['FF FB','FF F3','FF F2','49 44 33'],
        'bmp' : ['42 4D'],
        'iso' : ['43 44 30 30 31'],
        'midi' : ['4D 54 68 64'],
        'vmdk' : ['4B 44 4D'],
        'tar' : ['75 73 74 61 72 00 30 30','75 73 74 61 72 20 20 00'],
        '7z' : ['37 7A BC AF 27 1C'],
        'gz/ tar.gz' : ['1F 8B'],
        'xz/ tar.xz' : ['FD 37 7A 58 5A 00'],
        'mkv/ mka' : ['1A 45 DF A3'],
        'xml' : ['3C 3F 78 6D 6C 20','3C 00 3F 00 78 00 6D 00 6C 00 20','00 3C 00 3F 00 78 00 6D 00 6C 00 20','3C 00 00 00 3F 00 00 00 78 00 00 00 6D 00 00 00 6C 00 00 00 20 00 00 00','00 00 00 3C 00 00 00 3F 00 00 00 78 00 00 00 6D 00 00 00 6C 00 00 00 20','4C 6F A7 94 93 40'],
        'deb' : ['21 3C 61 72 63 68 3E 0A'],
        'webp' : ['52 49 46 46'],
        'rtf' : ['7B 5C 72 74 66 31'],
        'mpg/ mpeg' : ['47','00 00 01 BA','00 00 01 B3'],
        'mp4' : ['66 74 79 70 69 73 6F 6D','18 66 74 79 70 33 67 70 35'],
        'zlib' : ['78 01','78 5E','78 9C','78 DA','78 20','78 7D','78 BB','78 F9'],
        'eml' : ['52 65 63 65 69 76 65 64 3A'],
        'pgp' : ['85'],
        'cab' : ['49 53 63 28'],
        'vdi' : ['C 3C 3C 20 4F 72 61 63 6C 65 20 56 4D 20 56 69 72 74 75 61 6C 42 6F 78 20 44 69 73 6B 20 49 6D 61 67 65 20 3E 3E 3E'],
        'vhdx' : ['76 68 64 78 66 69 6C 65'],
        
    }
