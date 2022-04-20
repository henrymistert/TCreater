import os
import shutil
from tkinter import *
import os
from tkinter import filedialog
import getpass
import jellyfish

endloop1 = False
endloop2 = False

f = open("InternalNames.txt", "r")
k = f.readlines()
f.close()

inf = open("InternalNames.txt", "r")
listofitems = (inf.readlines())
ITEMS = []
for l2 in listofitems:
    Name = l2.replace("\n", "")
    ITEMS.append(Name)

print(ITEMS)

Buffs = ["None", "Max Minions", "Health Regen", "Magic Damage", "Ranged Damage", "Melee Damage", "Summoning Damage", "Movement Speed", "Mana Cost", "No Knockback", "Melee Speed", "Crit Chance", "Double Jump"]
Operators = ["Set", "/", "*", "+", "-"]
AiType = ["Zombie", "Slime", "Demon Eye"]

def Blank(gap):
    Label(tk, text = "", font = f"System {gap}").pack()
def Notice(text):
    Label(tk, text = text, font = "System 15").pack()
def ReadItemInput(InputItem) :
    OgInput = InputItem.get("1.0", "end-1c")
    HighestSim = 0
    HighestName = ""
    f2 = open("InternalNames.txt", "r")
    k2 = f2.readlines()
    for l2 in k2 :
        Name = l2.replace("\n", "")
        Sim = jellyfish.jaro_similarity(Name, OgInput)
        if Sim >= HighestSim :
            HighestSim = Sim
            HighestName = Name
    return HighestName

Dir = ""
tk = Tk()
tk.title("TCreator - Mod Setup")
tk.geometry("500x550")
tk.update()
Title = Label(tk, text = "Mod Setup", font = "System 18")
Title.pack()
Blank(10)
tk.update()
DirText = Label(tk, text = "Mod Directory", font = "System 15").pack()
DirInput = Text(tk, width = 50, height = 1)
DirInput.pack()
tk.update()
a = False
while not endloop1:
    def ReadDir():
        global Dir
        global endloop1
        Dir = DirInput.get("1.0", "end-1c")
        if os.path.isdir(Dir) :
            if os.path.isfile(f"{Dir}/build.txt") :
                endloop1 = True
            else :
                Log.configure(text = "This Isnt A Real Mod :(")
        else :
            Log.configure(text = "Folder Not Found :(")
    if not a:
        Blank(5)
        Start = Button(tk, text="Start!", width=10, height=2, command=ReadDir).pack()
        Log = Label(tk, text="", font="System 16")
        Log.pack()
        user = getpass.getuser()
        dirs = filedialog.askdirectory(initialdir=fr"C:\Users\{user}\Documents\My Games\Terraria\ModLoader\Mod Sources",title="Select A Mod!")
        DirInput.delete("1.0", END)
        DirInput.insert(END, dirs)
        a = True
    tk.update()

tk.destroy()

tk = Tk()
tk.title("TCreator - Mod Setup")
tk.geometry("500x550")
tk.update()
Title = Label(tk, text = "Mod Setup", font = "System 18").pack()
Blank(10)
Notice("Mod Author")
ModAuthorInput = Text(tk, width = 20, height = 1)
ModAuthorInput.pack()
Blank(5)
Notice("Mod Version")
ModVersionInput = Text(tk, width = 20, height = 1)
ModVersionInput.pack()
tk.update()
Blank(10)
ModName = ""
ModAuthor = ""
ModVersion = ""

endloop1 = False
a = False
while not endloop1:
    def ReadInfo() :
        global endloop1
        global ModName
        global ModAuthor
        global ModVersion
        f = open(f"{Dir}/build.txt", "r")
        h = f.readlines()
        f.close()
        ModName = h[0].replace("\n", "")
        ModName = ModName.replace("displayName = ", "")
        ModName = ModName.replace(" ","")
        ModAuthor = ModAuthorInput.get("1.0", "end-1c")
        ModVersion = ModVersionInput.get("1.0", "end-1c")
        endloop1 = True
    if not a:
        Start = Button(tk, text="Next!", width=10, height=2, command=ReadInfo).pack()
        a = True
    tk.update()
tk.destroy()
ModDataFile = open(f"{Dir}/build.txt", "w")
ModDataFile.truncate(0)
ModDataFile.writelines([f"displayName = {ModName}", f"\nauthor = {ModAuthor}", f"\nversion = {ModVersion}"])
ModDataFile.close()

if os.path.isdir(f"{Dir}/Items"):
    print("Already Exists!")
else:
    os.mkdir(f"{Dir}/Items")
    print("Successfully Created Folder: Items")
if os.path.isdir(f"{Dir}/Items/Armor"):
    print("Already Exists!")
else:
    os.mkdir(f"{Dir}/Items/Armor")
    print("Successfully Created Folder: Armor")
if os.path.isdir(f"{Dir}/Items/Accessories"):
    print("Already Exists!")
else:
    os.mkdir(f"{Dir}/Items/Accessories")
    print("Successfully Created Folder: Accessories")
print("Creating Directory: Tiles")
if os.path.isdir(f"{Dir}/Tiles"):
    print("Already Exists!")
else:
    os.mkdir(f"{Dir}/Tiles")
    print("Successfully Created Folder: Tiles")
print("Creating Directory: NPCs")
if os.path.isdir(f"{Dir}/NPCs"):
    print("Already Exists!")
else:
    os.mkdir(f"{Dir}/NPCs")
    print("Successfully Created Folder: NPCs")
print("Creating Directory: Projectiles")
if os.path.isdir(f"{Dir}/Projectiles"):
    print("Already Exists!")
else:
    os.mkdir(f"{Dir}/Projectiles")
    print("Successfully Created Folder: Projectiles")
print("Creating Directory: Weapons")
if os.path.isdir(f"{Dir}/Items/Weapons"):
    print("Already Exists!")
else:
    os.mkdir(f"{Dir}/Items/Weapons")
    print("Successfully Created Folder: Weapons")
print(" ")
print("Setup Complete (0 Errors). You Can Now Start Work On Your Mod! Have Fun!")
print(" ")
print("\n" * 100)
endloop2 = False

a = False
CreateUi = True
while not endloop2:
    Command = ""
    def Exit() :
        global endloop2
        endloop2 = True
    def Add():
        global Command
        Command = "Add"
    if CreateUi:
        tk = Tk()
        tk.title("TCreator - Mod Creation")
        tk.geometry("500x550")
        tk.update()
        Title = Label(tk, text="Mod Creation", font="System 18").pack()
        tk.update()
        Blank(5)
        tk.update()

        AddB = Button(tk, text="Add", command=Add).pack()
        ExitB = Button(tk, text="Exit", command=Exit).pack()
        CreateUi = False
    tk.update()
    if Command == "Add":
        tk.destroy()
        tk = Tk()
        tk.title("TCreator - Add Mod Element")
        tk.geometry("500x550")
        tk.update()
        Title = Label(tk, text="Add Mod Element", font="System 18").pack()
        tk.update()
        Blank(5)
        endloop3 = False
        b = False
        Command = ""
        while not endloop3:
            def Click():
                print(devmode.get())
            def Sword():
                global Command
                Command = "Sword"
            def Gun():
                global Command
                Command = "Gun"
            def Bullet():
                global Command
                Command = "Bullet"
            def Bag():
                global Command
                Command = "Bag"
            def Zombie():
                global Command
                Command = "Zombie"
            def Breastplate():
                global Command
                Command = "Breastplate"
            def Helmet():
                global Command
                Command = "Helmet"
            def Leggings():
                global Command
                Command = "Leggings"
            def Accessory():
                global Command
                Command = "Accessory"
            def Boss():
                global Command
                Command = "Boss"
            if not b:
                SwordB = Button(tk, text = "Sword", command = Sword).pack()
                GunB = Button(tk, text="Gun", command=Gun).pack()
                BulletB = Button(tk, text="Bullet", command=Bullet).pack()
                BagB = Button(tk, text="Bag", command=Bag).pack()
                ZombieB = Button(tk, text="Enemy", command=Zombie).pack()
                BreastplateB = Button(tk, text="Breastplate", command=Breastplate).pack()
                HelmetB = Button(tk, text="Helmet", command=Helmet).pack()
                LeggingsB = Button(tk, text="Leggings", command=Leggings).pack()
                AccessoryB = Button(tk, text="Accessory", command=Accessory).pack()
                BossB = Button(tk, text="Boss", command=Boss).pack()
                devmode = IntVar()
                DevModeCheck = Checkbutton(tk, text='Developer Mode (Only Tick If You Can Code In C#)', variable=devmode, command = Click).pack()
                b = True
            tk.update()
            if Command == "Sword":
                variable = StringVar(tk)
                variable.set("default_value")
                endloop4 = False
                tk.destroy()
                tk = Tk()
                tk.title("TCreator - Create Sword")
                tk.geometry("500x700")
                tk.update()
                Title = Label(tk, text="Sword", font="System 18").pack()
                tk.update()
                Blank(5)
                Notice("Sword Name")
                SwordNameInput = Text(tk, width = 20, height = 1)
                SwordNameInput.pack()
                Blank(5)
                Notice("Sword Description")
                SwordDescriptionInput = Text(tk, width=20, height=1)
                SwordDescriptionInput.pack()
                Blank(5)
                Notice("Sword Damage")
                SwordDamageInput = Text(tk, width=20, height=1)
                SwordDamageInput.pack()
                Blank(5)
                Notice("Sword Use Time")
                SwordUseTimeInput = Text(tk, width=20, height=1)
                SwordUseTimeInput.pack()
                Blank(5)
                Notice("Sword Knockback")
                SwordKnockbackInput = Text(tk, width=20, height=1)
                SwordKnockbackInput.pack()
                Blank(5)
                Notice("Sword Crafting Item")
                SwordCraftingItemInput = Text(tk, width=20, height=1)
                SwordCraftingItemInput.pack()
                Blank(5)
                Notice("Sword Crafting Amount")
                SwordCraftingAmountInput = Text(tk, width=20, height=1)
                SwordCraftingAmountInput.pack()
                Blank(5)
                Notice("Sword Crafting Station")
                SwordCraftingStationInput = Text(tk, width=20, height=1)
                SwordCraftingStationInput.pack()
                Blank(5)

                c = False

                while not endloop4:
                    tk.update()
                    if not c:
                        def Create():
                            global tk
                            global endloop4
                            global CreateUi
                            global endloop3

                            SwordName = SwordNameInput.get("1.0", "end-1c")
                            shutil.copyfile("Examples/Items/Sword/ExampleSword.cs", f"{Dir}/Items/{SwordName}.cs")
                            shutil.copyfile("Examples/Items/Sword/ExampleSword.png", f"{Dir}/Items/{SwordName}.png")
                            Sword1 = open(f"{Dir}/Items/{SwordName}.cs", "r")
                            listoflines = Sword1.readlines()
                            print(listoflines)
                            listoflines[3] = f"namespace {ModName}.Items\n"
                            listoflines[5] = f"\tpublic class {SwordName} : ModItem\n"
                            Description = SwordDescriptionInput.get("1.0", "end-1c")
                            listoflines[10] = f'\t\t\tTooltip.SetDefault("{Description}");\n'
                            Damage = SwordDamageInput.get("1.0", "end-1c")
                            listoflines[15] = f"\t\t\titem.damage = {Damage};\n"
                            UseTime = SwordUseTimeInput.get("1.0", "end-1c")
                            listoflines[19] = f"\t\t\titem.useTime = {UseTime};\n"
                            listoflines[20] = f"\t\t\titem.useAnimation = {UseTime};\n"
                            Knockback = SwordKnockbackInput.get("1.0", "end-1c")
                            listoflines[22] = f"\t\t\titem.knockBack = {Knockback};\n"
                            CraftingRecipe = ReadItemInput(SwordCraftingItemInput)
                            CraftingAmount = SwordCraftingAmountInput.get("1.0", "end-1c")
                            listoflines[32] = f"\t\t\trecipe.AddIngredient(ItemID.{CraftingRecipe}, {CraftingAmount});\n"
                            CraftingDevice = SwordCraftingStationInput.get("1.0", "end-1c")
                            listoflines[33] = f"\t\t\trecipe.AddTile(TileID.{CraftingDevice});\n"
                            Sword1.close()
                            Sword1 = open(f"{Dir}/Items/{SwordName}.cs", "w")
                            Sword1.writelines(listoflines)
                            Sword1.close()
                            endloop3 = True
                            endloop4 = True
                            tk.destroy()
                            CreateUi = True
                            endloop5 = False
                            if devmode.get() == 1:
                                CreateUi2 = True
                                while not endloop5:
                                    def Submit() :
                                        global endloop5
                                        listoflines7 = Code.get("1.0", "end-1c")
                                        Sword2 = open(f"{Dir}/Items/{SwordName}.cs", "w")
                                        Sword2.writelines(listoflines7)
                                        Sword2.close()
                                        tk.destroy()
                                        endloop5 = True
                                    if CreateUi2:
                                        CreateUi2 = False
                                        tk = Tk()
                                        tk.title("TCreater - Edit Code")
                                        tk.geometry("1500x1000")
                                        Code = Text(tk, width=150, height=50)
                                        Code.pack()
                                        Create2 = Button(tk, text = "Submit!", command = Submit).pack()
                                        start = 1.0
                                        for i in listoflines:
                                            Code.insert(str(start), i)
                                            start += 1.0


                        CreateB = Button(tk, text = "Create!", command = Create).pack()
                        c = True
            if Command == "Gun":
                endloop4 = False
                tk.destroy()
                tk = Tk()
                tk.title("TCreator - Create Gun")
                tk.geometry("500x700")
                tk.update()
                Title = Label(tk, text="Gun", font="System 18").pack()
                tk.update()
                Blank(5)
                Notice("Gun Name")
                GunNameInput = Text(tk, width = 20, height = 1)
                GunNameInput.pack()
                Blank(5)
                Notice("Gun Description")
                GunDescriptionInput = Text(tk, width=20, height=1)
                GunDescriptionInput.pack()
                Blank(5)
                Notice("Gun Damage")
                GunDamageInput = Text(tk, width=20, height=1)
                GunDamageInput.pack()
                Blank(5)
                Notice("Gun Use Time")
                GunUseTimeInput = Text(tk, width=20, height=1)
                GunUseTimeInput.pack()
                Blank(5)
                Notice("Gun Knockback")
                GunKnockbackInput = Text(tk, width=20, height=1)
                GunKnockbackInput.pack()
                Blank(5)
                Notice("Gun Crafting Item")
                GunCraftingItemInput = Text(tk, width=20, height=1)
                GunCraftingItemInput.pack()
                Blank(5)
                Notice("Gun Crafting Amount")
                GunCraftingAmountInput = Text(tk, width=20, height=1)
                GunCraftingAmountInput.pack()
                Blank(5)
                Notice("Gun Crafting Station")
                GunCraftingStationInput = Text(tk, width=20, height=1)
                GunCraftingStationInput.pack()
                Blank(5)

                c = False

                while not endloop4:
                    tk.update()
                    if not c:
                        def Create():
                            global endloop4
                            global CreateUi
                            global endloop3
                            global tk
                            print(" ")
                            GunName = GunNameInput.get("1.0", "end-1c")
                            shutil.copyfile("Examples/Items/Weapons/Gun/ExampleGun.cs", f"{Dir}/Items/Weapons/{GunName}.cs")
                            shutil.copyfile("Examples/Items/Weapons/Gun/ExampleGun.png", f"{Dir}/Items/Weapons/{GunName}.png")
                            Sword1 = open(f"{Dir}/Items/Weapons/{GunName}.cs", "r")
                            listoflines2 = Sword1.readlines()
                            print(listoflines2)
                            listoflines2[0] = f" "
                            listoflines2[5] = f"namespace {ModName}.Items.Weapons\n"
                            listoflines2[7] = f"\tpublic class {GunName} : ModItem\n"
                            GunDesc = GunDescriptionInput.get("1.0", "end-1c")
                            listoflines2[10] = f'\t\t\tTooltip.SetDefault("{GunDesc}");\n'
                            GunDamage = GunDamageInput.get("1.0", "end-1c")
                            listoflines2[14] = f"\t\t\titem.damage = {GunDamage};\n"
                            GunUseTime = GunUseTimeInput.get("1.0", "end-1c")
                            listoflines2[18] = f"\t\t\titem.useTime = {GunUseTime};\n"
                            listoflines2[19] = f"\t\t\titem.useAnimation = {GunUseTime};\n"
                            GunKnockback = GunKnockbackInput.get("1.0", "end-1c")
                            listoflines2[22] = f"\t\t\titem.knockBack = {GunKnockback};\n"
                            ItemToCraft = ReadItemInput(GunCraftingItemInput)
                            ItemAmount = GunCraftingAmountInput.get("1.0", "end-1c")
                            listoflines2[34] = f"\t\t\trecipe.AddIngredient(ItemID.{ItemToCraft}, {ItemAmount});\n"
                            Workbench = GunCraftingStationInput.get("1.0", "end-1c")
                            listoflines2[35] = f"\t\t\trecipe.AddTile(TileID.{Workbench});\n"
                            Sword1.close()
                            Sword1 = open(f"{Dir}/Items/Weapons/{GunName}.cs", "w")
                            Sword1.writelines(listoflines2)
                            Sword1.close()
                            endloop3 = True
                            endloop4 = True
                            tk.destroy()
                            CreateUi = True
                            endloop5 = False
                            if devmode.get() == 1 :
                                CreateUi2 = True
                                while not endloop5 :
                                    def Submit() :
                                        global endloop5
                                        listoflines7 = Code.get("1.0", "end-1c")
                                        Sword2 = open(f"{Dir}/Items/Weapons/{GunName}.cs", "w")
                                        Sword2.writelines(listoflines7)
                                        Sword2.close()
                                        tk.destroy()
                                        endloop5 = True

                                    if CreateUi2 :
                                        CreateUi2 = False
                                        tk = Tk()
                                        tk.title("TCreater - Edit Code")
                                        tk.geometry("1500x1000")
                                        Code = Text(tk, width=150, height=50)
                                        Code.pack()
                                        Create2 = Button(tk, text="Submit!", command=Submit).pack()
                                        start = 1.0
                                        for i in listoflines2:
                                            Code.insert(str(start), i)
                                            start += 1.0

                        CreateB = Button(tk, text = "Create!", command = Create).pack()
                        c = True
            if Command == "Bullet":
                endloop4 = False
                tk.destroy()
                tk = Tk()
                tk.title("TCreator - Create Bullet")
                tk.geometry("500x700")
                tk.update()
                Title = Label(tk, text="Gun", font="System 18").pack()
                tk.update()
                Blank(5)
                Notice("Bullet Name")
                BulletNameInput = Text(tk, width=20, height=1)
                BulletNameInput.pack()
                Blank(5)
                Notice("Bullet Width (Default = 8)")
                BulletWidthInput = Text(tk, width=20, height=1)
                BulletWidthInput.pack()
                Blank(5)
                Notice("Bullet Height (Default = 8)")
                BulletHeightInput = Text(tk, width=20, height=1)
                BulletHeightInput.pack()
                Blank(5)
                Notice("Bullet Description")
                BulletDescInput = Text(tk, width=20, height=1)
                BulletDescInput.pack()
                Blank(5)
                Notice("Bullet Damage")
                BulletDamageInput = Text(tk, width=20, height=1)
                BulletDamageInput.pack()
                Blank(5)
                Notice("Bullet Speed (Default = 16)")
                BulletSpeedInput = Text(tk, width=20, height=1)
                BulletSpeedInput.pack()
                Blank(5)
                Notice("Bullet Crafting Item")
                BulletCraftingItemInput = Text(tk, width=20, height=1)
                BulletCraftingItemInput.pack()
                Blank(5)
                Notice("Bullet Crafting Amount")
                BulletCraftingAmountInput = Text(tk, width=20, height=1)
                BulletCraftingAmountInput.pack()
                Blank(5)
                Notice("Bullet Crafting Station")
                BulletCraftingStationInput = Text(tk, width=20, height=1)
                BulletCraftingStationInput.pack()
                Blank(5)

                c = False

                while not endloop4:
                    tk.update()
                    if not c:
                        def Create():
                            global endloop4
                            global CreateUi
                            global endloop3
                            global tk
                            BulletName = BulletNameInput.get("1.0", "end-1c")
                            shutil.copyfile("Examples/Projectiles/ExampleBullet.cs", f"{Dir}/Projectiles/{BulletName}.cs")
                            shutil.copyfile("Examples/Projectiles/ExampleBullet.png", f"{Dir}/Projectiles/{BulletName}.png")
                            shutil.copyfile("Examples/Items/Weapons/ExampleBullet.cs", f"{Dir}/Items/Weapons/{BulletName}.cs")
                            shutil.copyfile("Examples/Items/Weapons/ExampleBullet.png", f"{Dir}/Items/Weapons/{BulletName}.png")
                            Sword1 = open(f"{Dir}/Projectiles/{BulletName}.cs", "r")
                            listoflines3 = Sword1.readlines()
                            Sword1.close()
                            Width = BulletWidthInput.get("1.0", "end-1c")
                            listoflines3[11] = f'\t\t\tDisplayName.SetDefault("{BulletName}");\n'
                            listoflines3[17] = f"\t\t\tprojectile.width = {Width};\n"
                            listoflines3[6] = f"namespace {ModName}.Projectiles\n"
                            listoflines3[8] = f"\tpublic class {BulletName} : ModProjectile\n"
                            Height = BulletHeightInput.get("1.0", "end-1c")
                            listoflines3[18] = f"\t\t\tprojectile.height = {Height};\n"
                            Sword1 = open(f"{Dir}/Projectiles/{BulletName}.cs", "w")
                            Sword1.writelines(listoflines3)
                            Sword1.close()
                            Sword1 = open(f"{Dir}/Items/Weapons/{BulletName}.cs", "r")
                            listoflines3 = Sword1.readlines()
                            Sword1.close()
                            listoflines3[5] = f"namespace {ModName}.Items.Weapons\n"
                            listoflines3[7] = f"\tpublic class {BulletName} : ModItem\n"
                            Desc = BulletDescInput.get("1.0", "end-1c")
                            listoflines3[10] = f'\t\t\tTooltip.SetDefault("{Desc}");\n'
                            Damage = BulletDamageInput.get("1.0", "end-1c")
                            listoflines3[14] = f"\t\t\titem.damage = {Damage};\n"
                            listoflines3[23] = f"\t\t\titem.shoot = ProjectileType<Projectiles.{BulletName}>();\n"
                            Speed = BulletSpeedInput.get("1.0", "end-1c")
                            listoflines3[24] = f"\t\t\titem.shootSpeed = {Speed}f;\n"
                            ItemToCraft = ReadItemInput(BulletCraftingItemInput)
                            ItemAmount = BulletCraftingAmountInput.get("1.0", "end-1c")
                            Workbench = BulletCraftingStationInput.get("1.0", "end-1c")
                            listoflines3[37] = f"\t\t\trecipe.AddIngredient(ItemID.{ItemToCraft}, {ItemAmount});\n"
                            listoflines3[38] = f"\t\t\trecipe.AddTile(TileID.{Workbench});\n"
                            listoflines3[16] = f"\t\t\titem.width = {Width};\n"
                            listoflines3[17] = f"\t\t\titem.height = {Height};\n"
                            Sword1 = open(f"{Dir}/Items/Weapons/{BulletName}.cs", "w")
                            Sword1.writelines(listoflines3)
                            Sword1.close()
                            endloop3 = True
                            endloop4 = True
                            tk.destroy()
                            CreateUi = True
                            endloop5 = False
                            if devmode.get() == 1 :
                                CreateUi2 = True
                                while not endloop5 :
                                    def Submit() :
                                        global endloop5
                                        listoflines7 = Code.get("1.0", "end-1c")
                                        Sword2 = open(f"{Dir}/Projectiles/{BulletName}.cs", "w")
                                        Sword2.writelines(listoflines7)
                                        Sword2.close()
                                        tk.destroy()
                                        endloop5 = True

                                    if CreateUi2 :
                                        CreateUi2 = False
                                        tk = Tk()
                                        tk.title("TCreater - Edit Code")
                                        tk.geometry("1500x1000")
                                        Code = Text(tk, width=150, height=50)
                                        Code.pack()
                                        Create2 = Button(tk, text="Submit!", command=Submit).pack()
                                        start = 1.0
                                        for i in listoflines3:
                                            Code.insert(str(start), i)
                                            start += 1.0

                        CreateB = Button(tk, text = "Create!", command = Create).pack()
                        c = True
            if Command == "Bag":
                endloop4 = False
                tk.destroy()
                tk = Tk()
                tk.title("TCreator - Create Bag")
                tk.geometry("500x1080")
                tk.update()
                Title = Label(tk, text="Bag", font="System 18").pack()
                Bags = []
                BagAmounts = []
                BagAmount = 0
                tk.update()
                Blank(5)
                Notice("Bag Name")
                BagNameInput = Text(tk, width=20, height=1)
                BagNameInput.pack()
                Blank(5)
                Notice("Bag Description")
                BagDescInput = Text(tk, width=20, height=1)
                BagDescInput.pack()
                Blank(5)
                def AddBagItem():
                    global BagAmount
                    BagAmount += 1
                    Notice(f"Bag Item {BagAmount}")
                    BagInput = Text(tk, width=20, height=1)
                    BagInput.pack()
                    Bags.append(BagInput)
                    Notice(f"Bag Item {BagAmount} Amount")
                    BagAInput = Text(tk, width=20, height=1)
                    BagAInput.pack()
                    BagAmounts.append(BagAInput)
                    Blank(5)
                Notice("Bag Crafting Item")
                BagCraftingItemInput = Text(tk, width=20, height=1)
                BagCraftingItemInput.pack()
                Blank(5)
                Notice("Bag Crafting Amount")
                BagCraftingAmountInput = Text(tk, width=20, height=1)
                BagCraftingAmountInput.pack()
                Blank(5)
                Notice("Bag Crafting Station")
                BagCraftingStationInput = Text(tk, width=20, height=1)
                BagCraftingStationInput.pack()
                Blank(5)

                c = False

                while not endloop4:
                    tk.update()
                    if not c:
                        def Create():
                            global endloop4
                            global CreateUi
                            global endloop3
                            global tk
                            BagName = BagNameInput.get("1.0", "end-1c")
                            shutil.copyfile("Examples/Items/ExampleBag.cs", f"{Dir}/Items/{BagName}.cs")
                            shutil.copyfile("Examples/Items/ExampleBag.png", f"{Dir}/Items/{BagName}.png")
                            Sword1 = open(f"{Dir}/Items/{BagName}.cs", "r")
                            listoflines3 = Sword1.readlines()
                            Sword1.close()
                            listoflines3[4] = f'namespace {ModName}.Items\n'
                            listoflines3[6] = f'\tpublic class {BagName} : ModItem\n'
                            listoflines3[9] = f'\t\t\tDisplayName.SetDefault("{BagName}");\n'
                            BagDesc = BagDescInput.get("1.0", "end-1c")
                            listoflines3[10] = f'\t\t\tTooltip.SetDefault("{BagDesc}");\n'

                            count = 0
                            SECTIONSTR = ""

                            BagCraftingItem = ReadItemInput(BagCraftingItemInput)
                            BagCraftingAmount = BagCraftingAmountInput.get("1.0", "end-1c")
                            BagCraftingStation = BagCraftingStationInput.get("1.0", "end-1c")
                            for i4 in Bags:
                                BagItem = ReadItemInput(i4)
                                BagItemAmount = BagAmounts[count].get("1.0", "end-1c")
                                SECTIONSTR += f'\t\t\tplayer.QuickSpawnItem(ItemID.{BagItem}, {BagItemAmount});\n'
                                count += 1
                            listoflines3[24] = SECTIONSTR
                            listoflines3[32 - count - 1] = f"\t\t\trecipe.AddIngredient(ItemID.{BagCraftingItem}, {BagCraftingAmount});\n"
                            listoflines3[33 - count - 1] = f"\t\t\trecipe.AddTile(TileID.{BagCraftingStation});\n"
                            Sword1 = open(f"{Dir}/Items/{BagName}.cs", "w")
                            Sword1.writelines(listoflines3)
                            Sword1.close()
                            endloop3 = True
                            endloop4 = True
                            tk.destroy()
                            CreateUi = True
                            endloop5 = False
                            if devmode.get() == 1 :
                                CreateUi2 = True
                                while not endloop5 :
                                    def Submit() :
                                        global endloop5
                                        listoflines7 = Code.get("1.0", "end-1c")
                                        Sword2 = open(f"{Dir}/Items/{BagName}.cs", "w")
                                        Sword2.writelines(listoflines7)
                                        Sword2.close()
                                        tk.destroy()
                                        endloop5 = True

                                    if CreateUi2 :
                                        CreateUi2 = False
                                        tk = Tk()
                                        tk.title("TCreater - Edit Code")
                                        tk.geometry("1500x1000")
                                        Code = Text(tk, width=150, height=50)
                                        Code.pack()
                                        Create2 = Button(tk, text="Submit!", command=Submit).pack()
                                        start = 1.0
                                        for i in listoflines3:
                                            Code.insert(str(start), i)
                                            start += 1.0

                        CreateB = Button(tk, text = "Create!", command = Create).pack()
                        Blank(5)
                        AddBagItemB = Button(tk, text="Add Bag Item", command=AddBagItem).pack()
                        c = True
            if Command == "Zombie":
                endloop4 = False
                tk.destroy()
                tk = Tk()
                tk.title("TCreator - Create Zombie")
                tk.geometry("500x700")
                tk.update()
                Title = Label(tk, text="Zombie", font="System 18").pack()
                tk.update()
                AiTypeVar = StringVar()
                AiTypeVar.set("Zombie")
                Blank(5)
                Notice("Zombie Name")
                ZombieNameInput = Text(tk, width = 20, height = 1)
                ZombieNameInput.pack()
                Blank(5)
                Notice("Zombie Damage")
                ZombieDamageInput = Text(tk, width=20, height=1)
                ZombieDamageInput.pack()
                Blank(5)
                Notice("Zombie Health")
                ZombieHealthInput = Text(tk, width=20, height=1)
                ZombieHealthInput.pack()
                Blank(5)
                Notice("Zombie Defence (Default = 6)")
                ZombieDefenceInput = Text(tk, width=20, height=1)
                ZombieDefenceInput.pack()
                Blank(5)
                Notice("Zombie Item Drop")
                ZombieItemDropInput = Text(tk, width=20, height=1)
                ZombieItemDropInput.pack()
                Blank(5)
                Notice1 = Label(tk, text="Zombie Item Drop Chance (1 in <Value>)", font="System 15")
                Notice1.pack()
                ZombieItemDropChanceInput = Text(tk, width=20, height=1)
                ZombieItemDropChanceInput.pack()
                Blank(5)
                Notice("Mod Item Drop (True Or False) (Unstable)}")
                ZombieModIDInput = Text(tk, width=20, height=1)
                ZombieModIDInput.pack()
                Blank(5)
                Notice("Zombie Item Drop Amount")
                ZombieDropAmountInput = Text(tk, width=20, height=1)
                ZombieDropAmountInput.pack()
                Blank(5)
                Notice("Enemy AI (W.I.P)")
                AiTypeInput = OptionMenu(tk, AiTypeVar, *AiType)
                AiTypeInput.pack()
                Blank(5)

                c = False

                while not endloop4:
                    Notice1.configure(text = f'Zombie Item Drop Chance (1 in {ZombieItemDropChanceInput.get("1.0", "end-1c")})')
                    tk.update()
                    if not c:
                        def Create():
                            global endloop4
                            global CreateUi
                            global endloop3
                            global tk
                            print(" ")
                            ZombieName = ZombieNameInput.get("1.0", "end-1c")
                            shutil.copyfile("Examples/NPCs/ExampleZombie.cs", f"{Dir}/NPCs/{ZombieName}.cs")
                            AiTypeInGet = AiTypeVar.get()
                            if AiTypeInGet == "Slime":
                                shutil.copyfile("Examples/NPCs/ExampleSlime.png", f"{Dir}/NPCs/{ZombieName}.png")
                            if AiTypeInGet == "Zombie":
                                shutil.copyfile("Examples/NPCs/ExampleZombie.png", f"{Dir}/NPCs/{ZombieName}.png")
                            if AiTypeInGet == "Demon Eye":
                                shutil.copyfile("Examples/NPCs/ExampleDemonEye.png", f"{Dir}/NPCs/{ZombieName}.png")
                            Sword1 = open(f"{Dir}/NPCs/{ZombieName}.cs", "r")
                            listoflines2 = Sword1.readlines()
                            Sword1.close()
                            listoflines2[4] = f"namespace {ModName}.NPCs\n"
                            listoflines2[7] = f"\tpublic class {ZombieName} : ModNPC\n"
                            listoflines2[10] = f'\t\t\tDisplayName.SetDefault("{ZombieName}");\n'
                            ZombieDamage = ZombieDamageInput.get("1.0", "end-1c")
                            listoflines2[17] = f"\t\t\tnpc.damage = {ZombieDamage};\n"
                            ZombieDefence = ZombieDefenceInput.get("1.0", "end-1c")
                            listoflines2[18] = f"\t\t\tnpc.defense = {ZombieDefence};\n"
                            ZombieLife = ZombieHealthInput.get("1.0", "end-1c")
                            listoflines2[19] = f"\t\t\tnpc.lifeMax = {ZombieLife};\n"
                            if AiTypeInGet == "Slime":
                                listoflines2[24] = f"\t\t\tnpc.aiStyle = 1;\n"
                                listoflines2[25] = f"\t\t\taiType = 1;\n"
                                listoflines2[26] = f"\t\t\tanimationType = 1;\n"
                            if AiTypeInGet == "Demon Eye":
                                listoflines2[24] = f"\t\t\tnpc.aiStyle = 2;\n"
                                listoflines2[25] = f"\t\t\taiType = 2;\n"
                                listoflines2[26] = f"\t\t\tanimationType = 2;\n"
                            DropChance = ZombieItemDropChanceInput.get("1.0", "end-1c")
                            DropItem = ZombieItemDropInput.get("1.0", "end-1c")
                            DropAmount = ZombieDropAmountInput.get("1.0", "end-1c")
                            if ZombieModIDInput.get("1.0", "end-1c") == "True":
                                listoflines2[31] = f"\t\t\tif (Main.rand.Next({DropChance}) == 0)\n"
                                listoflines2[32] = f'\t\t\t\tItem.NewItem(npc.getRect(), mod.ItemType("{DropItem}"), {DropAmount});\n'
                            else:
                                listoflines2[31] = f"\t\t\tif (Main.rand.Next({DropChance}) == 0)\n"
                                listoflines2[32] = f"\t\t\t\tItem.NewItem(npc.getRect(), ItemID.{ReadItemInput(ZombieItemDropInput)}, {DropAmount});\n"
                            Sword1 = open(f"{Dir}/NPCs/{ZombieName}.cs", "w")
                            Sword1.writelines(listoflines2)
                            Sword1.close()
                            endloop4 = True
                            tk.destroy()
                            CreateUi = True
                            endloop5 = False
                            if devmode.get() == 1 :
                                CreateUi2 = True
                                while not endloop5 :
                                    def Submit() :
                                        global endloop5
                                        listoflines7 = Code.get("1.0", "end-1c")
                                        Sword2 = open(f"{Dir}/NPCs/{ZombieName}.cs", "w")
                                        Sword2.writelines(listoflines7)
                                        Sword2.close()
                                        tk.destroy()
                                        endloop5 = True

                                    if CreateUi2 :
                                        CreateUi2 = False
                                        tk = Tk()
                                        tk.title("TCreater - Edit Code")
                                        tk.geometry("1500x1000")
                                        Code = Text(tk, width=150, height=50)
                                        Code.pack()
                                        Create2 = Button(tk, text="Submit!", command=Submit).pack()
                                        start = 1.0
                                        for i in listoflines2:
                                            Code.insert(str(start), i)
                                            start += 1.0

                        CreateB = Button(tk, text = "Create!", command = Create).pack()
                        c = True
            if Command == "Breastplate":
                endloop4 = False
                tk.destroy()
                tk = Tk()
                tk.title("TCreator - Create Breastplate")
                tk.geometry("500x700")
                tk.update()
                Title = Label(tk, text="Breastplate", font="System 18").pack()
                tk.update()
                Blank(5)
                Notice("Breastplate Name")
                BreastplateNameInput = Text(tk, width = 20, height = 1)
                BreastplateNameInput.pack()
                Blank(5)
                Notice("Breastplate Description")
                BreastplateDescriptionInput = Text(tk, width=20, height=1)
                BreastplateDescriptionInput.pack()
                Blank(5)
                Notice("Breastplate Defence")
                BreastplateDefenceInput = Text(tk, width=20, height=1)
                BreastplateDefenceInput.pack()
                Blank(5)
                Notice("Breastplate Crafting Item")
                BreastplateCraftingItemInput = Text(tk, width=20, height=1)
                BreastplateCraftingItemInput.pack()
                Blank(5)
                Notice("Breastplate Crafting Amount")
                BreastplateCraftingAmountInput = Text(tk, width=20, height=1)
                BreastplateCraftingAmountInput.pack()
                Blank(5)
                Notice("Breastplate Crafting Station")
                BreastplateCraftingStationInput = Text(tk, width=20, height=1)
                BreastplateCraftingStationInput.pack()
                Blank(5)

                c = False

                while not endloop4:
                    tk.update()
                    if not c:
                        def Create():
                            global endloop4
                            global CreateUi
                            global endloop3
                            global tk

                            BreastplateName = BreastplateNameInput.get("1.0", "end-1c")
                            shutil.copyfile("Examples/Items/Armor/ExampleBreastplate.cs", f"{Dir}/Items/Armor/{BreastplateName}.cs")
                            shutil.copyfile("Examples/Items/Armor/ExampleBreastplate.png", f"{Dir}/Items/Armor/{BreastplateName}.png")
                            shutil.copyfile("Examples/Items/Armor/ExampleBreastplate_Body.png", f"{Dir}/Items/Armor/{BreastplateName}_Body.png")
                            shutil.copyfile("Examples/Items/Armor/ExampleBreastplate_Arms.png", f"{Dir}/Items/Armor/{BreastplateName}_Arms.png")
                            shutil.copyfile("Examples/Items/Armor/ExampleBreastplate_Body.png", f"{Dir}/Items/Armor/{BreastplateName}_FemaleBody.png")
                            Sword1 = open(f"{Dir}/Items/Armor/{BreastplateName}.cs", "r")
                            listoflines = Sword1.readlines()
                            print(listoflines)
                            listoflines[4] = f"namespace {ModName}.Items.Armor\n"
                            listoflines[7] = f"\tpublic class {BreastplateName} : ModItem\n"
                            Description = BreastplateDescriptionInput.get("1.0", "end-1c")
                            listoflines[11] = f'\t\t\tDisplayName.SetDefault("{BreastplateName}");\n'
                            listoflines[12] = f'\t\t\tTooltip.SetDefault("{Description}");'
                            Defence = BreastplateDefenceInput.get("1.0", "end-1c")
                            listoflines[20] = f"\t\t\titem.defense = {Defence};\n"
                            CraftingRecipe = ReadItemInput(BreastplateCraftingItemInput)
                            CraftingAmount = BreastplateCraftingAmountInput.get("1.0", "end-1c")
                            listoflines[25] = f"\t\t\trecipe.AddIngredient(ItemID.{CraftingRecipe}, {CraftingAmount});\n"
                            CraftingDevice = BreastplateCraftingStationInput.get("1.0", "end-1c")
                            listoflines[26] = f"\t\t\trecipe.AddTile(TileID.{CraftingDevice});\n"
                            Sword1.close()
                            Sword1 = open(f"{Dir}/Items/Armor/{BreastplateName}.cs", "w")
                            Sword1.writelines(listoflines)
                            Sword1.close()
                            endloop3 = True
                            endloop4 = True
                            tk.destroy()
                            CreateUi = True
                            endloop5 = False
                            if devmode.get() == 1 :
                                CreateUi2 = True
                                while not endloop5 :
                                    def Submit() :
                                        global endloop5
                                        listoflines7 = Code.get("1.0", "end-1c")
                                        Sword2 = open(f"{Dir}/Items/Armor/{BreastplateName}.cs", "w")
                                        Sword2.writelines(listoflines7)
                                        Sword2.close()
                                        tk.destroy()
                                        endloop5 = True

                                    if CreateUi2 :
                                        CreateUi2 = False
                                        tk = Tk()
                                        tk.title("TCreater - Edit Code")
                                        tk.geometry("1500x1000")
                                        Code = Text(tk, width=150, height=50)
                                        Code.pack()
                                        Create2 = Button(tk, text="Submit!", command=Submit).pack()
                                        start = 1.0
                                        for i in listoflines:
                                            Code.insert(str(start), i)
                                            start += 1.0

                        CreateB = Button(tk, text = "Create!", command = Create).pack()
                        c = True
            if Command == "Helmet":
                endloop4 = False
                tk.destroy()
                tk = Tk()
                tk.title("TCreator - Create Helmet")
                tk.geometry("500x700")
                tk.update()
                Title = Label(tk, text="Helmet", font="System 18").pack()
                tk.update()
                Blank(5)
                Notice("Helmet Name")
                HelmetNameInput = Text(tk, width = 20, height = 1)
                HelmetNameInput.pack()
                Blank(5)
                Notice("Helmet Description")
                HelmetDescriptionInput = Text(tk, width=20, height=1)
                HelmetDescriptionInput.pack()
                Blank(5)
                Notice("Helmet Defence")
                HelmetDefenceInput = Text(tk, width=20, height=1)
                HelmetDefenceInput.pack()
                Blank(5)
                Notice("Helmet Crafting Item")
                HelmetCraftingItemInput = Text(tk, width=20, height=1)
                HelmetCraftingItemInput.pack()
                Blank(5)
                Notice("Helmet Crafting Amount")
                HelmetCraftingAmountInput = Text(tk, width=20, height=1)
                HelmetCraftingAmountInput.pack()
                Blank(5)
                Notice("Helmet Crafting Station")
                HelmetCraftingStationInput = Text(tk, width=20, height=1)
                HelmetCraftingStationInput.pack()
                Blank(5)

                c = False

                while not endloop4:
                    tk.update()
                    if not c:
                        def Create():
                            global endloop4
                            global CreateUi
                            global endloop3
                            global tk

                            HelmetName = HelmetNameInput.get("1.0", "end-1c")
                            shutil.copyfile("Examples/Items/Armor/ExampleHelmet.cs", f"{Dir}/Items/Armor/{HelmetName}.cs")
                            shutil.copyfile("Examples/Items/Armor/ExampleHelmet.png", f"{Dir}/Items/Armor/{HelmetName}.png")
                            shutil.copyfile("Examples/Items/Armor/ExampleHelmet_Head.png", f"{Dir}/Items/Armor/{HelmetName}_Head.png")
                            Sword1 = open(f"{Dir}/Items/Armor/{HelmetName}.cs", "r")
                            listoflines = Sword1.readlines()
                            print(listoflines)
                            listoflines[4] = f"namespace {ModName}.Items.Armor\n"
                            listoflines[7] = f"\tpublic class {HelmetName} : ModItem\n"
                            Description = HelmetDescriptionInput.get("1.0", "end-1c")
                            listoflines[10] = f'\t\t\tTooltip.SetDefault("{Description}");'
                            Defence = HelmetDefenceInput.get("1.0", "end-1c")
                            listoflines[18] = f"\t\t\titem.defense = {Defence};\n"
                            CraftingRecipe = ReadItemInput(HelmetCraftingItemInput)
                            CraftingAmount = HelmetCraftingAmountInput.get("1.0", "end-1c")
                            listoflines[23] = f"\t\t\trecipe.AddIngredient(ItemID.{CraftingRecipe}, {CraftingAmount});\n"
                            CraftingDevice = HelmetCraftingStationInput.get("1.0", "end-1c")
                            listoflines[24] = f"\t\t\trecipe.AddTile(TileID.{CraftingDevice});\n"
                            Sword1.close()
                            Sword1 = open(f"{Dir}/Items/Armor/{HelmetName}.cs", "w")
                            Sword1.writelines(listoflines)
                            Sword1.close()
                            endloop3 = True
                            endloop4 = True
                            CreateUi = True
                            tk.destroy()
                            endloop5 = False
                            if devmode.get() == 1 :
                                CreateUi2 = True
                                while not endloop5 :
                                    def Submit() :
                                        global endloop5
                                        listoflines7 = Code.get("1.0", "end-1c")
                                        Sword2 = open(f"{Dir}/Items/Armor/{HelmetName}.cs", "w")
                                        Sword2.writelines(listoflines7)
                                        Sword2.close()
                                        tk.destroy()
                                        endloop5 = True

                                    if CreateUi2 :
                                        CreateUi2 = False
                                        tk = Tk()
                                        tk.title("TCreater - Edit Code")
                                        tk.geometry("1500x1000")
                                        Code = Text(tk, width=150, height=50)
                                        Code.pack()
                                        Create2 = Button(tk, text="Submit!", command=Submit).pack()
                                        start = 1.0
                                        for i in listoflines:
                                            Code.insert(str(start), i)
                                            start += 1.0

                        CreateB = Button(tk, text = "Create!", command = Create).pack()
                        c = True
            if Command == "Leggings":
                endloop4 = False
                tk.destroy()
                tk = Tk()
                tk.title("TCreator - Create Leggings")
                tk.geometry("500x700")
                tk.update()
                Title = Label(tk, text="Leggings", font="System 18").pack()
                tk.update()
                Blank(5)
                Notice("Leggings Name")
                LeggingsNameInput = Text(tk, width = 20, height = 1)
                LeggingsNameInput.pack()
                Blank(5)
                Notice("Leggings Description")
                LeggingsDescriptionInput = Text(tk, width=20, height=1)
                LeggingsDescriptionInput.pack()
                Blank(5)
                Notice("Leggings Defence")
                LeggingsDefenceInput = Text(tk, width=20, height=1)
                LeggingsDefenceInput.pack()
                Blank(5)
                Notice("Leggings Crafting Item")
                LeggingsCraftingItemInput = Text(tk, width=20, height=1)
                LeggingsCraftingItemInput.pack()
                Blank(5)
                Notice("Leggings Crafting Amount")
                LeggingsCraftingAmountInput = Text(tk, width=20, height=1)
                LeggingsCraftingAmountInput.pack()
                Blank(5)
                Notice("Leggings Crafting Station")
                LeggingsCraftingStationInput = Text(tk, width=20, height=1)
                LeggingsCraftingStationInput.pack()
                Blank(5)

                c = False

                while not endloop4:
                    tk.update()
                    if not c:
                        def Create():
                            global endloop4
                            global CreateUi
                            global endloop3
                            global tk

                            LeggingsName = LeggingsNameInput.get("1.0", "end-1c")
                            shutil.copyfile("Examples/Items/Armor/ExampleLeggings.cs", f"{Dir}/Items/Armor/{LeggingsName}.cs")
                            shutil.copyfile("Examples/Items/Armor/ExampleLeggings.png", f"{Dir}/Items/Armor/{LeggingsName}.png")
                            shutil.copyfile("Examples/Items/Armor/ExampleLeggings_Legs.png", f"{Dir}/Items/Armor/{LeggingsName}_Legs.png")
                            Sword1 = open(f"{Dir}/Items/Armor/{LeggingsName}.cs", "r")
                            listoflines = Sword1.readlines()
                            print(listoflines)
                            listoflines[4] = f"namespace {ModName}.Items.Armor\n"
                            listoflines[7] = f"\tpublic class {LeggingsName} : ModItem\n"
                            Description = LeggingsDescriptionInput.get("1.0", "end-1c")
                            listoflines[10] = f'\t\t\tTooltip.SetDefault("{Description}");'
                            Defence = LeggingsDefenceInput.get("1.0", "end-1c")
                            listoflines[18] = f"\t\t\titem.defense = {Defence};\n"
                            CraftingRecipe = ReadItemInput(LeggingsCraftingItemInput)
                            CraftingAmount = LeggingsCraftingAmountInput.get("1.0", "end-1c")
                            listoflines[23] = f"\t\t\trecipe.AddIngredient(ItemID.{CraftingRecipe}, {CraftingAmount});\n"
                            CraftingDevice = LeggingsCraftingStationInput.get("1.0", "end-1c")
                            listoflines[24] = f"\t\t\trecipe.AddTile(TileID.{CraftingDevice});\n"
                            Sword1.close()
                            Sword1 = open(f"{Dir}/Items/Armor/{LeggingsName}.cs", "w")
                            Sword1.writelines(listoflines)
                            Sword1.close()
                            endloop3 = True
                            endloop4 = True
                            tk.destroy()
                            CreateUi = True
                            endloop5 = False
                            if devmode.get() == 1 :
                                CreateUi2 = True
                                while not endloop5 :
                                    def Submit() :
                                        global endloop5
                                        listoflines7 = Code.get("1.0", "end-1c")
                                        Sword2 = open(f"{Dir}/Items/Armor/{LeggingsName}.cs", "w")
                                        Sword2.writelines(listoflines7)
                                        Sword2.close()
                                        tk.destroy()
                                        endloop5 = True

                                    if CreateUi2 :
                                        CreateUi2 = False
                                        tk = Tk()
                                        tk.title("TCreater - Edit Code")
                                        tk.geometry("1500x1000")
                                        Code = Text(tk, width=150, height=50)
                                        Code.pack()
                                        Create2 = Button(tk, text="Submit!", command=Submit).pack()
                                        start = 1.0
                                        for i in listoflines:
                                            Code.insert(str(start), i)
                                            start += 1.0

                        CreateB = Button(tk, text = "Create!", command = Create).pack()
                        c = True
            if Command == "Accessory":
                endloop4 = False
                tk.destroy()
                tk = Tk()
                tk.title("TCreator - Create Accessory")
                tk.geometry("500x700")
                tk.update()
                Buff = StringVar()
                Buff.set("None")
                BuffOp = StringVar()
                BuffOp.set("Set")
                Title = Label(tk, text="Accessory", font="System 18").pack()
                tk.update()
                Blank(5)
                Notice("Accessory Name")
                AccessoryNameInput = Text(tk, width = 20, height = 1)
                AccessoryNameInput.pack()
                Blank(5)
                Notice("Accessory Description")
                AccessoryDescriptionInput = Text(tk, width=20, height=1)
                AccessoryDescriptionInput.pack()
                Blank(5)
                Notice("Accessory Crafting Item")
                AccessoryCraftingItemInput = Text(tk, width=20, height=1)
                AccessoryCraftingItemInput.pack()
                Blank(5)
                Notice("Accessory Crafting Amount")
                AccessoryCraftingAmountInput = Text(tk, width=20, height=1)
                AccessoryCraftingAmountInput.pack()
                Blank(5)
                Notice("Accessory Crafting Station")
                AccessoryCraftingStationInput = Text(tk, width=20, height=1)
                AccessoryCraftingStationInput.pack()
                Blank(5)
                Notice("Accessory Buff")
                AccessoryBuffInput = OptionMenu(tk, Buff, *Buffs)
                AccessoryBuffInput.pack()
                Notice("Accessory Buff Operator")
                AccessoryBuffOpInput = OptionMenu(tk, BuffOp, *Operators)
                AccessoryBuffOpInput.pack()
                Notice("Accessory Buff Value")
                AccessoryBuffValueInput = Text(tk, width=20, height=1)
                AccessoryBuffValueInput.pack()
                Blank(5)

                c = False

                while not endloop4:
                    tk.update()
                    if not c:
                        def Create():
                            global endloop4
                            global CreateUi
                            global endloop3
                            global tk

                            AccessoryName = AccessoryNameInput.get("1.0", "end-1c")
                            shutil.copyfile("Examples/Items/Accessories/ExampleAccessory.cs", f"{Dir}/Items/Accessories/{AccessoryName}.cs")
                            shutil.copyfile("Examples/Items/Accessories/ExampleAccessory.png", f"{Dir}/Items/Accessories/{AccessoryName}.png")
                            Sword1 = open(f"{Dir}/Items/Accessories/{AccessoryName}.cs", "r")
                            listoflines = Sword1.readlines()
                            print(listoflines)
                            listoflines[5] = f"namespace {ModName}.Items.Accessories\n"
                            listoflines[7] = f"\tpublic class {AccessoryName} : ModItem\n"
                            Description = AccessoryDescriptionInput.get("1.0", "end-1c")
                            listoflines[10] = f'\t\t\tTooltip.SetDefault("{Description}");\n'
                            CraftingRecipe = ReadItemInput(AccessoryCraftingItemInput)
                            CraftingAmount = AccessoryCraftingAmountInput.get("1.0", "end-1c")
                            listoflines[27] = f"\t\t\trecipe.AddIngredient(ItemID.{CraftingRecipe}, {CraftingAmount});\n"
                            CraftingDevice = AccessoryCraftingStationInput.get("1.0", "end-1c")
                            listoflines[28] = f"\t\t\trecipe.AddTile(TileID.{CraftingDevice});\n"
                            BuffA = Buff.get()
                            BuffOpA = BuffOp.get()
                            BuffAmountA = AccessoryBuffValueInput.get("1.0", "end-1c")
                            Operator = ""
                            if BuffOpA == "Set":
                                Operator = "="
                            else:
                                Operator = f"{BuffOpA}="
                            if BuffA == "None" :
                                line = "\t\t\t//What Happens While Its Equippeds. e.g: player.maxMinions += 1"
                            elif BuffA == "Max Minions" :
                                line = f"player.maxMinions {Operator} {BuffAmountA};"
                            elif BuffA == "Health Regen" :
                                line = f"player.lifeRegenTime {Operator} {BuffAmountA};"
                            elif BuffA == "Magic Damage" :
                                line = f"vmagicDamage {Operator} {BuffAmountA};"
                            elif BuffA == "Ranged Damage" :
                                line = f"player.rangedDamage {Operator} {BuffAmountA};"
                            elif BuffA == "Summoning Damage" :
                                line = f"player.minionDamage {Operator} {BuffAmountA};"
                            elif BuffA == "Melee Damage" :
                                line = f"player.meleeDamage {Operator} {BuffAmountA};"
                            elif BuffA == "Melee Speed" :
                                line = f"player.meleeSpeed {Operator} {BuffAmountA};"
                            elif BuffA == "Movement Speed" :
                                line = f"player.moveSpeed {Operator} {BuffAmountA};"
                            elif BuffA == "Mana Cost" :
                                line = f"player.manaCost {Operator} {BuffAmountA};"
                            elif BuffA == "No Knockback" :
                                line = f"player.noKnockback {Operator} {BuffAmountA};"
                            elif BuffA == "Crit Chance" :
                                line = f"player.meleeCrit {Operator} {BuffAmountA};"
                            elif BuffA == "Double Jump" :
                                line = f"player.doubleJump {Operator} {BuffAmountA};"
                            listoflines[22] = f"\t\t\t{line}"
                            Sword1.close()
                            Sword1 = open(f"{Dir}/Items/Accessories/{AccessoryName}.cs", "w")
                            Sword1.writelines(listoflines)
                            Sword1.close()
                            endloop3 = True
                            endloop4 = True
                            tk.destroy()
                            CreateUi = True
                            endloop5 = False
                            if devmode.get() == 1 :
                                CreateUi2 = True
                                while not endloop5 :
                                    def Submit() :
                                        global endloop5
                                        listoflines7 = Code.get("1.0", "end-1c")
                                        Sword2 = open(f"{Dir}/Items/Accessories/{AccessoryName}.cs", "w")
                                        Sword2.writelines(listoflines7)
                                        Sword2.close()
                                        tk.destroy()
                                        endloop5 = True

                                    if CreateUi2 :
                                        CreateUi2 = False
                                        tk = Tk()
                                        tk.title("TCreater - Edit Code")
                                        tk.geometry("1500x1000")
                                        Code = Text(tk, width=150, height=50)
                                        Code.pack()
                                        Create2 = Button(tk, text="Submit!", command=Submit).pack()
                                        start = 1.0
                                        for i in listoflines:
                                            Code.insert(str(start), i)
                                            start += 1.0

                        CreateB = Button(tk, text = "Create!", command = Create).pack()
                        c = True
            if Command == "Boss":
                endloop4 = False
                tk.destroy()
                tk = Tk()
                tk.title("TCreator - Create Boss")
                tk.geometry("500x800")
                tk.update()
                Title = Label(tk, text="Boss", font="System 18").pack()
                tk.update()
                AiTypeVar = StringVar()
                AiTypeVar.set("Zombie")
                Blank(5)
                Notice("Boss Name")
                ZombieNameInput = Text(tk, width = 20, height = 1)
                ZombieNameInput.pack()
                Blank(5)
                Notice("Boss Width Default: 18")
                ZombieWidthInput = Text(tk, width=20, height=1)
                ZombieWidthInput.pack()
                Blank(5)
                Notice("Boss Height Default: 40")
                ZombieHeightInput = Text(tk, width=20, height=1)
                ZombieHeightInput.pack()
                Blank(5)
                Notice("Boss Damage")
                ZombieDamageInput = Text(tk, width=20, height=1)
                ZombieDamageInput.pack()
                Blank(5)
                Notice("Boss Health")
                ZombieHealthInput = Text(tk, width=20, height=1)
                ZombieHealthInput.pack()
                Blank(5)
                Notice("Boss Defence (Default = 6)")
                ZombieDefenceInput = Text(tk, width=20, height=1)
                ZombieDefenceInput.pack()
                Blank(5)
                Notice("Enemy AI (not W.I.P anymore)")
                AiTypeInput = OptionMenu(tk, AiTypeVar, *AiType)
                AiTypeInput.pack()
                Blank(5)
                Notice("Enemy Projectile Damage")
                ProjDamageInput = Text(tk, width=20, height=1)
                ProjDamageInput.pack()
                Blank(5)
                Notice("Enemy Projectile Knockback")
                ProjKnockInput = Text(tk, width=20, height=1)
                ProjKnockInput.pack()
                Blank(5)
                Notice("Enemy Projectile")
                ProjInput = Text(tk, width=20, height=1)
                ProjInput.pack()
                Blank(5)

                c = False

                while not endloop4:
                    tk.update()
                    if not c:
                        def Create():
                            global endloop4
                            global CreateUi
                            global endloop3
                            global tk
                            print(" ")
                            ZombieName = ZombieNameInput.get("1.0", "end-1c")
                            shutil.copyfile("Examples/BossStuff/NPCs/ExampleZombie.cs", f"{Dir}/NPCs/{ZombieName}.cs")
                            AiTypeInGet = AiTypeVar.get()
                            if AiTypeInGet == "Slime":
                                shutil.copyfile("Examples/BossStuff/NPCs/ExampleSlime.png", f"{Dir}/NPCs/{ZombieName}.png")
                            if AiTypeInGet == "Zombie":
                                shutil.copyfile("Examples/BossStuff/NPCs/ExampleZombie.png", f"{Dir}/NPCs/{ZombieName}.png")
                            if AiTypeInGet == "Demon Eye":
                                shutil.copyfile("Examples/BossStuff/NPCs/ExampleDemonEye.png", f"{Dir}/NPCs/{ZombieName}.png")
                            Sword1 = open(f"{Dir}/NPCs/{ZombieName}.cs", "r")
                            listoflines2 = Sword1.readlines()
                            Sword1.close()
                            listoflines2[6] = f"namespace {ModName.replace(' ', '')}.NPCs\n"
                            listoflines2[3] = f"using {ModName.replace(' ', '')}.Items;\n"
                            listoflines2[8] = f"\tpublic class {ZombieName} : ModNPC\n"
                            listoflines2[11] = f'\t\t\tDisplayName.SetDefault("{ZombieName}");\n'
                            ZombieDamage = ZombieDamageInput.get("1.0", "end-1c")
                            ZombieWidth = ZombieWidthInput.get("1.0", "end-1c")
                            ZombieHeight = ZombieHeightInput.get("1.0", "end-1c")
                            listoflines2[17] = f"\t\t\tnpc.width = {ZombieWidth};\n"
                            listoflines2[18] = f"\t\t\tnpc.height = {ZombieHeight};\n"
                            listoflines2[19] = f"\t\t\tnpc.damage = {ZombieDamage};\n"
                            ZombieDefence = ZombieDefenceInput.get("1.0", "end-1c")
                            listoflines2[20] = f"\t\t\tnpc.defense = {ZombieDefence};\n"
                            ZombieLife = ZombieHealthInput.get("1.0", "end-1c")
                            ProjDamage = ProjDamageInput.get("1.0", "end-1c")
                            ProjKnockback = ProjKnockInput.get("1.0", "end-1c")
                            Proj = ProjInput.get("1.0", "end-1c")
                            listoflines2[21] = f"\t\t\tnpc.lifeMax = {ZombieLife};\n"
                            listoflines2[31] = f"\t\t\tbossBag = ModContent.ItemType<{ZombieName}Bag>();\n"
                            listoflines2[47] = f"\t\t\tProjectile.NewProjectile(position: npc.position, velocity: npc.velocity, Type: ProjectileID.{Proj}, Damage: {ProjDamage}, KnockBack: {ProjKnockback}, Owner: 0);\n"
                            if AiTypeInGet == "Slime":
                                listoflines2[26] = f"\t\t\tnpc.aiStyle = 1;\n"
                                listoflines2[27] = f"\t\t\taiType = 1;\n"
                                listoflines2[28] = f"\t\t\tanimationType = 1;\n"
                            if AiTypeInGet == "Demon Eye":
                                listoflines2[26] = f"\t\t\tnpc.aiStyle = 2;\n"
                                listoflines2[27] = f"\t\t\taiType = 2;\n"
                                listoflines2[28] = f"\t\t\tanimationType = 2;\n"
                            Sword1 = open(f"{Dir}/NPCs/{ZombieName}.cs", "w")
                            Sword1.writelines(listoflines2)
                            Sword1.close()
                            CreateUi = True
                            endloop4 = False
                            tk.destroy()
                            tk = Tk()
                            tk.title("TCreator - Create Boss Bag")
                            tk.geometry("500x1080")
                            tk.update()
                            Title = Label(tk, text="Boss Bag + Summon Item", font="System 18").pack()
                            tk.update()
                            Blank(5)
                            Bags = []
                            BagAmounts = []
                            BagAmount = 0
                            tk.update()
                            Blank(5)
                            Notice("Summon Crafting Item")
                            SummonCraftingItemInput = Text(tk, width=20, height=1)
                            SummonCraftingItemInput.pack()
                            Blank(5)
                            Notice("Summon Crafting Amount")
                            SummonCraftingAmountInput = Text(tk, width=20, height=1)
                            SummonCraftingAmountInput.pack()
                            Blank(5)
                            Notice("Summon Name")
                            SummonNameInput = Text(tk, width=20, height=1)
                            SummonNameInput.pack()
                            Blank(5)

                            def AddBagItem() :
                                global BagAmount
                                Notice(f"Bag Item")
                                BagInput = Text(tk, width=20, height=1)
                                BagInput.pack()
                                Bags.append(BagInput)
                                Notice(f"Bag Item Amount")
                                BagAInput = Text(tk, width=20, height=1)
                                BagAInput.pack()
                                BagAmounts.append(BagAInput)
                                Blank(5)
                            Blank(5)

                            c = False

                            while not endloop4 :
                                tk.update()
                                if not c :
                                    def Create2() :
                                        global endloop4
                                        global CreateUi
                                        global endloop3
                                        global tk
                                        shutil.copyfile("Examples/BossStuff/Items/ExampleBag.cs", f"{Dir}/Items/{ZombieName}Bag.cs")
                                        shutil.copyfile("Examples/BossStuff/Items/ExampleBag.png", f"{Dir}/Items/{ZombieName}Bag.png")
                                        Sword1 = open(f"{Dir}/Items/{ZombieName}Bag.cs", "r")
                                        listoflines3 = Sword1.readlines()
                                        Sword1.close()
                                        listoflines3[6] = f'namespace {ModName.replace(" ", "")}.Items\n'
                                        listoflines3[8] = f'\tpublic class {ZombieName}Bag : ModItem\n'
                                        listoflines3[11] = f'\t\t\tDisplayName.SetDefault("Treasure Bag");\n'
                                        listoflines3[33] = f'\t\tpublic override int BossBagNPC => NPCType<NPCs.{ZombieName}>();\n'

                                        count = 0
                                        SECTIONSTR = ""
                                        for i4 in Bags :
                                            BagItem = ReadItemInput(i4)
                                            BagItemAmount = BagAmounts[count].get("1.0", "end-1c")
                                            SECTIONSTR += f'\t\t\tplayer.QuickSpawnItem(ItemID.{BagItem}, {BagItemAmount});\n'
                                            count += 1
                                        listoflines3[30] = SECTIONSTR
                                        Sword1 = open(f"{Dir}/Items/{ZombieName}Bag.cs", "w")
                                        Sword1.writelines(listoflines3)
                                        Sword1.close()
                                        shutil.copyfile("Examples/BossStuff/Items/Summon.cs", f"{Dir}/Items/{ZombieName}Summon.cs")
                                        shutil.copyfile("Examples/BossStuff/Items/Summon.png", f"{Dir}/Items/{ZombieName}Summon.png")
                                        Sword1 = open(f"{Dir}/Items/{ZombieName}Summon.cs", "r")
                                        listoflines3 = Sword1.readlines()
                                        Sword1.close()
                                        SummonName = SummonNameInput.get("1.0", "end-1c")
                                        listoflines3[8] = f'namespace {ModName.replace(" ", "")}.Items\n'
                                        listoflines3[5] = f'using {ModName.replace(" ", "")}.Items;\n'
                                        listoflines3[6] = f'using {ModName.replace(" ", "")}.NPCs;\n'
                                        listoflines3[13] = f'\tinternal class {ZombieName}Summon : ModItem\n'
                                        listoflines3[18] = f'\t\t\tTooltip.SetDefault("Summons the {ZombieName}");\n'
                                        listoflines3[19] = f'\t\t\tDisplayName.SetDefault("{SummonName}");\n'
                                        listoflines3[36] = f'\t\t\treturn !NPC.AnyNPCs(mod.NPCType("{ZombieName}"));\n'
                                        listoflines3[42] = f'\t\t\t\tNPC.SpawnOnPlayer(player.whoAmI, mod.NPCType("{ZombieName}"));\n'
                                        SummonCraftingItem = ReadItemInput(SummonCraftingItemInput)
                                        SummonCraftingAmount = SummonCraftingAmountInput.get("1.0", "end-1c")
                                        listoflines3[53] = f'\t\t\trecipe.AddIngredient(ItemID.{SummonCraftingItem}, {SummonCraftingAmount});\n'
                                        Sword1 = open(f"{Dir}/Items/{ZombieName}Summon.cs", "w")
                                        Sword1.writelines(listoflines3)
                                        Sword1.close()
                                        path = f"{Dir}/NPCs"
                                        path = os.path.realpath(path)
                                        os.startfile(path)
                                        path = f"{Dir}/Items"
                                        path = os.path.realpath(path)
                                        os.startfile(path)

                                        endloop3 = True
                                        endloop4 = True
                                        tk.destroy()
                                        CreateUi = True

                                    CreateB2 = Button(tk, text="Create!", command=Create2).pack()
                                    Blank(5)
                                    AddBagItemB = Button(tk, text="Add Bag Item", command=AddBagItem).pack()
                                    c = True
                        CreateB = Button(tk, text="Create!", command=Create).pack()
                        c = True
    '''
    if Command == "Bullet":
        print(" ")
        BulletName = input("Enter The Name Of The Bullet")
        shutil.copyfile("Examples/Projectiles/ExampleBullet.cs", f"{Dir}/Projectiles/{BulletName}.cs")
        shutil.copyfile("Examples/Projectiles/ExampleBullet.png", f"{Dir}/Projectiles/{BulletName}.png")
        shutil.copyfile("Examples/Items/Weapons/ExampleBullet.cs", f"{Dir}/Items/Weapons/{BulletName}.cs")
        shutil.copyfile("Examples/Items/Weapons/ExampleBullet.png", f"{Dir}/Items/Weapons/{BulletName}.png")
        Sword = open(f"{Dir}/Projectiles/{BulletName}.cs", "r")
        listoflines3 = Sword.readlines()
        Sword.close()
        Width = input("Enter The Width Of Your Projectile (Default Is 8): ")
        listoflines3[11] = f'\t\t\tDisplayName.SetDefault("{BulletName}");\n'
        listoflines3[17] = f"\t\t\tprojectile.width = {Width};\n"
        listoflines3[6] = f"namespace {ModName}.Projectiles\n"
        listoflines3[8] = f"\tpublic class {BulletName} : ModProjectile\n"
        Height = input("Enter The Height Of Your Projectile (Default Is 8): ")
        listoflines3[18] = f"\t\t\tprojectile.height = {Height};\n"
        Sword = open(f"{Dir}/Projectiles/{BulletName}.cs", "w")
        Sword.writelines(listoflines3)
        Sword.close()
        Sword = open(f"{Dir}/Items/Weapons/{BulletName}.cs", "r")
        listoflines3 = Sword.readlines()
        Sword.close()
        listoflines3[5] = f"namespace {ModName}.Items.Weapons\n"
        listoflines3[7] = f"\tpublic class {BulletName} : ModItem\n"
        Desc = input("Enter The Description Of The Bullet: ")
        listoflines3[10] = f'\t\t\tTooltip.SetDefault("{Desc}");\n'
        Damage = input("Enter The Damage Of The Bullet: ")
        listoflines3[14] = f"\t\t\titem.damage = {Damage};\n"
        listoflines3[23] = f"\t\t\titem.shoot = ProjectileType<Projectiles.{BulletName}>();\n"
        Speed = input("Enter The Speed Of The Bullet (Default Is 16): ")
        listoflines3[24] = f"\t\t\titem.shootSpeed = {Speed}f;\n"
        ItemToCraft = input("Enter The Name Of The Item You Need To Craft The Bullet: ")
        ItemAmount = input("Enter The Amount Of That Item You Need To Craft The Bullet: ")
        Workbench = input("Enter The Crafting Station You Need To Be At To Craft The Bullet: ")
        listoflines3[37] = f"\t\t\trecipe.AddIngredient(ItemID.{ItemToCraft}, {ItemAmount});\n"
        listoflines3[38] = f"\t\t\trecipe.AddTile(TileID.{Workbench});\n"
        listoflines3[16] = f"\t\t\titem.width = {Width};\n"
        listoflines3[17] = f"\t\t\titem.height = {Height};\n"
        Sword = open(f"{Dir}/Items/Weapons/{BulletName}.cs", "w")
        Sword.writelines(listoflines3)
        Sword.close()
    '''