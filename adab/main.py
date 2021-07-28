import requests
from bs4 import BeautifulSoup as bs4
from typing import Optional, List

class Adab:
    """adab.com أدب هو كلاس بسيط يساعدك بالبحث في موقع"""
    def __init__(self) -> None:
        # الرابط الرئيسي
        self.host = "https://adab.com"
        # رابط البحث بالموقع
        self.search_url = self.host+"/post/search_get_post/0"
        # رابط ارجاع انواع الكتابات (شعر، سرد الخ)
        self.genres_url = self.host+"/home/get_genre"
        # رابط طريقة الكاتبة (عامي، فصحى الخ)
        self.writing_types_url = self.host+"/home/writing_type"
        # رابط العصر (جاهلي، اسلامي الخ)
        self.era_url = self.host+"/post/get_era"
        # رابط الدول (السعودية، فلسطين الخ)
        self.country_url = self.host+"/post/get_country"
        # رابط انواع المستخدمين (موثوق، مشارك الخ)
        self.user_type_url = self.host+"/post/get_user_type"
        # رابط عرض المنشور (يحتاج ايدي المنشور بالاخير)
        self.post_url = self.host+"/post/view_post/"
        # رابط ارجاع المواضيع المشابها للمنشور (نوعه بوست يحتاج ايدي البوت في الداتا)
        self.related_url = self.host+"/post/get_related_posts"
        
    def __html_prepare(self, html:str, post: Optional[bool]=False) -> dict:
        """ تقوم الدالة بمعالجة نص صفحة الويب وجعله قاموس يحتوي المعلومات المهمة
        
        المتغيرات:
            html (str): نص الصفحة
            post (Optional[bool], optional): استخراج محتوى البوست. Defaults to False.
        
        المخرجات:
            dict: قاموس بعد فلترة نص الصفحة
        """
        soup = bs4(str(html), "html.parser")
        if post:
            # استخراج محتةى البوست (شعراو سرد الخ)
            text = soup.find('p', attrs={'id': "post_content_view"}).text if soup.find('p', attrs={'id': "post_content_view"}) else None
            title = text.split('\n')[0] if text else None
            return {
                "title": title,
                    "text": text,
                    }
        else:
            # تحديد الالمنت الذي يحتوي معلومات اليوزر
            user_profile = soup.find('div', class_="post-profile-info").find('a') if soup.find('div', class_="post-profile-info") else None
            # استخراج اسم المستخدم من الالمنت اعلاه
            username = user_profile.text if user_profile else None
            # استخراج رابط ملف المستخدم
            user_url = user_profile.get('href') if user_profile else None
            # استخراج صورة المستخدم
            user_img = soup.find('img').get('src') if soup.find('img') else None
            # تحديد الامنت الذي يوجد مه المحتوى (عنوان ورابط ونبذة عن البوست)
            content = soup.find('div', class_="highlight_content")
            # تحديد الامنت الذي يوجد به عنوان ورابط البوست
            url_title = content.find('a') if content else None
            # استخراج رابط البوست
            post_url = url_title.get('href') if url_title else None
            # استخراج عنوان البوست
            post_title = url_title.text if url_title else None
            # استخراج نبذة للنص
            post_short_text = content.find('p', class_="blog-p post_li").text.strip() if content else None
            # استخراج مشاهدات البوست
            post_views = content.find_all('p', class_="list-detail-p")[1].text.replace('المشاهدات', '').strip() if content else None
            # ترتيبهم في قاموس
            return {
                "username":username, "user_url": user_url,
                "user_img": user_img, "post_url": post_url,
                "post_id": post_url.replace(self.post_url, '') if post_url else None, 
                "post_title": post_title, "post_views": post_views, 
                "post_short_text": post_short_text,
            }
    def __filter_ids(self, data: List[dict], required_id: Optional[int]=None) -> List[dict]:
        """ تستقبل الدالة مصفوفة مكونة من قواميس كل قاموس يحتوي ايدي، وتستقبل ايدي، وتستخرج الدالة القاموس الذي يحتوي هذا الايدي
        او ترجع جميع اقواميس اذ لم يكن هناك ايدي
        
        المتغيرات:
            data (List[dict]): المصفوصة التي تحتوي القواميس
            required_id (Optional[int], optional): الايدي المراد التحقق من وجوده. Defaults to None.
            
        الاخطاء:
            Exception: اذا كان الايدي غير موجود
            
        المخرجات:
            List[dict]: مصفوفة تحتوي على القواميس بعد مقارنة الايدي او جميعها اذ لم يكن معطى الايدي
        """
        # جمع جميع الايديات في لستة
        required_ids = map(lambda dct: int(dct['id']), data)
        if required_id and required_id not in required_ids:
            raise Exception(f"ايدي خاطئ، '{required_id}' الايدي ليس صحيح")
        else:
            # ارجاع القواميس التي تحتوي نفس الايدي او جميعها اذ لم يكن هناك ايدي معطى
            return list(filter(
                lambda dct: True if not required_id else required_id == int(dct['id']),
                    data
            ))
    def __data_prepare(self, data: List[dict], required_id: Optional[int] = None) -> List[dict]:
        """ تقوم الدالة باعداد البيانات التي تعطى والتحقق اذا كان الايدي موجود في البيانات
        
        المتغيرات:
            data (List[dict]): البيانات المراد اعدادها
            required_id (Optional[int], optional): الايدي المطلوب ارجاع بياناته. Defaults to None.
            
        الاخطاء:
            Exception: اذا كان الايدي غير موجود
            
        المخرجات:
            List[dict]: مصفوفة تحتوي بيانات الانواع التي طلبتها
        """
        # فلترة القواميس
        data = self.__filter_ids(data, required_id)
        # ارجاع لستة قوامبس تحتوي البيانات المهمة
        return list(map(
            lambda dct: {"id":int(dct['id']), 
                            "arabic_title":dct['arabic_title'].strip(),
                                "post_count":dct['post_count']},
                data
                ))

    def genres(self, genre_id: Optional[int] = None) -> List[dict]:
        """ ارجاع بيانات انواع الكتابات التي يمكن البحث عبرها في الموقع او بيانات نوع عبر الايدي.
        انواع الكتابات هي (شعر، سرد الخ)
        
        المتغيرات:
            genre_id (Optional[int], optional): ايدي النوع الذي تريد بياناته. Defaults to None.
        
        الاخطاء:
            Exception: اذا كان الايدي غير موجود
        
        المخرجات:
            List[dict]: مصفوفة تحتوي بيانات الانواع التي طلبتها
        """
        # استخراج الجسون
        genres = requests.get(self.genres_url).json()
        # ارجاع البيانات بعد اعدادها
        return self.__data_prepare(genres, genre_id)
    
    def writing_types(self, type_id: Optional[int] = None) -> List[dict]:
        """ ترجع الدالة الطرق الكاتبية التي يمكنك البحث عبرها او بيانات نوع كتابي معين عبر الايدي.
        طرف الكتابة هي (عامي، فصحى الخ)
        
        المتغيرات:
            type_id (Optional[int], optional): ايدي الطريقة التي تريد بياناتها. Defaults to None.
        
        الاخطاء:
            Exception: اذا كان الايدي غير موجود
        
        المخرجات:
            List[dict]: مصفوفة تحتوي بيانات الطرق التي طلبتها
        """
        # استخراج الجسون
        writings = requests.get(self.writing_types_url).json()
        # ارجاع البيانات بعد اعدادها
        return self.__data_prepare(writings, type_id)
    def era(self, era_id: Optional[int] = None) -> List[dict]:
        """ ارجاع بيانات العصور التي يمكن البحث عبرها في الموقع او بيانات عصر معين عبر الايدي
        
        المتغيرات:
            era_id (Optional[int], optional): ايدي العصر الذي تريد بياناته. Defaults to None.
        
        الاخطاء:
            Exception: اذا كان الايدي غير موجود
        
        المخرجات:
            List[dict]: مصفوفة تحتوي بيانات العصور التي طلبتها
        """
        # استخراج الجسون
        eras = requests.get(self.era_url).json()
        # تغير اسم المفتاح الى اسم اخر
        eras = list(map(
                lambda dct: dict(
                # انشاء تكشنري من مصفوفتين
                zip(
                    # تحويل مفاتيح الدكشنري الى مصفوفة وتغير اسم مفتاح الى اخر
                    [key.replace('arabic_name', 'arabic_title') for key in dct.keys()],
                        # المصفوفة الاخرى وهي قيم المفاتيح
                        dct.values()
                        )
                ), eras
            )
        )
        # ارجاع البيانات بعد اعدادها
        return self.__data_prepare(eras, era_id)
    def country(self, country_id: Optional[int] = None) -> List[dict]:
        """ ارجاع بيانات الدول التي يمكن البحث عبرها في الموقع او بيانات دولة معينة عبر الايدي
        
        المتغيرات:
            country_id (Optional[int], optional): ايدي الدولة الذي تريد بياناتها. Defaults to None.
        
        الاخطاء:
            Exception: اذا كان الايدي غير موجود
        
        المخرجات:
            List[dict]: مصفوفة تحتوي بيانات الدول التي طلبتها
        """
        # استخراج الجسون
        countrys = requests.get(self.country_url).json()
        # فلترة القواميس
        countrys = self.__filter_ids(countrys, country_id)
        # ارجاع البيانات المهمة لكل دولة
        return list(map(
            lambda dct: {
                "id": int(dct['id']),
                    'name': dct['name'],
                        "arabic_name": dct['arabic_name'],
                            "sortname": dct['sortname'],
            }, countrys
        ))
    def user_type(self, type_id: Optional[int] = None) -> List[dict]:
        """ ترجع الدالة انواع المستخدمين اللذين يمكنك البحث عبرهم او بيانات نوع عبر الايدي
        
        المتغيرات:
            type_id (Optional[int], optional): ايدي النوع الذي تريد بياناته. Defaults to None.
        
        الاخطاء:
            Exception: اذا كان الايدي غير موجود
        
        المخرجات:
            List[dict]: مصفوفة تحتوي الانواع المستخدمين التي طلبتها
        """
        # استخراج الجسون
        user_types = requests.get(self.user_type_url).json()
        # فلترة القواميس
        user_types = self.__filter_ids(user_types, type_id)
        # ارجاع البيانات المهمة لكل لكل نوع من المستخدمين
        return list(map(
            lambda dct: {
                "id": int(dct['id']),
                    "name": dct['arabic_name'],
            }, user_types
        ))
    def post(self, post_id: int) -> dict:
        """ استخراج محتوى البوست والمواضيع المشابها له عبر الايدي الخاص به
        
        المتغيرات:
            post_id (int): ايدي البوست المراد استخراج محتواه والمواضيع المشابها
            
        الاخطاء:
            Exception: اذا كان الايدي غير صحيح
            
        المخرجات:
            dict: دكشنري يحتوي محتوى البوست والمواضيع المشابها له
        """
        # رابط البوست
        url = f"{self.post_url}{post_id}"
        response = requests.get(url)
        # اذا تم التحويل الى رابط اخر (رابط الصفحة الرئيسية)
        # يتم التحويل الى الصفحة الرئيسية اذ كان ايدي البوست غير صحيح
        if response.url != url:
            raise Exception("ايدي خاطئ، الايدي '{}' ليس موجود".format(post_id))
        else:
            # استخراج المواضيع المشابها
            releted_posts = requests.post(
                self.related_url, data={"post_id":f"{post_id}"}).json()
            # استخراج محتوى البوست
            post_content = self.__html_prepare(response.text, post=True)
            # ارجاعهم في دكشنري
            return {
                "post_id": post_id, "title": post_content['title'],
                    "post_content": post_content['text'], "releted_posts": releted_posts,
            }
    def search(self, text: Optional[str]="", page: Optional[int]=0, 
                genres: Optional[List[int]]=[], user_type: Optional[List[int]]=[], 
                    writing_types: Optional[List[int]]=[], era: Optional[List[int]]=[], 
                        country: Optional[List[int]]=[], gender: Optional[List[str]]=[''], 
                            sort_by: Optional[str]="",) -> List[dict]:
        """ البحث في موقع أدب
        
        متفيرات:
            text (Optional[str], optional): النص المراد البحث عنه في الموقع. Defaults to "".
            genres (Optional[List[int]], optional): نوع الأدب المراد جلب نتائج حوله. Defaults to [].
            user_type (Optional[List[int]], optional): نوع الشخص المراد جلب نتائج حوله. Defaults to [].
            writing_types (Optional[List[int]], optional): نوع الكاتب المراد جلب نتائج حوله. Defaults to [].
            era (Optional[List[int]], optional): العصور المراد جلب نتائج حولها. Defaults to [].
            country (Optional[List[int]], optional): المدن المراد جلب نتائج حولها. Defaults to [].
            gender (Optional[List[str]], optional): جنس الكاتب المراد جلب نتائج حوله يجب ان يكون [F, M]. Defaults to [''].
            sort_by (Optional[str], optional): ترتيب النتائج بحسب [likes, created, views]. Defaults to "".
            page (Optional[int], optional): رقم الصفحة لاظهار نتائج مختلفة عدد النتائج في كل صفحة 10. Defaults to 0.
            
        الاخطاء:
            Exception: اذا لم تتوقر نتائج
            
        المخرجات:
            List[dict]: لستة تحتوي قواميس يوجد بها بيانات كل عملية بحث
        """
        # دالة لدمح محتوى المصفوفة في سلسلة نصية
        join = lambda lst: ','.join(map(str, lst))
        # تجهيز الداتا التي سوف يتم ارسلها في الركوست
        data = {
            "page": page,
            "genre_filter_list": join(genres),
            "writing_type_filter_list": join(writing_types),
            "search_key": text,
            "user_type": join(user_type),
            "era_select": join(era),
            "country": join(country) if len(country) > 0 else '-1',
            "gender": join(gender).upper(),
            "sort_by": sort_by
        }
        # تخزين محتوى الركوست
        search_results = requests.post(
            self.search_url, data=data
        ).json()
        if len(search_results) == 1:
            raise Exception(f"لاتوجد نتائج حول '{text}'")
        else:
            # استخراج عدد النتائج وليس المخرجات
            # النتائج تكون في جميع الصفحات وليس في صفحة واحدة
            post_count = search_results.get('post_count')
            # استخراج لستة تحتوي نص الصفحة لكل نتيجة
            search_results = search_results.get('html')
            # ارجاع النتائج في تكشنري
            return {"page": page, "text": text, 
                    "post_count": post_count, "result": list(map(self.__html_prepare, search_results))}
adab = Adab()