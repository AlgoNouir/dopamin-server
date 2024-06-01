from core.models import RefCommand
from models.main.item import ItemModel
from models.main.category import CategoryModel

data = [
    {
        "name":"پرتغال",
        "price":40000,
        "category_id":2,
    },
    {
        "name":"انبه",
        "price":80000,
        "category_id":2,
    },
    {
        "name":"آناناس",
        "price":80000,
        "category_id":2,
    },
    {
        "name":"آب هویج",
        "price":10000,
        "category_id":2,
    },
    {
        "name":"آب کرفس",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"توت فرنگی",
        "price":50000,
        "category_id":2,
    },
    {
        "name":"آب سیب ترش",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"آب سیب شیرین",
        "price":25000,
        "category_id":2,
    },
    {
        "name":"انار",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"شاه توت",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"طالبی",
        "price":25000,
        "category_id":2,
    },
    {
        "name":"آلو جنگلی",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"آلوکشمیری",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"معجون آلو",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"آلبالو",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"تمرهندی",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"تمشک",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"آلوبخارا",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"زردآلو",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"معجون ترش",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"زرشک قرمز",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"زرشک کوهی",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"معجون زرشک",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"هلو",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"گریپ فروت",
        "price":40000,
        "category_id":2,
    },
    {
        "name":"ذغال آخته",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"هندوانه",
        "price":25000,
        "category_id":2,
    },
    {
        "name":"آب انجیر",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"کیوی",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"میکس بری",
        "price":30000,
        "category_id":2,
    },
    {
        "name":"معجون استوایی",
        "price":100000,
        "category_id":2,
    },
    {
        "name":"معجون",
        "price":80000,
        "category_id":2,
    },
    {
        "name":"کوکونات تایلندی",
        "price":260000,
        "category_id":2,
    },
    {
        "name":"شیر موز",
        "price":30000,
        "category_id":3,
    },
    {
        "name":"شیر موز خرما",
        "price":35000,
        "category_id":3,
    },
    {
        "name":"شیر موز کنجد گردو خرما",
        "price":40000,
        "category_id":3,
    },
    {
        "name":"شیر موز کنجد گردو خرما شیره انگور",
        "price":45000,
        "category_id":3,
    },
    {
        "name":"شیر پسته",
        "price":50000,
        "category_id":3,
    },
    {
        "name":"شیر موز خرما اواکادو",
        "price":60000,
        "category_id":3,
    },
    {
        "name":"شیر موز فندق",
        "price":40000,
        "category_id":3,
    },
    {
        "name":"شیر موز عسل اواکادو",
        "price":60000,
        "category_id":3,
    },
    {
        "name":"شیر موز پسته",
        "price":50000,
        "category_id":3,
    },
    {
        "name":"شیر انبه پسته",
        "price":60000,
        "category_id":3,
    },
    {
        "name":"شیر موز کنجد گردو پسته خرما",
        "price":60000,
        "category_id":3,
    },
    {
        "name":"شیر نارگیل",
        "price":50000,
        "category_id":3,
    },
    {
        "name":"شیر نارگیل انبه",
        "price":70000,
        "category_id":3,
    },
    {
        "name":"شیر موز نارگیل",
        "price":50000,
        "category_id":3,
    },
    {
        "name":"شیر موز نارگیل اواکادو",
        "price":70000,
        "category_id":3,
    },
    {
        "name":"قیفی",
        "price":10000,
        "category_id":4,
    },
    {
        "name":"قیفی نان قندی",
        "price":12000,
        "category_id":4,
    },
    {
        "name":"نسکافه",
        "price":10000,
        "category_id":4,
    },
    {
        "name":"شکلات تلخ",
        "price":10000,
        "category_id":4,
    },
    {
        "name":"وانیل پسته",
        "price":15000,
        "category_id":4,
    },
    {
        "name":"زعفران",
        "price":10000,
        "category_id":4,
    },
    {
        "name":"شاه توت",
        "price":10000,
        "category_id":4,
    },
    {
        "name":"انبه",
        "price":10000,
        "category_id":4,
    },
    {
        "name":"طالبی",
        "price":10000,
        "category_id":4,
    },
    {
        "name":"توت فرنگی",
        "price":10000,
        "category_id":4,
    },
    {
        "name":"موز",
        "price":10000,
        "category_id":4,
    },
    {
        "name":"وانیل",
        "price":10000,
        "category_id":4,
    },
    {
        "name":"کارامل",
        "price":10000,
        "category_id":4,
    },
    {
        "name":"شکلات",
        "price":10000,
        "category_id":4,
    },
    {
        "name":"موز شکلات",
        "price":10000,
        "category_id":4,
    },
    {
        "name":"فالوده ساده",
        "price":30000,
        "category_id":5,
    },
    {
        "name":"فالوده بستنی",
        "price":35000,
        "category_id":5,
    },
    {
        "name":"سینگل",
        "price":30000,
        "category_id":6,
    },
    {
        "name":"دبل",
        "price":40000,
        "category_id":6,
    },
    {
        "name":"آمریکانو",
        "price":40000,
        "category_id":6,
    },
    {
        "name":"اسپرسو نعنا",
        "price":50000,
        "category_id":6,
    },
    {
        "name":"شیر قهوه",
        "price":50000,
        "category_id":6,
    },
    {
        "name":"لته",
        "price":70000,
        "category_id":6,
    },
    {
        "name":"کاپوچینو",
        "price":65000,
        "category_id":6,
    },
    {
        "name":"کاپوچینو دوپینگ",
        "price":70000,
        "category_id":6,
    },
    {
        "name":"نسکافه",
        "price":60000,
        "category_id":6,
    },
    {
        "name":"نسکافه,دوپینگ",
        "price":70000,
        "category_id":6,
    },
    {
        "name":"موکا",
        "price":70000,
        "category_id":6,
    },
    {
        "name":"لته فندوق",
        "price":75000,
        "category_id":6,
    },
    {
        "name":"کارامل ماکیاتو",
        "price":75000,
        "category_id":6,
    },
    {
        "name":"قهوه ترک",
        "price":50000,
        "category_id":6,
    },
    {
        "name":"قهوه یونانی",
        "price":60000,
        "category_id":6,
    },
    {
        "name":"فرنچ پرس",
        "price":80000,
        "category_id":6,
    },
    {
        "name":"فرانسه",
        "price":90000,
        "category_id":6,
    },
    {
        "name":"رومانو",
        "price":60000,
        "category_id":6,
    },
    {
        "name":"آمریکانو سینگل",
        "price":30000,
        "category_id":6,
    },
    {
        "name":"شیر کاکائو",
        "price":50000,
        "category_id":7,
    },
    {
        "name":"هات چاکلت",
        "price":60000,
        "category_id":7,
    },
    {
        "name":"هات چاکلت دوپینگ",
        "price":80000,
        "category_id":7,
    },
    {
        "name":"ماسالا",
        "price":70000,
        "category_id":7,
    },
    {
        "name":"وایت چاکلت",
        "price":60000,
        "category_id":7,
    },
    {
        "name":"میکس چاکلت",
        "price":70000,
        "category_id":7,
    },
    {
        "name":"کوکو وایت",
        "price":80000,
        "category_id":7,
    },
    {
        "name":"اسپشیال",
        "price":80000,
        "category_id":7,
    },
    {
        "name":"املت سنتی",
        "price":80000,
        "category_id":8,
    },
    {
        "name":"املت بیکن",
        "price":120000,
        "category_id":8,
    },
    {
        "name":"املت ژامبون",
        "price":110000,
        "category_id":8,
    },
    {
        "name":"املت هات داگ",
        "price":100000,
        "category_id":8,
    },
    {
        "name":"سوسیس و تخم مرغ",
        "price":70000,
        "category_id":8,
    },
    {
        "name":"نیمرو",
        "price":60000,
        "category_id":8,
    },
    {
        "name":"نیمرو سوجوک",
        "price":110000,
        "category_id":8,
    },
    {
        "name":"املت قارچ و پنیر",
        "price":110000,
        "category_id":8,
    },
    {
        "name":"صبحانه انگلیسی",
        "price":140000,
        "category_id":8,
    },
    {
        "name":"سیب زمینی ساده",
        "price":70000,
        "category_id":9,
    },
    {
        "name":"سیب زمینی با قارچ و پنیر",
        "price":90000,
        "category_id":9,
    },
    {
        "name":"سیب زمینی دبل چیز",
        "price":110000,
        "category_id":9,
    },
    {
        "name":"سیب زمینی اسپشیال",
        "price":125000,
        "category_id":9,
    },
    {
        "name":"سیب زمینی آلفردو",
        "price":100000,
        "category_id":9,
    },
    {
        "name":"نان سیر",
        "price":110000,
        "category_id":9,
    },
    {
        "name":"پاستا چیکن آلفردو",
        "price":170000,
        "category_id":10,
    },
    {
        "name":"پاستا چیکن پستو",
        "price":160000,
        "category_id":10,
    },
    {
        "name":"پاستا چیلی (تند)",
        "price":150000,
        "category_id":10,
    },
    {
        "name":"پاستا پستو سبزیجات",
        "price":150000,
        "category_id":10,
    },
    {
        "name":"کلاسیک برگر",
        "price":140000,
        "category_id":11,
    },
    {
        "name":"چیز برگر",
        "price":155000,
        "category_id":11,
    },
    {
        "name":"ماشروم برگر",
        "price":165000,
        "category_id":11,
    },
    {
        "name":"رویال برگر",
        "price":210000,
        "category_id":11,
    },
    {
        "name":"دوبل برگر",
        "price":200000,
        "category_id":11,
    },
    {
        "name":"برگر چیکن سوخاری",
        "price":140000,
        "category_id":11,
    },
    {
        "name":"برگر اسپشیال",
        "price":225000,
        "category_id":11,
    },
    {
        "name":"(پیتزا مارگاریتا (ایتالیایی 32 سانتیمتری",
        "price":150000,
        "category_id":12,
    },
    {
        "name":"(پیتزا پپرونی (ایتالیایی 32 سانتیمتر",
        "price":220000,
        "category_id":12,
    },
    {
        "name":"(پیتزا چهارفصل (ایتالیایی 32 سانتیمتری",
        "price":275000,
        "category_id":12,
    },
    {
        "name":"(پیتزا قارچ و مرغ (ایتالیایی 32 سانتیمتری",
        "price":220000,
        "category_id":12,
    },
    {
        "name":"(پیتزا بلونیز (ایتالیایی 32 سانتیمتری",
        "price":245000,
        "category_id":12,
    },
    {
        "name":"(پیتزا مخلوط (ایتالیایی 32 سانتیمتری",
        "price":200000,
        "category_id":12,
    },
    {
        "name":"(پیتزا اسپشیال (ایتالیایی 32 سانتیمتری",
        "price":260000,
        "category_id":12,
    },
    {
        "name":"تکه 2",
        "price":140000,
        "category_id":13,
    },
    {
        "name":"تکه 3",
        "price":160000,
        "category_id":13,
    },
    {
        "name":"تکه 4",
        "price":180000,
        "category_id":13,
    },
]

class Command(RefCommand):

    def handle(self, *args, **options):
        
        # ------------------------------------------ SET MAIN
        
        self.info("set data to database")

        c = CategoryModel(
            name="tmp"
        )
        c.save()
        c.delete()
        
        categories_name = [
            "آبمیوه",
            "ویتامینه",
            "بستنی",
            "فالوده",
            "قهوه",
            "بار گرم",
            "صبحانه",
            "پیش غذا",
            "پاستا",
            "برگر",
            "پیتزا",
            "فیله سوخاری"
        ]
        
        categories = []
        
        for name in categories_name:
            c = CategoryModel(
                name=name
            )
            
            c.save()
            categories.append(c)
            
        for item in data:
            
            i = ItemModel(
                name=item["name"],
                price=item["price"],
                category=categories[item["category_id"] - 2],
            )
            
            i.save()