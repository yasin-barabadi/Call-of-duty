class acoupment:
    def __init__(self, gun):
        self.gun = gun
        
class Gun(acoupment):
    def __init__(self ,gun ,Fire_Rate ,Damage ,Accuracy ,Range ,Magazine_Capacity ,Reload_Time ,Mobility):
        super().__init__(gun)
        self.Fire_Rate = Fire_Rate #سرعت شلیک
        self.Damage = Damage #آسیب
        self.Accuracy = Accuracy #دقت
        self.Range = Range #برد
        self.Magazine_Capacity = Magazine_Capacity #ظرفیت خشاب
        self.Reload_Time = Reload_Time #زمان بارگیری
        self.Mobility = Mobility #انعطاف پذیری
        
    def Comparison(self):
        Fire_Rate_max = max(guns, key=lambda p: p.Fire_Rate)
        Damage_max = max(guns, key=lambda p: p.Damage)
        Accuracy_max = max(guns, key=lambda p: p.Accuracy)
        Range_max = max(guns, key=lambda p: p.Range)
        Magazine_Capacity_max = max(guns, key=lambda p: p.Magazine_Capacity)
        Reload_Time_max = max(guns, key=lambda p: p.Reload_Time)
        Mobility_max = max(guns, key=lambda p: p.Mobility)
        
        print(f"Fire_Rate_max: {Fire_Rate_max.gun}")
        print(f"Damage_max: {Damage_max.gun}")
        print(f"Accuracy_max: {Accuracy_max.gun}")
        print(f"Range_max: {Range_max.gun}")
        print(f"Magazine_Capacity_max: {Magazine_Capacity_max.gun}")
        print(f"Reload_Time_max: {Reload_Time_max.gun}")
        print(f"Mobility_max: {Mobility_max.gun}")
        
        
name = input().split()
guns = []
for i in name:
    Fire_Rate = int(input(f"Fire_Rate {i}: "))
    Damage = int(input(f"Damage {i}: "))
    Accuracy = int(input(f"Accuracy {i}: "))
    Range = int(input(f"Range {i}: "))
    Magazine_Capacity = int(input(f"MagazineReload_Time {i}: "))
    Reload_Time = int(input(f"Reload_Time {i}: "))
    Mobility = int(input(f"Mobility {i}: "))
    guns.append(Gun(i ,Fire_Rate ,Damage ,Accuracy ,Range ,Magazine_Capacity ,Reload_Time ,Mobility))
    
guns[0].Comparison()