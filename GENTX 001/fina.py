import tkinter as tk
from tkinter import *
from tkinter import filedialog
import shutil
import os
import subprocess
from PIL import Image, ImageTk
def generate_fields(v,frame1,frame2,frame3,m,r4cx):  
    for i in range(v):
            print("recc44",m)
            start_label = tk.Label(frame1, text=f"Start Time {i+1}:", bg=r4cx)
            start_label.pack(side=tk.TOP)
            
            end_label = tk.Label(frame2, text=f"End Time {i+1}:", bg=r4cx)
            end_label.pack(side=tk.TOP)
            
            start_entry = tk.Entry(frame1, bg=r4cx)
            start_entry.pack(side=tk.TOP)
           
            end_entry = tk.Entry(frame2, bg=r4cx)
            end_entry.pack(side=tk.TOP)
            if (m==0):
            
            
             startk.append(start_entry)
             endk.append(end_entry)
            if (m==1):
             
             
             start1.append(start_entry)
             end1.append(end_entry)
            if(m==5):
             end_labelx = tk.Label(frame3, text=f"which side do you want for overlay", bg=r4cx)
             end_labelx.pack(side=tk.TOP)
             end_entryx = tk.Entry(frame3, bg=r4cx)
             end_entryx.pack(side=tk.TOP)
             start2.append(start_entry)
             end2.append(end_entry)
             moto2.append(end_entryx)            
    if(m==0):
     load_text('saved_text.txt',num_trims.get(),startk)
     cd1=tk.Button(frame1, text="save start", bg=r4cx, command=lambda: save(startk,'saved_text.txt')).pack(side=tk.TOP)
     cd2=tk.Button(frame2, text="save end", bg=r4cx, command=lambda: save(endk,'saved1_text.txt')).pack(side=tk.TOP)
     load_text('saved1_text.txt',num_trims.get(),endk)
     
    if(m==1):
     load_text('saved4_text.txt',zooms.get(),start1)
     load_text('saved3_text.txt',zooms.get(),end1)
     cd1=tk.Button(frame1, text="effects seconds", bg=r4cx, command=lambda: save(start1,'saved4_text.txt')).pack(side=tk.TOP)
     cd2=tk.Button(frame2, text="speed mirror", bg=r4cx, command=lambda: save(end1,'saved3_text.txt')).pack(side=tk.TOP)
     
    if(m==5):
      load_text('saved7_text.txt',overs.get(),start2)
      load_text('saved8_text.txt',overs.get(),end2)
      cd1=tk.Button(frame1, text="save over start", bg=r4cx, command=lambda: save(start2,'saved7_text.txt')).pack(side=tk.TOP)
      cd2=tk.Button(frame2, text="save over end", bg=r4cx, command=lambda: save(end2,'saved8_text.txt')).pack(side=tk.TOP)
      load_text('saved6_text.txt',overs.get(),moto2)
      cd5=tk.Button(frame3, text="save position", bg=r4cx, command=lambda: save(moto2,'saved6_text.txt')).pack(side=tk.TOP) 
def submit_values(z):
    start_entries.clear()
    end_entries.clear()
    moto_entries.clear()
    if (z==1):
     start=start1
     end=end1
     log=zooms.get()
    if(z==0):
     start=startk
     end=endk
     log=num_trims.get()
    if(z==5):
     start=start2
     end=end2
     moto=moto2
     log=overs.get() 
    print(start)
    print(end)
    print("Start Times:", start_entries)
    print("End Times:", end_entries)
    for i in range(log):
        if(z==5):
         moto_time = moto[i].get()
         print(i,moto_time,moto[i])
         moto_entries.append(moto_time)
        start_time = start[i].get()
        print(i,start_time,start[i])
        end_time = end[i].get()
        start_entries.append(start_time)
        end_entries.append(end_time)
    start_time1 = start_entries[0]
    end_time1 = end_entries[0]
    print("Start Times:", start_entries)
    print("End Times:", end_entries)  
def suxmit_values():
   print("ll")
   starxt_entries.clear()
   for i in range(num_files.get()):
        no= starxt[i].get()
        print("jok")
        starxt_entries.append(no)
   print(starxt_entries)
def man_remon():
    global input_video 
    submit_values(0)
    po=0
    for i in range(num_trims.get()):
        if (i==0):
            rx=1
            print("OOL")
            print(input_video)
            output_video = 'vc.mp4'
            start_time1 = '00:00'
            end_time1 = start_entries[i]
            #start_time2= end_entries[i]
            vi=len(start_entries)-1
            print(start_time1,end_time1)
            if(start_time1!=end_time1):
             po=i-1
             trim_and_concat_videos(input_video, output_video, start_time1, end_time1,i,vi,po,rx)
        # Example Usage
        
        if (i==i):
            po=po+1
            start_time1=end_entries[i]
            if(i<vi):
              rx=rx+1
              end_time1=start_entries[i+1]
            else:
              rx=0 
            output_video = 'vc.mp4'
            trim_and_concat_videos(input_video, output_video, start_time1, end_time1,i,vi,po,rx)
    input_video='output.mp4'
    deletex('input.txt')
    with open('input.txt', 'w') as file:
       file.write("")   
def watermark(frame,z1):
        xo=xo4.get()
        vn=vx.get()
        global image
        global entry5
        if(z1==0):
         if(vn==1):
            image=refe(1,'image_files1.txt',bframe,2,"LightBlue3")
            print(image)
            entry5="none"
         if(vn==2):
                label = tk.Label(frame, text="Enter Text:",bg="LightBlue3")
                label.pack()
                entry5=refe(1,'niman.txt',bframe,2,"LightBlue3")
                image="none"
         start_buxtton = tk.Button(frame, text="OK",bg="LightBlue3", command=lambda n=xo,vz=vn: bo(n,vz,frame,image,entry5))
         start_buxtton.pack()
        if(z1==4):
         bo(xo,vn,frame,image,entry5)
def bo(xo4,vz,frame,image,entry):
        global input_video
        while 1==1:
            if(vz==1):
                ew="ffmpeg -i {} -y -v quiet -vf scale=1100*0.15:-1 scaled.png".format(image)
                subprocess.call(ew,shell=True) 
                print(image)
                if(xo4==1):
                    os.system(f'ffmpeg  -y -i  {input_video} -i scaled.png -filter_complex "overlay=main_w-overlay_w-5:5" -codec:a copy marked.mp4')
                if(xo4==2):               
                     os.system(f'ffmpeg  -y -i {input_video} -i scaled.png -filter_complex "overlay=5:5" -codec:a copy marked.mp4')
                if(xo4==3):                
                     os.system(f'ffmpeg -y  -i {input_video} -i scaled.png -filter_complex "overlay=5:main_h-overlay_h" -codec:a copy marked.mp4')
                if(xo4==4):                
                     os.system(f'ffmpeg -y -i {input_video} -i scaled.png -filter_complex "overlay=main_w-overlay_w-5:main_h-overlay_h-5" -codec:a copy marked.mp4')
                input_video='marked.mp4'             
            if(vz==2):
                oxk_button = tk.Button(frame, text="OK", command=lambda n=xo4,entry=entry: print_text(n,entry))
                oxk_button.pack()
                #ffmpeg -i "output.mp4" -vf "drawtext=text='{}':x=10:y=H-th-10:fontfile=Unlock-Regular.ttf:fontsize=30:fontcolor=white:shadowcolor=black:shadowx=5:shadowy=5" marked.mp4
                           
            break  
def water_text(text,n):
    global input_video
    i=0
    while i==0:  
         if(n==1):
                    os.system(f'ffmpeg -y  -i {input_video} -vf "drawtext=text=\'{text}\':x=w-tw-10:y=10:fontfile=UnlockRegular.ttf:fontsize=30:fontcolor=white:shadowcolor=black:shadowx=5:shadowy=5" marked.mp4')
         if(n==2):                         
                    os.system(f'ffmpeg -y  -i {input_video} -vf "drawtext=text=\'{text}\':x=10:y=10:fontfile=UnlockRegular.ttf:fontsize=30:fontcolor=white:shadowcolor=black:shadowx=5:shadowy=5" marked.mp4')
         if(n==3):                         
                     os.system(f'ffmpeg -y -i {input_video}  -vf "drawtext=text=\'{text}\':x=10:y=h-th-10:fontfile=UnlockRegular.ttf:fontsize=30:fontcolor=white:shadowcolor=black:shadowx=5:shadowy=5" marked.mp4')
         if(n==4):                        
                     os.system(f'ffmpeg -y  -i {input_video}  -vf "drawtext=text=\'{text}\':x=w-tw-10:y=h-th-10:fontfile=UnlockRegular.ttf:fontsize=30:fontcolor=white:shadowcolor=black:shadowx=5:shadowy=5" marked.mp4')               
         input_video='marked.mp4'
         break   
def print_text(n,entry):
    entered_text = entry.get()
    print(entered_text)
    water_text(entered_text,n)
def trim_and_concat_videos(input_video, output_video, start_time1, end_time1,i,vi,po,rx):

            print(i)
            while i<=vi:
                ile_path = 'input.txt'
                print(start_time1,end_time1)
                if(start_time1!=end_time1):
                    if(rx>0):
                        output_filename = f"trim{po}.mp4"
                        print(po)
                        bin=0
                        trim_command =  "ffmpeg -i {} -ss {} -to {} -c:v copy -c:a copy {}".format(input_video, start_time1,end_time1, output_filename)
                        subprocess.call(trim_command, shell=True)
                        if(po==po):
                         with open(ile_path, 'a') as file:
                          file.write("\nfile 'trim{}.mp4'".format(po))
                        
                        break
                    
                if(rx==0):
                    output_filename = f"trim{po}.mp4"
                    trim_command1 = "ffmpeg -i {} -ss {} -c:v copy -c:a copy {}".format(input_video, start_time1,output_filename )
                    subprocess.call(trim_command1, shell=True)
                    if(po==po):
                        print(po,"CJVJIVYBIVF")
                        with open(ile_path, 'a') as file:
                         file.write("\nfile 'trim{}.mp4'".format(po))
                if (i==vi):
                  #Command 2: Concatenate videos
                  concat_command = "ffmpeg -y -f concat -i input.txt -codec copy output.mp4"
                  subprocess.call(concat_command, shell=True)
                    #delete_command = "del {}.format(fi"
                    #subprocess.call(delete_command,shell=True)
                    #delete_commawnd = "del output12.mp4"
                    #subprocess.call(delete_commawnd,shell=True)
                  break  
def genezrate_file_fields(frame,r4cx):
    global file_paths
    file_paths = []
    num_dfiles = int(num_files.get())
    for i in range(num_dfiles):
            starxt_label = tk.Label(frame, text=f"Start Time {i+1}:", bg=r4cx)
            starxt_label.pack()
            starxt_entry = tk.Entry(frame, bg=r4cx)
            starxt_entry.pack()                                    
            starxt.append(starxt_entry) 
    load_text('saved2_text.txt',num_files.get(),starxt)
    cd5=tk.Button(frame, text="save clip", bg=r4cx, command=lambda: save(starxt,'saved2_text.txt')).pack()            
def deletex(file_path):
    with open(file_path, 'r') as file:
        files_to_delete = file.readlines()
        for file_name in files_to_delete:
            file_name = file_name.strip()
            file_name=file_name[6:-1]
            try:
                os.remove(file_name)
                print(f"Deleted: {file_name}")
            except FileNotFoundError:
                print(f"File not found: {file_name}")
            except Exception as e:
                print(f"Error deleting {file_name}: {e}")
def clip(staxt_tome,clipz,don,inpuxt_video,rn,man_ix,k3):
    global fuckd
    r42=[];r45=[]
    print(fuckd)
    i = 0
    while i == i:
        xile_path = 'clipo1.txt'
        if (k3==0):
            ouxtput_filename = f"clip{rn}.mp4"
            
            clim_command = "ffmpeg  -y -i {} -ss {} -to {} -c:v copy -c:a copy {}".format(inpuxt_video,man_ix, staxt_tome, ouxtput_filename)
            subprocess.call(clim_command, shell=True)
            get_tbn(ouxtput_filename,r42,44)
            get_tbn(clipz,r45,5)
            print(r42)
            #odod=int(input())
            if(r42!=r45):
             commandw=" ffmpeg -y -i {} -vf \"setpts=N/{}/TB,fps={},format=yuv420p\"  -c:v libx264 -preset ultrafast -c:a aac -ar 48k -b:v 1843k -video_track_timescale {} bron.mp4".format(clipz,r42[2],r42[2],r42[0]) 
             subprocess.call(commandw, shell=True)
             clipz="bron.mp4"
            
            with open(xile_path, 'a') as file:
                file.write("\nfile 'clip{}.mp4'".format(rn))
                vco=clipz.strip('"')
                file.write("\nfile '{}'".format(vco))
            if((rn+1)==len(fuckd)): 
                k3=1
            else:    
                break
        if (k3>0):
            ouxtput_filename = f"clip{rn+1}.mp4"
            clixm_command = "ffmpeg -y -i {} -ss {} -c:v copy -c:a copy {}".format(inpuxt_video, staxt_tome, ouxtput_filename)
            subprocess.call(clixm_command, shell=True)
            
            with open(xile_path, 'a') as file:
                file.write("\nfile 'clip{}.mp4'".format(rn+1))
            
            coxncat_command = "ffmpeg  -y -f concat -safe 0 -i clipo1.txt -c:v libx264 -preset ultrafast -video_track_timescale 90000 -c:a copy {}".format(don)
            subprocess.call(coxncat_command, shell=True)
            
            with open('clipo1.txt', 'w') as file:
                file.write("")
            break
def loose():
     global fuckd
     global input_video
     print("Selected Files:", fuckc)
     print("Selected Files:", fuckd)
     suxmit_values()
     for i in range(num_files.get()):
        print(fuckd[i])
        print(i)
        if(i==0):
            staxt_tome=starxt_entries[i]
            man_ix='00:00'
            clipz=fuckd[i] 
            print(clipz,"flsdfjs;ldfjsd;lfjsd")
            #roz=vxz(clipz,0)
            #if (roz==1):
             #clipz="bron.mp4"
            #teri=int(input())
            if(len(fuckd)==(i+1)):
              print(i,"th")
              don='output1.mp4'
            else:
             print(i,"txh")
             don=f"break{i}.mp4"
            rn=i;k3=0
            print("dxx",input_video)
            print(clipz)
           # loc=int(input())
            clip(staxt_tome,clipz,don,input_video,rn,man_ix,k3)
        if(i>0):
            staxt_tome=starxt_entries[i]
            man_ix=starxt_entries[i-1]
            clipz=fuckd[i] 
            print(clipz)
            #roz=vxz(clipz,0)
            #if (roz==1):
             #clipz="bron.mp4"
            #teri=int(input())            
            if(len(fuckd)==(i+1)):
             print(i,"th")
             don='output1.mp4'
            else:
             print(i,"txh")
             don=f"break{i}.mp4"
            rn=i;k3=0
            clip(staxt_tome,clipz,don,input_video,rn,man_ix,k3)
     input_video='output1.mp4'
     open_popup()
def man(bframe,cframe,inner_frame):
    try:
        with open("fuck.txt", "r") as f:
            num_trims.set(int(f.readline().strip()))    #int(file.read()))
            num_files.set(int(f.readline().strip())) 
            vx.set(int(f.readline().strip()))
            xo4.set(int(f.readline().strip()))
            zooms.set(int(f.readline().strip()))
            overs.set(int(f.readline().strip()))
            generate_fields(num_trims.get(),inner_frame,cframe,bframe,0,"DarkOliveGreen1");genezrate_file_fields(inner_frame,"orange")
            watermark(bframe,0); generate_fields(zooms.get(),inner_frame,cframe,bframe,1,"gray35");generate_fields(overs.get(),inner_frame,cframe,bframe,5,"sea green")        #int(file.read())) 
    except ValueError:
        pass
    except FileNotFoundError:
        pass
def refe(k,input_fuck,frame,j,r4cx):
 text_boxes=[]
 browse_buttons =[]
 global fuck
 global fuckd
 global fuckc
 global input_video
 fuck.clear()
 #print("rexxx",i)
 print(input_fuck)
 print(fuckd,"clipsxzzzz")
 
# Initialize the list of previously browsed files
 prev_files = []

# Load previously browsed files from a file
 if os.path.exists(input_fuck):
    print("legc")
    with open(input_fuck, 'r') as f:
        prev_files = [line.strip() for line in f]
        prev_files = ['"' + elem + '"' for elem in prev_files]
# Create the text boxes and browse buttons for multiple inputs
 print(prev_files)
 if(j==1):
  input_video=prev_files[0]
 
 for i in range(k):
    text_box = tk.Entry(frame,width=50, bg=r4cx)
    text_boxes.append(text_box)
    text_box.pack()

    # Create a browse button and add it to the list
    print(i,"xxxxx")
    browse_button = tk.Button(frame, text="Browse Files", bg=r4cx , command=lambda i=i: browse_files(text_boxes[i], prev_files,i))
    browse_buttons.append(browse_button)
    browse_button.pack()
    efdu=tk.Button(frame,text="clear", bg=r4cx ,command=lambda i=i :call(text_boxes[i],prev_files,i)).pack()

    # If there are previously browsed files, display them in the text boxes
    if i < len(prev_files):
        print(len(prev_files))
        text_box.insert(0, prev_files[i])
        fuck.insert(i,text_box.get())
        print("ggg")
# Define the function to browse files
 def browse_files(text_box, prev_files,i):
    # If there are no previously browsed files, ask the user to select a file
    if i<len(prev_files) and len(prev_files[i])>5:
         print(i,"fr")
         filename = prev_files[i]
         print("fdf",filename)
    else:
        # Otherwise, use the first previously browsed file
        print("rome")
        filename = filedialog.askopenfilename()
        #filename'
        print(filename)
    # Update the text box with the selected file path
    text_box.delete(0, tk.END)
    text_box.insert(0, filename)
    fuck.insert(i,text_box.get())
 cd=tk.Button(frame, text="save", bg=r4cx ,command=lambda: save(text_boxes,input_fuck)).pack()
 print(fuckd,"clipsx")
 if(j==2):
  return fuck[0]
 if(j==3):
  fuckd=fuck.copy()
  print(fuckd,"clip")
 if(j==0):
  fuckc=fuck.copy()
  print(fuckc,"over")
def save(text_boxes,input_fuck):
    with open(input_fuck, "w") as file:
        for box in text_boxes:
            text = box.get()
            file.write(text + "\n")
def call(text_box,prev_files,i):
   print(i)
   text_box.delete(0, tk.END)
   prev_files[i]="0"
def load_text(input_suck,b,text_boxes):
    try:
        with open(input_suck, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
               if i>=b:
                   break
               text_boxes[i].insert(0, line.strip())
               print(text_boxes[i].get())
    except FileNotFoundError:
        pass
def inoco(frame1,frame2,frame3):
 xouu=num_trims.get()
 if(xouu>0):
  man_remon()#trim
 xouu=num_files.get()
 if(xouu>0):
  loose()#clip add
 xouu=vx.get()
 if(xouu>0):
  watermark(frame1,4)#obviosly watermark
 xouu=overs.get()
 if(xouu>0):
  lofu()# clip overlay
 xouu=zooms.get()
 if(xouu>0):
   levent()#zooming
 open_popup()#finlay
def zoom_in_video(start_time, end_time,input_video):
    global box
    b,rep= end_time.split()
    b=int(b)
    rep= int(rep)
    r=int(start_time)
    """
    Zoom in on a specific region of a video using FFmpeg.

    Args:
        input_video (str): Path to the input video file.
        start_time (str): Start time of the zoom region in HH:MM:SS format.
        end_time (str): End time of the zoom region in HH:MM:SS format.
        zoom_factor (float): Zoom factor (e.g. 2.0 for 2x zoom).
        output_filename (str): Path to the output video file.
    """
    print_text_with_time(input_video,b,r,rep)
    """ 
    print(box[0])
    xees=input()
    output_filename="zoomed.mp4"
    zand =  "ffmpeg -i {} -ss 00:00 -to {} -c:v copy -c:a copy {}".format(input_video, start_time,"zoom1.mp4" )
    subprocess.call(zand, shell=True)
    zand1 =  "ffmpeg -i {} -ss {} -to {} -c:v copy -c:a copy {}".format(input_video, start_time,end_time,"zoom2.mp4" )
    subprocess.call(zand1, shell=True)
    zand3= "ffmpeg -y -i {} -vf \"scale=-2:720,crop=in_w/2:in_h/2,setsar=1\" -c:v libx264 -preset ultrafast -video_track_timescale {} -c:a copy {}".format("zoom2.mp4",box[0],"zoom3.mp4")
    subprocess.call(zand3, shell=True)
    zand5 =  "ffmpeg -y -i {} -ss {}   -c:v copy -c:a copy {}".format(input_video,end_time,"zoom2.mp4" )
    subprocess.call(zand5, shell=True)
    mand = "ffmpeg -f concat -i zoomi.txt -codec copy zoomed.mp4"
    subprocess.call(mand, shell=True)
    deletex('zoomi.txt')  """
def levent():
 global input_video
 input_video1=input_video
 submit_values(1)
 for i in range (zooms.get()):
   start_time=start_entries[i]
   end_time=end_entries[i]
   zoom_in_video(start_time, end_time,input_video1)
   input_video1="zoomed.mp4"
 input_video="zoomed.mp4"
def open_popup():
   #global bg_photo5
   global input_video
   top= Toplevel(root)
   top.geometry("1000x200")
   top.title("Child Window")
   #background_label = tk.Label(top, image=bg_image5)
   Label(top, text= "DONE GOD!", font=('Mistral 18 bold')).place(x=400,y=40)
   Label(top, text= f"THIS IS THE FINAL VIDEO {input_video} save it", font=('Mistral 18 bold')).place(x=0,y=90)   
def overlay(start_time,end_time,input_video,ko,vadio):
    print(ko,start_time,end_time,input_video,vadio) 
    ko=int(ko)   
    output_filename="overlayed.mp4"
    over_video="fuckx.mp4"
    zand3x= "ffmpeg -y -i {} -vcodec copy -an fuckx.mp4".format(vadio)
    subprocess.call(zand3x, shell=True)
    if(ko==1):
             zoomi = "ffmpeg -y  -i {} -i {} -filter_complex \"[1:v]scale=320:240[ovly];[0:v][ovly]overlay=x=(W-w-10):y=10:enable='between(t,{},{})'\" -c:a copy overlayed.mp4".format(input_video,over_video,start_time,end_time)
             subprocess.run(zoomi, shell=True)      
    if(ko==2):   
            zoomi = "ffmpeg -y  -i {} -i {} -filter_complex \"[1:v]scale=320:240[ovly];[0:v][ovly]overlay=x=10:y=10:enable='between(t,{},{})'\" -c:a copy overlayed.mp4".format(input_video,over_video,start_time,end_time)
            subprocess.run(zoomi, shell=True)      
    if(ko==3):                         
             zoomi = "ffmpeg -y  -i {} -i {}-filter_complex \"[1:v]scale=320:240[ovly];[0:v][ovly]overlay=x=10:y=(H-h-10):enable='between(t,{},{})'\" -c:a copy overlayed.mp4}".format(input_video,over_video,start_time,end_time)
             subprocess.run(zoomi, shell=True)     
    if(ko==4):                        
            zoomi = "ffmpeg -y -i {} -i {} -filter_complex \"[1:v]scale=320:240[ovly];[0:v][ovly]overlay=x=(W-w-10):y=(H-h-10):enable='between(t,{},{})'\" -c:a copy overlayed.mp4".format(input_video,over_video,start_time,end_time)
            subprocess.run(zoomi, shell=True)       
    deletex('over.txt')
def lofu():
 global input_video
 global fuckc
 input_video1=input_video
 submit_values(5)
 for i in range (overs.get()):
   start_time=convert3x(start_entries[i])
   end_time=convert3x(end_entries[i])
   ko=moto_entries[i]
   print(ko)
   vadio=fuckc[i]
   print(vadio,"gkheriugidfilhgr44545")
   overlay(start_time, end_time,input_video1,ko,vadio)
   input_video1="overlayed.mp4"
 input_video="overlayed.mp4"
 open_popup() 
def vxz(input_video2,wq):
 global box 
 global input_video
 input_string = input_video2
 print("12345",input_string)
 if(wq==1):
  if input_string[-5:] == '.mkv"':
    print("dsfdfx222")
    commandw=" ffmpeg -i {} -vf \"setpts=N/23.98/TB,fps=23.98,format=yuv420p\"  -c:v libx264 -preset ultrafast -c:a aac -ar 48k  -b:v 1843k -video_track_timescale 90k inputze.mp4".format(input_video2) 
    subprocess.call(commandw, shell=True)
    input_video="inputze.mp4"
 if(wq==0):
  print("onnd")
  bam=[]
  get_tbn(input_video2,bam)
  print(bam,box)
  if(box!=bam):
    commandw=" ffmpeg -y -i {} -vf \"setpts=N/{}/TB,fps={},format=yuv420p\"  -c:v libx264 -preset ultrafast -c:a aac -ar 48k -b:v 1843k -video_track_timescale {} bron.mp4".format(input_video2,box[2],box[2],box[0]) 
    subprocess.call(commandw, shell=True)
    return 1 
def get_tbn(video_file_path,beve,bo):
    vomax=1;man="67l";result=99
    print("jdgufgsdjfxxxxxxx",video_file_path)
    #video_file_path=video_file_path.strip('"')
    if(bo==5):
     video_file_path= video_file_path[1:-1]
    command = ["ffprobe", "-v", "0", "-of", "compact=p=0:nk=1", "-show_entries", "stream=time_base", "-select_streams", "v:0", video_file_path]
    output = subprocess.run(command,stdout=subprocess.PIPE).stdout.decode('utf-8')
    vout = ["ffprobe", video_file_path, "-v", "0", "-select_streams", "v", "-print_format", "flat", "-show_entries", "stream=r_frame_rate"]
    out = subprocess.run(vout,stdout=subprocess.PIPE).stdout.decode('utf-8')
    vout2 = ["ffprobe", video_file_path, "-v", "0", "-select_streams", "a", "-print_format", "flat", "-show_entries", "stream=sample_rate"]
    out2 = subprocess.run(vout2,stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(out2,out,output)
    vomax=int((out[31:33])) 
    man=(out2[30:32])+"k"  
    result = output[2:]
    result=int(result)
    print(result)
    beve.append(result)
    beve.append(man)
    beve.append(vomax)
def convert3x(mm_ss):
    minutes, seconds = map(int, mm_ss.split(':'))
    total_seconds = minutes * 60 + seconds
    return total_seconds
def savez():
    box=[1,2,3,4,5,6,7,8,9,10]
    box[0]=num_trims.get()   #int(file.read()))
    box[1]=num_files.get()
    box[2]=vx.get()
    box[3]=xo4.get()
    box[4]=zooms.get()
    box[5]=overs.get()
    with open("fuck.txt", "w") as file:
        for i in range(6):
            print(i,box[i])
            text = box[i]
            file.write(str(text)+ "\n")
def print_text_with_time(video_path,b,r,rep):
    print(video_path)
    video_length = get_video_length(video_path)  # Calculate the video length
    print(video_length)
    #osi=input()
    k = 1
    brom = video_path
    if(r>0):
     for i in range(10, video_length, r):
        start_time = i
        end_time = i + 5
        lop=i-r
        if k == 1:
            print("staet",start_time,end_time)
            #osi=input()
            # Define zoomed video segments
            if (lop==0): 
             subprocess.call(f"ffmpeg -y -i {video_path} -ss  00 -to {start_time}  -c:v libx264 -preset ultrafast -video_track_timescale 90000 -c:a copy zoom1.mp4", shell=True)
            else:
             subprocess.call(f"ffmpeg -i {video_path} -ss  {lop+5} -to {start_time}  -c:v libx264 -preset ultrafast -video_track_timescale 90000 -c:a copy zoom1.mp4", shell=True)
            subprocess.call(f"ffmpeg  -y -i {video_path} -ss {start_time} -to {end_time} -c:v libx264 -preset ultrafast -video_track_timescale 90000 -c:a copy zoom2.mp4", shell=True)
            kom = f"xev{i}.mp4"

            # Scale and crop zoom2
            subprocess.call(f"ffmpeg -y -i zoom2.mp4 -vf \"scale=-2:720,crop=in_w/2:in_h/2,setsar=1\" -c:v libx264 -preset ultrafast -video_track_timescale 90000 -c:a copy zoom3.mp4", shell=True)
            os.remove('zoom2.mp4')
            #subprocess.call(f"ffmpeg -i {video_path} -ss {end_time + 2} -c copy zoom2.mp4", shell=True)
            # Combine the parts
            #subprocess.call(f"ffmpeg -y -i xtest3.mp4 -ss {end_time} -c:v copy -c:a copy zoom2.mp4", shell=True)
            subprocess.call(f"ffmpeg  -y -f concat -i zoomi.txt -codec copy -avoid_negative_ts make_zero {kom}", shell=True)
            with open("goin.txt", "a") as file:
             file.write("\nfile 'xev{}.mp4'".format(i))

            # Clean up
            deletex('zoomi.txt')
            # os.remove("zoomi.txt")  # Uncomment if you want to delete the file
            print(start_time,end_time)
            #osi=input()
            k += 1
        # Determine which text to print based on time
        elif k == 2:
            print("staet",start_time,end_time)
            #osi=input()
            # Split the video into parts
            subprocess.call(f"ffmpeg -i {video_path}  -ss {lop+5} -to {start_time} -c:v libx264 -preset ultrafast -video_track_timescale 90000 -c:a copy part1.mp4", shell=True)
            subprocess.call(f"ffmpeg -i {video_path} -ss {start_time} -to {end_time} -c:v libx264 -preset ultrafast -video_track_timescale 90000 -c:a copy part2.mp4", shell=True)
            #subprocess.call(f"ffmpeg -i {video_path} -ss {end_time} -c copy part3.mp4", shell=True)

            # Apply fade effect to part2
            subprocess.call(f"ffmpeg -i part2.mp4 -vf \"fade=t=out:st=0:d=2\" -c:v libx264 -preset ultrafast -video_track_timescale 90000 -c:a copy part2_fade.mp4", shell=True)

            # Create input.txt for concatenation
           # with open("input.txt", "w") as f:
               # f.write("file 'part1.mp4'\n")
               # f.write("file 'part2_fade.mp4'\n")
                #f.write("file 'part3.mp4'\n")
            kom = f"xev{i}.mp4"
            # Concatenate parts
            subprocess.call(f"ffmpeg  -y -f concat -safe 0 -i concat_list.txt -c copy -avoid_negative_ts make_zero {kom}", shell=True)
            with open("goin.txt", "a") as file:
                file.write("\nfile 'xev{}.mp4'".format(i))
            deletex('concat_list.txt')
            #os.remove('zoomed.mp4')
            print(start_time,end_time)
            #osi=input()
            k += 1

        elif k == 3:
            print("staet",start_time,end_time)
            #osi=input()
            #os.remove('spin.mp4')
            subprocess.call(f"ffmpeg -i {video_path} -ss {lop+5} -to {start_time} -c:v libx264 -preset ultrafast -video_track_timescale 90000 -c:a copy part1.mp4", shell=True)
            os.remove('part2.mp4')
            subprocess.call(f"ffmpeg -i {video_path}  -ss {start_time} -to {end_time} -c:v libx264 -preset ultrafast -video_track_timescale 90000 -c:a copy part2.mp4", shell=True)
            #subprocess.call(f"ffmpeg -i {video_path}  -ss {end_time} -c copy part3.mp4", shell=True)
            # Rotate the video for a specific segment
            subprocess.call(f"ffmpeg -i part2.mp4 -vf \"rotate=PI/2*t\" -c:v libx264 -preset ultrafast -video_track_timescale 90000 -c:a copy part2_fade.mp4", shell=True)
            kom = f"xev{i}.mp4"
            # Concatenate parts
            subprocess.call(f"ffmpeg -f concat -safe 0 -i concat_list.txt -c copy -avoid_negative_ts make_zero {kom}", shell=True)
            with open("goin.txt", "a") as file:
                file.write("\nfile 'xev{}.mp4'".format(i))
            #video_path='spin.mp4'
            deletex('concat_list.txt')
            #os.remove('kes.mp4')
            os.remove('part2.mp4')
            print(start_time,end_time)
            #osi=input()
            
            k = 1
     subprocess.call("ffmpeg -f concat -safe 0 -i goin.txt -c copy -avoid_negative_ts make_zero kes.mp4", shell=True)
     deletex('goin.txt')
     subprocess.call(f"ffmpeg -y -i {video_path}  -ss {end_time} -c copy part3.mp4", shell=True)
     subprocess.call("ffmpeg -f concat -safe 0 -i goinz.txt -c copy -avoid_negative_ts make_zero finala.mp4", shell=True)
     with open("goin.txt", "w") as file:
      file.write("".format(i))
     brom='finala.mp4'
    if(b==1):
     subprocess.call(f"ffmpeg -y -i {brom} -filter:v \"setpts=0.5*PTS\" -c:v libx264 -preset ultrafast -video_track_timescale 90000 -c:a copy final3.mp4", shell=True)
    if(rep==2):
     if(b==1):
      subprocess.call(f"ffmpeg  -y -i final3.mp4 -vf \"hflip\" -c:v libx264 -preset ultrafast -video_track_timescale 90000 -c:a copy finala.mp4", shell=True)
      os.remove('final3.mp4')
     else:
      subprocess.call(f"ffmpeg  -y -i {brom} -vf \"hflip\" -c:v libx264 -preset ultrafast -video_track_timescale 90000 -c:a copy final3.mp4", shell=True)
def get_video_length(video_path):
    """Get the length of the video in seconds."""
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
             '-of', 'default=noprint_wrappers=1:nokey=1', video_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        duration = float(result.stdout.strip())
        return int(duration)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
root = tk.Tk()
root.title("GIRL")
root.geometry("1300x900")
bg_image = Image.open("remen.jpg")
bg_photo = ImageTk.PhotoImage(bg_image,master=root)
bg_image1 = Image.open("remen1.jpg")
bg_photo1 = ImageTk.PhotoImage(bg_image1,master=root)
bg_image2 = Image.open("remen2.jpg")
bg_photo2 = ImageTk.PhotoImage(bg_image2,master=root)
bg_image5 = Image.open("remen.jpg")
bg_photo5 = ImageTk.PhotoImage(bg_image5)
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)
canvas = tk.Canvas(frame)
canvas.pack(side="left", fill="both", expand=True)
canvas.create_image(0,0,image=bg_photo, anchor="nw")
# Create a scrollbar
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
# Configure the canvas to use the scrollbar
canvas.config(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion =canvas.bbox("all")))
# Create an inner frame to hold the widgets
inner_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")
bframe = tk.Frame(canvas)
canvas.create_window((400, 0), window=bframe, anchor="nw")
cframe = tk.Frame(canvas)
canvas.create_window((1000, 0), window=cframe, anchor="nw")
label = Label(inner_frame, image=bg_photo)
label.image = bg_photo
label.place(x=0, y=0)
label = Label(bframe, image=bg_photo1)
label.image = bg_photo1
label.place(x=0, y=0)
label = Label(cframe, image=bg_photo2)
label.image = bg_photo2
label.place(x=0, y=0)
loz=tk.IntVar()
fuck=[];fuckd=[];fuckc=[]
input_folder = tk.StringVar();num_trims = tk.IntVar();zooms= tk.IntVar();overs= tk.IntVar()
input_video ="dd"
bonao="DarkOliveGreen1"
tk.Label(bframe, text="Input Folder:").pack(side=tk.TOP)
refe(1,'image_files.txt',bframe,1,"white")
print("xxs",input_video)
vxz(input_video,1)
box=[]
get_tbn(input_video,box,5)
xo4 = tk.IntVar()
vx = tk.IntVar()
image="dfkff"
entry5="dkfgf"
starxt = []
startk = [];start1=[];start2=[];folu=[];moto2=[];vccx=[];endk = [];end1=[];end2=[]
start_entries = [];end_entries = [];moto_entries=[];starxt_entries = []
vi=0;rx=1
def scroll_canvas():
    global ka
    # Calculate the current position of the canvas
    x_scroll = canvas.xview()[0]
    y_scroll = canvas.yview()[0]

    # Calculate the new position of the canvas
    new_x_scroll = x_scroll + 0.01
    new_y_scroll = y_scroll + 0.01

    # Scroll the canvas to the new position
    canvas.xview_moveto(new_x_scroll)
    canvas.yview_moveto(new_y_scroll)

    # Schedule the next scrolling step
    if(ka==0):
     root.after(10,scroll_canvas)
#scroll_canvas()
trim_label = tk.Label(bframe, text="Enter Number of Trims:",bg=bonao)
trim_label.pack(side=tk.TOP)
trim_input = tk.Entry(bframe, textvariable=num_trims,bg=bonao)
trim_input.pack(side=tk.TOP)
generate_button = tk.Button(bframe, text="Generate Trim Fields",bg=bonao, command= lambda :generate_fields(inner_frame,cframe,bframe,0))
generate_button.pack(side=tk.TOP)
tk.Button(bframe, text="START TORIM",bg=bonao,command=man_remon).pack(side=tk.TOP)
num_files=tk.IntVar()
bonao="orange"
labexl = tk.Label(bframe, text="Enter the number of files:",bg=bonao)
labexl.pack(side=tk.TOP)
enxtry = tk.Entry(bframe,textvariable=num_files,bg=bonao)
enxtry.pack(side=tk.TOP)
butzton = tk.Button(bframe, text="Generate CLIP Fields",bg=bonao, command=lambda:genezrate_file_fields(inner_frame))
butzton.pack(side=tk.TOP)
suxmit_button = tk.Button(bframe, text="Submit CLIP",bg=bonao, command=loose)
suxmit_button.pack(side=tk.TOP)
bonao="LightBlue3"
xo = tk.Label(bframe, text="choose 1 for image 2 f0r text",bg=bonao)
xo.pack(side=tk.TOP)
wate1r_input = tk.Entry(bframe, textvariable=vx,bg=bonao)
wate1r_input.pack(side=tk.TOP)
water = tk.Label(bframe, text="choose 1 for Top right 2 f0r Top left 3 bottom left 4 bottom right",bg=bonao)
water.pack(side=tk.TOP)
water_input = tk.Entry(bframe, textvariable=xo4,bg=bonao)
water_input.pack(side=tk.TOP)
tk.Button(bframe, text="WATERXMARK",bg=bonao,command= lambda :watermark(bframe)).pack()
tk.Button(bframe, text="SAVERE",command=savez).pack()
bonao="gray35"
l = tk.Label(bframe, text="Enter Number of Zooms:",bg=bonao)
l.pack(side=tk.TOP)
t = tk.Entry(bframe, textvariable=zooms,bg=bonao)
t.pack(side=tk.TOP)
bonao="forest green"
lo = tk.Label(bframe, text="Enter Number of OVERLAYS:",bg=bonao)
lo.pack(side=tk.TOP)
to = tk.Entry(bframe, textvariable=overs,bg=bonao)
to.pack(side=tk.TOP)
man(bframe,cframe,inner_frame)
lo3 = tk.Label(cframe,text="I AM CLIPPER")
lo3.pack(side=tk.TOP)
refe(num_files.get(),'clipo.txt',cframe,3,"orange")
print(fuckd,"clipdfgdfgdnfga")
print(fuckc,"overfsdfsdfsdfsdfsd")
lo7 = tk.Label(inner_frame, text="I AM SLAYER",bg="forest green")
lo7.pack(side=tk.TOP)
refe(overs.get(),'overo.txt',inner_frame,0,"forest green")
tk.Button(bframe , text="ZOOMI",command=levent,bg="gray35").pack()
tk.Button(bframe , text="OVERLAY",command=lofu,bg="forest green").pack()
tk.Button(bframe , text="HELP?",command=open_popup).pack()
tk.Button(bframe , text="WAR",command=lambda:inoco(bframe,cframe,inner_frame)).pack()
#canvas.xview_moveto(500)
#canvas.yview_moveto(100000)
print(fuckd,"clip")
print(fuckc,"over")
root.mainloop()


# Create a canvas to hold the inner frame
# Create a label with the background image
#bg_label = tk.Label(root, image=bg_photo)
#bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame to hold the text boxes and buttons
# Example Usage

#output_video = 'output.mp4'
#start_time2 = '00:01:30'
#print(input_video)
#inner_frame.place(relx=0.5, rely=0.5, anchor=CENTER)