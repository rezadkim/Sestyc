#Lo itu Ngentod
#gausah sok kerad


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
    print(ttp+"Version : "+y+"SestycBOT v0.5 ( Member Free Version )")
    print(ttp+"Coded   : "+g+"Rezadkim (ZP)")
    print(ttp+"Source  : "+underline+gl+"https://github.com/rezadkim"+ttp)
    print(ttp+"Support : "+g+"Lord Wazowski & Lord Sullivan")
    print(ttp+50*"-")
    print(ttp+"Username : "+g+"@"+menuk['post_data'][0]['owner_user_name']+ttp+" | ID : "+g+menuk['post_data'][0]['owner'])
    if str(menuk['verified']) in "0":
        print(ttp+"Verified Account : "+red+"False")
    else:
        print(ttp+"Verified Account : "+b+"True")
    print(ttp+"Post>"+y+str(menuk['post'])+ttp+" Followers>"+y+str(menuk['followers'])+ttp+" Followings>"+y+str(menuk['followings'])+ttp)
    print("Popularity : ("+y+str(menuk['popularity'])+ttp+")")
    print(50*"-")
    print(ttp+"["+b+"nb"+ttp+"] Ingin membuka semua fitur bisa beli disini : "+g+"0895611252563"+ttp)
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
    print(ttp+"["+red+"!!!"+ttp+"] Anda perlu membeli versi premium untuk membuka semua fitur ini")
    input(w+"\n["+b+">>"+w+"] Press Enter to back menu ...")
    menu()

def bot():
    print(ttp+"["+red+"!!!"+ttp+"] Anda perlu membeli versi premium untuk membuka semua fitur ini")
    input(w+"\n["+b+">>"+w+"] Press Enter to back menu ...")
    menu()

def botsapa():
    print(ttp+"["+red+"!!!"+ttp+"] Anda perlu membeli versi premium untuk membuka semua fitur ini")
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
    print(ttp+"["+red+"!!!"+ttp+"] Anda perlu membeli versi premium untuk membuka semua fitur ini")
    input(w+"\n["+b+">>"+w+"] Press Enter to back menu ...")
    menu()

def deletemass():
    print(ttp+"["+red+"!!!"+ttp+"] Anda perlu membeli versi premium untuk membuka semua fitur ini")
    input(w+"\n["+b+">>"+w+"] Press Enter to back menu ...")
    menu()


if __name__ == "__main__":
    try:
        ck = open("keys.txt", "r").readlines()
    except:
        os.system("clear")
        print(ttp+logo)
    try:
        main()
    except KeyboardInterrupt:
       exit(ttp+"\n["+red+"!"+ttp+"] Keluar")
