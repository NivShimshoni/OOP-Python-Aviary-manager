from datetime import datetime, date
from random import randrange

class Bird():
    def __init__(self, ID: str, btype: str, birth: str, colors: list, foodtype: str, volume: int):
        #בדיקת תקינות קלט ID: רק ספרות ואותיות גדולות
        #עבור כל תו, אם הוא לא ספרה ולא אות גדולה: שגיאה
        for char in ID:
            if not(char.isdigit() or (char.isalpha() and char.isupper())):
                raise ValueError(f"Invalid ID: {ID}. Must contain only digits and uppercase letters.")
        #2. בדיקת תקינות תאריך והמרה לאובייקט תאריך
        try:
            #מנסים להמיר את המחרוזת לתאריך לפי הפורמט DD:MM:YYYY
            self.birth_date = datetime.strptime(birth, "%d:%m:%Y").date()
        except ValueError:
            raise ValueError(f"Invalid Date Format: {birth}. Must be DD:MM:YYYY")
        #3. בדיקת צבעים (צריכה להיות רשימה לא ריקה)
        if not isinstance(colors, list) or len(colors)== 0:
            raise ValueError(f"Colours must be a non empty list.")
        #שמירת הנתונים
        self.ID = ID
        self.btype = btype
        self.colors = colors
        self.foodtype = foodtype
        self.volume = volume

    def get_age(self):
        #חישוב הגיל לפי ההוראות: שנה=365 ימים, חודש=30 ימים
        today = date.today()
        delta = (today - self.birth_date).days
        #המרה משנים לחודשים וימים נעשית לפי שארית החלוקה
        years = delta // 365
        remainder = delta % 365
        months = remainder // 30
        days = remainder % 30
        #הפורמט הנדרש: 24D, 5M, 3Y
        return f"{years}Y, {months}M, {days}D"

    def get_type(self):
        return self.btype

    def get_colors(self):
        return self.colors

    def get_food_type(self):
        return self.foodtype

    def get_volume(self):
        return self.volume

    def __str__(self):
        #הדפסה בדיוק לפי הפורמט בדוגמאות הפלט
        return (f"Bird ID: {self.ID}\n"
                f"Bird type: {self.btype}\n"
                f"Age: {self.get_age()}\n"
                f"Colors: {self.colors}\n"
                f"Food type: {self.foodtype}")

    def __eq__(self, other):
        if not isinstance(other, Bird):
            raise TypeError(f"Comparison allowed only between Bird objects.")
        return self.btype == other.btype

    def __gt__(self, other):
        #גדול ממש - אם מספר הצבעים שלי גדול משל השני
        if not isinstance(other, Bird):
            raise TypeError(f"Comparison allowed only between Bird objects.")
        return len(self.colors) > len(other.colors)

    def __lt__(self, other):
        #קטן ממש - אם מספר הצבעים שלי קטן משל השני
        if not isinstance(other,Bird):
            raise TypeError(f"Comparison allowed only between Bird objects.")
        return len(self.colors) < len(other.colors)


class Finch(Bird):
    def __init__(self, ID: str, btype: str, birth: str, colors: list, volume: int):
        #קריאה לבנאי של מחלקת האם (Bird)
        #אתחול סוג המזון ל-"Seeds"
        super().__init__(ID, btype, birth, colors, "Seeds", volume)

    def nest_building(self):
        #חילוץ הגיל בשנים מתוך המחרוזת שמחזירה get_age
        #הפורמט הוא 24D, 5M, 3Y לכן נחתוך את המחרוזת עד האות Y
        age_str = self.get_age()
        years_str = age_str.split('Y')[0] #לוקח את החלק שלפני ה-Y
        years = int(years_str)

        #בניית הקן: קן אנכי, ואז קווים תחתונים כמספר השנים, ואז קו אנכי
        nest = ['|']
        for _ in range(years):
            nest.append('_')
        nest.append('|')

        return nest


class Parrot(Bird):
    def __init__(self, ID: str, btype: str, birth: str, colors: list, volume: int):
        #תוכי אוכל תירס
        super().__init__(ID, btype, birth, colors, "Corn", volume)

    def find_nestbox(self):
        #הגודל נקבע לפי הגיל בשנים
        age_str = self.get_age()
        years = int(age_str.split('Y')[0])
        #תוכי מחפש בית רק מגיל שנתיים ומעלה
        if years < 2:
            return None
        nest_box = []
        for i in range(years): #יצירת מטריצת כוכביות ריבועית מסדר x שנים
            row = []
            for j in range(years):
                row.append('*')
            nest_box.append(row)
        return nest_box



class Zebrafinch(Finch):
    def __init__(self, ID: str, birth: str, colors: list):
        allowed = ['Brown','Orange','Black','White']#רשימת צבעים חוקיים במחלקה
        for c in colors:#בדיקת חוקיות קלט צבע במחלקה
            if c not in allowed:
                raise ValueError(f"Invalid color for Zebra Finch: {c}")
        super().__init__(ID, "Zebra Finch", birth,colors, 27000)#קריאה לאבא Finch

    def jump(self):
        return "I like to jump"

    def get_type_let(self):
        return 'Z'


class Gouldianfinch(Finch):
    def __init__(self, ID: str, birth: str, colors: list):#בדיקת צבעים חוקיים
        allowed = ['Red', 'Green','Blue','Yellow','Orange','Black','Purple','White']
        for c in colors:
            if c not in allowed:
                raise ValueError(f"Invalid color for Gouldian Finch: {c}")
        super().__init__(ID, "Gouldian Finch", birth, colors, 96000)#קריאה לאבא נפח 96000
        self.singing_strength = randrange(1,11)

    def sing(self):
        return "I like to sing", self.singing_strength

    def get_type_let(self):
        return 'G'

    def __str__(self):
        return super().__str__() + f"\nSinging strength: {self.singing_strength}"


class Budgerigar(Parrot):
    def __init__(self, ID: str, birth: str, colors: list): #בדיקת צבעים חוקיים
        allowed = ['Green', 'Blue', 'Yellow', 'Purple', 'White']
        for c in colors:
            if c not in allowed:
                raise ValueError(f"Invalid color for Budgerigar: {c}")
        super().__init__(ID, "Budgerigar", birth, colors, 96000)
        self.tweeting_strength = randrange(1,11)

    def tweet(self):
        return "I like to tweet", self.tweeting_strength

    def get_type_let(self):
        return 'B'

    def __str__(self):
        return super().__str__() + f"\nTweeting strength: {self.tweeting_strength}"


class Lovebird(Parrot):
    def __init__(self, ID: str, birth: str, colors: list):
        allowed = ['Red', 'Green', 'Blue', 'Yellow', 'Black', 'White']
        for c in colors:
            if c not in allowed:
                raise ValueError(f"Invalid color for Love Bird: {c}")
        super().__init__(ID, "Love Bird", birth, colors, 120000)

    def get_type_let(self):
        return 'L'

    def kiss(self):
        return "I like to kiss"


class Cage:
    def __init__(self, ID: str, length: int, depth: int, height: int, color: str):
        self.ID = ID
        self.length = length
        self.depth = depth
        self.height = height
        self.color = color
        self.birds = [] #רשימה שתחזיק את הציפורים בכלוב
        self.max_volume = length * depth * height #נפח כלוב מקסימלי
        self.current_occupied_volume = 0 #מעקב אחרי הנפח הנוכחי שתפוס ע"י ציפורים

    def add_bird(self, bird):
        if not isinstance(bird, Bird): #בדיקה שהקלט אכן מסוג Bird
            return False
        if len(self.birds) > 0:
            if self.birds[0].get_type() != bird.get_type():
                return False
        bird_vol = bird.get_volume() #חישוב הנפח שהציפור החדשה תתפוס
        if self.current_occupied_volume + bird_vol <= self.max_volume:
            self.birds.append(bird) #הוספה לכלוב
            self.current_occupied_volume += bird_vol #עדכון נפח תפוס
            return True #הצלחה
        return False #עבור אין מקום בכלוב או קלט לא תקין

    def get_birds(self):
        return self.birds #מחזיר את רשימת הציפורים

    def get_num_of_birds(self):
        return len(self.birds) #מחזיר את מספר הציפורים

    def get_cage(self):
        """
        Returns a 2D list representing the cage.
        Empty cage is represented by '#'.
        Occupied cage is represented by the first letter of the bird type.
        Grid resolution is 10x10 cm.
        """
        # 1. חישוב מספר השורות והעמודות (חלוקה ב-10 לפי ההנחיות)
        num_rows = self.height // 10
        num_cols = self.length // 10

        # 2. קביעת התו לציור
        # ברירת מחדל לכלוב ריק לפי ההוראות: '#'
        char_to_print = '#'

        # אם יש ציפורים, לוקחים את האות הראשונה של הסוג (למשל Z, G, B, L)
        if len(self.birds) > 0:
            first_bird = self.birds[0]
            char_to_print = first_bird.get_type()[0]

        # 3. בניית המטריצה (רשימה של רשימות)
        cage_grid = []
        for _ in range(num_rows):
            row = []
            for _ in range(num_cols):
                row.append(char_to_print)
            cage_grid.append(row)

        return cage_grid

    def __str__(self):
        if len(self.birds) >0: #טיפול במצב קצה: כלוב ריק
            b_type = self.birds[0].get_type()
        else:
            b_type = "None"
        birds_output = "" #יצירת מחרוזת הציפורים: כל ציפור בשורה חדשה
        for bird in self.birds:
            birds_output += "\n" + str(bird)
        return (f"Cage ID: {self.ID}\n"
                f"Size: ({self.length},{self.depth}, {self.height})\n"
                f"Color: {self.color}\n"
                f"Num of birds: {self.get_num_of_birds()}\n"
                f"Birds type: {b_type}\n"
                f"{birds_output}")



class Birdroom:
    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height
        self.cages = [] #רשימת הכלובים
        #גובה ואורך הינם במטרים, לכן מכפילים ב-10 כדי לקבל יחידות של 10cm
        self.rows = int(height * 10) + 2
        self.cols = int(length * 10) + 2
        #אתחול המטריצה המייצגת את הקיר (רוווחים = מקום ריק)
        self.grid = []
        for current_row in range(self.rows):
            row = []
            for current_col in range(self.cols):
                if current_row == self.rows -1 or current_row == 0:
                    row.append('-')
                elif current_col == self.cols - 1 or current_col == 0:
                    row.append('|')
                else:
                    row.append(' ')
            self.grid.append(row)

    def get_cages(self):
        return self.cages #מחזירה את רשימת הכלובים

    def get_birds(self):
        all_birds = [] #רשימה שטוחה של כל הציפורים בכל הכלובים
        for cage in self.cages:
            all_birds.extend(cage.get_birds())
        return all_birds


    def get_strength(self):
        total_strength = 0
        for bird in self.get_birds():
            if hasattr(bird, 'singing_strength'): #בדיקה האם יש לציפור תכונת שירה
                total_strength += bird.singing_strength
            elif hasattr(bird, 'tweeting_strength'): #בדיקה האם לציפור יש תכונת ציוץ
                total_strength += bird.tweeting_strength
        return total_strength

    def add_cage(self, cage, x: float, y: float):
        if not isinstance(cage, Cage): #בדיקת תקינות קלט Cage
            return False
        if cage.get_num_of_birds() == 0: #בדיקה שהכלוב לא ריק
            return False
        start_row = int(y * 10) #המרת מידות ממטרים לאינדקסים של המטריצה (יחידות 10cm)
        start_col = int(x * 10)
        #המרת גודל כלוב (שהוא בcm) ליחידות של 10cm
        #דוגמא: אורך 70cm נותן 7 משבצות
        cage_rows = int(cage.height /10)
        cage_cols = int(cage.length /10)
        #בדיקה האם הכלוב יוצא מגבולות הקיר
        if start_row<0 or start_col<0: return False
        if start_row + cage_rows > self.rows: return False #חורג למטה
        if start_col + cage_cols > self.cols: return False #חורג לצדדים
        #בדיקת חפיפה עם כלובים קיימים
        #עוברים על האזור המיועד ובודקים אם הוא פנוי (מכיל רווח)
        for current_row in range(start_row, start_row + cage_rows):
            for current_col in range(start_col, start_col + cage_cols):
                if self.grid[current_row][current_col] != ' ':
                    return False
        #אם הגענו עד פה, הכל תקין
        self.cages.append(cage)
        #זיהוי התו לציור (האות הראשונה של סוג הציפור הראשונה בכלוב)
        #למשל:  Zebra Finch -> Z, Gouldian Finch -> G
        first_bird = cage.get_birds()[0]
        char_to_print = first_bird.get_type()[0]
        for current_row in range(start_row, start_row + cage_rows): #עדכון המטריצה
            for current_col in range(start_col, start_col + cage_cols):
                self.grid[current_row][current_col] = char_to_print
        return True

    def get_birdroom(self):
        return self.grid #מחזירה את המטריצה המייצגת את הקיר

    def get_most_colorful(self):
        birds = self.get_birds()
        if not birds: return None
        most_colorful = birds[0]
        for bird in birds:
            if len(bird.colors) > len(most_colorful.colors):
                most_colorful = bird
        return most_colorful

    def __str__(self):
        return (f"The Bird-Room\n"
                f"Size: ({self.length},{self.width},{self.height})\n"
                f"Num of cages: {len(self.cages)}\n"
                f"Num of birds: {len(self.get_birds())}")