# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .. import Provider as AddressProvider


class Provider(AddressProvider):
    city_prefixes = (
        'شمال', 'غرب', 'شرق', 'جنوب', 'بندر', 'شهر', 'روستای', 'دهستان',
        'شهرستان', 'باغات', 'استان',
    )
    building_number_formats = ('#####', '####', '###')
    street_suffixes = (
        'کوچه', 'خیابان', 'پل', 'دره', 'میدان', 'چهار راه', 'بن بست', 'بلوار',
        'جنب', 'تقاطع', 'آزاد راه', 'بزرگ راه', 'جزیره', 'کوه', 'جاده', 'تونل',
    )
    postcode_formats = ('###', '####', '#####', '######', '##########',)
    states = (
        'آذربایجان شرقی', 'آذربایجان غربی', 'اردبیل', 'خراسان', 'کردستان',
        'گیلان', 'اصفهان', 'البرز', 'ایلام', 'بوشهر', 'تهران',
        'چهارمحال و بختیاری', 'خراسان جنوبی', 'خراسان رضوی', 'خراسان شمالی',
        'خوزستان', 'زنجان', 'سمنان', 'سیستان و بلوچستان', 'فارس', 'قزوین', 'قم',
        'کرمان', 'کرمانشاه', 'کهگیلویه و بویراحمد', 'گلستان', 'لرستان',
        'مازندران', 'مرکزی', 'هرمزگان', 'همدان', 'یزد',
    )
    countries = (
        'جمهوری آذربایجان', 'آرژانتین', 'آفریقای جنوبی', 'جمهوری آفریقای مرکزی',
        'آلبانی', 'آلمان', 'آنتیگوا و باربودا', 'آندورا', 'آنگولا', 'اتریش',
        'اتیوپی', 'اردن', 'ارمنستان', 'اروگوئه', 'اریتره', 'ازبکستان',
        'اسپانیا', 'استرالیا', 'استونی', 'اسرائیل', 'اسلواکی', 'اسلوونی',
        'افغانستان', 'اکوادور', 'الجزایر', 'السالوادور', 'امارات متحده عربی',
        'اندونزی', 'اوکراین', 'اوگاندا', 'ایالات متحده آمریکا', 'ایتالیا',
        'ایران', 'جمهوری ایرلند', 'ایسلند', 'باربادوس', 'باهاما', 'بحرین',
        'برزیل', 'برونئی', 'بریتانیا', 'بلاروس', 'بلژیک', 'بلغارستان', 'بلیز',
        'بنگلادش', 'بنین', 'پادشاهی بوتان', 'بوتسوانا', 'بورکینافاسو',
        'بوروندی', 'بوسنی و هرزگوین', 'بولیوی', 'پاپوآ گینه نو', 'پاراگوئه',
        'پاناما', 'پاکستان', 'پرتغال', 'پرو', 'پورتوریکو', 'تاجیکستان',
        'تانزانیا', 'تایلند', 'جمهوری چین', 'ترکمنستان', 'ترکیه',
        'ترینیداد و توباگو', 'توگو', 'تونس', 'تونگا', 'تووالو', 'تیمور شرقی',
        'جامائیکا', 'جزایر سلیمان', 'جزایر مارشال', 'جمهوری چک',
        'جمهوری دومینیکن', 'جیبوتی', 'چاد', 'چین', 'دانمارک', 'دومینیکا',
        'جمهوری دومینیکن', 'رواندا', 'روسیه', 'رومانی', 'زامبیا', 'نیوزیلند',
        'زیمباوه', 'جمهوری دموکراتیک کنگو (زئیر)', 'ژاپن', 'سائوتومه و پرینسیپ',
        'ساحل عاج', 'ساموآی غربی', 'سن مارینو', 'سری‌لانکا', 'سنت کیتس و نویس',
        'سنت لوسیا', 'سنت وینسنت و گرنادین‌ها', 'سنگاپور', 'سنگال', 'سوئد',
        'سوئیس', 'سوازیلند', 'سودان', 'سودان جنوبی', 'سورینام', 'سوریه',
        'سومالی', 'سیرالئون', 'سیشل', 'شیلی', 'صربستان', 'عراق',
        'عربستان سعودی', 'عمان', 'غنا', 'فرانسه', 'فلسطین', 'فنلاند', 'فیجی',
        'فیلیپین', 'قبرس', 'قرقیزستان', 'قزاقستان', 'قطر', 'کامبوج', 'کامرون',
        'کانادا', 'کره جنوبی', 'کره شمالی', 'کرواسی', 'کاستاریکا', 'کلمبیا',
        'جمهوری کنگو', 'جمهوری دموکراتیک کنگو', 'کنیا', 'کوبا', 'کوزوو',
        'مجمع‌الجزایر قمر', 'کویت', 'کیپ ورد', 'کیریباتی', 'گابن', 'گامبیا',
        'گرجستان', 'گرنادا', 'گرینلند(از مستعمرات دانمارک)', 'گواتمالا',
        'گویان', 'گینه', 'گینه استوایی', 'گینه بیسائو', 'لائوس', 'لبنان',
        'لتونی', 'لسوتو', 'لهستان', 'لوکزامبورگ', 'لیبریا', 'لیبی', 'لیتوانی',
        'لیختن‌اشتاین', 'ماداگاسکار', 'مالاوی', 'مالت', 'مالدیو', 'مالزی',
        'مالی', 'مجارستان', 'مراکش', 'مصر', 'مغولستان', 'مقدونیه', 'مکزیک',
        'موریتانی', 'موریس', 'موزامبیک', 'مولداوی', 'موناکو', 'مونته‌نگرو',
        'میانمار', 'ایالات فدرال میکرونزی', 'نائورو', 'نامیبیا', 'نپال',
        'نروژ', 'نیجریه', 'نیکاراگوئه', 'نیوزیلند', 'واتیکان', 'وانواتو',
        'ونزوئلا', 'ویتنام', 'هائیتی', 'هلند', 'هندوراس', 'هند', 'یمن', 'یونان',
    )

    city_formats = (
        '{{city_prefix}} {{first_name}}',
    )
    street_name_formats = (
        '{{first_name}} {{street_suffix}}',
        '{{last_name}} {{street_suffix}}'
    )
    street_address_formats = (
        '{{building_number}} {{street_name}}',
        '{{building_number}} {{street_name}} {{secondary_address}}',
    )
    address_formats = (
        "{{street_address}}\n{{city}}, {{state}} {{postcode}}",
    )
    secondary_address_formats = ('سوئیت ###', 'واحد ###')

    def city_prefix(self):
        return self.random_element(self.city_prefixes)

    def secondary_address(self):
        return self.numerify(self.random_element(self.secondary_address_formats))

    def state(self):
        return self.random_element(self.states)
