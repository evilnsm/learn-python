#!/usr/bin/env python
# -*- coding: iso-8859-1

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

domains=[]

################################################################################

def write_to_db(filename):
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
  while offset<ENTRY_SIZE:
    entry[offset]=0
    if fnpos<fnlen:
      entry[offset+1]=ord(filename[fnpos])
      fnpos+=1
    else:
      entry[offset+1]=0
    offset+=2
  if ext!=".m4b" and ext!=".aa":
    entry[555]=1
  entry.tofile(iTunesSD)
  domains[-1].append(total_count);
  total_count+=1

################################################################################

def browse(path):
  global header,entry,domains
  count=0

  if path=='.': print "/:",
  else: print "%s:"%path[1:],
  sys.stdout.flush()

  try:
    dir=os.listdir(path)
  except OSError:
    print "cannot browse"
    return

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
    fullname=path+'/'+item[1:]
    if item[0]=='D':
      browse(fullname)
    elif item[0]=='F':
      write_to_db(fullname)
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
