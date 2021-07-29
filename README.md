<h1 align="center">
  <br>
  <a><img src="https://mir-s3-cdn-cf.behance.net/project_modules/1400_opt_1/995c5a64557221.5ad77047dd227.png" alt="adab.com - img"></a>
  <br>
  Adab | أدب
  <br>
</h1>

<div dir="rtl">

<p align="center">مكتبة بايثون مبنية على موقع <a href=https://adab.com>adab.com</a>، موقع الاشعار والمواضيع الادبية
<p align="center">
  <a href="https://pypi.org/project/adab/">
    <img alt="اصدارات بايثون" src="https://img.shields.io/pypi/pyversions/adab?color=9cf">
  </a>
  <a href="https://pypi.org/project/adab/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/adab?color=9cf">
  </a>
  <a href="https://www.gnu.org/licenses/gpl-3.0.html">
    <img src="https://img.shields.io/pypi/l/adab?color=9cf&label=License" alt="الرخصة">
  </a>
</p>



<p align="center">
  <a href="#التنزيل">التنزيل</a>
  •
  <a href="#المميزات">المميزات</a>
  •
  <a href="#الاستخدام">الاستخدام</a>
  •
  <a href="#الرخصة">الرخصة</a>
  •
  <a href="#تنويهات">تنويهات</a>
</p>



## التنزيل

سوف يتم استخدام [PyPi](https://pypi.org) لتنزيل المكتبة

<div dir="ltr">

```bash
pip3 install adab
```
<div dir="rtl">


## المميزات

* البحث في موقع [أدب](adab.com)

* استخراج محتوى البوست والمواضيع المشابها له عبر الايدي الخاص به

* استخراج بيانات انواع الكتابات او عبر الايدي الخاص بالنوع

* استخراج الطرق الكاتبية التي يمكن البحث عبرها في الموقع

* استخراج بيانات العصور (العصر الاسلامي الخ) التي يمكن البحث عبرها في الموقع

* استخراج بيانات الدول التي يمكن البحث عبرها في الموقع

* استخراج انواع المستخدمين اللذين يمكنك البحث عبرهم في الموقع

<br>

## تنويهات

* لقد تم استخدام في الامثلة كائن افتراضي، يمكنك انشاء كان خاص عبر كلاس Adab

<br>

## الاستخدام

**البحث في موقع أدب :**
<div dir="ltr">

```python
from adab import adab

# البحث العام
resutl = adab.search()
print("General Search", resutl, sep="\n\n", end="\n\n")

# تخصيص البحث
resutl = adab.search(
    page=23, genres=[1, 2], 
        era=[2, 3, 1], user_type=[3, 2], 
            gender=['f'], writing_types=[15])
print("Custom Search", resutl, sep="\n\n", end="\n\n")
```
<div dir="rtl">

<details>
<summary>المخرجات</summary>

<div dir="ltr">

```bash
General search

{'page': 0, 'text': '', 'post_count': '75634', 'result': [{'username': 'أبو فراس الحمداني', 'user_url': 'https://adab.com/Abu_Firas_Alhamdani', 'user_img': 'https://adab.com/assets/uploads/images/daba776289f67907b34241ae437bc76c.png', 'post_url': 'https://adab.com/post/view_post/16557', 'post_id': '16557', 'post_title': 'أرَاكَ عَصِيَّ الدّمعِ شِيمَتُكَ الصّبرُ', 'post_views': '1701995', 'post_short_text': 'أرَاكَ عَصِيَّ الدّمعِ شِيمَتُكَ الصّبرُ،\nأما للهوى نهيٌّ عليكَ ولا أمرُ ؟\nبلى أنا مشتاقٌ وعنديَ لوع...'}, ...

Custom Search

{'page': 23, 'text': '', 'post_count': '246', 'result': [
{'username': 'علية بنت المهدي', 'user_url': 'https://adab.com/Ulayya_Bint_Almahdi', 'user_img': 'https://adab.com/', 'post_url': 'https://adab.com/post/view_post/17697', 'post_id': '17697', 'post_title': 'بني الحبُّ على الجورِ فلو', 'post_views': '7464', 'post_short_text': 'بني الحبُّ على الجورِ فلو\nأنصَفَ المعشوقُ فيهِ لَسَمَجْ\nليسَ يستحسنُ في وصفِ الهوى\nعاشقٌ يَعْرِفُ تَ...'},
{'username': 'ليلى الأخيلية', 'user_url': 'https://adab.com/Layla_AlAkheeliyya', 'user_img': 'https://adab.com/', 'post_url': 'https://adab.com/post/view_post/15107', 'post_id': '15107', 'post_title': 'جَزَى اللُّه شَرّا قابِضاً بصنيعه', 'post_views': '7036', 'post_short_text': 'جَزَى اللُّه شَرّا قابِضاً بصنيعه\nوكل امرىء يجزى بما كان ساعيا\nدعا قابضاً والمرهفات يردنه\nفقُبحْتَ م...'}, ...

```
<div dir="rtl">
</details>
<br><br>

**استخراج محتوى البوست والمواضيع المشابها له عبر الايدي الخاص به :**
<div dir="ltr">

```python
from adab import adab
result = adab.post(post_id=15107)
print(result)
```
<div dir="rtl">

<details>
<summary>المخرجات</summary>

<div dir="ltr">

```json
{
    "post_id": 15107,
    "title": "جَزَى اللُّه شَرّا قابِضاً بصنيعه",
    "post_content": 
        "جَزَى اللُّه شَرّا قابِضاً بصنيعه\n'
        وكل امرىء يجزى بما كان ساعيا\n
        دعا قابضاً والمرهفات يردنه\n
        فقُبحْتَ مدعّوا، ولبّيك داعيَا\n
        فَليْتَ عُبيدَ اللِّه كانَ مكانَه\n
        صَرِيعا؛ولم أسمَعْ لتوبة َ ناعِيَا\n",
    "releted_posts": [
        {"id": "76128", "title": "لن أرثيَ للشجر"},
        {"id": "76127", "title": "العشب.."},
        {"id": "76126", "title": "محاولة للبوح"},
        {"id": "76125", "title": "لوجة الصرخة"},
        {"id": "76124", "title": "بلا عنوان..."}]
    }


```
<div dir="rtl">
</details>
<br><br>

**استخراج انواع الكتابات:**
<div dir="ltr">

```python
from adab import adab

# جميعها
resutl = adab.genres()
print("All", resutl, sep="\n\n", end="\n\n")

# عبر الايدي
resutl = adab.genres(genre_id=1)
print("By id", resutl, sep="\n\n", end="\n\n")
```
<div dir="rtl">

<details>
<summary>المخرجات</summary>

<div dir="ltr">

```bash
All

[{'id': 1, 'arabic_title': 'شعر', 'post_count': '74635'}, {'id': 2, 'arabic_title': 'مقال', 'post_count': '507'}, {'id': 3, 'arabic_title': 'سرد', 'post_count': '488'}]

By id

[{'id': 1, 'arabic_title': 'شعر', 'post_count': '74635'}]

```
<div dir="rtl">
</details>
<br><br>

**استخراج الطرق الكاتبية:**
<div dir="ltr">

```python
from adab import adab

# جميعها
resutl = adab.writing_types()
print("All", resutl, sep="\n\n", end="\n\n")

# عبر الايدي
resutl = adab.writing_types(type_id=15)
print("By id", resutl, sep="\n\n", end="\n\n")
```
<div dir="rtl">

<details>
<summary>المخرجات</summary>

<div dir="ltr">

```bash
All

[{'id': 15, 'arabic_title': 'فصحى', 'post_count': '61509'},
{'id': 16, 'arabic_title': 'عامّي', 'post_count': '10730'}, 
{'id': 17, 'arabic_title': 'مترجم للعربية', 'post_count': '2829'},
{'id': 20, 'arabic_title': 'مترجم للإنجليزية', 'post_count': '566'}]

By id

[{'id': 15, 'arabic_title': 'فصحى', 'post_count': '61509'}]

```
<div dir="rtl">
</details>
<br><br>

**استخراج العصور:**
<div dir="ltr">

```python
from adab import adab

# جميعها
resutl = adab.era()
print("All", resutl, sep="\n\n", end="\n\n")

# عبر الايدي
resutl = adab.era(era_id=3)
print("By id", resutl, sep="\n\n", end="\n\n")
```
<div dir="rtl">

<details>
<summary>المخرجات</summary>

<div dir="ltr">

```bash
All

[{'id': 2, 'arabic_title': 'العصر الجاهلي', 'post_count': '1473'}, {'id': 3, 'arabic_title': 'العصر الإسلامي', 'post_count': '3977'}, {'id': 1, 'arabic_title': 'العصر العباسي', 'post_count': '18023'}, {'id': 4, 'arabic_title': 'العصر الأندلسي', 'post_count': '6350'}, {'id': 55, 'arabic_title': 'عصرالدول المتتابعة', 'post_count': '1572'}, {'id': 29, 'arabic_title': 'العصر الحديث', 'post_count': '44551'}]

By id

[{'id': 3, 'arabic_title': 'العصر الإسلامي', 'post_count': '3977'}]

```
<div dir="rtl">
</details>
<br><br>

**استخراج الدول التي يمكن البحث من خلالها :**
<div dir="ltr">

```python
from adab import adab

# جميعها
resutl = adab.country()
print("All", resutl, sep="\n\n", end="\n\n")

# عبر الايدي
resutl = adab.country(country_id=191)
print("By id", resutl, sep="\n\n", end="\n\n")
```
<div dir="rtl">

<details>
<summary>المخرجات</summary>

<div dir="ltr">

```bash
All

[{'id': 1, 'name': 'Afghanistan', 'arabic_name': 'أفغانستان', 'sortname': 'AF'}, {'id': 3, 'name': 'Algeria', 'arabic_name': 'الجزائر', 'sortname': 'DZ'}, {'id': 6, 'name': 'Angola', 'arabic_name': 'أنغولا', 'sortname': 'AO'}, {'id': 10, 'name': 'Argentina', 'arabic_name': 'الأرجنتين', 'sortname': 'AR'}, {'id': 11, 'name': 'Armenia', 'arabic_name': 'أرمينيا', 'sortname': 'AM'}, ... 

By id

[{'id': 191, 'name': 'Saudi Arabia', 'arabic_name': 'المملكة العربية السعودية', 'sortname': 'SA'}]



```
<div dir="rtl">
</details>
<br><br>

**استخراج المستخدمين اللذين يمكنك البحث عبرهم :**
<div dir="ltr">

```python
from adab import adab

# جميعها
resutl = adab.user_type()
print("All", resutl, sep="\n\n", end="\n\n")

# عبر الايدي
resutl = adab.user_type(type_id=3)
print("By id", resutl, sep="\n\n", end="\n\n")
```
<div dir="rtl">

<details>
<summary>المخرجات</summary>

<div dir="ltr">

```bash
All

[{'id': 3, 'name': 'موثق'}, {'id': 2, 'name': 'معتمد'}, {'id': 1, 'name': 'مشارك'}]

By id

[{'id': 3, 'name': 'موثق'}]

```
<div dir="rtl">
</details>
<br><br>




## الرخصة
[رخصة جنو العمومية الاصدار 3](https://www.gnu.org/licenses/gpl-3.0.html)