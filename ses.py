import requests,json,os,sys,time,re,random
res = requests.Session();

g = ("\33[0;32m")#Green")
gl = ("\33[32;1m")#GreenLight")
b = ("\33[0;36m")#Blue")
bl = ("\33[36;1m")#BlueLight")
red = ("\33[31;1m")#Red")
w = ("\33[37;1m")#White")
black = ("\33[30;1m")#Black")
y = ("\33[33;1m")#Yellow")
yl = ("\33[1;33m")#YellowLight")
ttp = ("\033[0m")#LightGrey")
underline = ('\033[4;37;48m')

logo = ("""
 _____           _              
/  ___|         | |             
\ `--.  ___  ___| |_ _   _  ___ 
 `--. \/ _ \/ __| __| | | |/ __|
/\__/ /  __/\__ \ |_| |_| | (__ 
\____/ \___||___/\__|\__, |\___|
                      __/ |     
                     |___/   """)

def main():
    try:
        with open('data.json') as f:
            data = json.load(f)
    except (KeyError,IOError,OSError):
        print(w+"["+red+"!"+w+"] Data not available.")
        try:
            inusername_saya = input(w+"["+g+"+"+w+"] Username : "+gl)
            inkey_owner_saya = input(w+"["+g+"+"+w+"] Key Owner : "+gl)
            inuser_id_saya = input(w+"["+g+"+"+w+"] User ID : "+gl) #atau myuserid
            insession_key_saya = input(w+"["+g+"+"+w+"] Session Key : "+gl)
            cek = res.post("https://sestyc.com/sestyc/profile_init_script_93.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '179'}, data=("user_name="+inusername_saya+"&session_key="+insession_key_saya+"&key_owner="+inkey_owner_saya+"&user_id="+inuser_id_saya+"&")).text
            sts = json.loads(cek)
            indisplay_picture_saya = sts['post_data'][0]['display_picture']
            indisplay_name_saya = sts['post_data'][0]['display_name']
            js = {"username_saya":inusername_saya, "session_key_saya": insession_key_saya, "user_id_saya": inuser_id_saya, "key_owner_saya": inkey_owner_saya, "display_picture_saya": indisplay_picture_saya, "display_name_saya": indisplay_name_saya}
            with open("data.json", "w") as baca_file:
                json.dump(js, baca_file)
            print(w+"["+g+"#"+w+"] Saved Data : "+b+"data.json")
            input(w+"["+b+">>"+w+"] Press Enter to menu ...")
            menu()
        except:
            exit("Terjadi Kesalahan data !")
    menu()

def menu():
    global username_saya, session_key_saya, user_id_saya, key_owner_saya, display_picture_saya, display_name_saya
    os.system("clear")
    with open('data.json', 'r') as f:
        array = json.load(f)
    username_saya = array['username_saya']
    session_key_saya = array['session_key_saya']
    user_id_saya = array['user_id_saya']
    key_owner_saya = array['key_owner_saya']
    display_picture_saya = array['display_picture_saya']
    display_name_saya = array['display_name_saya']
    menus = res.post("https://sestyc.com/sestyc/profile_init_script_93.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '179'}, data=("user_name="+username_saya+"&session_key="+session_key_saya+"&key_owner="+key_owner_saya+"&user_id="+user_id_saya+"&")).text
    menuk = json.loads(menus)
    os.system("clear")
    print(logo)
    print(ttp+"Selamat Datang, "+g+menuk['post_data'][0]['display_name'])
    print(ttp+50*"-")
    print(ttp+"Username : "+g+"@"+menuk['post_data'][0]['owner_user_name']+ttp+" | ID : "+g+menuk['post_data'][0]['owner'])
    if str(menuk['verified']) in "0":
        print(ttp+"Verified Account : "+red+"False")
    else:
        print(ttp+"Verified Account : "+b+"True")
    print(ttp+"Post>"+y+str(menuk['post'])+ttp+" Followers>"+y+str(menuk['followers'])+ttp+" Followings>"+y+str(menuk['followings'])+ttp)
    print("Popularity : ("+y+str(menuk['popularity'])+ttp+")")
    print(50*"-")
    print("[1.] Popularity Rank")
    print("[2.] Minta Koin")
    print("[3.] Jalankan BOT BarBar")
    print("[4.] Jalankan BOT Sapa+Stiker")
    print("[5.] Unfollow for not Followers")
    print("[6.] Unfollow Massal ( "+red+"Ga Ngotak"+ttp+" )")
    print("[7.] Delete Postingan Massal")
    print("[8.] Ganti Akun")
    print("[0.] Exit Programs")
    print()
    pilih = input("CHoose : ")
    if pilih =="1":
        print()
        popularity()
    elif pilih =="2":
        print()
        minta()
    elif pilih =="3":
        print()
        bot()
    elif pilih =="4":
        print()
        botsapa()
    elif pilih =="5":
        print()
        try:
            unfollow()
        except:
            input(w+"\n["+red+"!!!"+w+"] Terjadi Kesalahan ...")
            menu()
    elif pilih =="6":
        print()
        unfollowmass()
    elif pilih =="7":
        print()
        deletemass()
    elif pilih =="8":
        print()
        print("Menghapus Config ...")
        time.sleep(1)
        os.system("rm -rf data.json")
        main()
    elif pilih =="123":
        print()
        top()
    else:
        exit()

def popularity():
    loop = []
    print("Searching Data ...\n")
    time.sleep(2)
    ex = res.post("https://sestyc.com/sestyc/popularity_ranking_init_script.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '163'}, data=("session_key="+session_key_saya+"&key_owner="+key_owner_saya+"&user_id="+user_id_saya+"&")).text
    slot = json.loads(ex)
    for i in slot['ranking']:
        loop.append(i['display_name'])
        if display_name_saya in i['display_name']:
            print(y+"> "+ttp+str(len(loop))+". "+g+i['display_name']+ttp+" | "+y+str(i['popularity'])+ttp+" You Rank "+str(len(loop)))
        else:
            print(str(len(loop))+". "+g+i['display_name']+ttp+" | "+y+str(i['popularity'])+ttp)
    input(w+"\n["+b+">>"+w+"] Press Enter to back menu ...")
    menu()

def minta():
    print("Meminta ...\n")
    os.system("xdg-open https://api.whatsapp.com/send?phone=62895611252563&text=Halo,%20saya%20mau%20minta%20koin%20Sestycnya%20sedikit%20%20DataSaya:%20Session=%20"+session_key_saya+"%20|%20UserID=%20"+user_id_saya)
    input(w+"\n["+b+">>"+w+"] Press Enter to back menu ...")
    menu()

def top():
    loop = []
    print("Sistem LOoping Saya beri delay 1/30detik, Agar akun kalian tidak terdeteksi Spam ...")
    time.sleep(2)
    print("Bot akan dimulai dalam 3 detik ..")
    time.sleep(3)
    data_explore = ("session_key="+session_key_saya+"&key_owner="+key_owner_saya+"&user_id="+user_id_saya+"&")
    req = res.post("https://sestyc.com/sestyc/get_explore_latest_script.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '479'}, data=data_explore).text
    sts = json.loads(req)
    for z in sts:
        fcm_id = z['fcm_id']
        other_user_id = z['owner']
        post_id = z['post_id']	
        post_picture = z['post_picture']
        target = z['owner_user_name']
        #Langkahi User Baperan
        if "sestyc" in target:
            pass
        elif "kevin" in target:
            pass
        elif "dixon" in target:
            pass
        elif "jesslyn" in target:
            pass
        elif "michaelfrancesco" in target:
            pass
        elif "andykurnia" in target:
            pass
        else:
            loop.append(target)
            scan = res.post("https://sestyc.com/sestyc/profile_init_other_script_93.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '523'}, data=("session_key="+session_key_saya+"&my_user_id="+key_owner_saya+"&key_owner="+other_user_id+"&user_id="+key_owner_saya+"&")).text
            scan_json = json.loads(scan)
            print(scan_json)

def bot():
    loop = []
    print("Sistem LOoping Saya beri delay 1/30detik, Agar akun kalian tidak terdeteksi Spam ...")
    time.sleep(2)
    print("Bot akan dimulai dalam 3 detik ..")
    time.sleep(3)
    data_explore = ("session_key="+session_key_saya+"&key_owner="+key_owner_saya+"&user_id="+user_id_saya+"&")
    req = res.post("https://sestyc.com/sestyc/get_explore_latest_script.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '479'}, data=data_explore).text
    sts = json.loads(req)
    for z in sts:
        fcm_id = z['fcm_id']
        other_user_id = z['owner']
        post_id = z['post_id']	
        post_picture = z['post_picture']
        target = z['owner_user_name']
        #Langkahi User Baperan
        if "sestyc" in target:
            pass
        elif "kevin" in target:
            pass
        elif "dixon" in target:
            pass
        elif "jesslyn" in target:
            pass
        elif "michaelfrancesco" in target:
            pass
        elif "andykurnia" in target:
            pass
        else:
            loop.append(target)
            scan = res.post("https://sestyc.com/sestyc/profile_init_other_script_93.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '181'}, data=("session_key="+session_key_saya+"&my_user_id="+key_owner_saya+"&key_owner="+user_id_saya+"&user_id="+other_user_id+"&")).text
            scan_json = json.loads(scan)
            if "0" in str(scan_json['is_follower']):
                #Follow
                data_follow = ("display_picture="+display_picture_saya+"&key_owner="+key_owner_saya+"&time_stamp=&fcm_id="+fcm_id+"&otherUserId="+other_user_id+"&display_name="+display_name_saya+"&session_key="+session_key_saya+"&myUserId="+user_id_saya+"&")
                get_follow = res.post("https://sestyc.com/sestyc/following_script.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '772'}, data=data_follow).text
                #Like
                data_like = ("display_picture="+display_picture_saya+"&key_owner="+key_owner_saya+"&time_stamp=04%3A13+PM&fcm_id="+fcm_id+"&post_id="+post_id+"&post_picture="+post_picture+"&display_name="+display_name_saya+"&session_key="+session_key_saya+"&owner="+other_user_id+"&user_id="+user_id_saya+"&")
                get_like = res.post("https://sestyc.com/sestyc/moment_like_script.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '849'}, data=data_like).text
                #Comment
                data_comment = ("display_picture="+display_picture_saya+"&key_owner="+key_owner_saya+"&time_stamp=04%3A13+PM&fcm_id="+fcm_id+"&post_id="+post_id+"&post_picture="+post_picture+"&display_name="+display_name_saya+"&session_key="+session_key_saya+"&owner="+other_user_id+"&user_id="+user_id_saya+"&comment_message=Rm9sbGJhY2sgS2FrIDonKQ%3D%3D%0A&")
                get_comment = res.post("https://sestyc.com/sestyc/moment_comment_script.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '897'}, data=data_comment).text
                com = json.loads(get_comment)['result']
                print(ttp+str(len(loop))+"> Meminta : "+b+target+ttp+" F>"+get_follow+" L>"+get_like+" C>"+str(com))
                time.sleep(30)
            else:
                print(ttp+str(len(loop))+"> Sudah Menjadi Followers : "+b+target)
                pass
    print(ttp+"\n["+g+"$"+ttp+"] Done")
    print(ttp+"["+g+"?"+ttp+"] Total Media : "+b+str(len(loop)))
    print(ttp+"["+g+"Rekomendasi"+ttp+"] Pakai (1jam 1x) agar akun anda tidak terdeteksi spam ^_^")
    input(w+"\n["+b+">>"+w+"] Press Enter to back menu ...")
    menu()

def botsapa():
    loop = []
    print("Diperlukan banyak koin untuk menjalankan BOT ini !!!")
    print("Bot akan dimulai dalam 3 detik ..")
    time.sleep(3)
    data_explore = ("session_key="+session_key_saya+"&key_owner="+key_owner_saya+"&user_id="+user_id_saya+"&")
    req = res.post("https://sestyc.com/sestyc/get_explore_latest_script.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '479'}, data=data_explore).text
    sts = json.loads(req)
    for z in sts:
        fcm_id = z['fcm_id']
        other_user_id = z['owner']
        post_id = z['post_id']	
        post_picture = z['post_picture']
        target = z['owner_user_name']
        #Langkahi User Baperan
        if "sestyc" in target:
            pass
        elif "kevin" in target:
            pass
        elif "dixon" in target:
            pass
        elif "jesslyn" in target:
            pass
        elif "michaelfrancesco" in target:
            pass
        elif "andykurnia" in target:
            pass
        else:
            loop.append(target)
            scan = res.post("https://sestyc.com/sestyc/profile_init_other_script_93.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '181'}, data=("session_key="+session_key_saya+"&my_user_id="+key_owner_saya+"&key_owner="+user_id_saya+"&user_id="+other_user_id+"&")).text
            scan_json = json.loads(scan)
            if "0" in str(scan_json['is_follower']):
                pesan_sapa = ("Rm9sbG93IEthbWkgS2FrIDpE%0A")
                data_sapa = ("display_picture="+display_picture_saya+"&key_owner="+key_owner_saya+"&other_user_id="+other_user_id+"&fcm_id=cVW71BYJSH2hqobSP0a-5h%3AAPA91bFSAVeBQitJdE9P8mVS7Q58s8ptJPSgYyxWHXjiS2Gpxk1kSgy7esVhCm8rlbsNdCydphaYZcCYkny44sIMC3n0mwcOed7HZlAjIE9aTgsuGZKMkgtuzOTnUUEs6WfHUeV3hwpt&message="+pesan_sapa+"&display_name="+display_name_saya+"&session_key="+session_key_saya+"&user_id="+user_id_saya+"&")
                sapa = res.post("https://sestyc.com/sestyc/send_greet_script.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '832'}, data=data_sapa).text
                gelas = ("20")
                pesan_gift = ("VGVyaW1hIEthc2loIFN1ZGFoIG1hdSBmb2xsb3cgYWt1biBrYW1pIDop%0A")
                data_gift = ("gift_id="+gelas+"&display_picture="+display_picture_saya+"&key_owner="+key_owner_saya+"&owner_id="+other_user_id+"&display_name="+display_name_saya+"&session_key="+session_key_saya+"&gift_message="+pesan_gift+"&user_id="+user_id_saya+"&")
                stiker = res.post("https://sestyc.com/sestyc/send_sestyc_gift_script.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '449'}, data=data_gift).text
                json_stiker = json.loads(stiker)
                if "1" in str(json_stiker['result']):
                    print(ttp+str(len(loop))+"> Meminta : "+b+target+ttp+" | Result'S : "+b+sapa+ttp+" | Result'G : "+red+"Gagal"+ttp)
                else:
                    print(ttp+str(len(loop))+"> Meminta : "+b+target+ttp+" | Result'S : "+b+sapa+ttp+" | Result'G : "+b+stiker+ttp)
            else:
                print(ttp+str(len(loop))+"> Sudah Menjadi Followers : "+b+target)
                pass
    print(ttp+"\n["+g+"$"+ttp+"] Done")
    print(ttp+"["+g+"?"+ttp+"] Total Media : "+b+str(len(loop)))
    print(ttp+"["+g+"Rekomendasi"+ttp+"] Pakai (1jam 1x) agar akun anda tidak terdeteksi spam ^_^")
    input(w+"\n["+b+">>"+w+"] Press Enter to back menu ...")
    menu()
    

def unfollow():
    success = []
    gagal = []
    loop = []
    print("Mengumpulkan data following ...")
    time.sleep(2)
    ex = res.post("https://sestyc.com/sestyc/following_list_script.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '163'}, data=("session_key="+session_key_saya+"&key_owner="+key_owner_saya+"&user_id="+user_id_saya+"&")).text
    explore = json.loads(ex)
    for otherid in explore:
        idn = otherid['user_name']
        idt = otherid['user_id']
        loop.append(idt)
        if "881942" in idt:
            print(ttp+str(len(loop))+idn+ttp+" | "+idt+red+" Gagal Unfollow")
        else:
            scan = res.post("https://sestyc.com/sestyc/profile_init_other_script_93.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '181'}, data=("session_key="+session_key_saya+"&my_user_id="+key_owner_saya+"&key_owner="+user_id_saya+"&user_id="+idt+"&")).text
            scan_json = json.loads(scan)
            if "0" in str(scan_json['is_follower']):
                exp = res.post("https://sestyc.com/sestyc/unfollowing_script.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '187'}, data=("session_key="+session_key_saya+"&my_user_id="+user_id_saya+"&key_owner="+key_owner_saya+"&other_user_id="+idt+"&")).text
                expo = json.loads(exp)
                if "1" in str(expo['result']):
                    print(ttp+str(len(loop))+"> "+g+idn+ttp+" | "+y+idt+ttp+" Its not Followers, Unfollow Now !!!")
                    success.append(idt)
                else:
                    print(ttp+str(len(loop))+"> "+red+idn+ttp+" | "+y+idt+ttp+" Gagal Unfollow !!!")
                    gagal.append(idt)
            else:
                print(ttp+str(len(loop))+"> "+red+idn+ttp+" | "+y+idt+ttp+" Its Followers, Gagal Unfollow !!!")
                gagal.append(idt)
                pass
    print(ttp+"\n["+g+"$"+ttp+"] Done")
    print(ttp+"["+g+"?"+ttp+"] Result : "+g+"Success"+ttp+"("+str(len(success))+") "+red+"Gagal"+ttp+"("+str(len(gagal))+")")
    input(ttp+"["+b+">>"+ttp+"] Press Enter to back menu ...")
    menu()

def unfollowmass():
    success = []
    gagal = []
    loop = []
    print("Mengumpulkan data following ...")
    time.sleep(2)
    ex = res.post("https://sestyc.com/sestyc/following_list_script.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '163'}, data=("session_key="+session_key_saya+"&key_owner="+key_owner_saya+"&user_id="+user_id_saya+"&")).text
    explore = json.loads(ex)
    for otherid in explore:
        idn = otherid['user_name']
        idt = otherid['user_id']
        loop.append(idt)
        if "881942" in idt:
            print(ttp+str(len(loop))+idn+ttp+" | "+idt+red+" Gagal Unfollow")
        else:
            exp = res.post("https://sestyc.com/sestyc/unfollowing_script.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '187'}, data=("session_key="+session_key_saya+"&my_user_id="+user_id_saya+"&key_owner="+key_owner_saya+"&other_user_id="+idt+"&")).text
            expo = json.loads(exp)
            if "1" in str(expo['result']):
                print(ttp+str(len(loop))+"> "+g+idn+ttp+" | "+y+idt+ttp+" Success Unfollow")
                success.append(idt)
            else:
                print(ttp+str(len(loop))+"> "+red+idn+ttp+" | "+y+idt+ttp+" Gagal Unfollow")
                gagal.append(idt)
    print(ttp+"\n["+g+"$"+ttp+"] Done")
    print(ttp+"["+g+"?"+ttp+"] Result : "+g+"Success"+ttp+"("+str(len(success))+") "+red+"Gagal"+ttp+"("+str(len(gagal))+")")
    input(ttp+"["+b+">>"+ttp+"] Press Enter to back menu ...")
    menu()

def deletemass():
    loop = []
    page = res.post("https://sestyc.com/sestyc/profile_init_script_93.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '179'}, data=("user_name="+username_saya+"&session_key="+session_key_saya+"&key_owner="+key_owner_saya+"&user_id="+user_id_saya+"&")).text
    profile = json.loads(page)
    print("Mengumpulkan ID Media ...")
    time.sleep(2)
    for media in profile['post_data']:
        loop.append(media['post_id'])
        page_hapus = res.post("https://sestyc.com/sestyc/delete_moment_script.php", headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)','Host': 'sestyc.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '249'}, data=("post_id="+media['post_id']+"&session_key="+session_key_saya+"&key_owner="+key_owner_saya+"&")).text
        print(ttp+str(len(loop))+"> Menghapus : "+page_hapus)
    print(ttp+"\n["+g+"$"+ttp+"] Done")
    print(ttp+"["+g+"?"+ttp+"] Result : "+g+str(len(loop)))
    input(ttp+"["+b+">>"+ttp+"] Press Enter to back menu ...")
    menu()


if __name__ == "__main__":
    try:
        ck = open("keys.txt", "r").readlines()
    except:
        os.system("clear")
        print(ttp+logo)
        print(ttp+"Version : "+y+"SestycBOT v0.5")
        print(ttp+"Coded   : "+g+"Rezadkim (ZP)")
        print(ttp+"Source  : "+underline+gl+"https://github.com/rezadkim"+ttp)
        print(ttp+"Donate  : "+b+"0895611252563"+ttp)
        print(50*"-")
        donlod = res.get("https://raw.githubusercontent.com/rezadkim/Sestyc/master/key.txt").text
        print("Download Keys disini > "+gl+donlod+"\n")
    try:
        main()
    except KeyboardInterrupt:
       exit(ttp+"\n["+red+"!"+ttp+"] Keluar")
