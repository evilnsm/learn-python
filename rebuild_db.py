#!/usr/bin/env python
# -*- coding: utf-8

# The iPod shuffle Database Generator
# (C) 2005 Martin J. Fiedler -|- KeyJ@s2000.ws
# This is free software.
__version__="0.4"
""" VERSION HISTORY
0.1 (2005-03-13)
    * initial public release, Win32 only
0.2 (2005-03-15)
    * added Python version
0.3 (2005-03-18)
    * Python version now includes a "smart shuffle" feature
0.4 (2005-03-20)
    * fixed iPod crashes after playing the shuffle playlist to the end
    * fixed incorrect databse entries for non-MP3 files
"""

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OF THIRD PARTY RIGHTS.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR HOLDERS INCLUDED IN THIS NOTICE BE
# LIABLE FOR ANY CLAIM, OR ANY SPECIAL INDIRECT OR CONSEQUENTIAL DAMAGES, OR
# ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import sys,os,os.path,array,random

HEADER_SIZE=18
ENTRY_SIZE=558
ENTRY_START=32

total_count=0
header=array.array('B')
entry=array.array('B')
'''
利用'B'生成  unsign integer数组，每个元素 = 1 byte = 8 bit = 2H(2位16进制的数)

header是iTunesSD文件的前18 byte，enrty用来记录文件的全路径以/作为分隔符，

entry的1,2,3,4,5,26,29,31元素其实是特定的，文件fullname以/打头从下标[32]开始写


@若目录级数>50且每级目录>10个字符(char)，558byte能写得下?含unicode的话更占位置
'''

domains=[]

################################################################################

def write_to_db(filename): #传过来的filename其实是/开头的
  global total_count,entry,iTunesSD,domains
  ext=os.path.splitext(filename[1:])[1].lower()
  if ext==".mp3":
    entry[13]=1
  elif ext==".m4a" or ext==".m4b" or ext==".m4p":
    entry[13]=2
  elif ext==".wav":
    entry[13]=4
  fnpos=1
  fnlen=len(filename)
  offset=ENTRY_START
  '''
  从33byte开始写文件名。名字中的每个char换算成ASCII码值(0-127)刚好与array的 B 参数吻合，占8位，在ultraledit里显示一组的2个数字

  典型：下标[32]为空，34格下标[33]为2F

  空一格,写一格。硬件要求的吧?
   '''
  while offset<ENTRY_SIZE:
    entry[offset]=0  #先空一格 offset格填0,offset+1格填ASCII码
    if fnpos<fnlen:  #fnpos用来迭代每个char
      entry[offset+1]=ord(filename[fnpos])  #char to ASCII 
      fnpos+=1
    else: #文件名写完毕，后面全部填0
      entry[offset+1]=0
    offset+=2
  '''
  上文的while循环不好理解。典型的C-code？试试pythonic，用列表推导式
  t1 = [ord(i) for i in list(filename)]  
  t2 = [0] * len(t1) 
  t3 = [rv for i in zip(t2,t1) for rv in i]
  t3.extend([0]*(ENTRY_SIZE - ENTRY_START - len(t3))) #不足的扩充0
  #将列表元素复制到array里,默认就是"追加"写入模式:)
  entry.fromlist(t3)

  推荐还是用while循环吧，比较高效 而且不用操心计算元素个数
  '''
  if ext!=".m4b" and ext!=".aa":
    entry[555]=1
  entry.tofile(iTunesSD)
  domains[-1].append(total_count);
  total_count+=1

################################################################################

def browse(path):
  global header,entry,domains
  count=0

  if path=='.': print "/:",  #好有心机的逗号 ，完美与下文的count files组成一行
  else: print "%s:"%path[1:],
  sys.stdout.flush()

  try:
    dir=os.listdir(path)
  except OSError:
    print "cannot browse"
    return
  '''
  用list dir 等词作为变量名，真的好么
  '''
  list=[]
  for item in dir:
    if item=="." or item=="..": continue
    fullname=path+'/'+item
    try: is_link=os.path.islink(fullname)
    except OSError: continue
    if is_link: continue

    try: is_dir=os.path.isdir(fullname)
    except OSError: continue
    if is_dir:
      list.append('D'+item)
      continue  

    ext=os.path.splitext(item)[1].lower()
    if ext==".mp3" or ext==".m4a" or ext==".m4b" or ext==".m4p" or ext==".wav" or ext==".aa":
      list.append('F'+item)
      count+=1
  print count,"files"

  list.sort(lambda a,b: cmp(a.lower(),b.lower()))
  domains.append([])
  for item in list:
    fullname=path+'/'+item[1:] #无论是Direcoty还是File,开头都加上了'/'
    if item[0]=='D':
      browse(fullname)
    elif item[0]=='F':
      write_to_db(fullname) #试试传入2个参数，对F加以区分，调用后就可以直接确定 entry[13]的值
    else:
      raise KeyError,"this should never happen"

################################################################################

def make_shuffle():
  global total_count,domains
  random.seed()

  # count required number of slices
  slice_count=0
  for domain in domains:
    l=len(domain)
    if l>slice_count: slice_count=l

  # generate slices
  slices=[]
  for i in xrange(slice_count):
    slices.append([])
  slice_fill=[0]*slice_count

  # fill slices
  for d in xrange(len(domains)):
    used=[]
    for n in domains[d]:
      # find slices where the nearest track of the same domain is far away
      metric=[slice_count]*slice_count
      for s in xrange(slice_count):
        m=metric[s]
        for u in used:
          m=min(m,abs(s-u),abs(s-u+slice_count),abs(s-u-slice_count))
        metric[s]=m
      m=(max(metric)+1)/2
      candidates=[s for s in xrange(slice_count) if metric[s]>=m]

      # find emptiest slices
      m=(min(slice_fill)+max(slice_fill)+1)/2
      cand2=[s for s in xrange(slice_count) if slice_fill[s]<=m and candidates.count(s)]
      if cand2: candidates=cand2

      # choose one of the remaining candidates and add the track to the chosen slice
      s=random.choice(candidates)
      p=random.randint(0,len(slices[s]))
      slices[s].insert(p,(n,d))
      slice_fill[s]+=1
      used.append(s)

  # avoid adjacent tracks of the same domain at slice boundaries
  last_domain=-1
  for s in xrange(len(slices)):
    l=len(slices[s])
    if l>1 and slices[s][0][1]==last_domain:
      temp=slices[s].pop(0)
      p=random.randint(1,l-1)
      slices[s].insert(p,temp)
    last_domain=slices[s][-1][1]

  # assemble shuffle sequence
  shuffle=[]
  for s in slices:
    for i in s:
      shuffle.append(i[0])

  # generate and write shuffle file
  data=array.array('B')
  for i in shuffle:
    data.fromlist([i&0xFF,i>>8,0])
  f=file("iPod_Control/iTunes/iTunesShuffle","wb")
  data.tofile(f)
  f.close()

################################################################################

have=0
try:
  iTunesSD=file("iPod_Control/iTunes/iTunesSD","rb")
  header=array.array('B')
  header.fromfile(iTunesSD,HEADER_SIZE)
  if len(header)==HEADER_SIZE:
    have=1
    entry=array.array('B')
    entry.fromfile(iTunesSD,ENTRY_SIZE)
    if len(entry)==ENTRY_SIZE:
      have=2
except IOError:
  pass
except EOFError:
  pass

if have<1:
  print "Rebuilding iTunesSD file header from scratch."
  header=array.array('B')
  '''
  如果没有上行的header重新定义会怎样？ have=1/2那些情景里，header应该是已经写好的
  fromlist会继续向里添加18格0，造成header长度为36
  但是此句是在if have<1 里运行，have=0说明header没有读到iTunesSD文件，fromfile失败
  觉得没有必要重新定义header
  '''
  header.fromlist([0]*HEADER_SIZE)
  header[3]=0x01
  header[4]=0x06
  header[8]=0x12
else:
  print "Using iTunesSD file header from existing database."

if have<2:
  print "Rebuilding iTunesSD entry header from scratch."
  entry=array.array('B')   
  entry.fromlist([0]*ENTRY_SIZE)
  entry[1]=0x02
  entry[2]=0x2E
  entry[3]=0x5A
  entry[4]=0xA5
  entry[5]=0x01
  entry[26]=0x64
  entry[29]=0x01
  entry[31]=0x02
else:
  print "Using iTunesSD entry header from existing database."

if have: iTunesSD.close()
try:
  iTunesSD=file("iPod_Control/iTunes/iTunesSD","wb")
  header.tofile(iTunesSD)
  '''
  header先是fromfile ，失败的话就重新定义18格0和3,4,8格
  entry也是fromfile后重定义前[31]下标
  好像真的没有必要判断来判断去?反正header和entry都要重写，何不直接生产一个？
  为了尽量减少设备的改写？ entry[0-31]也只判断了第一首歌
  
  '''
except IOError:
  print "Critical error: cannot write iTunesSD database file!"
  sys.exit(1)

print
print "Searching for files on the iPod."
browse(".")
print
print total_count,"tracks were found on your iPod."

print "Fixing iTunesSD header."
header[2]=total_count&0xFF
header[1]=total_count>>8
iTunesSD.seek(0)
header.tofile(iTunesSD)
iTunesSD.close()

print "Generating new shuffle sequence."
try:
  make_shuffle()
except:
  print "Oops! There was an error while generating the shuffle sequence!"
  raise

print "Resetting playback state."
if os.path.isfile("iPod_Control/iTunes/iTunesPState"):
  try:
    os.remove("iPod_Control/iTunes/iTunesPState")
  except:
    print "Oops! There was an error while removing the playback state file!"

print "Resetting statistics."
if os.path.isfile("iPod_Control/iTunes/iTunesStats"):
  try:
    os.remove("iPod_Control/iTunes/iTunesStats")
  except:
    print "Oops! There was an error while removing the statistics file!"

print
print "iPod shuffle database was rebuilt successfully."
